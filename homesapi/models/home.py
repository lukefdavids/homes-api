from django.db import models
from django.contrib.auth.models import User
from .home_type import HomeType
from .listing_agent import ListingAgent

class Home(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='homes'
    )
    home_type = models.ForeignKey(
        HomeType,
        on_delete=models.PROTECT,  # Prevent deletion of HomeType if homes exist
        related_name='homes'
    )
    listing_agent = models.ForeignKey(
        ListingAgent,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='listings'
    )
    beds = models.PositiveIntegerField()
    bath = models.PositiveIntegerField()
    price = models.PositiveIntegerField()  
    sqft = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)  
    image = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now_add=True)    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.address}, {self.state} {self.zip}"
    
    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Homes"
        ordering = ['-created_at']  # Show newest listings first

