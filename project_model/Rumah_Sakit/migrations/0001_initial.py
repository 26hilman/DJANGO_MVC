# Generated by Django 2.1.5 on 2019-02-11 08:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dokter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nomor_telepon', models.CharField(max_length=25)),
                ('bidang', models.CharField(max_length=255)),
                ('jadwal_praktek', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Obat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('kandungan', models.TextField(max_length=255)),
                ('khasiat', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pasien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nomor_telepon', models.CharField(max_length=25)),
                ('alamat', models.TextField(max_length=255)),
                ('keluhan', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('total_harga', models.IntegerField(default=0)),
                ('kumpulan_obat', models.TextField(max_length=255)),
            ],
        ),
    ]
