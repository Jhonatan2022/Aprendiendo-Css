"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importamos admin para poder utilizar el administrador de Django
from django.contrib import admin

# Importamos path para la creación de rutas y include para incluir las rutas de nuestra aplicación
from django.urls import path, include

# Importamos las vistas de theme para el dark mode
from theme.views import change_theme
#---------------------------IMPORT LIBRARIES----------------------




#---------------------------CREATED VIEWS-------------------------
urlpatterns = [

    # Ruta para el administrador de Django 
    path('admin/', admin.site.urls),


    # Ruta para cambiar de tema claro a oscuro
    path('switch-theme/', change_theme, name="change-theme"),


    # Incluimos las rutas de nuestra aplicación
    path('', include('app.urls', namespace='app')),


    # Incluimos __reload__ para que se recargue el navegador cuando se haga un cambio
    path('__reload__/', include('django_browser_reload.urls')),
]
