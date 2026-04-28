from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product




def say_hello(request):
   
    query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20)) means inventory less than 10 and unit price greater than or equal to 20
    # returns None if not found
    # exists = Product.objects.filter(pk=0).exists() # returns True or False
   

    

    return render(request,'hello.html',{'name':'Taha Waheed','products':list(query_set)})
