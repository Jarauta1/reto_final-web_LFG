# Configurar endpoints

from django.contrib import admin

# Importamos las urls que teníamos definidas dentro de nuestra api
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apilfg.urls')),
]
