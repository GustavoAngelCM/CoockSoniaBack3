from django.db import models

class Dominio(models.Model):
    NombreDominio = models.CharField(max_length=100)
    class Meta:
        db_table = 'Dominio'

class Reino(models.Model):
    NombreReino = models.CharField(max_length=100)
    class Meta:
        db_table = 'Reino'

class Filo(models.Model):
    NombreFilo = models.CharField(max_length=100)
    class Meta:
        db_table = 'Filo'

class Clase(models.Model):
    NombreClase = models.CharField(max_length=100)
    class Meta:
        db_table = 'Clase'

class Orden(models.Model):
    NombreOrden = models.CharField(max_length=100)
    class Meta:
        db_table = 'Orden'

class Familia(models.Model):
    NombreFamilia = models.CharField(max_length=100)
    class Meta:
        db_table = 'Familia'

class Genero(models.Model):
    NombreGenero = models.CharField(max_length=100)
    class Meta:
        db_table = 'Genero'

class Fosil(models.Model):
    CodigoFosil = models.CharField(max_length=25)
    NombreEspecie = models.CharField(max_length=100)
    GeneroID = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True, blank=True)
    FamiliaID = models.ForeignKey(Familia, on_delete=models.CASCADE, null=True, blank=True)
    OrdenID = models.ForeignKey(Orden, on_delete=models.CASCADE, null=True, blank=True)
    ClaseID = models.ForeignKey(Clase, on_delete=models.CASCADE, null=True, blank=True)
    FiloID = models.ForeignKey(Filo, on_delete=models.CASCADE, null=True, blank=True)
    ReinoID = models.ForeignKey(Reino, on_delete=models.CASCADE, null=True, blank=True)
    DominioID = models.ForeignKey(Dominio, on_delete=models.CASCADE, null=True, blank=True)
    Descripcion = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'Fosil'
