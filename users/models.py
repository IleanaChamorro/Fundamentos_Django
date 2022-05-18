from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField("El nombre de la persona" ,max_length=30)
    last_name = models.CharField("El apellido de la persona" ,max_length=30)
    #Nombre Verbose 
    cars = models.ManyToManyField('Car', verbose_name='Los carros del usuario')


STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted')
)

class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['rating']
        db_table = 'website_custom_table_name'
        verbose_name = 'La Pagina Web'
        verbose_name_plural = 'Las Paginas'

        
class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)