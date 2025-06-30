# GÜVENLİ KİMLİK DOĞRULAMA VE TOKEN YÖNETİMİ REHBERİ
🧩 1. Neleri Şifrelemeliyim?
🎯 Şifrelenmesi gerekenler:
Veri	Sebep
OAuth access_token (Instagram, GA4)	Erişim yetkisi taşır, ele geçirilirse veri çekilir
refresh_token	Sürekli yeni access_token üretir, uzun ömürlüdür
Payment API Key’leri	Stripe/PayPal gibi servislerin key'leri çalınırsa işlem yapılabilir
Şifre	Django zaten hash’ler (PBKDF2, bcrypt)
Kullanıcıya özel hassas analiz verileri	(Opsiyonel) Gizlilik açısından şifrelenebilir

🔐 2. Ne ile Şifrelemeliyim?
✅ Fernet (AES tabanlı)
Simetrik şifreleme: Aynı key ile şifreler, çözer.

cryptography kütüphanesi kullanılır.


pip install cryptography

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

enc = f.encrypt(b"access_token_xyz")
dec = f.decrypt(enc)
➡️ Şifrelenmiş token’ları PostgreSQL içinde tutabilirsin.
➡️ .env içinde FERNET_KEY olarak saklanmalı.

🛡️ 3. CSRF Nedir? Ne işe yarar?
📌 CSRF: Cross-Site Request Forgery
Bir saldırgan, kullanıcı adına sahte istek gönderir.

🧪 Örnek saldırı:
Kullanıcı panelinizde: /profile/delete

Kullanıcı giriş yapmıştır (session/cookie aktif)

Saldırgan kullanıcıyı şu linke yönlendirir:

<img src="https://seninsiten.com/profile/delete" />
➡️ Kullanıcının cookie'si varsa istek başarılı olur ve profil silinir.

✅ Django çözümü:
CSRF token üretir ve her POST formuna koyar

Her istekte bu token formdan gelmezse reddeder

🔑 4. JWT Nedir? Kullanmalı mıyım?
📌 JWT: JSON Web Token
Kullanıcı giriş yaptığında ona verilen dijital “kimlik kartı”dır.

İçeriği:

{
  "sub": 123,
  "exp": 1712345678,
  "is_staff": true
}
JWT → Base64 + imza ile şifrelenmiştir.

🟢 Ne zaman kullanılır?
Frontend ayrıysa (React/Vue)

Mobil uygulaman varsa

Token bazlı stateless kimlik doğrulama istiyorsan

🔴 Ne zaman kullanma?
Sadece Django Template + session tabanlı isen, JWT gereksiz karmaşa getirir.

🔐 5. Session ve Cookie Yönetimi: Güvenli Prensipler
🗂️ Django Varsayılanı:
Kullanıcı giriş yapar → session cookie oluşur → bu cookie ile oturum sürer

⚠️ Riskler:
Cookie ele geçirilirse oturum da ele geçirilir (örnek: XSS)

🛡️ Güvenli Cookie / Session Yönetimi için Altın Kurallar
Ayar	Açıklama
SESSION_COOKIE_SECURE = True	HTTPS dışı oturum aktarımı engellenir
SESSION_COOKIE_HTTPONLY = True	JavaScript erişemez (XSS koruması)
CSRF_COOKIE_SECURE = True	CSRF token sadece HTTPS ile gönderilir
CSRF_COOKIE_HTTPONLY = True	JavaScript erişemez (opsiyonel)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True	Sekme kapanınca oturum biter (isteğe bağlı)

🔐 JWT kullanıyorsan:
Token’ı HttpOnly cookie içinde tut (localStorage kullanma)

Her API çağrısında Authorization: Bearer <token> header’ı kullan

💬 6. Django'da Token Saklama Yapısı Örneği (OAuth)

# models.py
from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet

class OAuthToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    encrypted_access_token = models.TextField()
    encrypted_refresh_token = models.TextField()
    expires_at = models.DateTimeField()

# utils/encryption.py
from cryptography.fernet import Fernet
import os

FERNET_KEY = os.environ.get("FERNET_KEY").encode()
cipher = Fernet(FERNET_KEY)

def encrypt(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt(text):
    return cipher.decrypt(text.encode()).decode()
➡️ Böylece tokenlarınız veritabanında şifreli, sistemde şeffaf şekilde dolaşır.

🧠 Özet: Ne Kullanmalıyım?
Kullanım Amacı	Öneri
Django Template + Server Side Login	✅ CSRF + Session (varsayılan)
Frontend ayrıysa (React/Vue vs.)	✅ JWT + Cookie
OAuth token saklama	✅ Fernet ile şifreleyip DB’ye yaz
Sensitive veriye erişim	✅ request.user kontrolü + permission sınıfı
Şifreler	❌ Kendin hashleme, Django otomatik yapar (User.set_password)

📌 Sonuç
Siz bir influencer–firma eşleşme platformu yapıyorsunuz:

Tokenlar dış API’lere erişim sağladığı için şifrelenmeli

Panel ayrıysa (subdomain) JWT + Cookie kullanmalısınız

Django klasik panelde kalacaksa CSRF + Session yeterlidir

