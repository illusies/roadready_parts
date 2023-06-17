from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

def contact(request):
    return render(request, 'core/contact.html')

def shoppingcart(request):
    return render(request, 'core/shoppingcart.html')

def search(request):
    return render(request, 'core/search.html')

def tellus(request):
    return render(request, 'core/tellus.html')

def condition(request):
    return render(request, 'core/condition.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def serviceterms(request):
    return render(request, 'core/serviceterms.html')

def eula(request):
    return render(request, 'core/eula.html')

def aboutus(request):
    return render(request, 'core/aboutus.html')