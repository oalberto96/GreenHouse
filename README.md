# GreenHouse
GreenHouse es un servidor web hecho en django para registrar temperatura y humedad de un invernadero por medio de arduino


![Screenshot](/images/arduino.jpg)
![Screenshot](/images/demo.png)



### Requerimientos

1. Python 3.6.+
1. Django 1.11.6

### Arduino
[Codigo para arduino](https://github.com/oalberto96/ArduinoESP8266/blob/master/Examples/SendSensorDataHttpDisplay.ino)

### Instalacion

1. Instalar python 3.5+
1. Crear un ambiente virtual con el commando `python -m venv myvenv`
1. Iniciar el ambiente virtual `myvenv\Scripts\activate`
1. Descargar Django `pip install django`

Dentro del proyecto debe existir un archivo llamado `manage.py`

1. Correr el comando `python manage.py makemigrations DataAnalyzer`
1. Correr el comando `python manage.py migrate DataAnalyzer`

Con un editor de textos abrir el archivo `settings.py` y agregar su direccion ip en la linea 28, dentro de `ALLOWED_HOST`
![Settings](/images/settings.png)

### Ejecucion

1. Con el comando `python manage.py runserver tudireccionip:8000` activamos el servidor

![Server running](/images/server.png)
