# Importamos path para la creación de rutas
from django.urls import path

# Importamos las vistas de nuestra aplicación
from .views import *
#------------------------------------------------




#------------------------------------------------
# Creamos las rutas de nuestra aplicación
urlpatterns = [

    # Ruta para listar los datos de la base de datos
    path('', PostList.as_view(), name='main'),


    # Ruta para ver los detalles de un registro
    path('detail/<int:pk>', PostDetail.as_view(), name='detail'),
]