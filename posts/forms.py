from django import forms
from .models import Post, Perfil

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['bio', 'imagen']    