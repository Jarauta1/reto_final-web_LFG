from django.db import models
from django.conf import settings
from django.utils import timezone

# Creamos los modelos del MER

class Server(models.Model):
    # Propiedades
    server_id = models.BigAutoField(primary_key=True)  # ID automática, aumenta un valor en cada registro nuevo
    members = models.JSONField()
    gropus = models.JSONField()

    # Método mágico
    def __str__(self):
        return self.server_id

class Users(models.Model):
    # Propiedades
    user_id = models.BigAutoField(primary_key=True)  # ID automática, aumenta un valor en cada registro nuevo
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    avatar = models.CharField(max_length=100)
    groups = models.JSONField()
    msg = models.JSONField()

    # Método mágico
    def __str__(self):
        return self.username

class Group(models.Model):
    # Propiedades
    group_id = models.BigAutoField(primary_key=True)  # ID automática, aumenta un valor en cada registro nuevo
    server_id = models.ForeignKey(Server, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    icon = models.CharField(max_length=100)
    group_name = models.CharField(max_length=20)
    members = models.JSONField()
    channels = models.JSONField()

    # Método mágico
    def __str__(self):
        return self.group_name

class Channel(models.Model):
    # Propiedades
    channel_id = models.BigAutoField(primary_key=True)  # ID automática, aumenta un valor en cada registro nuevo
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=50)
    topic = models.CharField(max_length=20)
    wall = models.JSONField()

    # Método mágico
    def __str__(self):
        return self.channel_name

class Mensage(models.Model):
    # Propiedades
    msg_id = models.BigAutoField(primary_key=True)  # ID automática, aumenta un valor en cada registro nuevo
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    msg = models.CharField(max_length=250)
    date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(default=timezone.now)

    # Método mágico
    def __str__(self):
        return self.msg