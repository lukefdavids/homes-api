from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from homesapi.models import ListingAgent, Home, HomeType
from .listing_agent import ListingAgentSerializer
from .home_type import HomeTypeSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class HomeSerializer(serializers.ModelSerializer):
    home_type = HomeTypeSerializer()
    listing_agent = ListingAgentSerializer()
    class Meta:
        model = Home
        fields = ("id", "beds", "bath", "sqft", "price", "description", "address", "state", "zip", "image", "home_type", "listing_agent")
        


class HomeViewSet(ViewSet):

    def create(self, request):
        home = Home()
        home.beds = request.data["beds"]
        home.bath = request.data["bath"]
        home.sqft = request.data["sqft"]
        home.price = request.data["price"]
        home.description = request.data["description"]
        home.address = request.data["address"]
        home.state = request.data["state"]
        home.zip = request.data["zip"]
        home.image = request.data["image"]
        home.user = request.user

        home_type = HomeType.objects.get(pk=request.data["home_type"])
        home.home_type = home_type

        listing_agent = ListingAgent.objects.get(pk=request.data["listing_agent"])
        home.listing_agent = listing_agent

        home.save()

        serializer = HomeSerializer(home, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def list(self, request):
        homes = Home.objects.all()
        serializer = HomeSerializer(homes, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            home = Home.objects.get(pk=pk)
            serializer = HomeSerializer(home, context={'request': request})
            return Response(serializer.data)
        except Home.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        
    def update(self, request, pk):
        home = Home.objects.get(pk=pk)
        home.beds = request.data["beds"]
        home.bath = request.data["bath"]
        home.sqft = request.data["sqft"]
        home.price = request.data["price"]
        home.description = request.data["description"]
        home.address = request.data["address"]
        home.state = request.data["state"]
        home.zip = request.data["zip"]
        home.image = request.data["image"]
        home.user = request.user

        home_type = HomeType.objects.get(pk=request.data["home_type"])
        home.home_type = home_type

        listing_agent = ListingAgent.objects.get(pk=request.data["listing_agent"])
        home.listing_agent = listing_agent
        home.save()

        serializer = HomeSerializer(home, many=False, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            home = Home.objects.get(pk=pk)
            home.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Home.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def user_homes(self, request):
        try:
            home = Home.objects.get(user=request.user, is_active=True)
            serializer = HomeSerializer(home, context={'request': request})
            return Response(serializer.data)
        except Home.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
                        