from django.shortcuts import render, redirect


from common.models import Customer, Seller
from django.core.mail import send_mail
from django.conf import settings

import random

# Create your views here.


def home(request):
    return render(request, 'common/home.html')


def cust_reg(request):
    if request.method == "POST":
        cust_name = request.POST["c_text"]
        cust_gender = request.POST["c_gender"]
        cust_mail = request.POST["c_mail"]
        cust_phone = request.POST["c_phone"]
        cust_address = request.POST["c_address"]
        cust_password = request.POST["c_password"]
        cust_image = request.FILES["c_img"]

        new_customer = Customer(
            customer_name=cust_name,
            gender=cust_gender,
            ph_number=cust_phone,
            e_mail=cust_mail,
            address=cust_address,
            password=cust_password,
            image=cust_image

        )

        new_customer.save()
    return render(request, 'common/cust_reg.html')


def cust_login(request):
    msg = ''
    if request.method == 'POST':
        cust_mail = request.POST['c_mail']
        cust_password = request.POST['c_password']
        try:
            customer = Customer.objects.get(
                e_mail=cust_mail, password=cust_password)
            request.session['customer'] = customer.id
            return redirect('customer:home')
        except:
            msg = "Invalid Email ID or Password"

    return render(request, 'common/cust_login.html', {'msg': msg})


def seller_reg(request):
    if request.method == 'POST':
        s_name = request.POST['s_name']
        s_company_name = request.POST['s_company_name']
        s_account_num = request.POST['s_account_num']
        s_account_holder_name = request.POST['s_account_holder_name']
        s_ifsc = request.POST['s_ifsc']
        s_branch_name = request.POST['s_branch_name']
        s_ph_num = request.POST['s_ph_num']
        s_email = request.POST['s_email']
        s_address = request.POST['s_address']
        s_image = request.FILES['S_image']
        s_username = random.randint(1111, 9999)
        s_pass = 'sel-' + s_name.lower() + str(s_username)
        message = 'Hii your username is :' + \
            str(s_username) + 'temporary password is ' + s_pass
        
        new_seller = Seller(
            seller_name=s_name,
            company_name=s_company_name,
            acc_no=s_account_num,
            ifsc=s_ifsc,
            branch_name=s_branch_name,
            acc_holder_name=s_account_holder_name,
            ph_num=s_ph_num,
            email=s_email,
            address=s_address,
            image=s_image,
            user_name=s_username,
            password=s_pass
        )
        send_mail(
            'Username and Temporary Password',
            message,
            settings.EMAIL_HOST_USER,
            [s_email],
            fail_silently=False
        )
        new_seller.save()
    return render(request, 'common/seller_reg.html')


def seller_login(request):
    msg = ''
    if request.method == 'POST':
        s_username = request.POST['s_email']
        s_password = request.POST['s_pass']
        try:
            seller = Seller.objects.get(
                user_name=s_username, password=s_password)
            request.session['Seller'] = seller.id
            return redirect('seller:home')
        except:
            msg = "Invalid Email ID or Password"
    return render(request, 'common/seller_login.html', {'msg': msg})
