# Generated by Django 3.1.3 on 2021-03-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='caratula',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
