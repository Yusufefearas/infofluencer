# Proje Hakkında Sorular
## Wordpress + Django Hibrit Mimari (Split Interface Architecture / Decoupled Website)

| Katman             | Subdomain                      | Teknoloji                      | Amaç                                                                  |
| ------------------ | ------------------------------ | ------------------------------ | --------------------------------------------------------------------- |
| Ana Sayfa (vitrin) | `https://infofluencer.com`     | WordPress (Litespeed Hosting)  | Home, FAQ, Pricing, İletişim gibi statik sayfalar                     |
| Uygulama Paneli    | `https://app.infofluencer.com` | Django + PostgreSQL + Tailwind | Giriş yapan kullanıcıların token bazlı özel analiz ve OAuth işlemleri |

| Bileşen      | Hosting Türü                                     | Açıklama                                             |
| ------------ | ------------------------------------------------ | ---------------------------------------------------- |
| WordPress    | Litespeed Hosting (örnek: Veridyen, Turhost Pro) | Hızlı önbellekleme, düşük CPU kullanımı, SEO uyumlu  |
| Django       | AWS EC2, DigitalOcean, Railway, Render           | Redis, Celery, OAuth işlemleri için esnek yapı sunar |
| Ortak Domain | Cloudflare DNS + SSL                             | Hem SEO hem HTTPS performansı için önerilir          |

Ana sayfa sadece tanıtım amaçlıysa WordPress mükemmel seçim

app.infofluencer.com alt alan adı ile tüm kullanıcı işlemlerini Django tarafında izole edin

WordPress ve Django arası veri aktarımı gerekiyorsa REST API veya embed kullanın

Oturum geçişi için JWT, cookie yönlendirmesi veya SSO mimarisi hazırlayın

Docker + GitHub Actions + Cloudflare ile profesyonel dağıtım süreci oluşturun

## Django ORM, SQL Injection ve Yetkisiz Erişimlerden Korunma
### Django ORM Nedir?
ORM (Object Relational Mapping):
Veritabanı işlemlerini doğrudan SQL yazmadan, Python objeleriyle gerçekleştirmemizi sağlayan bir araçtır. Django’da bu ORM sistemi otomatik gelir.

🔧 Örnek:
ORM ile veri alma
user = User.objects.get(id=1)

SQL eşdeğeri:
SELECT * FROM auth_user WHERE id = 1;
❌ 2. Kullanıcıdan Gelen Veriyi Doğrudan SQL'e İşlemek Neden Tehlikelidir?
Kullanıcı bir form, query parametresi veya frontend üzerinden gönderdiği bir input içine kötü niyetli SQL kodları yerleştirebilir.

🔥 Tehlikeli Örnek:
user_input = "1 OR 1=1"

cursor.execute(f"SELECT * FROM users WHERE id = {user_input}")
❗ Sonuç: Tüm kullanıcılar döner. Saldırgan tüm hesapları görebilir!

### SQL Injection Nedir? Nasıl Yapılır?
Tanım: SQL Injection, kötü niyetli kullanıcıların SQL sorgularına dışarıdan müdahale ederek veritabanını kontrol altına almasıdır.

🎯 Amaçlar:
Diğer kullanıcıların verilerini görmek

Admin gibi davranmak

Tokenları, şifreleri çekmek

Veritabanını silmek

👿 Basit Bir Saldırı Senaryosu:
Login Formu:
Kullanıcı Adı: admin' --  
Şifre: [boş bırakılır]
Sorgu şu hale gelir:

SELECT * FROM users WHERE username = 'admin' --' AND password = '...';
-- sonrası yorum satırı sayıldığı için şifre kontrolü iptal olur.
Saldırgan şifresiz giriş yapar.

✅ 4. Nasıl Korunurum? Altın Kurallar
🥇 1. ORM KULLAN!

### Güvenli sorgu
User.objects.get(username="admin")
🥈 2. Raw SQL Kullansan Bile %s ile Parametrize Et


cursor.execute("SELECT * FROM users WHERE id = %s", [user_input])
🥉 3. Query Parametrelerini Whitelist Et


VALID_SORT_FIELDS = ['username', 'email']

if sort_by not in VALID_SORT_FIELDS:
    raise PermissionDenied

### 5. SQL Injection Olmasa Bile Kullanıcılar Verileri Nasıl Görebilir?
Bu çok ciddi ve yaygın bir durumdur: Yetkisiz veri sızıntısı

📌 Örnek:

Giriş yapılmış kullanıcı için profil verisi

def get_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return JsonResponse({"email": user.email})
Saldırgan:

GET /api/profile/1/ → kendi ID'si
GET /api/profile/2/ → başka kullanıcının ID'si
🧨 Eğer kontrol yoksa → Veriler açığa çıkar!

### Yetkisiz Erişimden Nasıl Korunurum?
Önlem	Açıklama
✅ request.user ile filtrele	Her sorguda user=request.user kontrolü yap
✅ @login_required kullan	View fonksiyonlarının başına @login_required ekle
✅ View’larda yetki kontrolü yap	Sadece kendi verisi çekilebilmeli
✅ Django permissions kullan	has_object_permission vs. ile kullanıcı kontrolü
✅ DRF varsa IsAuthenticated, IsOwner gibi custom permission class'ları yaz	

### Doğru View Örneği: Kendi Verisini Çekme

from django.contrib.auth.decorators import login_required

@login_required
def get_profile(request):
    user = request.user
    return JsonResponse({
        "email": user.email,
        "username": user.username
    })
➡️ Burada kimse başka bir ID’yi sorgulayamaz, sadece kendi oturumuyla veri alır.

### Ekstra Güvenlik Tavsiyeleri
🧤 Tokenlarınızı AES ile şifreleyin
from cryptography.fernet import Fernet

cipher = Fernet(key)
encrypted_token = cipher.encrypt(token.encode())
🔍 Django Middleware ile IP/log takibi yap
Her API çağrısı loglanabilir

IP, user-agent ile anormal hareket tespit edilir

🔑 Form verilerini cleaned_data ile validate et
Regex, max_length, EmailField vs. kullanın

🧠 SONUÇ: En Kritik 5 Güvenlik Prensibi
Prensip	Açıklama
🔒 ORM kullan	SQL sorgularını parametrik yapar, injection'ı engeller
🔐 Yetki kontrolü	request.user dışında veri sorgulama izni verme
🛡️ Tokenları şifrele	Access token'lar düz metin tutulmamalı
🧼 Input sanitize et	Query parametrelerini whitelist ile doğrula
🔍 Erişim logla	Kimin hangi veriye ulaştığı bilinsin
