# Generated by Django 3.1.7 on 2021-03-16 11:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0009_auto_20210311_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
