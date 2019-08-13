from __future__ import unicode_literals

from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=100, blank=True)
    document = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title