# coding: utf-8
from django.db import models
from tinymce import models as tinymce_models


class Post(models.Model):
    class Meta:
          verbose_name = u"Книга"
          verbose_name_plural = u"Книги"
          ordering = ['-datetime',]
    title = models.CharField(max_length=255, verbose_name=u"Название") # заголовок поста
    image = models.ImageField(upload_to='img', blank=True, null=True, verbose_name=u"Изображение")
    datetime = models.DateTimeField(verbose_name=u"Дата и время")
    content = tinymce_models.HTMLField(verbose_name=u"Контент") # текст поста

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/books/%i/" % self.id

