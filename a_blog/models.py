from django.db import models
from django import forms
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalManyToManyField
from datetime import date


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=80, unique=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "blog categories"


class BlogPage(Page):
    date = models.DateField("Post date", default = date.today)
    intro = models.CharField(max_length=250, blank = True, default = "")
    body = RichTextField()
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    # ✅ Important: use the actual class name, not a string
    categories = ParentalManyToManyField(BlogCategory, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
        FieldPanel("header_image"),
        FieldPanel("categories", widget=forms.CheckboxSelectMultiple),
    ]
