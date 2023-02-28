from django.urls import path
from .import views
app_name = 'common'
urlpatterns=[
     path('home',views.home, name="home"),
     path('cust_reg',views.cust_reg, name="cust_reg"),
     path('seller_reg',views.seller_reg, name="seller_reg"),
     path('cust_login',views.cust_login, name="cust_login"),
     path('seller_login',views.seller_login, name="seller_login")
]

