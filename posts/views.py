from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})


def about(request):

    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
