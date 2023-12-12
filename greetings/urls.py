from django.urls import path
from .views import greetings, greetings_with_name

urlpatterns = [
   path('', greetings),
   path('<a>', greetings_with_name)
]