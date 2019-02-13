from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

from django.db import models

# Create your models here.
class Blog(models.Model):
    gambar = models.ImageField(upload_to = 'images')
    judul = models.CharField(max_length=255)
    isi = models.TextField()

    def __str__(self):
        return self.judul