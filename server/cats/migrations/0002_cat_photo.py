# Generated by Django 5.1.1 on 2024-10-04 08:53

import cats.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='photo',
            field=models.ImageField(default='', upload_to=cats.models.upload_cat_image_to, verbose_name='Фотография'),
            preserve_default=False,
        ),
    ]
