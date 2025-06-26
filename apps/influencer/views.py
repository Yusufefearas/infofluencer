from django.shortcuts import render

def influencer_dashboard(request):
    return render(request,"influencer/dashboard.html")
