from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("hello1/", hello),
    path("hello3/",hello3,name='hello3'),
    path("",homepage,name='homepage'),
    path("t/",travelpackage,name='travel package'),
    path("print2/",print1,name='print1'),
    path("t2/",print_to_console, name='print_to_console'),
    path("ran/",random123,name='random123'),
    path("tm/",datetime1),
    path("tm1/",get_date),
    path ("tz/",tz,name='tz'),
    path("tk/",register_function,name="register_function"),
    path("tkk/",pagecall,name="pagecall"),
    path("ttt/",pie_chart,name="pie_chart"),
    path("tmm/",slides,name="slides"),
    path("wh/",weatherlogic,name='weatherlogic'),
    path("wh1/",weather1,name='weather1'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('login1/',login1,name='login1'),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),
]

