# Generated by Django 2.1.5 on 2019-02-13 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mentor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='gambar',
            field=models.ImageField(upload_to='images'),
        ),
    ]
