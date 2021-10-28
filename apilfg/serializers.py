# Serializar el modelo de datos

# Importar los serializadores
from rest_framework import serializers

# Nos traemos los modelos de datos definidos en el MER
from .models import Server, Group, Users, Mensage, Channel

# Crear los serializadores para los modelos
class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = ('members', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('server_id', 'user_id', 'icon', 'group_name', 'members', 'channels')

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password', 'email', 'avatar', 'groups', 'msg')

class MensageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mensage
        fields = ('channel_id', 'user_id', 'msg', 'date', 'edited_date')

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ('group_id', 'channel_name', 'topic', 'wall')