from django.db import models

# Create your models here.
class Appartments(models.Model):
    name = models.CharField(max_length=62, null=True)
    numberOfAp = models.IntegerField()

    
