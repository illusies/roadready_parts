from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('shoppingcart/', views.shoppingcart, name='shoppingcart'),
    path('tellus/', views.tellus, name='tellus'),
    path('condition/', views.condition, name='condition'),
    path('privacy/', views.privacy, name='privacy'),
    path('serviceterms/', views.serviceterms, name='serviceterms'),
    path('eula/', views.eula, name='eula'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path("logout/", views.logout_request, name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]