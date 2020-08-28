from django.db import models

# Create your models here.
class AudioGear(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return self.name