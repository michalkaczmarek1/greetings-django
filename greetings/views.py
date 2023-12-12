from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greetings(request):
   return HttpResponse("Hello World!")

def greetings_with_name(request, a):
   name_cap = a.capitalize()
   return HttpResponse("Hello " + name_cap)