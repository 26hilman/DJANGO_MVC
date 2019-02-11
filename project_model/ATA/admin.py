from django.contrib import admin
from .models import Direksi, Mentee, Mentor, MataPelajaran, Challange, LiveCode

# Register your models here.
my_ata = [Direksi, Mentee, Mentor, MataPelajaran, Challange, LiveCode]
admin.site.register(my_ata)
