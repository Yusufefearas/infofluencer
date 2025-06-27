from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/",views.influencer_dashboard,name="influencer_dashboard"),
    path("logout/",views.influencer_logout,name="influencer_logout"),
]
