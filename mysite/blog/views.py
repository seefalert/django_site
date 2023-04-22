from django.shortcuts import render

posts = [
    {
        'author': 'SeefAlert',
        'title': 'First post',
        'content': 'Hello first post',
        'date_posted': '21 april, 2023'
    },
    {
        'author': 'User',
        'title': 'Second post',
        'content': 'Hello second post',
        'date_posted': '22 april, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About club Python'})
