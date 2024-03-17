from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage , name =""),
    path('register', views.register , name ="register"),
    path('login', views.my_login , name ="login"),
    path('dashboard', views.dashboard , name ="dashboard"),
    path('user-logout', views.user_logout , name ="user-logout"),
    path('form-2',views.form2 , name = "form-2"),
    path('form-3',views.form3 , name = "form-3"),
    path('form-4',views.form4 , name = "form-4"),
    path('form-5',views.form5 , name = "form-5"),

]