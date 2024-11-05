from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author':'coeryMs',
        'title':'Blog post1',
        'content':'first post content',
        'date_posted': 'august 27'
    },
    {
        'author':'coeryGs',
        'title':'Blog post2',
        'content':'second post content',
        'date_posted': 'august 69'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})