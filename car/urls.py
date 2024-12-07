from django.urls import path
from . import views


urlpatterns = [
    path("details/<int:id>/", views.All_details.as_view(), name= 'all_details'),
    
]
