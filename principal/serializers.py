from rest_framework import serializers
from .models import Nota, Categoria

class NotaSerializer(serializers.HyperlinkedModelSerializer):
	titulo_minusculas = serializers.Field(source='titulo_minusculas')
	saludo = serializers.SerializerMethodField('saludar')
	saludo2 = serializers.SerializerMethodField('saludar2')

	class Meta:
		model = Nota

	def saludar(self, obj):
		return 'Hola mundo'

	def saludar2(self, obj):
		return 'adsasd'

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
	notas = NotaSerializer(many=True)

	class Meta:
		model = Categoria


class EjemploSerializer(serializers.Serializer):
	nombre = serializers.CharField(max_length=20)
	email = serializers.EmailField()