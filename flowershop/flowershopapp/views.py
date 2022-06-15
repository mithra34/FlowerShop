from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import context
from .forms import Customerform

from .models import Flower, Branches, Subbranches


# Create your views here.
def index(request):
    return render(request, "base.html",)
def  login(request):
    return render(request, "login.html")
def reg(request):
    return render(request,"reg.html")
def order(request):
    return render(request,"order.html")
def order_confirm(request):
    d_page = None
    f_list=None


    d_page=Branches.objects.all().filter()
    f_list=Flower.objects.all().filter()
    # d_id=int(request.data.get('branch'))
    # if sub in request.GET:
    #     d_list=request.GET['sub']

        # sub_list=Subbranches.objects.all().filter(Q(branch__contains=d_list))
    return render(request, "order_confirm.html",{'branch':d_page,'flower':f_list})
def load_cities(request):

    country_id = request.GET.get('country_id')
    # country_id = request.GET.get('country_id')
    # cities = Subbranches.objects.all().filter(branch_id=country_id)
    cities = Subbranches.objects.filter(branch_id=country_id).all()

    return render(request,"new.html", {'cities': cities})

def logout(request):
    return render(request,'login.html')
def ordered(request):
    msg="Your Order Placed"
    return render(request,'ordered.html',{'msg':msg})