from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from homesapi.models import ListingAgent


class ListingAgentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ListingAgent
        fields = ("id", "name", "email", "phone", "image")
        depth = 1


class ListingAgentViewSet(ViewSet):

    def list(self, request):
        agents = ListingAgent.objects.all()
        serializer = ListingAgentSerializer(agents, many=True)
        return Response(serializer.data)