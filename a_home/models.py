from django.db import models
from wagtail.snippets.models import register_snippet 
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
 

@register_snippet
class NavigationItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=500, help_text="Use absolute path (eg /about/) or full external URL")
    sort_order = models.IntegerField(default=0)

    panels = [
        FieldPanel('title'),
        FieldPanel('link'),
        FieldPanel('sort_order'),
    ]
    class Meta:
        ordering = ['sort_order']
  

    def __str__(self):
        return self.title

@register_snippet
class SiteHeader(models.Model):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tagline = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('logo'),
        FieldPanel('tagline'),
    ]

    def __str__(self):
        return "Site Header"    

class FeatureBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    description = blocks.TextBlock(required=False)
    icon = ImageChooserBlock(required=False)

class CourseBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    excerpt = blocks.TextBlock(required=False)
    date = blocks.DateBlock(required=False)
    image = ImageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)
    price = blocks.CharBlock(required=False, help_text="e.g., $49.99")
    reviews_count = blocks.IntegerBlock(required=False, help_text="Number of reviews")

class RegisterBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    cta_text = blocks.CharBlock()
    cta_link = blocks.URLBlock()

class ProfileBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    role = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    bio = blocks.TextBlock(required=False)

class TrustBlock(blocks.StructBlock):
    logo = ImageChooserBlock()
    name = blocks.CharBlock()

class HomePage(Page):
    template = "a_home/index.html"   # use your existing template or create a new home template
    body = StreamField([
        ('features', blocks.ListBlock(FeatureBlock())),
        ('courses', blocks.ListBlock(CourseBlock())),
        ('registration', RegisterBlock()),
        ('profiles', blocks.ListBlock(ProfileBlock())),
        ('trusted_by', blocks.ListBlock(TrustBlock())),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
