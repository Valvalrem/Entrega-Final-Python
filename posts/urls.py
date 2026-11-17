from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('crear/', views.crear_post, name='crear_post'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('post/<int:pk>/editar/', views.editar_post, name='editar_post'),
    path('post/<int:pk>/borrar/', views.borrar_post, name='borrar_post'),
    path('perfil/', views.perfil_usuario, name='perfil'),
]