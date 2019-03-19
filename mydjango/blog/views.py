from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    page = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/page.html', {'page': page})


def edit(request):
    return render(request, 'blog/edit.html')


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    models.Article.objects.create(title=title, content=content)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})
