from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

from django.db import models

# Create your models here.
class Mentor(models.Model):
    gambar = models.ImageField(upload_to = 'images')
    nama = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    note = models.TextField()

    def __str__(self):
        return self.nama