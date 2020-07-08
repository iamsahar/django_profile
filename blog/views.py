from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'sahar',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'sina',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
