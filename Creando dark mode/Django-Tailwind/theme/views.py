# Importamos redirect para redireccionar a una ruta
from django.shortcuts import render, redirect

# Importamos httpresponseredirect para redireccionar a una ruta
from django.http import HttpResponseRedirect
#------------------------------IMPORT LIBREARIES--------------------------------




#------------------------------CREATED VIEWS------------------------------------
# Creamos la vista para cambiar de tema claro a oscuro
def change_theme(request, **kwargs):

    # Si la sesion es oscura la cambiamos a clara
    if 'is_dark_theme' in request.session:

        # Cambiamos el valor de la sesion a su contrario
        request.session['is_dark_theme'] = not request.session.get('is_dark_theme')

    # Si la sesion no existe la creamos
    else:

        # Creamos la sesion
        request.session['   is_dark_theme'] = True

    # Redireccionamos a la ruta anterior
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))