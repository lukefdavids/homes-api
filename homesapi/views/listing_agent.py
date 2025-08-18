from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from homesapi.models import ListingAgent
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


class ListingAgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListingAgent
        fields = ("id", "name", "email", "phone", "image")
        depth = 1


class ListingAgentViewSet(ViewSet):
    permission_classes=[AllowAny]
    def list(self, request):
        agents = ListingAgent.objects.all()
        serializer = ListingAgentSerializer(agents, many=True)
        return Response(serializer.data)