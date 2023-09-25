# Dark mode con Django y Tailwind

![image](https://github.com/Jhonatan2022/Aprendiendo-Css/assets/101368711/063ea72b-4629-4171-8193-c117ba255aae)
![image](https://github.com/Jhonatan2022/Aprendiendo-Css/assets/101368711/163ebbbd-1b9a-4e1e-b93b-7eb5dfe1b72a)

# Requisitos

- [Python](https://www.python.org/downloads/)
- [Nodejs](https://nodejs.org/es/download/)
- [Django with Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html)

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
.\env\Scripts\activate
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

# Wwbs recomendadas
* [Tailwind CSS](https://tailwindcss.com/)
* [Django Tailwind](https://django-tailwind.readthedocs.io/en/latest/)
* [DarkMode Tailwind](https://tailwindcss.com/docs/dark-mode)