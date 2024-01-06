from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm
from . import models


# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


def products(request):
    category = request.GET.get('category', 0)
    products = models.Product.objects.filter(category_id=int(category))
    context = { "category": category, 'products': products }
    return render(request, 'products.html', context)


def product(request, id):
    product = models.Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)