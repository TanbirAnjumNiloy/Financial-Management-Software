from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('account/',views.account,name='account'),
    path('lifting/',views.lifting,name='lifting'),
    path('sales/',views.sales,name='sales'),
    path('damage/', views.damage, name='damage'),
    path('supplierspayment/', views.supplierspayment, name='supplierspayment'),
    path('dailycost/', views.dailycost, name='dailycost'),
    path('redamage/', views.redamage, name='redamage'),
    path('displaybill/', views.displaybill, name='displaybill'),
    path('claim/', views.claim, name='claim'),
    path('collection/', views.collection, name='collection'),



]