from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


def home(request):
    return render(request, 'ecom_admin/home.html')


def approve_seller(request):
    return render(request, 'ecom_admin/approve_seller.html')


def view_seller(request):
    return render(request, 'ecom_admin/view_seller.html')


def view_cust(request):
    return render(request, 'ecom_admin/view_cust.html')


def login(request):
    return render(request, 'ecom_admin/login.html')

@api_view(['GET'])
def index(request):
    message = "Congratulations, you have created an API"
    return Response(message)
