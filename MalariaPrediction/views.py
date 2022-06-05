from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .utility import image_prediction

from tensorflow.keras.models import load_model

MALARIA_MODEL = load_model('MalariaPrediction/malaria.h5')


class AboutWebsite(TemplateView):
    template_name = "MalariaPrediction/about.html"


class ContactWebsite(TemplateView):
    template_name = "MalariaPrediction/contact.html"


class HomeWebsite(TemplateView):
    template_name = "MalariaPrediction/index.html"


def PredictionPage(request):
    output = ''
    if request.method == "POST":
        output = image_prediction(request.FILES['image'], MALARIA_MODEL)
        return render(request, "MalariaPrediction/result.html",
                      {"output": output})
    else:
        output = ''
    return render(request, "MalariaPrediction/predict.html")
