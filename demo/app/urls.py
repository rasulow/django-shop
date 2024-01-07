from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('product/<int:id>/', views.product, name='product'),
    path('products/', views.products, name='products'),
    path('create-order/', views.create_order, name='create-order'),
]