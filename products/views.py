from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
# function for main page
def index(request):
    db_products = Products.objects_all()
    return render(request, 'index.html', {'db_products':db_products})


def for_sale(request):
    return HttpResponse('For sale Products')
