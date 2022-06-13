from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<slug:title_slug>', title_page, name='title_page'),
    path('<slug:title_slug>/<slug:book_slug>', page_viewer, name='book_page')
]
