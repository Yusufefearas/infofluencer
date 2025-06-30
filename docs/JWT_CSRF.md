# ✅ 1. JWT ile Login Sistemi (DRF)
# -------------------------------
# Kurulum:
# pip install djangorestframework djangorestframework-simplejwt

# settings.py
INSTALLED_APPS += [
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProtectedAPIView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/protected/', ProtectedAPIView.as_view(), name='protected'),
]

# views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ProtectedAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Merhaba {request.user.username}, erişimin onaylandı!"})

# Açıklama:
# - Kullanıcı POST ile /api/token/ adresine kullanıcı adı + şifre gönderir
# - JWT token döner
# - Her API isteğinde Authorization header'ında token ile gelir
# - CSRF gerekmez, çünkü cookie kullanılmaz

# ✅ 2. CSRF ile Login Sistemi (Klasik Django)
# -------------------------------------------
# settings.py -> varsayılan session yapısı kullanılır
# Middleware'de CSRF zaten aktiftir

# urls.py
from django.urls import path
from .views import login_view, dashboard_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]

# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)  # Django session başlatır
            return redirect('dashboard')
    return render(request, 'login.html')


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {"user": request.user})

# login.html (form örneği)
'''
<form method="POST">
  {% csrf_token %}
  <input type="text" name="username" placeholder="Kullanıcı adı">
  <input type="password" name="password" placeholder="Şifre">
  <button type="submit">Giriş Yap</button>
</form>
'''

# Açıklama:
# - Form içindeki {% csrf_token %} ile güvenlik sağlanır
# - Kullanıcı giriş yaptıktan sonra session cookie atanır
# - request.user her sayfada otomatik olarak tanımlı olur
# - API yapılmaz, HTML template döner

# 🔁 Farklar:
# - JWT → mobil, frontend uygulamalarda kullanılır; header'da taşınır, CSRF gerekmez
# - CSRF → klasik form tabanlı yapılarda kullanılır; cookie ile çalışır, güvenlik için csrf_token gerekir


1. CSRF Neden Savunmasızdır?
🎯 CSRF (Cross-Site Request Forgery) nedir?
Kullanıcının tarayıcısındaki aktif oturumu kullanarak, onun adına işlem yapılmasıdır.

🧪 Örnek saldırı:
Sen infofluencer.com’a giriş yaptın → sessionid cookien var.
Sonra kötü niyetli bir siteye girdin → o site tarayıcında şunu yaptı:

<form action="https://infofluencer.com/profile/update" method="POST">
  <input name="bio" value="Hacked by evil">
  <input type="submit">
</form>
➡️ Tarayıcın, cookie’yi otomatik gönderdiği için bu işlem senin adına yapılır.
İşte bu CSRF’dir.

🛡️ Django çözümü ne?
csrf_token adında gizli bir input oluşturur

Sunucuya gelen her POST istekte bunu kontrol eder

Ancak:

Eğer csrf_token çalınırsa, saldırı yine mümkün olur

Mobil uygulamalar ve JS fetch’lerinde karmaşıklık yaratır

🛡️ 2. JWT Neden Daha Güvenilir?
Çünkü JWT:

Tarayıcıya otomatik gönderilmez

Explicit olarak Authorization: Bearer ... şeklinde header’a yazılır

Yani kullanıcı bir şey yapmadıkça kimlik taşımaz

📦 Örnek:
Sen bir token aldıktan sonra, onu bilinçli olarak şöyle yollarsın:

http
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
Eğer kötü niyetli bir site tarayıcında bir form POST etmeye çalışsa bile,
JWT token tarayıcıda otomatik gitmez.
Bu nedenle CSRF korumasına gerek kalmaz.

JWT sadece şununla çalınabilir:

XSS (tarayıcı içi script saldırısı)

localStorage’a erişim

Token’ın açık şekilde sızdırılması

Bunlara karşı da SameSite ve HttpOnly cookie kullanımı önerilir.

⚙️ 3. SPA (Single Page Application) Nedir?
SPA = Tek sayfalı uygulama.

🔁 Klasik Yapı:
Her sayfa tıklamasında sunucudan yeni bir HTML alınır

Tarayıcı ekranı yeniler

🔀 SPA:
Sayfa bir kez yüklenir

Sonra her şey JavaScript ile güncellenir

Sayfa yenilenmeden içerik değişir

🧠 Neden önemli?
Kullanıcı deneyimi çok hızlı olur

Mobil uygulama gibi çalışır

API kullanarak verileri parçalı çeker

Framework’ler:

React ✅

Vue ✅

Angular ✅

🧑‍💻 4. Modern JWT Login Sayfası Nasıl Olmalı?
🎨 Arayüz:
Giriş ekranı (React, Vue ya da basit HTML + JS)

Formdan veri al → fetch ile API’ye POST et

Sunucudan gelen access_token + refresh_token localStorage’a kaydet

🔒 Güvenlik:
Token’ları HttpOnly cookie olarak kaydedersen XSS’den korursun

API’lere erişimde Authorization: Bearer header’ı kullan

Refresh token süresi uzundur ama erişimi sınırlı tut

🛡️ Ekstra Koruma:
Rate limiting → DRF throttling

Token blacklisting (logout sonrası token geçersiz)

SameSite=Strict → cookie'yi başka domain'e gönderme

🧾 Özet Tablo
Özellik	CSRF	JWT
Kullanıcı tanıma	Cookie + Session	Token (Authorization header)
Otomatik taşınır mı?	✅ Evet	❌ Hayır
CSRF koruması gerekir mi?	✅ Gerekir	❌ Gerekmez
Mobil uyum	❌ Zor	✅ Kolay
API ile uyum	❌ Kısıtlı	✅ Uyumlu

🔚 Sonuç
JWT ile çalışan modern sistemler:

Frontend’ini ister React ister basit HTML/JS ile yapar

Giriş POST’unda token alır, depolar

Authorization header ile API’lere erişir

csrf_token kullanmaz

Mobil, masaüstü ve web için aynı backend’i kullanabilir

