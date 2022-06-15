from django.contrib import admin
from django.urls import path, include

from flowershopapp import views
import flowershopapp
urlpatterns = [
    path('', views.index,name='index'),
    path('login/',views.login,name='login'),
    path('reg/', views.reg, name='reg'),

    path('order/',views.order,name='order'),
    path('order_confirm/',views.order_confirm,name='order_confirm'),
    path('load-cities/', views.load_cities, name='ajax_load_cities'),
    path('logout/',views.logout,name='logout'),
    path('ordered/',views.ordered,name='ordered')
    ]