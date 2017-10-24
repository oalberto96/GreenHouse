# GreenHouse
GreenHouse es una aplicacion basada en django, un framework 

### Requerimientos

1. Python 3.6.+
1. Django 1.11.6

### Instalacion

1. Instalar python 3.5+
1. Crear un ambiente virtual con el commando `python -m venv myvenv`
1. Iniciar el ambiente virtual `myvenv\Scripts\activate`
1. Descargar Django `pip install django`

Dentro de la carpeta debe existir un archivo llamado `manage.py

1. Correr el comando `python manage.py makemigrations DataAnalyzer`
1. Correr el comando `python manage.py migrate DataAnalyzer`

Con un editor de textos abrir el archivo `settings.py` y agregar su direccion ip en la linea 28, dentro de `ALLOWED_HOST`
![Settings](/images/settings.png)

### Ejecucion

1. Con el comando `python manage.py runserver tudireccionip:8000` activamos el servidor

![Server running](/images/server.png)
