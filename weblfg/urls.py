# Configure endpoints

from django.contrib import admin

# We import the urls that we had defined within our api
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apilfg.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]
