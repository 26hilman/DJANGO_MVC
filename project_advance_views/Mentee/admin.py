from django.contrib import admin
from .models import Mentee

# Register your models here.
model_mentee = [Mentee]
admin.site.register(model_mentee)