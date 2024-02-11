from django.contrib import admin
from django.urls import path
from control import views

urlpatterns = [
    path('control/',views.control,name='control'),
    path('collectionmanname/',views.collectionmanname,name='collectionmanname'),
    path('damagebackdate/',views.damagebackdate,name='damagebackdate'),
    path('dailycostbackdate/',views.dailycostbackdate,name='dailycostbackdate'),
    path('displaybackdate/',views.displaybackdate,name='displaybackdate'),
]