# Importamos render para renderizar las vistas
from django.shortcuts import render

# Importamos listview para listar los datos de la base de datos
# Importamos DetailView para ver los detalles de un registro
from django.views.generic import ListView, DetailView

# Importamos los modelos
from .models import Post
#------------------------------------------------




#------------------------------------------------
# Creamos una clase para listar los datos de la base de datos
class PostList(ListView):

   # Le decimos que modelo va a listar
    model = Post

    # Le decimos que template va a utilizar
    template_name = 'main.html'

    # Le decimos que el contexto se va a llamar posts
    context_object_name = 'posts'