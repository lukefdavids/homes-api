from django.db import models
from django.contrib.auth.models import User
from .home import Home

class FavoriteHome(models.Model):
    home = models.ForeignKey(
        Home,
        on_delete=models.CASCADE,
        related_name='favorited_by'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_homes'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.home.address}"
    
    class Meta:
        verbose_name = "Favorite Home"
        verbose_name_plural = "Favorite Homes"
        unique_together = ('home', 'user')  # Prevent duplicate favorites
        ordering = ['-created_at']