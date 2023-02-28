from django.urls import path
from .import views
app_name="seller"
urlpatterns = [
    path('home', views.home, name="home"),
    path('prod_ctlg', views.prod_ctlg, name="prod_ctlg"),
    path('add_prod', views.add_prod, name="add_prod"),
    path('updt_stock', views.updt_stock, name="updt_stock"),
    path('chge_pass', views.chge_pass, name="chge_pass"),
    path('profile', views.profile, name="profile"),
    path('rcnt_orders', views.rcnt_orders, name="cnt_orders"),
    path('order_history', views.order_history, name="order_history"),
    path('logout', views.logout, name="logout")
]
