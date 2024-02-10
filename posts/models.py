from django.db import models
from datetime import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    written_at = models.DateField(default=datetime.now, blank=True)
