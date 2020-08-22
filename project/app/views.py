from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from .models import product
from .choices import type_demand
# Create your views here.

def home_page(request):
# this function is to render the homepage to our website with data fetch from database order by arrive_date,filter by available status and show 4 only
    products=product.objects.order_by('arrive_date').filter(is_available=True)[:4]

#this variable is to get all object from class product which is our data in database

    context={
        'products':products,
        'type_demand':type_demand,
    }
#then we set it to a variable where we can use it in our template to fetch our data from database

    return render(request,'html/dynamic/home.html',context)

def register(request):
    #just to show the register page
    return render(request,'html/pages/register.html')

def login(request):
    # just to show the login page
    return render(request,'html/pages/login.html')

def detail(request,product_id):
    #get_object_or_404 mean if there is such a page exist with a database(object), illustrate it. otherwise, show page not found(404)
    products = get_object_or_404(product,pk=product_id)
    context={
        'products':products,
        'type_demand':type_demand,
    }
    # just to show the detail page
    return render(request,'html/dynamic/detail.html',context)

def clothes(request):
    # just to show the clothes page
    # same functionality as the home-page in fetching database
    products = product.objects.all()

    context = {
        'products': products,
    }
    return render(request,'html/dynamic/clothes.html',context)

def jewelery(request):
    # just to show the jewelery page
    return render(request,'html/dynamic/jewelery.html')

def contact_us(request):
    # just to show the contact_us page
    return render(request,'html/pages/contact_us.html')

def about_us(request):
    return render(request,'html/pages/about_us.html')




#this search funcion render the search page



def search(request):
    # the query_search is used to get all the object in our database based On the order(order_by) and filter(.filter)
    query_search=product.objects.order_by('arrive_date').filter(is_available=True)
    #keywords
    # the keyword variable is used as a keyword from the search engine we get by(request.GET) if there is keyword then get that word store
        # then if it is stored, the query_search will execute by getting the object based on the(.filter)
        # name__icontaions=keywords mean if name variable in database consist of such keywords(the one from user), shows it.
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            query_search=query_search.filter(name__icontains=keywords)

    # if type is set then store the set type in temporary memory
    #then if it is stored, use it to filter the result we want from the database and query it back
    # type__iexact==type, the type has to be the exact same word you get from the user.

    if 'type' in request.GET:
        type=request.GET['type']
        if type:
            query_search=query_search.filter(type__iexact=type)

    context={
        'products':query_search,
    }

    return render(request,'html/dynamic/search.html',context)
