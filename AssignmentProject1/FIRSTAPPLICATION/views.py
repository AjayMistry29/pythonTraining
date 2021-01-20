from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")

def welcome(request):
    context = {'tag_var':"tag_var"}
    return render(request,"demo.html",context)
