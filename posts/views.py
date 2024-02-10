from django.shortcuts import render, redirect

from .models import Post, ContactMessage
import re

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


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def saveContactMsg(request):
    if request.method == 'POST':
       email = request.POST['email']
       name = request.POST['name']
       message = request.POST['message']
       if is_valid_email(email):
           contact_msg = ContactMessage()
           contact_msg.email = email
           contact_msg.name = name
           contact_msg.message = message
           contact_msg.save()

    return redirect('contact')
