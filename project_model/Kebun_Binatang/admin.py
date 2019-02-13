from django.contrib import admin
from .models import Hewan, Kandang, Penjaga, Pengunjung

# Register your models here.
kebun_binatangku = [Hewan, Kandang, Penjaga, Pengunjung]
admin.site.register(kebun_binatangku)
