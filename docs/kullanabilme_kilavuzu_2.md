## INFOFLUENCER Django Projesi

---

### 📁 Ana Dizin (`/`)

| Dosya / Klasör     | Açıklama                                                                                                        |
| ------------------ | --------------------------------------------------------------------------------------------------------------- |
| `manage.py`        | Django yönetim komutlarını çalıştırmak için ana dosya.                                                          |
| `.env`             | Ortam değişkenlerini içerir. Gizli API anahtarları burada tutulur. **Versiyon kontrolüne dahil edilmemelidir.** |
| `.gitignore`       | Git tarafından takip edilmeyecek dosyaları belirtir (örn. `.env`, `__pycache__`, `*.pyc`).                      |
| `README.md`        | Projenin genel açıklaması, kurulumu ve kullanım bilgileri.                                                      |
| `requirements.txt` | Gerekli tüm Python kütüphanelerini listeler. `pip install -r requirements.txt` ile kurulum yapılır.             |

---

### 📁 apps/

Tüm iş mantığı burada modüler Django uygulamaları şeklinde organize edilmiştir. Her app, belirli bir göreve odaklanır.

#### ├── `accounts/`

* Kullanıcı yönetimi (firma ve influencer modelleri, login, register)
* `models.py`, `views.py`, `services.py`, `serializers.py` içerir.

#### ├── `analytics/`

* GA4 verilerinin çekilmesi, hedef kitle analizi.
* Firma bazlı metriklerin analiz edilmesi burada yapılır.

#### ├── `common/`

* Ortak kullanılacak yardımcı fonksiyonlar.
* `utils.py`, `constants.py`, `helpers.py` gibi genel fonksiyonları içerir.

#### ├── `influencers/`

* Influencer sosyal medya hesapları (Instagram, YouTube) ile ilgili modeller ve işlemler.
* Verilerin alınması, normalize edilmesi ve saklanması.

#### ├── `messaging/`

* İleriye dönük planlanan mesajlaşma altyapısı için placeholder klasör.
* Şu an boş olabilir. `__init__.py` içerir.

#### ├── `payment/`

* Ödeme sistemleri entegrasyonu için ayrılmış klasör. Şu anda MVP’de kullanılmaz ancak yapı hazırdır.

#### ├── `subscription/`

* Abonelik yönetimi (paketler, erişim kısıtlamaları) için ayrılmış boş klasör. İleride kullanılmak üzere yapılandırılmıştır.

#### └── `__init__.py`

* apps dizinini Python modülü haline getirir. Geliştirme esnasında boş bırakılabilir, sonradan global işlem yapılacaksa içerik eklenebilir.

---

### 📁 celerybeat\_schedule/

* Celery Beat zamanlanmış görevlerinin zamanlama verilerini tutar.
* Periyodik görevler (örn. her gün Instagram verilerini güncelle) burada yönetilir.

---

### 📁 client\_secrets/

* Google, YouTube, Instagram OAuth istemci dosyaları (`client_secret.json`) burada tutulur.
* `.gitignore` içinde yer almalı. Versiyon kontrolüne alınmamalıdır.
* `.env` dosyası bu dosyaların yollarını referans alabilir.

---

### 📁 infofluencer/

* Ana Django proje konfigürasyonu.
* `settings.py`: proje ayarlarını içerir.
* `urls.py`: URL yönlendirmelerini tanımlar.
* `celery.py`: Celery worker yapılandırma dosyası.
* `__init__.py`, `asgi.py`, `wsgi.py`: sunucu başlangıç dosyaları.

---

### 📁 migrations/

* Django migration dosyaları (veri tabanı şema değişiklik kayıtları) burada tutulur.
* Otomatik veya elle oluşturulur.

---

### 📁 scripts/

* Token alma, scraping gibi script dosyaları burada yer alır.
* Örnek: `get_ga4_token.py`, `youtube_scraper.py`

---

### 📁 tests/

* Her app için ayrı test dosyaları içerir.
* `test_accounts.py`, `test_influencers.py` gibi modül bazlı test yapısı önerilir.

---

### 🧩 Önemli Dosyalar:

#### `__init__.py`

* Her klasörün Python modülü olarak tanınmasını sağlar.
* Genellikle boş bırakılır ancak global importlar yapılacaksa kod eklenebilir.

#### `.env`

* API anahtarları, veri tabanı bağlantı bilgileri gibi hassas bilgiler buraya yazılır:

```dotenv
SECRET_KEY=xxx
DATABASE_URL=postgres://...
GA4_CLIENT_ID=...
INSTAGRAM_CLIENT_SECRET=...
```

#### `.gitignore`

```gitignore
.env
__pycache__/
*.pyc
client_secrets/
*.sqlite3
celerybeat_schedule/*
```

---

### 🛡️ Güvenlik ve Entegrasyon Notları

* `client_secrets/` ve `.env` dosyaları dış kaynaklara açık bırakılmamalı.
* Token'lar `EncryptedField`, `Fernet` gibi yöntemlerle şifrelenmeli.
* OAuth token süreleri `expires_at` üzerinden takip edilmeli.
* Celery task'lar başarısız olduğunda loglama yapılmalı (örn. Sentry).

---

### 🔚 Sonuç

Bu dosya yapısı:

* 🚀 **modüler ve ölçeklenebilir** bir Django projesine uygundur.
* 🔐 **güvenli veri yönetimi** sağlar.
* 🔄 OAuth, scraping ve zamanlanmış görevler için yapısal temel sunar.


