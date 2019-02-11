# Generated by Django 2.1.5 on 2019-02-11 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('full_name', models.TextField(max_length=255)),
                ('gender', models.CharField(max_length=1)),
                ('telephone', models.TextField(max_length=25)),
                ('mobile', models.TextField(max_length=25)),
                ('address', models.TextField(max_length=255)),
            ],
        ),
    ]
