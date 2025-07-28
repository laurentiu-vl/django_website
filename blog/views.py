from django.shortcuts import render

posts = [
    {
        'author': 'LV',
        'title': 'My App',
        'content': 'First App',
        'date_posted': '28-Jul-25'
    },
    {   'author': 'LAV',
        'title': 'His App',
        'content': 'Initial App',
        'date_posted': '27-Jul-25'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
