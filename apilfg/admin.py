from django.contrib import admin
from .models import Server, Group, Users, Message, Channel

# Model registration

admin.site.register(Server)
admin.site.register(Group)
admin.site.register(Users)
admin.site.register(Message)
admin.site.register(Channel)
