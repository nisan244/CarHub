from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.user_signup, name= "user_signup"),
    path("login/", views.user_login.as_view(), name= "user_login"),
    path("logout/", views.user_logout, name= "user_logout"),
    path("profile/", views.user_profile, name= "user_profile"),
    path("profile/edit_profile/", views.edit_profile, name= "edit_profile"),
    path("profile/edit_profile/change_pass/", views.change_pass, name= "change_pass"),
    
]

