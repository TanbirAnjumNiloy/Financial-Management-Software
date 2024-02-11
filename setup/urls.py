from django.contrib import admin
from django.urls import path
from setup import views

urlpatterns = [
    path('setup/',views.setup,name='setup'),
    path('supplierssetup/', views.supplierssetup, name='supplierssetup'),
    path('market_setup/', views.market_setup, name='market_setup'),
    path('bank_setup/', views.bank_setup, name='bank_setup'),
    path('dsr_setup/', views.dsr_setup, name='dsr_setup'),
    path('salesmanager/', views.salesmanager, name='salesmanager'),
    path('collectionsetup/', views.collectionsetup, name='collectionsetup'),
    ]