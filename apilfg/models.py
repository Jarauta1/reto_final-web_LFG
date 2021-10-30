from django.db import models
from django.conf import settings
from django.utils import timezone

# We create the MER models


# Server table with fields id (primary key), members and groups
class Server(models.Model):

    # Properties
    # Automatic ID, increases by one value with each new record
    server_id = models.BigAutoField(primary_key=True)
    members = models.JSONField(default=dict)
    groups = models.JSONField(default=dict)

    # Magic method
    def __str__(self):
        return self.server_id


# Users table with the fields id (primary key), password, email, a url for the avatar, groups to which the user
# belongs to and writings by the user
class Users(models.Model):

    # Properties
    # Automatic ID, increases by one value with each new record
    user_id = models.BigAutoField(primary_key=True)
    password = models.CharField(blank=True, max_length=50)
    email = models.EmailField('email', unique=True)
    avatar = models.TextField()
    discord_user = models.CharField(blank=True, max_length=50)
    epicgames_user = models.CharField(blank=True, max_length=50)
    steam_user = models.CharField(blank=True, max_length=50)
    groups = models.JSONField(default=dict)
    msg = models.JSONField(default=dict)

    # Magic method
    def __str__(self):
        return self.email


# Groups table with the fields id (primary key), with the foreign keys of server and user, url for the image
# of the icon, name of the group, members belonging to the group and channels owned by the group. icon, name
# of the group, members belonging to the group and channels owned by the group.
class Group(models.Model):

    # Properties
    # Automatic ID, increases by one value with each new record
    group_id = models.BigAutoField(primary_key=True)
    server_id = models.ForeignKey(Server, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    icon = models.CharField(blank=True, max_length=100)
    group_name = models.CharField(blank=True, max_length=50)
    members = models.JSONField(default=dict)
    channels = models.JSONField(default=dict)

    # Magic method
    def __str__(self):
        return self.group_name


# Table Channels with the fields id (primary key), the foreign key of the group to which the channel belongs,
# the name of the channel, the topic for the searches and a wall where to store the messages.
class Channel(models.Model):

    # Properties
    # Automatic ID, increases by one value with each new record
    channel_id = models.BigAutoField(primary_key=True)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    channel_name = models.CharField(blank=True, max_length=50)
    topic = models.CharField(blank=True, max_length=50)
    wall = models.JSONField(default=dict)

    # Magic method
    def __str__(self):
        return self.channel_name


# Table Message with the fields id (primary key), the foreign keys of the channel it belongs to and the user who
# writes it, the message written, the date it was written and the date it was edited.
class Message(models.Model):

    # Properties
    # Automatic ID, increases by one value with each new record
    msg_id = models.BigAutoField(primary_key=True)
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    msg = models.CharField(blank=True, max_length=250)
    date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(default=timezone.now)

    # Magic method
    def __str__(self):
        return self.msg
