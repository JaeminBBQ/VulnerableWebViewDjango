from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("passwords/", views.passwords, name="passwords"),
    path("registerapi/", views.registerAPI, name="register_api"),
    path("loginapi/", views.loginAPI, name="login_api")
]