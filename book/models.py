from django.db import models

# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title