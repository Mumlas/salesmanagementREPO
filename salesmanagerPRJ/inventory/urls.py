from django.urls import path
from . import views

urlpatterns = [  
    path('get-facilities/<int:branch_id>/', views.get_facilities, name='get_facilities'),
    path('get-products/<int:facility_id>/', views.get_products, name='get_products'),
    path('get-quantity/<int:product_id>/', views.get_quantity, name='get_quantity'),
    path('update/', views.update_inventory, name='update'),
    path('', views.getInventory, name='get_inventory')
]