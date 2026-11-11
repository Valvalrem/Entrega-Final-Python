# Blog Web en Django - Proyecto Final Python Coderhouse

## Descripción breve
Aplicación web de blog desarrollada en Python utilizando Django, la cual permite la gestión completa de publicaciones con soporte de imágenes, autenticación de usuarios (registro, login, logout) y rutas protegidas.

## Tecnologías utilizadas
* Python
* Django
* SQLite
* Bootstrap
* Pillow (para manejo de imágenes)
* python-decouple (para variables de entorno)

## Funcionalidades principales
* Listado y visualización detallada de publicaciones.
* Creación, edición y eliminación de posts desde la interfaz web (requiere autenticación).
* Carga de imágenes en las publicaciones.
* Sistema de usuarios: Registro, inicio y cierre de sesión.
* Rutas protegidas mediante decoradores de autenticación (`@login_required`).

## Instrucciones de instalación y ejecución local

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DE_TU_REPOSUTORIO>
   cd <NOMBRE_DE_TU_CARPETA>