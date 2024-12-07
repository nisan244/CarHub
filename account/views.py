from django.shortcuts import render, redirect
from account.forms import RegistrationForm, ChangeUserDataForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from car.models import Purchase


# Create your views here.

# -----------------------------------------

def user_signup(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            signup_form = RegistrationForm(req.POST)
            if signup_form.is_valid():
                signup_form.save()
                return redirect("user_login")
        else:
            signup_form = RegistrationForm()
        return render(req, 'account/signup.html', {'form' : signup_form})
    else:
        return redirect("user_profile")

   
# -----------------------------------------
   
class user_login(LoginView): 
    authentication_form = AuthenticationForm
    template_name = 'account/login.html'  
    success_url = reverse_lazy("account/login.html")
        
    def get_success_url(self):
        return reverse_lazy("user_profile")
    

# -----------------------------------------

@login_required
def user_logout(req):
    logout(req)
    return redirect("user_login")
    
# -----------------------------------------

@login_required
def user_profile(req):
    # if req.user.is_authenticated:
        purchases = Purchase.objects.filter(user = req.user)
        return render(req, 'account/profile.html', {'purchases' : purchases})
    # else:
    #     return redirect('user_login')

# -----------------------------------------

@login_required
def edit_profile(req):
    if req.method == "POST":
        update_form = ChangeUserDataForm(req.POST, instance = req.user)
        if update_form.is_valid():
            update_form.save()
            return redirect("user_profile")
    else:
        update_form = ChangeUserDataForm(instance = req.user)
    return render(req, 'account/edit_profile.html', {'form' : update_form})

# -----------------------------------------

@login_required
def change_pass(req):
    if req.method == "POST":
        change_form = PasswordChangeForm(req.user, req.POST)
        if change_form.is_valid():
            change_form.save()
            update_session_auth_hash(req, req.user)
            return redirect("user_profile")
            
    else:
        change_form = PasswordChangeForm(req.user)
        
    return render(req, 'account/change_pass.html', {'form' : change_form})



