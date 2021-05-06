from django.db import models

# Create your models here.
class Citizen(models.Model):
    
    first_name = models.CharField(max_length=200)
        
    sur_name = models.CharField(max_length=200)
        
    age = models.IntegerField()

    gender = models.CharField(max_length=10)
        
    mobile = models.IntegerField()
            
    email = models.EmailField(max_length=254)
        
    address = models.CharField(max_length=200)
        
    tribe = models.CharField(max_length=20)
        
    state = models.CharField(max_length=20)