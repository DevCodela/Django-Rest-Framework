from django.conf.urls import patterns, include, url
from rest_framework import routers
from .views import NotaViewSet, CategoriaViewSet

router = routers.SimpleRouter()
router.register(r'notas', NotaViewSet)
router.register(r'categorias', CategoriaViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apisDjango.views.home', name='home'),
    url(r'^api/', include(router.urls)),
)
