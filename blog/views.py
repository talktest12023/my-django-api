from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post  # Import the Post model
from django.http import Http404  # Import Http404


def home(request):
    books = ["The Alchemist", "Harry Potter", "Django for Beginners"]
    return render(request, "blog/home.html", {"books": books})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Automatically raises 404
    return render(request, 'blog/post_detail.html', {'post': post})


def post_list(request):
    posts = Post.objects.all()  # Get all posts from the database
    return render(request, 'blog/post_list.html', {'posts': posts})
