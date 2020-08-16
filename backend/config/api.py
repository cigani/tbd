from rest_framework import routers
from apps.users.views import UserViewSet
from apps.flavor.views import FlavorViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = "/?"

# Users API

api.register(r"flavors", FlavorViewSet)
api.register(r"users", UserViewSet)
