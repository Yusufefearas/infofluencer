from django.shortcuts import render,redirect
from django.contrib.auth import logout,login

def influencer_dashboard(request):
    return render(request,"influencer/dashboard.html")
def influencer_logout(request):
    logout(request)
    return redirect("home")