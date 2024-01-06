from django.shortcuts import render
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm
from django.contrib import messages

# Create your views here.


def posts_list(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Post.objects.get_or_create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                author=Author.objects.get(id=form.cleaned_data['author'])
            )
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy post!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = PostForm()
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/list.html",
        context={
            "posts": posts,
            "form": form
        }
    )


def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(
        request=request,
        template_name='posts/details.html',
        context={"post": post}
    )


def authors_list(request):
    if request.method == "POST":
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            Author.objects.get_or_create(email=form.cleaned_data['email'], nick=form.cleaned_data['nick'], bio=form.cleaned_data['bio'])
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowego autora!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = AuthorForm()
    authors = Author.objects.all()
    return render(
        request=request,
        template_name="authors/list.html",
        context={
            "authors": authors,
            "form": form
        }
    )


def author_details(request, id):
    author = Author.objects.get(id=id)
    return render(
        request=request,
        template_name='authors/details.html',
        context={"author": author}
    )
