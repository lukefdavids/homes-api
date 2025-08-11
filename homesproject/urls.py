from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from homesapi.views import login_user, register_user, get_current_user, ListingAgentViewSet, HomeViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"agents", ListingAgentViewSet, "agent")
router.register(r"homes", HomeViewSet, "home")


urlpatterns = [
    path('', include(router.urls)),
    path('login', login_user),
    path('register', register_user),
    path('current_user', get_current_user)
    
]

