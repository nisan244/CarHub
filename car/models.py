from django.db import models
from brand.models import Brand_Model
from django.contrib.auth.models import User


# Create your models here.


class Car_Model(models.Model):
    name = models.CharField(max_length= 150)
    price = models.CharField(max_length= 20)
    Description = models.TextField()
    quantity = models.IntegerField()
    img = models.ImageField(upload_to= 'uploads/')
    brand = models.ForeignKey(Brand_Model, on_delete= models.CASCADE, related_name= 'cars')
    
    
    def __str__(self):
        return self.name
    
    

class Comment(models.Model):
    name = models.CharField(max_length= 150)
    email = models.EmailField()
    body = models.TextField()
    time = models.DateTimeField(auto_now_add= True)
    
    car = models.ForeignKey(Car_Model, on_delete= models.CASCADE, related_name= 'comments')
    
    
    def __str__(self):
        return f"Comments by {self.name}"
    
    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Car_Model, on_delete= models.CASCADE)
    time = models.DateTimeField(auto_now_add= True)
    
    
    def __str__(self):
        return f"{self.user.username} bought {self.product.name}"
    
    