from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import ProveedoresSerializer
from .models import Proveedores
# Create your views here.

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset=Proveedores.objects.all()
    serializer_class = ProveedoresSerializer

class ProvedoresList(generics.ListCreateAPIView):
    queryset=Proveedores.objects.all()
    serializer_class = ProveedoresSerializer

class ProvedoresDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Proveedores
    serializer_class = ProveedoresSerializer