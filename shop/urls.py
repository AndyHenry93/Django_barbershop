from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('',views.index,name="homepage"),
    path('signin/',views.signin,name="signin"),
    path('register/',views.register,name="register"),
]
