# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'books_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('content', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'books', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'books_post')


    models = {
        u'books.post': {
            'Meta': {'ordering': "['-datetime']", 'object_name': 'Post'},
            'content': ('tinymce.models.HTMLField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['books']