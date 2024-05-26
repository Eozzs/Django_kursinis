from django.shortcuts import render, get_object_or_404
from photogallery.models import Trip, Photo, Post
from django.views.generic.base import TemplateView


def my_trips(request):
    trips_count = Trip.objects.all().count()
    trips_list_ordered = Trip.objects.all().order_by('continent')
    
    data = {
        "trips_count": trips_count,
        "trips_list_ordered": trips_list_ordered,
    }

    return render(request, "my_trips.html", context=data)


def trip_photos(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    photos_list = Photo.objects.filter(trip=trip)
    posts = Post.objects.filter(trip=trip).count()
    photos_count = trip.photos.count()
    # kaip atsifiltruoti postus...
    # gal nauja funkcija ? #book instance pvz.

    data = { 
        "trip": trip,
        "photos_list": photos_list,
        "photos_count": photos_count,
        "comments_count": posts,
    }

    return render (request, "trip_photos.html", context=data)


# class PostView??
# def phot_posts(request, photo_id):
#     photo = get_object_or_404(Photo, pk=photo_id)
#     posts_list = Post.objects.filter(photo=photo)
#     posts_count = photo.post.count()

#     data = { 
#         "photo": photo,
#         "posts_list": posts_list,
#         "posts_count": posts_count,
#     }

#     return render (request, "trip_photos.html", context=data)


class IndexPageView(TemplateView):
    template_name = "index.html"

class IntroPageView(TemplateView):
    template_name = "intro.html"

class GalleryPageView(TemplateView):
    model = Photo
    template_name = "photo_gallery.html"

class BookPageView(TemplateView):
    template_name = "book.html"
