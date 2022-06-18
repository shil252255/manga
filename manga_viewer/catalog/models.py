from django.db import models
from django.urls import reverse


class MangaTitles(models.Model):
    origin_id = models.IntegerField(unique=True)
    title = models.TextField(unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    poster = models.ImageField(upload_to='posters/', default='posters/def.jpg')
    banner = models.ImageField(upload_to='banners/', default='banners/def.jpg')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('title_page', kwargs={'title_slug': self.slug})


class Chapters(models.Model):
    origin_id = models.IntegerField(unique=True)
    title = models.ForeignKey(MangaTitles, on_delete=models.CASCADE)
    number = models.FloatField()
    poster = models.ImageField(upload_to='posters/')
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('book_page', kwargs={'book_slug': self.slug, 'title_slug': self.title.slug})

    def get_number(self):
        return str(int(self.number)) if self.number == int(self.number) else str(self.number)

    def __str__(self):
        return self.name


class Pages(models.Model):
    chapter = models.ForeignKey(Chapters, on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    number = models.IntegerField(default=0)
    size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number


class OtherTitles(models.Model):
    title = models.ForeignKey(MangaTitles, on_delete=models.CASCADE)
    title_other = models.TextField()
    lang = models.CharField(max_length=4)

    def __str__(self):
        return self.title


class Covers(models.Model):
    chapter = models.ForeignKey(Chapters, on_delete=models.CASCADE)
    page = models.ForeignKey(Pages, on_delete=models.CASCADE)
    miniature = models.FileField(upload_to='covers/', null=True, blank=True)
    

