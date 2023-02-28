# from common.decorators import auth_customer

from django.shortcuts import render, redirect
from customer.models import Cart

from seller.models import Product
from common.models import Customer
from django.db.models import F

# Create your views here.


def home(request):
    customer = Customer.objects.get(id=request.session['customer'])
    return render(request, 'customer/home.html', {'data': customer})


def prod_dtls(request, pid):
    msg = ''
    product = Product.objects.get(id=pid)
    if request.method == 'POST':
        quantity = request.POST['qty']
        product_exist = Cart.objects.filter(
            product=pid, customer=request.session['customer']).exists()
        if not product_exist:
            item = Cart(customer_id=request.session['customer'], product_id=pid, quantity=quantity)
            item.save()
        else:
            msg = 'item already exist'
    context = {
        'product': product,
        'msg': msg
    }

    return render(request, 'customer/prod_dtls.html', context)


def mycart(request):
    
    cart_data = Cart.objects.filter(customer_id=request.session['customer']).annotate(total=F('product__prod_price')*F('quantity'))
    grand_total = 0
    for i in cart_data:
        grand_total = i.total+grand_total

    request.session['grand'] = grand_total
    context = {
        'data': cart_data,
        'grand_total': grand_total
    }
    return render(request, 'customer/mycart.html',context)


def myorder(request):
    return render(request, 'customer/myorder.html')


def chge_pass(request):
    return render(request, 'customer/chge_pass.html')


def profile(request):
    return render(request, 'customer/profile.html')


def product(request):
    product_data = Product.objects.all()
    return render(request, 'customer/product.html', {'data': product_data})


def remove(request, pid):
    remove_data = Cart.objects.filter(product_id=pid)
    remove_data.delete()
    return redirect('customer:mycart')
