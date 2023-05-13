# Procesaremos el contexto de la aplicación para el dark mode

# Creamos la función para procesar el contexto
def theme(request):

    # Si la sesion existe
    if 'is_dark_theme' in request.session:

        # Obtenemos el dark mode por medio del metodo get
        is_dark_theme = request.session.get('is_dark_theme')

        # Retornamos el contexto con el valor del dark mode
        return {'is_dark_theme': is_dark_theme}
    
    # Si no retornamos el contexto con el valor false
    return { 'is_dark_theme': False }