from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product




def say_hello(request):
   
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set = Product.objects.filter(inventory=F('collection__id'))
    # query_set = Product.objects.order_by('unit_price','title')
    # query_set = Product.objects.order_by('unit_price','title').reverse()
    # query_set = Product.objects.all()[:5] # returns the first 5 products
    query_set = Product.objects.all()[5:10] # returns products from index 5 to index 9
    # product = Product.objects.order_by('unit_price')[0] # returns the first product with the lowest unit price
    # product = Product.objects.earliest('unit_price') # returns the first product with the lowest unit price
    # product = Product.objects.latest('unit_price') # returns the first product with the highest

    
    # query_set = Product.objects.order_by('-title')
    # query_set = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20)) means inventory less than 10 and unit price greater than or equal to 20
    # returns None if not found
    # exists = Product.objects.filter(pk=0).exists() # returns True or False
   

    

    return render(request,'hello.html',{'name':'Taha Waheed','products':list(query_set)})
