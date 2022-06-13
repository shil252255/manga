from django.shortcuts import render

from catalog.models import *


def index(request):
    return render(request, 'catalog/catalog.html', {'title': 'Каталог', 'titles': Titles.objects.all()})


def title_page(request, title_slug):
    title = Titles.objects.get(slug=title_slug)
    chapters = Books.objects.filter(title_id=title.id)
    return render(request, 'catalog/title_page.html', {'title': title, 'chapters': chapters})


def page_viewer(request, title_slug, book_slug):
    title = Titles.objects.get(slug=title_slug)
    chapter = Books.objects.get(slug=book_slug, title__slug=title_slug)
    pages = Pages.objects.filter(book_id=chapter.id)
    return render(request, 'catalog/page_viewer.html', {'title': chapter.name, 'pages': pages})

