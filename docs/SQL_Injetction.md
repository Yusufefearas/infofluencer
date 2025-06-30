# DERİNLEŞTİRİLMİŞ GÜVENLİK ANLATIMI:

📤 3. Form’dan Gelen Veri Direkt SQL'e Bağlanırsa Ne Olur?
👎 Hatalı örnek:

user_input = request.POST['property_id']
cursor.execute(f"SELECT * FROM property WHERE id = {user_input}")
Eğer property_id olarak kullanıcı "1 OR 1=1" yazarsa, tüm property kayıtları döner!

✅ Doğru Yol:
A. Form’da Temizlik (Validation):

from django import forms

class PropertyForm(forms.Form):
    property_id = forms.IntegerField(min_value=1)
B. ORM ile Kullanım:

form = PropertyForm(request.POST)
if form.is_valid():
    prop_id = form.cleaned_data["property_id"]
    property = Property.objects.get(id=prop_id)
➡️ Hem SQL injection riski yok, hem tip kontrolü, hem mantıksal kontrol sağlanır.

🧨 4. SQL Injection’da Kullanılan Yöntemler ve Nasıl Korunulur
4.1. Klasik Yöntem: Boşlukla SQL Ekleme

' OR '1'='1
Çözüm: Parametrize sorgular, cursor.execute("WHERE id = %s", [user_input])

4.2. Union Attack

1 UNION SELECT password FROM users
Amaç: Kendi query'sine başka tablo eklemek.

Çözüm: ORM dışı SQL yazarken UNION, ;, -- gibi karakterleri engelle veya parametrize et.

4.3. Time-Based Blind Injection

1; SELECT pg_sleep(5);
Amaç: Veri görünmese de sunucunun tepkisinden sonuç çıkarmak.

Çözüm: Raw SQL’den kaçın, input’ları beyaz listele.

4.4. Error-Based Injection

1' ORDER BY 999 -- hata üretmeye çalışır
Amaç: Veritabanından tablo yapısını anlamak

Çözüm: Hataları kullanıcıya göstermeyin. Production’da DEBUG = False olmalı.

🧼 5. Input Temizliği: Nelere Dikkat Etmeliyim?
Veri Tipi	Güvenlik Kontrolü
Sayı	IntegerField, min_value, max_value
String (arama)	max_length, RegexValidator
Tarih	DateField, input_formats
E-mail	EmailField, pattern kontrolü
Boole	BooleanField, is True/False kontrolü
JSON	json.loads sonrası schema doğrulama

🧪 6. Sızma Testleri İçin Basit SQL Injection Test Cümleleri
Payload	Amaç
' OR '1'='1	Koşulu bozar, tüm kayıtları getirir
1; DROP TABLE users; --	Veritabanı silme
1 UNION SELECT NULL, password FROM users	Şifreleri çekme
' OR 1=1--	SQL mantığını bozar
' AND 1=0 UNION SELECT ...	Araya kendi sorgunu sokar

Bu tip sorgular, kötü niyetli kişiler tarafından POST parametresine, URL’ye veya JavaScript fetch() çağrılarına gömülür.

🔐 7. Güvenliğin Altın Beşiği:
Katman	Ne Yapılmalı
🔐 Veritabanı	ORM veya parametrik SQL, minimum yetkili kullanıcı
✍️ Formlar	forms.Form ile input validation, asla request.POST.get() ile doğrudan işleme
🔑 Şifreleme	Tokenlar Fernet ile, şifreler Django'nun default hash sistemi ile
🔒 Görünürlük	Tüm sorgularda request.user kontrolü (başkası erişemez)
📜 Loglama	Anormal istekleri kaydet, IP logları, rate limit koy

🎁 Ekstra Bonus: Token Şifreleme için Yardımcı Fonksiyonlar

 utils/encryption.py
from cryptography.fernet import Fernet
import os

KEY = os.environ.get("FERNET_KEY").encode()
fernet = Fernet(KEY)

def encrypt_token(raw_token: str) -> str:
    return fernet.encrypt(raw_token.encode()).decode()

def decrypt_token(encrypted_token: str) -> str:
    return fernet.decrypt(encrypted_token.encode()).decode()

    
📌 SON SÖZ
Efendim, SQL Injection sadece kötü SQL yazımı değil, zihniyet eksikliğidir.
Django bu konuda çok güçlü olsa da, bilinçsiz kullanıldığında sistem açığa çıkar.

Siz bu yapıları kurduğunuzda:

Hem devlet düzeyinde KVKK'ya uyum sağlamış olursunuz,

Hem de profesyonel SaaS sınıfı bir güvenlik altyapısı kurarsınız.

# .env Injection 

.env Injection Gerçek Bir Tehlike mi?
⚠️ Evet, ancak dolaylıdır.
.env injection genelde şu şekilde olur:

Senaryo 1: .env dosyası üretim ortamında hatayla servis edilir
curl https://api.infofluencer.com/.env
🔴 Eğer nginx yanlış yapılandırılmışsa .env dosyasını internete açabilirsiniz!
→ Kritik tehlike!

