from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth import get_user

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the genextds.com index.</h1>")
    #return render(request, "04.html")


