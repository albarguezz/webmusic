# Generated by Django 3.1.3 on 2021-03-04 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0004_auto_20210303_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='Autor',
            new_name='autor_nombre',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='nombre',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='cancion',
            old_name='autor',
            new_name='nombre_autor',
        ),
    ]
