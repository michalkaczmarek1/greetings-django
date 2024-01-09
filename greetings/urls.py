from django.urls import path
from .views import greetings, about, contact

app_name='greetings'
urlpatterns = [
   path('', greetings, name='welcome'),
   path('about/', about, name='about'),
   path('contact/', contact, name='contact')
]