from rest_framework import viewsets
from .models import Nota, Categoria
from .serializers import NotaSerializer, CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer

class NotaViewSet(viewsets.ModelViewSet):
	queryset = Nota.objects.all()
	serializer_class = NotaSerializer