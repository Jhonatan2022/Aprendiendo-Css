from django.db import models

# Create your models here.


# Creamos un modelo de post sencillo
class Post(models.Model):

    tittle = models.CharField(max_length=50)
    description = models.TextField()


    # Creamos un método para retornar el título del post
    def __str__(self):

        # Restornamos el titulo para uqe se pueda ver en el panel de administración
        return self.tittle

