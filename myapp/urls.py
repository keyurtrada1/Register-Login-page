from django.urls import path
from . import views

urlpatterns = [
    path('',views.registerpage,name="register"),
    path('fetchregdata',views.fetchregdata,name="fetchdata"),
    path('loginpage',views.loginpage,name="loginpage"),
    path('fetchlogindata',views.fetchlogindata,name="fetchlogindata"),
    path('dashboardpage',views.dashboardpage,name="dashboardpage"),
    path('logout',views.logout,name="logout"),
    path('dashboard',views.dashboardpage,name="dashboard")
]

