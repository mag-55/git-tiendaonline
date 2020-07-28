from django.db import models

# Create your models here.
# se crean las tablas aqui

class Clientes(models.Model): #generar tabla 
    nombre=models.CharField(max_length=30) #generar campos, models nos da el tipo y la capacidad del campoS
    direccion=models.CharField(max_length=50, verbose_name='La dirección') #asi modifico el label del panel
    email=models.EmailField(blank=True, null=True) #asi hago que un campo no sea obligatorio  
    telefono=models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):# esto transforma la informacion del objeto a string 
        return 'El nombre es %s, la seccion es %s y el precio es %s'%(self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

