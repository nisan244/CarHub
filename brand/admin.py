from django.contrib import admin
from . import models

# Register your models here.

class Brand_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('brand_name',)}
    list_display = ['brand_name', 'slug']

admin.site.register(models.Brand_Model, Brand_Admin)

