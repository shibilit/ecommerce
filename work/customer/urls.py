from django.urls import path
from .import views
app_name = "customer"
urlpatterns = [
    path('home', views.home, name="home"),

    path('mycart', views.mycart, name="mycart"),
    path('myorder', views.myorder, name="myorder"),
    path('chge_pass', views.chge_pass, name="chge_pass"),
    path('profile', views.profile, name="profile"),
    path('product', views.product, name="product"),
    path('prod_dtls/ <int:pid>', views.prod_dtls, name="prod_dtls"),
    path('remove/<int:pid>', views.remove, name='remove')
    

]
