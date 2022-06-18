from django.shortcuts import render

from catalog.models import *


def index(request):
    context = {'title': 'Каталог', 'manga_titles': MangaTitles.objects.all()}
    return render(request, 'catalog/catalog.html', context)


def manga_title_view(request, manga_title_slug):
    manga_title = MangaTitles.objects.get(slug=manga_title_slug)
    chapters = Chapters.objects.filter(title_id=manga_title.id).order_by('-number')
    context = {'title': manga_title.title, 'manga_title': manga_title, 'chapters': chapters}
    return render(request, 'catalog/manga_title.html', context)


def chapter_view(request, manga_title_slug, chapter_slug):
    chapter = Chapters.objects.get(slug=chapter_slug, title__slug=manga_title_slug)
    pages = Pages.objects.filter(chapter=chapter.id).order_by('url')
    return render(request, 'catalog/chapter.html', {'title': chapter.name, 'pages': pages})

