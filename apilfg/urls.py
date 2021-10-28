# Añadimos toda la configuración y patrones de las rutas

from django.urls import include, pathlib
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.resgister(r'server', views.ServerViewSet)
router.register(r'group', views.GroupsViewSet)
router.register(r'user', views.UsersViewSet)
router.register(r'mensage', views.MensageViewSet)
router.register(r'channel', views.ChannelViewSet)

# Incluimos url login
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]