from django.urls import path, include

from .views import *


urlpatterns = (
    path('', HomeWebsite.as_view(), name='index'),
    path('about/', AboutWebsite.as_view(), name="about"),
    path('contact/', ContactWebsite.as_view(), name="contact"),
    path('service/', PredictionPage, name="service"),
)
