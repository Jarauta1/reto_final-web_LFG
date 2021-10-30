# Serialise the data model


# Import serialisers
from rest_framework import serializers


# We bring with us the data models defined in the MER
from .models import Server, Group, Users, Message, Channel


# Create the serialisers for the models
class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = ('server_id', 'members', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('group_id', 'server_id', 'user_id', 'icon', 'group_name', 'members', 'channels')


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'password', 'email', 'avatar', 'discord_user', 'epicgames_user', 'steam_user',
                  'groups', 'msg')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('msg_id', 'channel_id', 'user_id', 'msg', 'date', 'edited_date')


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ('channel_id', 'group_id', 'channel_name', 'topic', 'wall')
