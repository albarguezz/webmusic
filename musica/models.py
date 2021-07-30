from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.shortcuts import redirect
from django.utils import timezone

# Create your models here.

# Creacion de la tabla Genero
class Genero(models.Model):
    genero = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        return (self.genero)


class Autor(models.Model):
    autor = models.CharField(max_length=50)
    photo = models.ImageField()
    biografia = models.TextField()

    def __str__(self):
        return (self.autor)


# Creacion de la tabla Album
class Album(models.Model):
    portada = models.ImageField(blank=True, null=True)
    album = models.CharField(max_length=100)
    autor_nombre = models.ForeignKey(Autor, on_delete=models.CASCADE)
    año_lanzamineto = models.DateField()

    def __str__(self):
        return (self.album)



# Creacion de la tabla Cancion
class Cancion (models.Model):
    titulo = models.CharField(max_length=100)
    nombre_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(default=timezone.now)
    subirCancion = models.FileField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    def get_absolute_url(self):
        return (f'media/{self.subirCancion}')


    def __str__(self):
        return self.titulo


# Creacion de la tabla Playlist
class Playlist(models.Model):
    photo_playlist = models.ImageField(blank=True)
    nombre_playlist = models.CharField(max_length=50)
    cancion = models.ManyToManyField(Cancion)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_playlist
