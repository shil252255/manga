from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<slug:manga_title_slug>', manga_title_view, name='manga_title_url'),
    path('<slug:manga_title_slug>/<slug:chapter_slug>', chapter_view, name='chapter_url')
]
