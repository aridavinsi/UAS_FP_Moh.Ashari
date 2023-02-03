# Generated by Django 2.2.12 on 2023-02-02 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20230202_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barangterjual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produk', models.CharField(max_length=50)),
                ('totalunit', models.IntegerField()),
                ('totalpenjualan', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Barang03',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('harga', models.BigIntegerField()),
                ('jenis_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Jenis')),
            ],
        ),
    ]