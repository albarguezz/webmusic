from django.contrib import admin
from .models import Cancion, Genero, Autor, Album, Playlist

# Register your models here.



@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'nombre_autor', 'titulo_album', 'genero','subirCancion']


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['genero']

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['autor']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album', 'autor_nombre', 'año_lanzamineto']

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['nombre_playlist', 'usuario']
