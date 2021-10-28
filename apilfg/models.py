from django.db import models
from django.conf import settings
from django.utils import timezone

# Creamos los modelos del MER

# Tabla Server con los campos id (primary key), members y groups
class Server(models.Model):
    # Propiedades
    server_id = models.BigAutoField(primary_key=True)  # ID automática, aumenta un valor en cada registro nuevo
    members = models.JSONField()
    groups = models.JSONField()

    # Método mágico
    def __str__(self):
        return self.server_id

# Tabla Users con los campos id (primary key), password, email, una url para el avatar, grupos a los que pertenece y escritos por el usuario
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

# Tabla Grupos con los campos id (primary key), con las foreigns keys de servidor y usuario, url para la imagen del icono,
# nombre del grupo, miembros que pertenecen al grupo y canales que posee el grupo
class Group(models.Model):
    # Propiedades
    group_id = models.BigAutoField(primary_key=True)  # ID automática, aumenta un valor en cada registro nuevo
    server_id = models.ForeignKey(Server, on_delete=models.CASCADE, on_update=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, on_update=models.CASCADE)
    icon = models.CharField(max_length=100)
    group_name = models.CharField(max_length=20)
    members = models.JSONField()
    channels = models.JSONField()

    # Método mágico
    def __str__(self):
        return self.group_name

# Tabla Canales con los campos id (primary key), la foreign key del grupo al que pertenece el canal, el nombre del canal,
# el topic para las busquedas y un muro donde almacenar los mensajes
class Channel(models.Model):
    # Propiedades
    channel_id = models.BigAutoField(primary_key=True)  # ID automática, aumenta un valor en cada registro nuevo
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, on_update=models.CASCADE)
    channel_name = models.CharField(max_length=50)
    topic = models.CharField(max_length=20)
    wall = models.JSONField()

    # Método mágico
    def __str__(self):
        return self.channel_name

# Tabla Mensaje con los campos id (primary key), las foreigns keys del canal que pertenece y usuario que lo escribe,
# el mensaje escrito, la fecha de escritura y la de edición
class Mensage(models.Model):
    # Propiedades
    msg_id = models.BigAutoField(primary_key=True)  # ID automática, aumenta un valor en cada registro nuevo
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE, on_update=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, on_update=models.CASCADE)
    msg = models.CharField(max_length=250)
    date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(default=timezone.now)

    # Método mágico
    def __str__(self):
        return self.msg