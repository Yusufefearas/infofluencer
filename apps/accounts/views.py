from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from apps.accounts.models import CompanyProfile,InfluencerProfile

FREE_EMAIL_DOMAINS = [
    'gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'icloud.com',
    'live.com', 'protonmail.com', 'gmx.com', 'mail.com', 'yandex.com'
]

def is_business_email(email):
    domain = email.split('@')[-1].lower()
    return domain not in FREE_EMAIL_DOMAINS

def company_register(request):
    errors = [] 

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            errors.append("Şifreler uyuşmuyor.")

        if User.objects.filter(username=email).exists():
            errors.append("Bu e-posta zaten kayıtlı.")

        if not is_business_email(email):
            errors.append("Lütfen iş e-posta adresinizi kullanın. (@gmail.com gibi adresler kabul edilmez)")

        if errors:
            return render(request, "accounts/company_register.html", {
                "errors": errors,
                "first_name": first_name,
                "last_name": last_name,
                "email": email
            })

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        CompanyProfile.objects.create(
            user=user,
            work_email=email,
            first_name=first_name,
            last_name=last_name
        )

        messages.success(request, "Kayıt başarılı. Giriş yapabilirsiniz.")
        return redirect("company_login")

    return render(request, "accounts/company_register.html")

def influencer_login(request):
    errors = []
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            errors.append("Lütfen tüm alanları doldurun.")
        else:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                            # 🔽 Influencer profili çekiyoruz
                try:
                    influencer_profile = InfluencerProfile.objects.get(user=user)
                except InfluencerProfile.DoesNotExist:
                    influencer_profile = None
                return render(request, "influencer/dashboard.html", {
                "influencer": influencer_profile
                })
            else:
                errors.append("Geçersiz e-posta veya şifre.")

    return render(request, "accounts/influencer_login.html", {"errors": errors})
    
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from apps.accounts.models import InfluencerProfile

def influencer_register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        errors = []

        if password != confirm_password:
            errors.append("Şifreler uyuşmuyor.")
        
        if User.objects.filter(username=email).exists():
            errors.append("Bu e-posta zaten kayıtlı.")

        if errors:
            return render(request, "accounts/influencer_register.html", {
                "errors": errors,
                "first_name": first_name,
                "last_name": last_name,
                "email": email
            })

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        InfluencerProfile.objects.create(
            user=user,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        return redirect("influencer_login")

    return render(request, "accounts/influencer_register.html")


def register_selection(request):
    if request.method == "POST":
        user_type = request.POST.get("user_type")
        if user_type == "company":
            return redirect("company_register")
        elif user_type == "influencer":
            return redirect("influencer_register")
        else:
            return redirect("register_select")  # boş seçim yapılırsa yine aynı sayfa

    return render(request, "register_select.html")

def company_login(request):
    error = None

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            try:
                # Firma mı kontrolü
                if hasattr(user, 'companyprofile'):
                    logout(request) 
                    request.session.flush()
                    login(request, user)
                    return redirect("company_dashboard")  # Firma paneline yönlendir
                else:
                    error = "Bu e-posta bir firma hesabına ait değil."
            except CompanyProfile.DoesNotExist:
                error = "Bu e-posta bir firma hesabına ait değil."
        else:
            error = "E-posta veya şifre hatalı."

    return render(request, "accounts/company_login.html", {"error": error})

def login_select(request):
    if request.method == "POST":
        user_type = request.POST.get("user_type")
        if user_type == "company":
            return redirect("company_login")
        elif user_type == "influencer":
            return redirect("influencer_login")
        else:
            return render(request, "accounts/login_select.html", {"error": "Lütfen giriş türünü seçin."})

    return render(request, "login_select.html")
