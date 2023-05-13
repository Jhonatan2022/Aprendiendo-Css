# Dark mode con Django y Tailwind



# Requisitos 
* Python Instalado: [Descargar](https://www.python.org/downloads/)
* Pip Instalado: [Descargar](https://pip.pypa.io/en/stable/installing/)
* Virtualenv Instalado: [Descargar](https://virtualenv.pypa.io/en/latest/installation.html)
* Nodejs Instalado: [Descargar](https://nodejs.org/es/download/)


## Pasos a seguir
```sh
# Clonar el repositorio
git clone https://github.com/Jhonatan2022/Cruds-Multi-languages.git
```
```sh
# Accedemos al la carpeta del proyecto
cd '.\Creando dark mode\Django-Tailwind\'
```
```sh
# Instalamos virtualenv si no lo tenemos 
pip install virtualenv
```
```sh
# Damos los permisos necesarios por powershell
Set-ExecutionPolicy RemoteSigned
```
```sh
# Creamos un entorno virtual
virtualenv env
```
```sh
# Activamos el entorno virtual
env\Scripts\activate
```
```sh
# Instalamos los requerimientos
pip install -r requirements.sh
```
```sh
# Creamos las migraciones
python manage.py migrate
```
```sh
# Corremos el app
python manage.py runserver
```
```sh
# Accedemos a la ruta donde se encuentra el proyecto
http://127.0.0.1:8000/
```