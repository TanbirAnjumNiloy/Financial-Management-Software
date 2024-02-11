from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse,HttpResponse
from django.db.models import Subquery, OuterRef
from django.utils import timezone
from django.db.models import Max
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import F
from django.contrib import messages
from django.shortcuts import render
from django.db.models import OuterRef, Subquery, Sum, Max
from django.urls import reverse
from django.shortcuts import get_object_or_404
from decimal import Decimal
from decimal import Decimal,InvalidOperation
from django.db import transaction
from .models import *
from setup.models import *
from decimal import Decimal
from django.db.models import Q

# Create your views here.




#  account start ------------------------------------------------------
@login_required
def account(request):
    return render(request,'account/account.html')


#  account start ------------------------------------------------------


#  lifting start ------------------------------------------------------
@login_required
def lifting(request):
    suppliers = Supplier.objects.all()
    total_lifting = Lifting.objects.aggregate(Sum('liftingpayment'))['liftingpayment__sum'] or 0
    total_sales = Sales.objects.aggregate(Sum('salestaka'))['salestaka__sum'] or 0
    current_balance = total_lifting - total_sales
    if request.method == 'POST':
        supplier_id = request.POST['supplier']
        lifting_payment = request.POST['lifting_payment']
        lifting_date = request.POST['lifting_date']

        supplier = Supplier.objects.get(id=supplier_id)
        new_lifting = Lifting(supplier=supplier, liftingpayment=lifting_payment, date=lifting_date)
        new_lifting.save()

        return redirect('account')  
    return render(request, 'account/lifting.html', {'suppliers': suppliers, 'current_balance': current_balance })




#  lifting End ------------------------------------------------------



#  sales start ------------------------------------------------------
@login_required
def sales(request):
    suppliers = Supplier.objects.all()
    dsrs = Dsr.objects.all()
    markets = Market.objects.all()

    total_lifting = Lifting.objects.aggregate(Sum('liftingpayment'))['liftingpayment__sum'] or 0
    total_sales = Sales.objects.aggregate(Sum('salestaka'))['salestaka__sum'] or 0
    current_balance = total_lifting - total_sales
    error_message = None

    if request.method == 'POST':
        supplier_id = request.POST['supplier']
        dsr_id = request.POST['dsr']
        market_id = request.POST['market']
        sales_type = request.POST['sales_type']
        sales_date = request.POST['sales_date']
        sales_taka = int(request.POST['salestaka'])

        if sales_taka > current_balance:
            error_message = "Insufficient balance, please lifting."
        else:
            supplier = Supplier.objects.get(id=supplier_id)
            dsr = Dsr.objects.get(id=dsr_id)
            market = Market.objects.get(id=market_id)

            new_sales = Sales(supplier=supplier, dsr=dsr, market=market, date=sales_date, salestaka=sales_taka, sales_type=sales_type)
            new_sales.save()

            return redirect('sales')

    return render(request, 'account/sales.html', {'suppliers': suppliers, 'dsrs': dsrs, 'markets': markets, 'total_lifting': total_lifting, 'current_balance': current_balance, 'error_message': error_message})

#  sales End ------------------------------------------------------



#  damage start ------------------------------------------------------
@login_required
def damage(request):
    suppliers = Supplier.objects.all()
    dsrs = Dsr.objects.all()
    markets = Market.objects.all()

    if request.method == 'POST':
        supplier_id = request.POST['supplier']
        dsr_id = request.POST['dsr']
        market_id = request.POST['market']
        damage_date = request.POST['date']
        damage_taka = request.POST['damage_taka']

        supplier = Supplier.objects.get(id=supplier_id)
        dsr = Dsr.objects.get(id=dsr_id)
        market = Market.objects.get(id=market_id)

        new_damage = Damage(supplier=supplier, dsr=dsr, market=market, date=damage_date, damagetaka=damage_taka)
        new_damage.save()

       
        return redirect('account')

    return render(request, 'account/damage.html', {'suppliers': suppliers, 'dsrs': dsrs, 'markets': markets})


#  damage End ------------------------------------------------------


# suppliers payment start ------------------------------------------------------
@login_required
def supplierspayment(request):
    suppliers = Supplier.objects.all()
    banks = Bank.objects.all()

    if request.method == 'POST':
        supplier_id = request.POST['supplier']
        bank_id = request.POST['bank']
        payment_amount = request.POST['amount']
        payment_date = request.POST['date']

        supplier = Supplier.objects.get(id=supplier_id)
        bank = Bank.objects.get(id=bank_id)

        new_payment = SupplierPayment(supplier=supplier, bank=bank, amount=payment_amount, date=payment_date)
        new_payment.save()

   
        return redirect('account')

    return render(request, 'account/supplierspayment.html', {'suppliers': suppliers, 'banks': banks})

# suppliers payment End ------------------------------------------------------







# daily cost start ------------------------------------------------------


@login_required
def dailycost(request):
    dsrs = Dsr.objects.all()

    if request.method == 'POST':
        dsr_id = request.POST['dsr']
        cost_date = request.POST['date']
        car_cost = request.POST['car_cost']
        dsr_bill = request.POST['dsr_bill']
        toll = request.POST['toll']
        other_cost = request.POST['other_cost']
        discription = request.POST['discription']

        dsr = Dsr.objects.get(id=dsr_id)

        new_daily_cost = Dailycost(
            dsr=dsr,
            date=cost_date,
            carcost=car_cost,
            dsrbill=dsr_bill,
            toll=toll,
            othercost=other_cost,
            discription=discription,
        )
        new_daily_cost.save()

        return redirect('account')

    return render(request, 'account/dailycost.html', {'dsrs': dsrs})




# daily cost End ------------------------------------------------------


@login_required
def redamage(request):
    suppliers = Supplier.objects.all()
    
    if request.method == 'POST':
        supplier_id = request.POST.get('supplier')
        supplier = Supplier.objects.get(id=supplier_id)  

        date = request.POST.get('date')
        amount = request.POST.get('amount')
        description = request.POST.get('description')

        data = Redamage(
            supplier=supplier,  
            date=date,
            amount=amount,
            description=description,
        )
        data.save()

    return render(request, 'account/redamage.html', {'suppliers': suppliers})


def displaybill(request):
    suppliers = Supplier.objects.all()

    if request.method == 'POST':
        supplier_id = request.POST.get('supplier')
        supplier = Supplier.objects.get(id=supplier_id)
        date = request.POST.get('date')
        amount = request.POST.get('display_bill')

        display_bill = Displaybill(supplier=supplier, date=date, amount=amount)
        display_bill.save()

        return redirect('displaybill') 

    return render(request, 'account/displaybill.html', {'suppliers': suppliers})



def claim(request):
    if request.method == 'POST':
        supplier_id = request.POST['supplier']
        date = request.POST['date']
        amount = request.POST['amount']

        supplier = Supplier.objects.get(pk=supplier_id)

        claim = Claim(supplier=supplier, date=date, amount=amount)
        claim.save()

        return redirect('claim')  

    suppliers = Supplier.objects.all()
    return render(request, 'account/claim.html', {'suppliers': suppliers})


   
def collection(request):
    current_amount = Decimal('0.00')

    if request.method == 'POST':
        collection_man_id = request.POST.get('collection-man')
        date = request.POST.get('date')
        transaction_type = request.POST.get('transaction-type')
        amount = Decimal(request.POST.get('amount'))

        collection_man = get_object_or_404(Collectionsetup, id=collection_man_id)
        latest_transaction = CollectionTransaction.objects.filter(collection_man=collection_man).last()

        if latest_transaction:
            current_amount = latest_transaction.current_amount

        if transaction_type == 'deposit':
            current_amount += amount
        else:
            current_amount -= amount

        transaction = CollectionTransaction(
            collection_man=collection_man,
            date=date,
            transaction_type=transaction_type,
            amount=amount,
            current_amount=current_amount
        )
        transaction.save()

    collection_men = Collectionsetup.objects.all()
    
    return render(request, 'account/collection.html', {'collection_men': collection_men, 'current_amount': current_amount})


