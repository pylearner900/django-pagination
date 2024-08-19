from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media")
    
    def __str__(self):
        return self.name