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
def report(request):
    return render(request,'report/report.html')

@login_required
def currentbalance(request):
    total_lifting = Lifting.objects.aggregate(Sum('liftingpayment'))['liftingpayment__sum']or 0
    total_sales = Sales.objects.aggregate(Sum('salestaka'))['salestaka__sum'] or 0
    current_balance = total_lifting - total_sales
    return render(request, 'report/currentbalance.html', {'current_balance': current_balance})
@login_required
def liftingreport(request):
    suppliers = Supplier.objects.all()

    if request.GET.get('search'):
        supplier_id = request.GET['supplier']
        from_date = request.GET['from-date']
        to_date = request.GET['to-date']

        filtered_lifts = Lifting.objects.filter(supplier=supplier_id, date__range=[from_date, to_date])
        total_filtered_lifts = filtered_lifts.aggregate(Sum('liftingpayment'))['liftingpayment__sum'] or 0

        return render(request, 'report/liftingreportresult.html', {'filtered_lifts': filtered_lifts, 'total_filtered_lifts': total_filtered_lifts})

    return render(request, 'report/liftingreport.html', {'suppliers': suppliers})



@login_required
def salesreport(request):
    suppliers = Supplier.objects.all()
    if request.method == 'GET' and 'search' in request.GET:
        supplier_id = request.GET['supplier']
        from_date = request.GET['from-date']
        to_date = request.GET['to-date']

        return redirect('salesreportresult', supplier_id=supplier_id, from_date=from_date, to_date=to_date)

    return render(request, 'report/salesreport.html', {'suppliers': suppliers})


from django.db.models import Sum, Case, When, IntegerField
@login_required
def salesreportresult(request, supplier_id, from_date, to_date):
    suppliers = Supplier.objects.all()
    
    sales_records = Sales.objects.filter(
        Q(supplier_id=supplier_id) & 
        Q(date__gte=from_date) & 
        Q(date__lte=to_date)
    ).select_related('dsr', 'market', 'supplier').annotate(
        psr_taka=Case(When(sales_type='psr', then='salestaka'), default=0, output_field=IntegerField()),
        holesale_taka=Case(When(sales_type='holesale', then='salestaka'), default=0, output_field=IntegerField()),
        retail_taka=Case(When(sales_type='retail', then='salestaka'), default=0, output_field=IntegerField()),
    ).order_by('date')

    total_psr_taka = sales_records.aggregate(total_psr_taka=Sum('psr_taka'))['total_psr_taka']
    total_holesale_taka = sales_records.aggregate(total_holesale_taka=Sum('holesale_taka'))['total_holesale_taka']
    total_retail_taka = sales_records.aggregate(total_retail_taka=Sum('retail_taka'))['total_retail_taka']

   
    profit_percentage_psr = 1
    profit_percentage_holesale = 3.5
    profit_percentage_retail = 5

    total_profit_psr = total_psr_taka * profit_percentage_psr / 100
    total_profit_holesale = total_holesale_taka * profit_percentage_holesale / 100
    total_profit_retail = total_retail_taka * profit_percentage_retail / 100

    context = {
        'suppliers': suppliers,
        'sales_records': sales_records,
        'total_psr_taka': total_psr_taka,
        'total_holesale_taka': total_holesale_taka,
        'total_retail_taka': total_retail_taka,
        'total_profit_psr': total_profit_psr,
        'total_profit_holesale': total_profit_holesale,
        'total_profit_retail': total_profit_retail
    }

    return render(request, 'report/salesreportresult.html', context)




@login_required
def damagereport(request):
    suppliers = Supplier.objects.all()

    if request.method == 'GET' and 'search' in request.GET:
        supplier_id = request.GET['supplier']
        from_date = request.GET['from-date']
        to_date = request.GET['to-date']

        return redirect(reverse('damage_report_result', args=[supplier_id, from_date, to_date]))

    return render(request, 'report/damagereport.html', {'suppliers': suppliers})


@login_required
def damage_report_result(request, supplier_id, from_date, to_date):
    damage_records = Damage.objects.filter(
        Q(supplier_id=supplier_id) &
        Q(date__gte=from_date) &
        Q(date__lte=to_date)
    ).select_related('dsr', 'market', 'supplier').order_by('date')

    total_damage_taka = sum(record.damagetaka for record in damage_records)

    return render(request, 'report/damagereportresult.html', {'damage_records': damage_records, 'total_damage_taka': total_damage_taka})



@login_required
def costreport(request):
    dsrs = Dsr.objects.all()

    if request.method == 'POST':
        dsr_id = request.POST['dsr']
        from_date = request.POST['from-date']
        to_date = request.POST['to-date']

        costs = Dailycost.objects.filter(dsr_id=dsr_id, date__range=(from_date, to_date))
        
        total_carcost = costs.aggregate(Sum('carcost'))['carcost__sum']
        total_dsrbill = costs.aggregate(Sum('dsrbill'))['dsrbill__sum']
        total_toll = costs.aggregate(Sum('toll'))['toll__sum']
        total_othercost = costs.aggregate(Sum('othercost'))['othercost__sum']

        context = {
            'costs': costs,
            'total_carcost': total_carcost,
            'total_dsrbill': total_dsrbill,
            'total_toll': total_toll,
            'total_othercost': total_othercost
        }

        return render(request, 'report/costreportresult.html', context)

    return render(request, 'report/costreport.html', {'dsrs': dsrs})


@login_required
def supplier_ledger_report (request):
    suppliers = Supplier.objects.all()
    return render(request, 'report/supplierledgerreport.html', {'suppliers': suppliers})




@login_required
def supplier_ledger_result(request):
    suppliers = Supplier.objects.all()

    if request.method == 'POST':
        supplier_id = request.POST['supplier']
        from_date = request.POST['from-date']
        to_date = request.POST['to-date']

        supplier = Supplier.objects.get(id=supplier_id)
        lifting_transactions = Lifting.objects.filter(supplier=supplier, date__range=(from_date, to_date))
        payment_transactions = SupplierPayment.objects.filter(supplier=supplier, date__range=(from_date, to_date))

        lifting_total = lifting_transactions.aggregate(Sum('liftingpayment'))['liftingpayment__sum']
        payment_total = payment_transactions.aggregate(Sum('amount'))['amount__sum']

        return render(request, 'report/supplierledgerresult.html', {
            'lifting_transactions': lifting_transactions,
            'payment_transactions': payment_transactions,
            'supplier': supplier,
            'lifting_total': lifting_total,
            'payment_total': payment_total,
        })

    return render(request, 'report/supplierledgerreport.html', {'suppliers': suppliers})

@login_required
def redamagetaka(request):
    redamage_data = Redamage.objects.all()
    return render(request, 'report/redamagetaka.html', {'redamage_data': redamage_data})

@login_required
def displaytaka(request):
    suppliers = Supplier.objects.all()
    return render(request,'report/displaytaka.html', {'suppliers': suppliers})


@login_required
def displaytakaresult(request):
    if request.method == 'POST':
        supplier_id = request.POST.get('supplier')
        from_date = request.POST.get('from-date')
        to_date = request.POST.get('to-date')

        supplier = Supplier.objects.get(id=supplier_id)
        display_bills = Displaybill.objects.filter(supplier=supplier, date__range=(from_date, to_date))

        total_display_bill = display_bills.aggregate(Sum('amount'))['amount__sum'] or 0

        context = {
            'display_bills': display_bills,
            'total_display_bill': total_display_bill,
        }

        return render(request, 'report/displaytakaresult.html', context)

    return redirect('displaytaka')

@login_required
def claimtaka(request):
    suppliers = Supplier.objects.all()
    return render(request,'report/claimtaka.html', {'suppliers': suppliers})
@login_required
def claimtakaresult(request):
    if request.method == 'POST':
        supplier_id = request.POST.get('supplier')
        from_date = request.POST.get('from-date')
        to_date = request.POST.get('to-date')

        supplier = Supplier.objects.get(id=supplier_id)
        claims = Claim.objects.filter(supplier=supplier, date__range=(from_date, to_date))

        total_claim = claims.aggregate(Sum('amount'))['amount__sum'] or 0

        context = {
            'claims': claims,
            'total_claim': total_claim,
        }

        return render(request, 'report/claimtakaresult.html', context)

    return redirect('claimtaka')

@login_required
def statement (request):
    collection_men = Collectionsetup.objects.all()
    return render(request, 'report/statement.html' , {'collection_men': collection_men })
    
from django.shortcuts import render, get_object_or_404
@login_required
def statementreportresult(request):
    if request.method == 'POST':
        collection_man_id = request.POST.get('collection-man')
        from_date = request.POST.get('from-date')
        to_date = request.POST.get('to-date')

        collection_man = get_object_or_404(Collectionsetup, id=collection_man_id)
        transactions = CollectionTransaction.objects.filter(
            collection_man=collection_man,
            date__range=(from_date, to_date)
        )

        return render(request, 'report/statementreportresult.html', {'transactions': transactions})

    return render(request, 'report/statementreportresult.html')


@login_required
def statementreportresultall(request):
    if request.method == 'POST':
        from_date = request.POST.get('from-date')
        to_date = request.POST.get('to-date')

        # Get all collection managers
        collection_men = Collectionsetup.objects.all()

      
        collection_balances = {}

        for collection_man in collection_men:
            transactions = CollectionTransaction.objects.filter(
                collection_man=collection_man,
                date__range=(from_date, to_date)
            )

            
            balance = Decimal('0.00')
            for transaction in transactions:
                if transaction.transaction_type == 'deposit':
                    balance += transaction.amount
                else:
                    balance -= transaction.amount

            
            collection_balances[collection_man] = balance

        return render(request, 'report/statementreportresultall.html', {'collection_balances': collection_balances})

    return render(request, 'report/statementreportresultall.html')

