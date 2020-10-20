from django.shortcuts import render


posts = [
    {
        'author': 'Ruslan M',
        'title': 'First blog post',
        'content': 'First post content',
        'date_posted': '18 October, 2020',
    },
    {
        'author': 'Roman M',
        'title': 'Second blog post',
        'content': 'Second post content',
        'date_posted': '18 October, 2010',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
