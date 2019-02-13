from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

from django.db import models as models


# Create your models here.

class Direksi(models.Model):
    nama = models.CharField (max_length=255)
    nomor_telepon = models.CharField (max_length=25)
    jabatan = models.CharField (max_length=100)

    def __str__ (self):
        return self.nama

class Mentee(models.Model):
    nama_lengkap = models.CharField (max_length=255)
    nomor_telepon = models.CharField (max_length=25)
    nomor_absen = models.CharField (max_length=5)
    nilai_rata_rata = models.IntegerField (default=0)

    def __str__ (self):
        return self.nama_lengkap

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField (max_length=100)
    jadwal_dimulai = models.DateTimeField (default=timezone.now)
    jadwal_berakhir = models.DateTimeField (default=timezone.now)

    def __str__ (self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField (max_length=255)
    nomor_telepon = models.CharField (max_length=25)
    mata_pelajaran = models.ForeignKey (MataPelajaran, on_delete=models.CASCADE)

    def __str__ (self):
        return self.nama_lengkap

class Challange(models.Model):
    nama_challange = models.CharField (max_length=255)
    banyak_soal = models.IntegerField (default=0)
    bobot_nilai = models.IntegerField (default=0)
    tanggal_pelaksanaan = models.DateTimeField (default=timezone.now)
    mata_pelajaran = models.ForeignKey (MataPelajaran, on_delete=models.CASCADE)

    def __str__ (self):
        return self.nama_challange

class LiveCode(models.Model):
    nama_live_code = models.CharField (max_length=255)
    banyak_soal = models.IntegerField (default=0)
    bobot_nilai = models.IntegerField (default=0)
    tanggal_pelaksanaan = models.DateTimeField (default=timezone.now)
    mata_pelajaran = models.ForeignKey (MataPelajaran, on_delete=models.CASCADE)

    def __str__ (self):
        return self.nama_live_code
