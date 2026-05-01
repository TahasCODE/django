from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F, DecimalField
from django.db.models.aggregates import Count,Min,Max,Avg,Sum
from django.db.models import Value,Func,ExpressionWrapper
from django.db.models.functions import Concat
from store.models import Product,OrderItem,Order,Customer




def say_hello(request):
    
    #query_set = Customer.objects.annotate(is_new=Value(True))

    # query_set = Customer.objects.annotate(
    #    full_name=Func(F('first_name'),Value(' '),F('last_name'),function='CONCAT')) // Using Func

    # query_set = Customer.objects.annotate(
    #   full_name = Concat('first_name',Value(' '),'last_name')  
    # )

    discounted_price = ExpressionWrapper(F('unit_price')*0.8,output_field=DecimalField())
   
    query_set = Product.objects.annotate(
       discounted_price=discounted_price)


    # query_set = Customer.objects.annotate(
    #   orders_count = Count('order'))  
    

    #result = Product.objects.aggregate(count=Count('id'),min_price=Min('unit_price'),max_price=Max('unit_price'),avg_price=Avg('unit_price'),sum_price=Sum('unit_price'))
    
    #query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5] # returns a list of orders with their customer data in a single query

    #query_set = OrderItem.objects.values('product_id').distinct() # returns a list of dictionaries with product_id of order items
    #query_set = Product.objects.prefetch_related('promotions').select_related('collection').all() # returns a list of products with their promotions data in a single query
    #query_set = Product.objects.select_related('collection').all() # returns a list of products with their collection data in a single query
    #query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title') # returns a list of products that are in order items
    #query_set = Product.objects.only('id','title')
     #query_set = Product.objects.defer('description')
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set = Product.objects.filter(inventory=F('collection__id'))
    # query_set = Product.objects.order_by('unit_price','title')
    # query_set = Product.objects.order_by('unit_price','title').reverse()
    # query_set = Product.objects.all()[:5] # returns the first 5 products
    #query_set = Product.objects.all()[5:10] # returns products from index 5 to index 9
    # query_set = Product.objects.values_list('id','title','collection__title') # returns a list of dictionaries with id and title of products
    # product = Product.objects.order_by('unit_price')[0] # returns the first product with the lowest unit price
    # product = Product.objects.earliest('unit_price') # returns the first product with the lowest unit price
    # product = Product.objects.latest('unit_price') # returns the first product with the highest

    
    # query_set = Product.objects.order_by('-title')
    # query_set = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20)) means inventory less than 10 and unit price greater than or equal to 20
    # returns None if not found
    # exists = Product.objects.filter(pk=0).exists() # returns True or False
   

    

    return render(request,'hello.html',{'name':'Taha Waheed','result':list(query_set)})
