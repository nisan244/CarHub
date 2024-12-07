from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name= 'home_page'),
    path("car/", include('car.urls')),
    path("account/", include('account.urls')),
    path("brand/", include('brand.urls')),
    path("", views.all_categories, name= 'all_categories'),
    path("category/<slug:category_slug>/", views.home, name= 'category_wise'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)