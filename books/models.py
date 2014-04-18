# coding: utf-8
from django.db import models
from tinymce import models as tinymce_models


class Post(models.Model):
    class Meta:
          verbose_name = u"Книга"
          verbose_name_plural = u"Книги"
          ordering = ['-datetime',]
    title = models.CharField(max_length=255) # заголовок поста
    image = models.ImageField(upload_to='img', blank=True, null=True)
    datetime = models.DateTimeField()
    content = tinymce_models.HTMLField() # текст поста

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/books/%i/" % self.id

