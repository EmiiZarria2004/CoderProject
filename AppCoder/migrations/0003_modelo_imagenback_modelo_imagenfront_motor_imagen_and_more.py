# Generated by Django 4.1.4 on 2023-01-16 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='imagenback',
            field=models.ImageField(blank=True, null=True, upload_to='modelos'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='imagenfront',
            field=models.ImageField(blank=True, null=True, upload_to='modelos'),
        ),
        migrations.AddField(
            model_name='motor',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='motores'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='descripcion',
            field=models.CharField(default='Falta descripción.', max_length=300),
        ),
    ]