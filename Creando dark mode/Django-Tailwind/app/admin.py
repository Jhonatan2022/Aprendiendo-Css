from django.contrib import admin

# Importamos los modelos
from .models import Post
# Register your models here.


# Registramos el modelo
admin.site.register(Post)