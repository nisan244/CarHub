from django.db import models

# Create your models here.

class Brand_Model(models.Model):
    brand_name = models.CharField(max_length= 200)
    slug = models.SlugField(max_length= 150)
    
    def __str__(self):
        return self.brand_name