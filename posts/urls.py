from django.urls import path
from .views import posts_list, post_details, authors_list, author_details

app_name="posts"
urlpatterns = [
   path('post/<int:id>', post_details, name="details"),
   path('list/', posts_list, name="list"),
   path('authors/list/', authors_list, name="authors_list"),
   path('author/<int:id>', author_details, name="authors_details")
]

