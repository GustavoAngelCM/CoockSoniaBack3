from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Dominio, Reino, Filo, Clase, Orden, Familia, Genero, Fosil
from .serializers import DominioSerializer, ReinoSerializer, FiloSerializer, ClaseSerializer, OrdenSerializer, FamiliaSerializer, GeneroSerializer, FosilSerializer

# Create your views here.

class DominioCL(generics.ListCreateAPIView):
    queryset = Dominio.objects.all()
    serializer_class = DominioSerializer

class ReinoCL(generics.ListCreateAPIView):
    queryset = Reino.objects.all()
    serializer_class = ReinoSerializer

class FiloCL(generics.ListCreateAPIView):
    queryset = Filo.objects.all()
    serializer_class = FiloSerializer

class ClaseCL(generics.ListCreateAPIView):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

class OrdenCL(generics.ListCreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class FamiliaCL(generics.ListCreateAPIView):
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer

class GeneroCL(generics.ListCreateAPIView):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class FosilCRUD(viewsets.ModelViewSet):
    queryset = Fosil.objects.all()
    serializer_class = FosilSerializer
