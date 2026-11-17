
# Blog Web - Proyecto Final de Python

## Descripción

Aplicación web de blog desarrollada con Python y Django.
Permite crear, visualizar, editar y eliminar publicaciones,
cargar imágenes y gestionar usuarios mediante autenticación.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- Pillow
- python-decouple
- HTML

## Funcionalidades principales

- Listado de publicaciones.
- Visualización individual de publicaciones.
- Creación, edición y eliminación de posts.
- Carga y visualización de imágenes.
- Registro de usuarios.
- Inicio y cierre de sesión.
- Rutas protegidas mediante @login_required.
- Perfil de usuario con biografía e imagen.

## Instalación

Para descargar el proyecto, ejecutar:

```bash
git clone https://github.com/Valvalrem/Entrega-Final-Python.git
cd Entrega-Final-Python
```

## Ejecución del proyecto

Continuar con las instrucciones...

### 1. Clonar el repositorio

git clone https://github.com/Valvalrem/Entrega-Final-Python.git

cd Entrega-Final-Python

### 2. Crear el entorno virtual

python -m venv venv

### 3. Activar el entorno virtual

Windows PowerShell:

.\venv\Scripts\Activate.ps1

Windows CMD:

venv\Scripts\activate.bat

Linux / macOS:

source venv/bin/activate

### 4. Instalar dependencias

python -m pip install --upgrade pip

pip install -r requirements.txt

### 5. Configurar variables de entorno

Crear un archivo llamado .env a partir de .env.example.

Configurar SECRET_KEY y DEBUG=True para desarrollo local.

No compartir el archivo .env ni subirlo a GitHub.

### 6. Ejecutar migraciones

python manage.py migrate

### 7. Crear un superusuario

python manage.py createsuperuser

### 8. Iniciar el servidor

python manage.py runserver

Abrir en el navegador:

http://127.0.0.1:8000/

## Base de datos e imágenes

La base de datos SQLite se genera mediante las migraciones.

Las imágenes cargadas por los usuarios se almacenan
en la carpeta media/.

## Autor

Valentino Piuzzi
Proyecto entregable final de Diplomatura en Python.
