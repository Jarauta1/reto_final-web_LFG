# Configure endpoints

from django.contrib import admin

# We import the urls that we had defined within our api
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apilfg.urls')),
]
