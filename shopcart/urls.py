from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'shopcart'
urlpatterns = [

    path('', views.home, name='home'),
    path('home', views.home, name='home'),
]

