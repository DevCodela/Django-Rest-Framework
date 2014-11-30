from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class Nota(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField()

	categoria = models.ForeignKey(Categoria, related_name='notas')

	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return 'Titulo: ' + self.titulo

	def titulo_minusculas(self):
		return self.titulo.lower()