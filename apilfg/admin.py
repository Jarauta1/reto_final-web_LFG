from django.contrib import admin
from .models import Server, Group, Users, Mensage, Channel

# Registro de modelos

admin.site.register(Server)
admin.site.register(Group)
admin.site.register(Users)
admin.site.register(Mensage)
admin.site.register(Channel)