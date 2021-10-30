# We add all the configuration and patterns of the routes.

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'server', views.ServerViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'user', views.UsersViewSet)
router.register(r'message', views.MessageViewSet)
router.register(r'channel', views.ChannelViewSet)

# We include url login
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
