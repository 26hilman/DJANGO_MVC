from django.contrib import admin
from .models import Blog

# Register your models here.
model_blog = [Blog]
admin.site.register(model_blog)