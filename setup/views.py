from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Subquery, OuterRef
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def setup(request):
    return render(request, "setup/setup.html")


@login_required
def supplierssetup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        balance = request.POST.get("balance")

        data = Supplier(
            name=name,
            address=address,
            balance=balance,
        )
        data.save()
    return render(request, "setup/suppliersetup.html")


@login_required
def market_setup(request):
    if request.method == "POST":
        area = request.POST.get("area")
        address = request.POST.get("address")
        market = Market(
            area=area,
            address=address,
        )
        market.save()
    return render(request, "setup/market_setup.html")


@login_required
def bank_setup(request):
    if request.method == "POST":
        bank_name = request.POST.get("bank_name")
        account_no = request.POST.get("account_no")
        branch = request.POST.get("branch")
        account_type = request.POST.get("account_type")

        Bank.objects.create(
            bank_name=bank_name,
            account_no=account_no,
            branch=branch,
            account_type=account_type,
        )

        return HttpResponseRedirect(reverse("bank_setup"))
    return render(request, "setup/bank_setup.html")


@login_required
def dsr_setup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        dsr = Dsr(
            name=name,
            phone=phone,
            email=email,
            address=address,
        )
        dsr.save()
    return render(request, "setup/dsr_setup.html")


@login_required
def salesmanager(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")

        sm = Salesmanager(
            name=name,
            phone=phone,
            email=email,
            address=address,
        )

        sm.save()

    return render(request, "setup/salesmanager.html")


@login_required
def collectionsetup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")

        clt = Collectionsetup(
            name=name,
            phone=phone,
            email=email,
            address=address,
        )
        clt.save()
    return render(request, "setup/collectionsetup.html")
