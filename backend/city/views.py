from django.shortcuts import render
from django.http import HttpResponse
from .utils.extract_city import load_cities

# Create your views here.
def load_data(requests):
    response = load_cities()

    return HttpResponse(response)