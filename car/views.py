from django.shortcuts import render, redirect
from car.models import Car_Model, Purchase
from django.views.generic import DetailView
from car.forms import Comment_Form
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class All_details(DetailView):
    model = Car_Model
    template_name = 'car/details_view.html'
    pk_url_kwarg = 'id'
    
    @method_decorator(login_required, name='dispatch')
    def post(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return redirect('user_login')
        
        comment_form = Comment_Form(data= self.request.POST)
        data = self.get_object()
        if comment_form.is_valid():
            comment = comment_form.save(commit= False)
            comment.car = data
            comment.save()
       
        
        if 'buy_now' in request.POST:      
            product = self.get_object()
            if product.quantity > 0: 
                Purchase.objects.create(user = request.user, product = product)
                product.quantity -= 1
                product.save()
                return redirect("user_profile")        

        return self.get(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_object()
        comments = data.comments.all()
        comment_form = Comment_Form()
        context['data'] = data
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

    
        
        
        