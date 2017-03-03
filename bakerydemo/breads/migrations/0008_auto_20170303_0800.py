# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 08:00
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('breads', '0007_auto_20170303_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breadpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading_block', wagtail.wagtailcore.blocks.StructBlock((('heading_text', wagtail.wagtailcore.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.wagtailcore.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('block_quote', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock()), ('attribute_name', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='e.g. Guy Picciotto', required=False))))), ('embed_block', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html'))), blank=True, verbose_name='Page body'),
        ),
        migrations.AlterField(
            model_name='breadsindexpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading_block', wagtail.wagtailcore.blocks.StructBlock((('heading_text', wagtail.wagtailcore.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.wagtailcore.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('block_quote', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock()), ('attribute_name', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='e.g. Guy Picciotto', required=False))))), ('embed_block', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html'))), blank=True, verbose_name='Page body'),
        ),
    ]
