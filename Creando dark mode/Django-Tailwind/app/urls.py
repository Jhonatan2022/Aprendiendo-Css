# Importamos path para la creación de rutas
from django.urls import path

# Importamos las vistas de nuestra aplicación
from .views import *
#------------------------------------------------



# Declaramos el nombre de la aplicación
app_name = 'app'


#------------------------------------------------
# Creamos las rutas de nuestra aplicación
urlpatterns = [

    # Ruta para listar los datos de la base de datos
    path('', PostList.as_view(), name="main"),
]