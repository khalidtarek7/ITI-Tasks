from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
# Create your views here.
def pagesIndex(request): 
    return HttpResponse("hello from pages/index")

def test(request):
    listOfUsers=[{"name":"khalid", "age":"27", "salary":"1900"},{"name":"shaimaa", "age":"23","salary":"1500"},{"name":"mohamed", "age":"25","salary":"1200"}]
    dict= {"users": listOfUsers}
    return render(request,'khalid.html',dict)

def returnBase(request):
    return render(request,'base.html')

def returnAbout(request):
    return render(request,'about.html')

def returnContact(request):
    return render(request,'contact.html')

def viewCars(request):
    return render(request, 'cars.html', {"cars" : Car.objects.all().order_by('model')})