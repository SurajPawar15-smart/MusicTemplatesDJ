from django.shortcuts import render
from django.http import HttpResponse


def about(request):
   return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog_details.html')


def contact(request):
    return render(request, 'contact.html')


def discography(request):
    return render(request, 'discography.html')


def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html')


def tours(request):
    return render(request, 'tours.html')


def videos(request):
    return render(request, 'videos.html')

