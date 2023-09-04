from django.db import models

# Create your models here.

class Clientes(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=40, verbose_name='Nombre')
    ape=models.CharField(max_length=40, verbose_name='Apellido Paterno')
    apm=models.CharField(max_length=40, verbose_name='Apellido Materno')
    dir= models.TextField(null=True, verbose_name='Direccion')
    foto = models.ImageField(upload_to='imagenes/',verbose_name='Foto',null=True)
    
    def __str__(self):
        fila= "id: " + str(self.id)+ "-"+ "Nombre: " + self.nom + "-" "Apellido Paterno: " + self.ape
        return fila

    def delete(self, using=None, keep_parents=False): #borrar  fotos del storage 
        self.foto.storage.delete(self.foto.name)
        super().delete



