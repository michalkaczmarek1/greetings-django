from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def greetings(request):
    
    return render(
        request=request,
        template_name="greetings/homepage.html",
        context={"hello": "powitanie"}
    )

def about(request):
    
    return render(
        request=request,
        template_name="greetings/about.html"
    )

def contact(request):
    
    return render(
        request=request,
        template_name="greetings/contact.html"
    )