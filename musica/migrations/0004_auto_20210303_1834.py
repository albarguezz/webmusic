# Generated by Django 3.1.3 on 2021-03-03 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0003_auto_20210302_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='caratula',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
