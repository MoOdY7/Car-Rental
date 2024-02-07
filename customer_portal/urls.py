from django.urls import path,include
from customer_portal.views import *
from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('auth/', views.auth_view, name='auth_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
    path('registration/', views.registration, name='registration'),
    path('search/', views.search, name='search'),
    path('search_results/', views.search_results, name='search_results'),
    path('rent/', views.rent_vehicle, name='rent_vehicle'),
    path('confirmed/', views.confirm, name='confirm'),
    path('manage/', views.manage, name='manage'),
    path('update/', views.update_order, name='update_order'),
    path('delete/', views.delete_order, name='delete_order'),
]


urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('auth/', views.auth_view, name='auth_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
    path('registration/', views.registration, name='registration'),
    path('search/', views.search, name='search'),
    path('search_results/', views.search_results, name='search_results'),
    path('rent/', views.rent_vehicle, name='rent_vehicle'),
    path('confirmed/', views.confirm, name='confirm'),
    path('manage/', views.manage, name='manage'),
    path('update/', views.update_order, name='update_order'),
    path('delete/', views.delete_order, name='delete_order'),
]
