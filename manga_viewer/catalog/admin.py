from django.contrib import admin
from catalog.models import *


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'poster', 'banner')


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'number')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Titles, TitlesAdmin)
admin.site.register(Books, BooksAdmin)