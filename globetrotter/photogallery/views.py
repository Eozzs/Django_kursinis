from django.shortcuts import render
from photogallery.models import Trip, Photo, Post
from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    template_name = "index.html"

class IntroPageView(TemplateView):
    template_name = "intro.html"

class GalleryPageView(TemplateView):
    template_name = "gallery.html"

class BookPageView(TemplateView):
    template_name = "book.html"
