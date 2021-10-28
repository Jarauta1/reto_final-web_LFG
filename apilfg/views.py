# Creamos las vistas

# Importamos las vistas
from rest_framework import viewsets

# Importamos los serializers creados
from .serializers import ServerSerializer, GroupSerializer, UsersSerializer, MensageSerializer, ChannelSerializer

# Importamos los modelos creados
from .models import Server, Group, Users, Mensage, Channel

# Indicamos lo que debe serializar
class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all().order_by('server_id')
    serializer_class = ServerSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('group_id')
    serializer_class = GroupSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('user_id')
    serializer_class = UsersSerializer

class MensageViewSet(viewsets.ModelViewSet):
    queryset = Mensage.objects.all().order_by('mensage_id')
    serializer_class = MensageSerializer

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all().order_by('channel_id')
    serializer_class = ChannelSerializer