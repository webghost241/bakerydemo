from __future__ import unicode_literals

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import Tag, TaggedItemBase

from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    StreamFieldPanel,
)
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from bakerydemo.base.blocks import BaseStreamBlock


class BlogPeopleRelationship(Orderable, models.Model):
    '''
    This defines the relationship between the `People` within the `base`
    app and the BlogPage below allowing us to add people to a BlogPage.
    '''
    page = ParentalKey(
        'BlogPage', related_name='blog_person_relationship'
    )
    people = models.ForeignKey(
        'base.People', related_name='person_blog_relationship'
    )
    panels = [
        SnippetChooserPanel('people')
    ]


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')


class BlogPage(Page):
    '''
    A Blog Page (Post)
    '''
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Location image'
    )

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    date_published = models.DateField("Date article published", blank=True, null=True)

    body = StreamField(
        BaseStreamBlock(), verbose_name="Blog post", blank=True
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        FieldPanel('date_published'),
        InlinePanel(
            'blog_person_relationship', label="Author(s)",
            panels=None, min_num=1),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('body'),
    ]

    def authors(self):
        '''
        Returns the BlogPage's related People
        '''
        authors = [
            n.people for n in self.blog_person_relationship.all()
        ]

        return authors

    @property
    def get_tags(self):
        '''
        Returns the BlogPage's related list of Tags.
        Each Tag is modified to include a url attribute
        '''
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/'+'/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    parent_page_types = ['BlogIndexPage']

    # Defining what content type can sit under the parent
    # The empty array means that no children can be placed under the
    # LocationPage page model
    subpage_types = []

    # api_fields = ['image', 'body']


class BlogIndexPage(RoutablePageMixin, Page):
    '''
    Index page for blogs.
    We need to alter the page model's context to return the child page objects - the
    BlogPage - so that it works as an index page

    The RoutablePageMixin is used to allow for a custom sub-URL
    '''
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Location listing image'
    )

    introduction = models.TextField(
        help_text='Text to describe the index page',
        blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('introduction')
    ]

    # parent_page_types = [
    #     'home.HomePage'
    # ]

    # Defining what content type can sit under the parent. Since it's a blank
    # array no subpage can be added
    subpage_types = ['BlogPage']

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = BlogPage.objects.descendant_of(
            self).live().order_by(
            '-first_published_at')
        return context

    @route('^tags/$', name='tag_archive')
    @route('^tags/(\w+)/$', name='tag_archive')
    def tag_archive(self, request, tag=None):
        '''
        A Custom view that utilizes Tags. This view will
        return all related BlogPages for a given Tag or redirect back to
        the BlogIndexPage
        '''
        try:
            tag = Tag.objects.get(slug=tag)
        except Tag.DoesNotExist:
            if tag:
                msg = 'There are no blog posts tagged with "{}"'.format(tag)
                messages.add_message(request, messages.INFO, msg)
            return redirect(self.url)

        blogs = BlogPage.objects.filter(tags=tag).live().descendant_of(self)

        context = {
            'title': 'Posts tagged with: {}'.format(tag.name),
            'blogs': blogs
        }
        return render(request, 'blog/blog_index_page.html', context)

    # api_fields = ['introduction']
