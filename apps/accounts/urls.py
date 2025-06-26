from django.urls import path
from . import views

urlpatterns = [
    path("register/company", views.company_register, name="company_register"),
    path("login/company", views.company_login, name="company_login"),
    path("register/influencer", views.influencer_register, name="influencer_register"),
    path("register/", views.register_selection, name="register_home"),
    path("login/",views.login_select,name="login_selects"),
    path("login/influencer/",views.influencer_login,name="influencer_login")
]