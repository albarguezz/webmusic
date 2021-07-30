from django.urls import path
from . import views

app_name = 'musica'

urlpatterns = [
    #Account
    path('register/', views.register, name="register"),
    path('', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('cambiarContraseña/', views.logout, name="cambiar_contraseña"),
    path('cambiarDatos/', views.logout, name="cambiar_datos"),
    path('profile/', views.perfil_detail, name="profile"),

    #Canciones
    path('dash/', views.ListarMusica, name="index"),    
    path('canciones/', views.cancionList, name="listar_canciones"),
    path("mis_canciones/", views.mis_canciones, name="mis_canciones"),
    path('subir/cancion', views.cancion_nueva, name="subir_cancion"),
    path('eliminar/<int:id>/', views.eliminar_cancion, name="eliminar_cancion"),


    # Albumnes
    path('subir/album', views.album_nuevo, name="subir_album"),    
    path('album/detail/<int:id>/', views.album_detail, name="album_detail"),
    path('albumnes/', views.ListaAlbums, name="listar_albumnes"),


    # Autores
    path('artistas/', views.ListaArtista, name="listar_artistas"),
    path('subir/autor', views.autor_nuevo, name="subir_autor"),
    path('autor/detail/<int:id>/', views.artista_detail, name="artista_detail"),


    #Busquedas
    path('search/', views.buscador, name="busqueda"),

    #Playlist
    path('crear/playlists/', views.playlist_nueva, name="crear_playlists"),
    path('playlists/', views.ListaPlaylist, name="listar_playlists"),
    path('playlists/detail/<int:id>/', views.playlist_detail, name="playlist_detail"),
    path('añadir/playlist/cancion/<int:id_cancion>/',
         views.añadir_cancion_form, name="añadir_cancion_form"),
    path('añadir/playlist/cancion/<int:id_cancion>/playlist/<int:id_playlist>',
         views.añadir_cancion_playlist, name="añadir_cancion_playlist"),
    path('eliminar/playlist/<int:id>/', views.eliminar_playlist, name="eliminar_playlist"),
    path('eliminar/playlist/<int:id_playlist>/cancion/<int:id_cancion>/', views.eliminar_cancion_playlist, name="eliminar_cancion_playlist"),


    #Likes
    path('likes/', views.ListaLikes, name="likes"),
    path("dar_like/", views.dar_like, name="dar_like")
]
