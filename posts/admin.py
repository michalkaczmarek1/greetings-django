from django.contrib import admin
from posts.models import Post, Author

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "created", "modified", "author"]
    list_filter = ["title", "created", "modified"]
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "bio", "nick"]
    list_filter = ["email", "nick"]
    search_fields = ["email", "nick"]

admin.site.register(Author, AuthorAdmin)
