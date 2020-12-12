from django.urls import path

from places.views.overview import overview

urlpatterns = [
    path('overview/', overview, name='overview'),
]
