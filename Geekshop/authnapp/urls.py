from django.urls import path

import authnapp.views as authnapp

app_name = "authnapp"

urlpatterns = [
    path("login/", authnapp.login, name="login"),
    path("logout/", authnapp.logout, name="logout"),
    path("register/", authnapp.register, name="register"),
    path("edit/", authnapp.edit, name="edit"),
]
