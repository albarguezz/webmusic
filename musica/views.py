from musica.forms import AutorForm, CancionForm, AlbumForm, PlaylistsForm, Añadir_cancion_PlaylistsForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout as do_logout, login as do_login
from django.contrib.auth.forms import AuthenticationForm
from .models import Autor, Cancion, User, Playlist, Album
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

# Vamos a crear las funciones del login


# -------------- USUARIOS --------------------

@login_required
# Funcion de Bienvenida
def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "musica/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/')


# Funcion de registro
def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('../../musica/dash')

    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "musica/register.html", {'form': form})


# Funcion de login
def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('../../musica/dash')

    # Si llegamos al final renderizamos el formulario
    return render(request, "musica/login.html", {'form': form})


# Funcion de perfil detallado de usuario
def perfil_detail(request):
    user = User.objects.all()
    return render(request, "musica/profile.html", {'user': user})


# funcion de cerrar sesion
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('../../musica/')


# -------------- MUSICA -----------------

@login_required
def ListarMusica(request):
    # Canciones
    cancion = Cancion.objects.all().order_by('titulo')

    paginator1 = Paginator(cancion, 3)
    page_number1 = request.GET.get('page1')
    page_obj_canciones = paginator1.get_page(page_number1)

    # Albumnes
    album = Album.objects.all().order_by('album')
    paginator2 = Paginator(album, 4)
    page_number2 = request.GET.get('page2')
    page_obj_album = paginator2.get_page(page_number2)

    # Playlists
    playlist = Playlist.objects.all().order_by('nombre_playlist')
    paginator4 = Paginator(playlist, 4)
    page_number4 = request.GET.get('page4')
    page_obj_playlist = paginator4.get_page(page_number4)

    # Autores
    autor = Autor.objects.all().order_by('autor')
    paginator3 = Paginator(autor, 4)
    page_number3 = request.GET.get('page3')
    page_obj_artist = paginator3.get_page(page_number3)

    return render(request, 'musica/welcome.html', {'autor': autor, 'page_obj_artist': page_obj_artist, 'cancion': cancion, 'page_obj_canciones': page_obj_canciones,  'album': album, 'page_obj_album': page_obj_album, 'playlist': playlist, 'page_obj_playlist': page_obj_playlist})


# ------------------ CANCIONES --------------------------

@login_required
# Funcion donde listo todas las canciones
def cancionList(request):
    # Recogo el objeto cancion
    cancion = Cancion.objects.all().order_by('titulo')
    # Que muestre 4 canciones por pagina

    paginator = Paginator(cancion, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'musica/canciones_list.html', {'cancion': cancion, 'page_obj': page_obj})


# Esta funcion lista todas las canciones subidas por el usuario logeado
@login_required
def mis_canciones(request):
    mis_canciones = Cancion.objects.filter(usuario=request.user)
    paginator = Paginator(mis_canciones, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'musica/likes.html', {'mis_canciones': mis_canciones, 'page_obj': page_obj})


# Subir Nueva Cancion
@login_required
def cancion_nueva(request):
    if request.method == "POST":
        form = CancionForm(request.POST, request.FILES)
        if form.is_valid():
            cancion = form.save(commit=False)
            cancion.usuario = request.user
            cancion.save()
            return redirect('../dash')
    else:
        form = CancionForm()

    return render(request, 'musica/subirCancion.html', {'form': form})


# Eliminar Canciones
@login_required
def eliminar_cancion(request, id):
    cancion_a_eliminar = Cancion.objects.filter(id=id)
    cancion_a_eliminar.delete()
    return redirect('../../dash')


# --------------------- ALBUMNES -----------------------

# Listar Albumnes
@login_required
def ListaAlbums(request):
    album = Album.objects.all().order_by('album')
    paginator = Paginator(album, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'musica/album_list.html', {'album': album, 'page_obj_album': page_obj})


@login_required
# Funcion que detalla el album
def album_detail(request, id):
    album = get_object_or_404(Album, id=id)
    canciones = Cancion.objects.filter(titulo_album__album=album)
    return render(request, 'musica/album_detail.html', {'album': album, 'canciones': canciones})


@login_required
# Album Nuevo
def album_nuevo(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.usuario = request.user
            album.save()
            return redirect('../dash')
    else:
        form = AlbumForm()

    return render(request, 'musica/subirAlbum.html', {'form': form})


# ------------------------- ARTISTAS -------------------------

# Listar Artistas
@login_required
def ListaArtista(request):
    autor = Autor.objects.all().order_by('autor')
    paginator = Paginator(autor, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'musica/autor_list.html', {'autor': autor, 'page_obj': page_obj})


@login_required
# Funcion que detalla el autor
def artista_detail(request, id):
    artista = get_object_or_404(Autor, id=id)
    albumnes = Album.objects.filter(autor_nombre__autor=artista)
    return render(request, 'musica/artista_detail.html', {'artista': artista, 'albumnes': albumnes})


@login_required
# Autor Nuevo
def autor_nuevo(request):
    if request.method == "POST":
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            autor = form.save(commit=False)
            autor.usuario = request.user
            autor.save()
            return redirect('../dash')
    else:
        form = AutorForm()

    return render(request, 'musica/subirAutor.html', {'form': form})


# ------------------------- PLAYLISTS --------------------------


@login_required
# Listar Playlist
def ListaPlaylist(request):
    # Recogo el objeto cancion
    playlist = Playlist.objects.all()
    # Que muestre 4 canciones por pagina
    paginator = Paginator(playlist, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'musica/playlist.html', {'playlist': playlist, 'page_obj': page_obj})


@login_required
def playlist_detail(request, id):
    playlist = get_object_or_404(Playlist, id=id)
    return render(request, 'musica/playlist_detail.html', {'playlist': playlist})


@login_required
# Funcion para crear una nueva Playlist
def playlist_nueva(request):
    if request.method == "POST":
        form = PlaylistsForm(request.POST, request.FILES)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.usuario = request.user
            playlist.save()
            return redirect('musica:listar_playlists')
    else:
        form = PlaylistsForm()

    return render(request, 'musica/crear_playlists.html', {'form': form})


@login_required
def añadir_cancion_form(request, id_cancion):
    playlists= Playlist.objects.all()
    playlists_form= Añadir_cancion_PlaylistsForm()
    return render(request, 'musica/añadir_a_playlist.html', {'playlists': playlists, 'playlists_form': playlists_form})

@login_required
def añadir_cancion_playlist(request, id_cancion, id_playlist):
    cancion_playlist_añadir = get_object_or_404(Cancion, id=id_cancion)
    playlist = get_object_or_404(
        Playlist, id=id_playlist, usuario=request.user)
    playlist.cancion.add(cancion_playlist_añadir)
    return redirect('musica:playlist_detail', playlist.id)


@login_required
def eliminar_playlist(request, id):
    playlist_a_eliminar = get_object_or_404(
        Playlist, id=id, usuario=request.user)
    playlist_a_eliminar.delete()
    return redirect('musica:listar_playlists')


@login_required
def eliminar_cancion_playlist(request, id_cancion, id_playlist):
    cancion_playlist_a_eliminar = get_object_or_404(Cancion, id=id_cancion)
    playlist = get_object_or_404(
        Playlist, id=id_playlist, usuario=request.user)
    playlist.cancion.remove(cancion_playlist_a_eliminar)
    return redirect('musica:playlist_detail', playlist.id)


# ----------------------------- LIKES ----------------------------

@login_required
def dar_like(request, id_cancion):
    like_cancion = request.POST.get('id')
    action = request.POST.get('action')
    if like_cancion and action:
        try:
            cancion = Cancion.objects.get(id=id_cancion)
            if action == 'like':
                cancion.likes.add(request.user)
            else:
                cancion.likes.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'error'})


@login_required
def ListaLikes(request):
    canciones_likes = Cancion.objects.filter(likes=request.user)
    print(canciones_likes)
    paginator = Paginator(canciones_likes, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'musica/likes.html', {'canciones_likes': canciones_likes, 'page_obj': page_obj})


# ---------------------------- BUSCADOR ------------------------------

@login_required
def buscador(request):
    query = request.GET.get('q', '')
    results_cancion = Cancion.objects.filter(
        Q(titulo__icontains=query)).order_by('titulo')
    results_album = Album.objects.filter(
        Q(album__icontains=query)).order_by('album')
    results_artista = Autor.objects.filter(
        Q(autor__icontains=query)).order_by('autor')
    results_playlists = Playlist.objects.filter(
        Q(nombre_playlist__icontains=query))

    return render(request, 'musica/busquedas.html', {'results_cancion': results_cancion, 'results_album': results_album, 'results_artista': results_artista, 'results_playlists': results_playlists})
