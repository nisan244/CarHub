from django.shortcuts import render
from car.models import Car_Model
from brand.models import Brand_Model

def all_categories(req):
    data = Car_Model.objects.all()
    categories = Brand_Model.objects.all()
    
    return render(req, 'home.html', {'data' : data, 'category' : categories})



def home(req, category_slug = None):
    data = Car_Model.objects.all()
    if category_slug is not None:
        category = Brand_Model.objects.get(slug = category_slug)
        data = Car_Model.objects.filter(brand = category)
    categories = Brand_Model.objects.all()
    
    return render(req, 'home.html', {'data' : data, 'category' : categories})



