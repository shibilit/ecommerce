from django.urls import path
from .import views
app_name='ecom_admin'
urlpatterns=[
     path('home',views.home, name="home"),    
     path('approve_seller',views.approve_seller, name="approve_seller"), 
     path('view_seller',views.view_seller, name="view_seller"),
     path('view_cust',views.view_cust, name="view_cust"),
     path('login',views.login, name="login"),
     path('index',views.index,name='index')         
]

