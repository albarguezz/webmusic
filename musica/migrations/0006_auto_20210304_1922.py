# Generated by Django 3.1.3 on 2021-03-04 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0005_auto_20210304_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='titulo_album',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='cancion',
            old_name='album',
            new_name='titulo_album',
        ),
    ]