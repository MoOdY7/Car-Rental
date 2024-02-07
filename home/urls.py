from django.urls import path,include
from home.views import *
from car_dealer_portal import *
from customer_portal import *

from . import views 

urlpatterns = [
    path('', views.home_page, name='home_page'),
]

