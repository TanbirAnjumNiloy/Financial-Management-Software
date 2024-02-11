from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render,redirect
from django.db.models import Sum
from django.db.models import Q
from django.db.models import Sum
from datetime import datetime
from .models import *
from account.models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def control(request):
    return render(request, 'control/control.html')
@login_required
def collectionmanname(request):
    if request.method == 'POST':
       
        updated_name = request.POST.get('updated_name')
        collection_id = request.POST.get('collection_id')
        collection_to_update = Collectionsetup.objects.get(id=collection_id)
        collection_to_update.name = updated_name
        collection_to_update.save()

    collection_men = Collectionsetup.objects.all()
    return render(request, 'control/collectionmanname.html', {'collection_men': collection_men})

def damagebackdate(request):
    damages = Damage.objects.all()  
    if request.method == 'POST':
        damage_id = request.POST['damage']
        new_date = request.POST['new_date']
        
        damage_to_update = Damage.objects.get(id=damage_id)
        damage_to_update.date = new_date 
        damage_to_update.save() 
        
        return redirect('damagebackdate')  
    
    return render(request, 'control/damagebackdate.html', {'damages': damages})


def dailycostbackdate(request):
    daily_costs = Dailycost.objects.all()  
    
    if request.method == 'POST':
        daily_cost_id = request.POST['daily_cost']
        new_date = request.POST['new_date']
        
        daily_cost_to_update = Dailycost.objects.get(id=daily_cost_id)
        daily_cost_to_update.date = new_date  
        daily_cost_to_update.save()  
        
        return redirect('dailycostbackdate')
    
    return render(request, 'control/dailycostbackdate.html', {'daily_costs': daily_costs})

def displaybackdate(request):
    display_bills = Displaybill.objects.all()  
    
    if request.method == 'POST':
        display_bill_id = request.POST['display_bill']
        new_date = request.POST['new_date']
        
        display_bill_to_update = Displaybill.objects.get(id=display_bill_id)
        display_bill_to_update.date = new_date  
        display_bill_to_update.save()  
        
        return redirect('displaybackdate')  
    
    return render(request, 'control/displaybackdate.html', {'display_bills': display_bills})


