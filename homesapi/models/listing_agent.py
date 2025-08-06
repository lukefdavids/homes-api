from django.db import models

class ListingAgent(models.Model):    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)  
    image = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Listing Agent"
        verbose_name_plural = "Listing Agents"