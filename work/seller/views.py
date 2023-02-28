from django.shortcuts import render, redirect

from common.models import Seller
from seller.models import Product

# Create your views here.


def home(request):
    seller_data = Seller.objects.get(id=request.session['Seller'])
    return render(request, 'seller/home.html', {'data': seller_data})


def prod_ctlg(request):
    product_list = Product.objects.filter(seller_id=request.session['Seller'])
    return render(request, 'seller/prod_ctlg.html', {'products': product_list})


def add_prod(request):

    #   /////////for displaying seller data
    seller_data = Seller.objects.get(id=request.session['Seller'])

    if request.method == 'POST':
        product_name = request.POST['prod_name']
        product_num = request.POST['prod_num']
        product_des = request.POST['prod_des']
        product_stock = request.POST['prod_stock']
        product_price = request.POST['prod_price']
        product_image = request.FILES['prod_image']

        add_product = Product(
            seller_id=request.session['Seller'],
            prod_name=product_name,
            prod_num=product_num,
            prod_des=product_des,
            prod_stock=product_stock,
            prod_price=product_price,
            prod_image=product_image
        )
        add_product.save()
    return render(request, 'seller/add_prod.html', {'data': seller_data})

def updt_stock(request):
    return render(request, 'seller/updt_stock.html')


def chge_pass(request):
    return render(request, 'seller/chge_pass.html')


def profile(request):
    return render(request, 'seller/profile.html')


def rcnt_orders(request):
    return render(request, 'seller/rcnt_orders.html')


def order_history(request):
    return render(request, 'seller/order_history.html')


def logout(request):
    del request.session['Seller']
    request.session.flush()
    return redirect('common:home')
