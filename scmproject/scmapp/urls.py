from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('account/', views.settings, name='account'),
    path('user/', views.userpage, name='userpage'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>', views.customer, name='customer'),

    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order")
]
