from django.db import models

class HomeType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Home Type"
        verbose_name_plural = "Home Types"