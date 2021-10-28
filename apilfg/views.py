# Creamos las vistas

# Importamos las vistas
from rest_framework import viewsets

# Importamos los serializers creados
from .serializers import ServerSerializer, GroupSerializer, UsersSerializer, GroupSerializer, MensageSerializer, ChannelSerializer

# Importamos los modelos creados
from .models import Server, Group, Users, Mensage, Channel

# Indicamos lo que debe serializar
class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all().order_by('server_id')
    serializer_class = ServerSerializer