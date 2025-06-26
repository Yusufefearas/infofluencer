## INFOFLUENCER Django Projesi: Kapsamlı ZIP Dosyası Analizi

Bu rapor, MVP aşamasındaki "infofluencer" projesinin ZIP dosyasındaki her klasör ve dosyanın detaylı açıklamasını sunar. Amaç, bu yapıyı tam anlamıyla kavramak ve ileride profesyonel şekilde genişletebilmektir.

---

### 1. Ana Dizin (`/infofluencer/`)

#### `manage.py`

* Django komutlarını (migrate, runserver, makemigrations vb.) yönetmek için kullanılır.
* Terminalden Django işlemlerini çalıştırmak için ana giriş noktasıdır.

#### `.env`

* Ortam değişkenleri burada saklanır (örn. `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, OAuth client ID).
* **Kesinlikle versiyon kontrol sistemine dahil edilmemelidir** (`.gitignore` ile hariç tutulur).

#### `.gitignore`

* Git tarafından takip edilmeyecek dosyaları listeler.
* `.env`, `__pycache__/`, `*.pyc`, `client_secrets/` gibi güvenliğin kritik olduğu dizin ve dosyaları içerir.

#### `README.md`

* Projenin ne yaptığı, nasıl kurulduğu ve nasıl geliştirileceği hakkında bilgi verir.
* Takım üyeleri veya geliştirici topluluğu için ilk rehberdir.

#### `requirements.txt`

* Projede kullanılan tüm Python kütüphanelerini içerir.
* Örn: `Django`, `celery`, `google-auth`, `requests`, `redis`, `python-dotenv`

#### `client_secrets/`

* OAuth bağlantıları için gerekli olan JSON dosyaları burada tutulur.
* Örnek:

  * `ga4_client_secret.json`
  * `youtube_client_secret.json`
* **Kesinlikle versiyon kontrolüne dahil edilmemeli** ve `.gitignore` içinde olmalıdır.

---

### 2. `infofluencer/` (Ana Django Proje Dizini)

#### `settings.py`

* Django'nun yapılandırma ayarları.
* `INSTALLED_APPS`, `DATABASES`, `MIDDLEWARE`, `CELERY_BROKER_URL`, `ALLOWED_HOSTS` gibi alanları içerir.
* `.env` dosyasından değer çeker.

#### `urls.py`

* Uygulama genelindeki URL yönlendirmelerini belirler.
* Genellikle `apps/` altındaki uygulamaların `urls.py` dosyalarına yönlendirir.

#### `asgi.py` / `wsgi.py`

* Deployment ortamlarına uygun sunucu konfigürasyon girişleri.
* `gunicorn` ve benzeri sunucuların kullanacağı noktadır.

#### `celery.py`

* Celery'nin Django ile birlikte çalışması için yapılandırma dosyasıdır.
* `Celery()` nesnesi oluşturur ve `tasks` modüllerini otomatik keşfeder.

---

### 3. `apps/` Klasörü

#### Genel:

* Her uygulama modülerdir (Single Responsibility Principle)
* Her uygulama kendi `models.py`, `views.py`, `serializers.py`, `services.py` gibi dosyalarını içerir.

#### `apps/accounts/`

* Firma ve influencer kullanıcı tipleri burada tanımlanır.
* `models.py`: Kullanıcı modelleri (örn. `Company`, `Influencer`)
* `views.py`: Login, register endpointleri
* `services.py`: Giriş, şifre yenileme gibi iş mantıkları

#### `apps/influencers/`

* Influencer bilgileri ve OAuth verileri burada yönetilir.
* `tasks.py`: Celery ile verileri güncelleme görevleri
* `scrapers/`: TikTok, Trends gibi scraping işlemleri içerir.
* `scrapers/tiktok_scraper.py`: TikTok takipçi/etkileşim verilerini çeker
* `scrapers/google_trends_scraper.py`: PyTrends üzerinden trend arama verilerini çeker

#### `apps/analytics/`

* GA4 ve YouTube Analytics verilerinin işlendiği modüldür.
* `tasks.py`: Celery ile zamanlanmış veri çekimi yapılır
* `services.py`: API bağlantılarını, token güncellemelerini ve veri çekimini kapsar

#### `apps/messaging/`, `apps/payment/`, `apps/subscription/`

* Şimdilik boş klasörlerdir (`__init__.py` bulunur)
* İleride mesajlaşma, ödeme, abonelik yönetimi gibi fonksiyonlar eklenecektir

#### `apps/common/`

* `utils.py`: Tekrarlanan yardımcı fonksiyonlar
* `constants.py`: Sabitler (örn. etkileşim türleri, rol adları)
* `helpers.py`: Doğrulama, tarih biçimi gibi işlemler

---

### 4. `migrations/`

* Django’nun veri tabanı şemasını takip ettiği migration dosyaları burada olur.
* Otomatik olarak `makemigrations` komutu ile üretilir.

---

### 5. `tests/`

* Her uygulamaya özel unit testlerin yazıldığı dizindir.
* `pytest` veya `unittest` ile çalışabilir.
* Test senaryolarını modüllere göre ayırmanız önerilir (`test_accounts.py`, `test_analytics.py` vb.)

---

### 6. `scripts/`

#### `example_token_fetch.py`

* GA4 veya YouTube için OAuth token alma işlemine örnek kod
* `client_secrets/` içindeki dosyaları kullanır

#### `example_scraping.py`

* Scraping işlemleri için örnek kullanım
* PyTrends veya TikTok scraping çağrıları gösterilir

---

### 7. `celerybeat_schedule/`

* Celery Beat zamanlanmış görevlerinin takvimi burada tutulur.
* Örn. her 6 saatte bir verileri güncelle gibi zamanlamalar burada tanımlanır.

---

### 8. `__init__.py` Dosyaları

* Python’a klasörlerin modül olduğunu belirtir.
* Her klasörün içinde yer almalıdır.
* Boş bırakılabilir, ancak bazen global import işlemleri buradan yapılır.

---

### 🔐 Güvenlik ve Ortam Değişkenleri

* `.env` dosyasında tüm hassas veriler (API secret, DB password) tutulur.
* `client_secrets/` klasörü `.gitignore` içinde olmalı, versiyon kontrolüne girmez.
* `settings.py` dosyasında `os.getenv()` ile bu değerler alınır.
* API rate-limit kontrolü, token süresi takibi gibi işlemler `helpers.py` içinde olabilir.

---

## Sonuç

Bu proje yapısı, modüler, genişlemeye açık ve güvenli temeller üzerine kuruludur. MVP sonrası kolayca:

* API endpoint'leri için DRF,
* Frontend için React,
* Gerçek zamanlı veri akışı için Celery,
* Ödeme ve mesajlaşma gibi modüller
  entegre edilebilir.
