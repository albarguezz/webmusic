from django import forms
from .models import Cancion, Autor, Album, Playlist


class CancionForm (forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['titulo', 'nombre_autor', 'titulo_album',
                  'subirCancion', 'genero', 'usuario', ]
        labels = {'titulo': 'Titulo',
                  'subirCancion': 'subirCancion', 'nombre_autor': 'NombreAutor', 'titulo_album': 'TituloAlbum', 'genero': 'Genero', 'usuario': 'Usuario', }

    #Esto es para añadir una clase
    def __init__(self, *args, **kwargs):
        super(CancionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class AutorForm (forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['autor', 'photo', ]
        label = {'autor': 'Autor', 'photo': 'Photo', }

    #Esto es para añadir una clase
    def __init__(self, *args, **kwargs):
        super(AutorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['portada', 'album', 'autor_nombre','año_lanzamineto']
        label = {'portada':'Portada', 'album': 'Album', 'autor_nombre': 'Nombre Autor', 'año_lanzamineto': 'Año de Lanzamiento' }

    #Esto es para añadir una clase
    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class PlaylistsForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['photo_playlist', 'nombre_playlist', 'cancion', 'usuario']
        label = {'photo_playlist': 'photo_playlist', 'nombre_playlist': 'Nombre de la Playlist', 'cancion': 'Canciones', 'usuario': 'Usuario'}

    #Esto es para añadir una clase
    def __init__(self, *args, **kwargs):
        super(PlaylistsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class Añadir_cancion_PlaylistsForm(forms.Form):
    nombre_playlist = forms.CharField(label='Nombre de la playlist:')

    #Esto es para añadir una clase
    def __init__(self, *args, **kwargs):
        super(Añadir_cancion_PlaylistsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



