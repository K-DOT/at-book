# coding: utf-8

from django.db import models
from tinymce import models as tinymce_models


class Category(models.Model):
    class Meta:
        verbose_name = u"Категория"
        verbose_name_plural = u"Катагории"
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/category/%i" % self.id

class Post(models.Model):
    class Meta:
          verbose_name = u"Запись"
          verbose_name_plural = u"Записи"
          ordering = ['-datetime',]
    title = models.CharField(max_length=255) # заголовок поста
    image = models.ImageField(upload_to='img', blank=True)

    def delete(self, using=None):
        try:
            obj = Post.objects.get(id=self.id)
            obj.image.delete()
        except (Post.DoesNotExist, ValueError):
            pass
        super(Post, self).delete()

    datetime = models.DateTimeField()
    content = tinymce_models.HTMLField() # текст поста
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

