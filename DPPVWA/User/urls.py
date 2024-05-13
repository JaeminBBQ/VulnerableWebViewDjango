from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("passwords/", views.passwords, name="passwords"),
    path("registerapi/", views.registerAPI, name="register_api"),
    path("loginapi/", views.loginAPI, name="login_api"),
    path("addpassword/", views.add_passwordAPI, name="add_pass_api"),
    path("getpassword/", views.get_passwordAPI, name="get_pass_api"),
    path("searchpassword/", views.search_passwordAPI, name="search_pass_api"),
]