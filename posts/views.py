from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Vista para listar posts
def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha')
    return render(request, 'posts/lista_posts.html', {'posts': posts})

# Vista para ver el detalle de un post
def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detalle_post.html', {'post': post})

# Vista para crear un post nuevo (requiere estar logueado)
@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'posts/crear_post.html', {'form': form})

# Vista de Registro de Usuarios
def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_posts')
    else:
        form = UserCreationForm()
    return render(request, 'posts/registro.html', {'form': form})

# Vista de Iniciar Sesión
def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_posts')
    else:
        form = AuthenticationForm()
    return render(request, 'posts/login.html', {'form': form})

# Vista de Cerrar Sesión
def logout_usuario(request):
    logout(request)
    return redirect('lista_posts')

# Vista para crear un post nuevo (requiere estar logueado)
@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'posts/crear_post.html', {'form': form})

# --- AGREGÁ ESTO AL FINAL DEL ARCHIVO VIEWS.PY ---

# Vista para Editar Post
@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/editar_post.html', {'form': form})

# Vista para Borrar Post
@login_required
def borrar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'posts/borrar_post.html', {'post': post})