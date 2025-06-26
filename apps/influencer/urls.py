from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/",views.influencer_dashboard,name="influencer_dashboard")    
]
