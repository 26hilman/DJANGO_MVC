# Generated by Django 2.1.5 on 2019-02-13 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.ImageField(upload_to='')),
                ('nama', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('note', models.TextField()),
            ],
        ),
    ]
