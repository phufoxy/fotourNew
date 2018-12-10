from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Speak(models.Model):
    name_speak = models.CharField(max_length=250)
    type_speak = models.CharField(max_length=250)
    date = models.DateTimeField(default=datetime.now())
    theme = models.FileField(upload_to='learn/',default='/default/user-avatar-default-165.png')

    def __str__(self):
        return self.name_speak + '-' + self.type_speak

class TaskSpeak(models.Model):
    speak = models.ForeignKey(Speak, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
