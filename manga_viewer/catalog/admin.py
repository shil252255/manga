from django.contrib import admin
from catalog.models import *


class MangaTitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'poster', 'banner')


class ChaptersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'number', 'poster')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(MangaTitles, MangaTitlesAdmin)
admin.site.register(Chapters, ChaptersAdmin)
