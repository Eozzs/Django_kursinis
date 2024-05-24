from django.db import models
from django.contrib.auth.models import User


class Trip(models.Model):
    CONTINENT = (
        ('as', 'Asia'),
        ('eu', 'Europe'),
        ('na', 'South America'),
        ('sa', 'North America'),
        ('af', 'Africa'),
        ('au', 'Australia'),
        ('an', 'Antarctica')
    )
    continent = models.CharField('Continent', max_length=2, default='eu', choices=CONTINENT)
    country = models.CharField('Country', max_length=50)
    city = models.CharField('City', max_length=50)
    date = models.DateField('Date')
    album_cover = models.ImageField('Album cover', upload_to='covers', default='covers/default.jpg')

    def __str__(self):
        return f'Trip: {self.city}, {self.country}'

    class Meta:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trips'


class Photo(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True, related_name='photo')# Atgalinis rysys: trip.photo !
    title = models.CharField('Photo title', max_length=500)
    description = models.TextField('Photo description', max_length=500, null=True, blank=True)
    photo = models.ImageField(upload_to='photos', default='photos/default.jpg')

    def __str__(self):
        return f'Photo: {self.title}'
    
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='post')

    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True, related_name='post')# Atgalinis rysys: trip.post !
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, related_name='post') # Atgalinis rysys: photo.post !
    comment = models.TextField('Comment', max_length=300, null=True, blank=True)
    
    REACTION = (
        ('l', 'I love it!'),
        ('a', 'Aww, amazing...'),
        ('f', 'Looks delicious :)'),
        ('h', 'Hugs (& kisses)'),
        ('g', 'You look great ;)'),
        ('n', 'Sry, not my taste.'),
        ('w', 'Whaat?!')
    )
    reaction=models.CharField('Reaction', max_length=1, choices=REACTION, null=True, blank=True)

    def __str__(self):
        return f'Comment - {self.photo} ({self.trip})'
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

