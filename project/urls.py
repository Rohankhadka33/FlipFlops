from django.contrib import admin
from django.urls import path, include
from . import views

# Django admin customization
urlpatterns = [
    path('', views.index, name='index'),
    path('shoes', views.shoes, name='shoes'),
    path('collection', views.collection, name='collection'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('product_create', views.product_create, name='product_create'),
    path('create', views.create, name='create'),
    path('authen', views.authen, name='authen'),
    path('logout', views.logout, name='logout'),
    path('billing', views.billing, name='billing'),
    path('adminpanel', views.adminpanel, name='adminpanel'),
    path('userpage', views.userpage, name='userpage'),
    path('orderpage', views.orderpage, name='orderpage'),
    path('contactpage', views.contactpage, name='contactpage'),
    path('Order_create', views.Order_create, name='Order_create'),
    path('deleteusers/<int:p_id>', views.deleteusers, name='deleteusers'),
    path('updateproduct/<str:p_id>', views.updateproduct, name='updateproduct'),
    path('deleteproducts/<int:p_id>', views.deleteproduct, name='deleteproducts'),
    path('deleteorder/<int:p_id>', views.deleteorder, name='deleteorder'),
    path('deletecontact/<int:p_id>', views.deletecontact, name='deletecontact')

]
