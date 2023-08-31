from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<h2 style="color:blue">This is a details page</h2>')
def detail(request):
    return HttpResponse('<h1 style="color:red">this is the detail page</h1>')