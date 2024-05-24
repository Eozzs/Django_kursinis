from django.urls import path
from photogallery import views
from photogallery.views import IndexPageView, GalleryPageView, IntroPageView, BookPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('intro/', IntroPageView.as_view(), name='intro'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
    path('book/', BookPageView.as_view(), name='book')
]

