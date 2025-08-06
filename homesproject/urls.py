from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from homesapi.views import login_user, register_user, get_current_user

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', include(router.urls)),
    path('login', login_user),
    path('register', register_user),
]

