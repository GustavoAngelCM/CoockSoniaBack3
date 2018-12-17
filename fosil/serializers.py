from .models import Dominio, Reino, Filo, Clase, Orden, Familia, Genero, Fosil
from rest_framework import serializers

class DominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dominio
        fields = ('id', 'NombreDominio')

class ReinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reino
        fields = ['id', 'NombreReino']

class FiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filo
        fields = ['id', 'NombreFilo']

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id', 'NombreClase']

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = ['id', 'NombreOrden']

class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familia
        fields = ['id', 'NombreFamilia']

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'NombreGenero']

class FosilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fosil
        fields = [
            'id',
            'CodigoFosil',
            'NombreEspecie',
            'GeneroID',
            'FamiliaID',
            'OrdenID',
            'ClaseID',
            'FiloID',
            'ReinoID',
            'DominioID',
            'Descripcion',
        ]
