from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from homesapi.models import ListingAgent, Home, HomeType, FavoriteHome
from .listing_agent import ListingAgentSerializer
from .home_type import HomeTypeSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class HomeSerializer(serializers.ModelSerializer):
    home_type = HomeTypeSerializer()
    listing_agent = ListingAgentSerializer()
    is_favorited = serializers.SerializerMethodField()
    
    class Meta:
        model = Home
        fields = ("id", "beds", "bath", "sqft", "price", "description", "address", "state", "zip", "image", "home_type", "listing_agent", "is_favorited")

    def get_is_favorited(self, obj):
        request=self.context.get('request')
        if request and request.user.is_authenticated:
            return FavoriteHome.objects.filter(user=request.user, home=obj).exists()
        return False

        


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

        try:
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
        except Home.DoesNotExist:
            return Response({'message': 'Home not found'}, status=status.HTTP_404_NOT_FOUND)

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
        # Return the currently authenticated Users Home if created
        try:
            home = Home.objects.get(user=request.user, is_active=True)
            serializer = HomeSerializer(home, context={'request': request})
            return Response(serializer.data)
        except Home.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
                        
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        user = request.user
        home = Home.objects.get(pk=pk)

        favorite, created = FavoriteHome.objects.get_or_create(user=user, home=home)
        if created:
            return Response({'message': 'Home favorited'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Already favorited'}, status=status.HTTP_200_OK)
    
    @favorite.mapping.delete
    def unfavorite(self, request, pk=None):
        user=request.user

        try:
            favorite = FavoriteHome.objects.get(user=user, home__pk=pk)
            favorite.delete()
            return Response({'message': 'Home unfavorited'}, status=status.HTTP_204_NO_CONTENT)
        except FavoriteHome.DoesNotExist:
            return Response({'message': 'Favorite not found'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def list_favorites(self, request):
        user = request.user
        favorites = FavoriteHome.objects.filter(user=request.user).select_related('home__home_type', 'home__listing_agent')
        homes = [favorite.home for favorite in favorites]
        serializer = HomeSerializer(homes, many=True, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)
