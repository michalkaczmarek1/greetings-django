from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

# Create your views here.

def math(request):
   return render(
    	    request=request,
    	    template_name="maths/main.html"
	)

def add(request, a, b):
	a, b = int(a), int(b)
	wynik = a+b
	c = {"a":a, "b":b, "operacja": "+" ,"wynik":wynik, "title": "dodawanie"}
	return render(
    	    request=request,
    	    template_name="operation.html",
    	    context=c
	)

def sub(request, a, b):
   a, b = int(a), int(b)
   wynik = a - b
   c = {"a":a, "b":b, "operacja": "-" ,"wynik":wynik, "title": "odejmowanie"}
   return render(
    	    request=request,
    	    template_name="operation.html",
    	    context=c
	   )

def mul(request, a, b):
   a, b = int(a), int(b)
   wynik = a*b
   c = {"a":a, "b":b, "operacja": "*" ,"wynik":wynik, "title": "mnozenie"}
   return render(
    	    request=request,
    	    template_name="operation.html",
    	    context=c
	)

def div(request, a, b):
   if int(b) == 0:
       wynik = "Error"
       messages.add_message(request, messages.ERROR, "Dzielenie przez zero!")
   else:
       wynik = int(a) / int(b)
   c = {"a": a, "b": b, "operacja": "/", "wynik": wynik, "title": "dzielenie"}
   return render(
       request=request,
       template_name="operation.html",
       context=c)