from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.index, name="index"),
    path('home/',views.home,name="homepage"),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name='signout'),
    path('register/',views.register,name="register"),
    path('profile/<int:id>/',views.profile_page, name="profile"),
    path('profile_edit/',views.account_edit,name="edit"),
    path('barber_edit/',views.barber_edit,name="barber_edit"),
]
