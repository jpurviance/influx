from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, "migrate/index.html", {})

def resources(request):
    return render(request, "migrate/resources.html", {})
