
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.store, name = 'store'),
    path('<slug:category_slug>/', views.store, name = "products_by_category"),
    path('search/', views.search, name='search'),

]
