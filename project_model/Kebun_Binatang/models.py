from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

from django.db import models as models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField (max_length=255)
    spesies = models.CharField (max_length=255)
    berat = models.IntegerField (default=0)
    umur = models.IntegerField (default=0)

    def __str__ (self):
        return self.nama

class Kandang(models.Model):
    nama = models.CharField (max_length=255)
    isi_kandang = models.CharField (max_length=255)
    luas_kandang = models.IntegerField (default=1)

    def __str__ (self):
        return self.nama

class Penjaga(models.Model):
    nama = models.CharField (max_length=255)
    nomor_telepon = models.CharField (max_length=25)
    jadwal_jaga = models.DateTimeField (default=timezone.now)

    def __str__ (self):
        return self.nama

class Pengunjung(models.Model):
    nama = models.CharField (max_length=255)
    nomor_telepon = models.CharField (max_length=25)
    hari_berkunjung = models.DateTimeField (default=timezone.now)

    def __str__ (self):
        return self.nama


