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


# products page
def products(request):
    category = request.GET.get('category', 0)
    search = request.GET.get('search', None)
    if category != 0:
        products = models.Product.objects.filter(category_id=int(category))
    elif search is not None:
        products = models.Product.objects.filter(name__icontains=search)
    else:
        products = models.Product.objects.all()
        
    context = { "category": category, 'products': products }
    return render(request, 'products.html', context)


# product-detail page
def product(request, id):
    product = models.Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)


# create-order page
@login_required(login_url='/login')
def create_order(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        note = request.POST.get('note')
        product_id = request.GET.get('product_id', 0)
        user_id = request.user.id
        models.Order.objects.create(phone_number=phone_number, user_id=user_id, product_id=product_id, note=note)
        return redirect('orders')
    return render(request, 'create_order.html') 


# create-product page
@login_required(login_url='/login')
def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        models.Product.objects.create(
            name=name,
            description=description,
            price=price,
            category_id=category_id,
            user_id=request.user.id,
            image1=image1,
            image2=image2,
            image3=image3,
            image4=image4,
            image5=image5,
        )
        return redirect('products')    
    category = models.Category.objects.all()
    context = {
        "category": category
    }
    return render(request, 'create_product.html', context)



# orders page
@login_required(login_url='/login')
def orders(request):
    orders = models.Order.objects.filter(user_id=request.user.id).order_by('-created_at')
    context = {
        'orders': orders
    }
    return render(request, 'orders.html', context)