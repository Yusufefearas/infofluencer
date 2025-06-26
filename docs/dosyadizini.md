infofluencer/                   # 🔧 Proje kökü
├── apps/                       # ⚙️ Tüm Django uygulamaları (modüller)
│   ├── accounts/               # 🔑 Kullanıcı işlemleri (firma/influencer)
│   │   ├── templates/          # 📁 Bu app’e özel şablonlar
│   │   │   └── accounts/       # 📁 “appname” tekrar klasörü (çakışmayı önler)
│   │   │       ├── login.html          # Firma/influencer giriş sayfası
│   │   │       ├── register.html       # Kayıt sayfası
│   │   │       └── profile.html        # Kullanıcı profil sayfası
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── services.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── analytics/              # 📊 GA4 ve hedef kitle analizleri
│   │   ├── templates/
│   │   │   └── analytics/      # 📁 Analiz sayfaları
│   │   │       ├── report.html         # Rapor görüntüleme
│   │   │       └── dashboard.html      # Firma analiz dashboard’u
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── services.py
│   │   ├── tasks.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── influencers/            # 👤 Influencer verileri ve yönetimi
│   │   ├── templates/
│   │   │   └── influencers/    # 📁 Influencer sayfaları
│   │   │       ├── list.html           # Influencer listesi
│   │   │       ├── detail.html         # Influencer detay profili
│   │   │       └── dashboard.html      # Influencer’a özel dashboard
│   │   ├── models.py
│   │   ├── scrapers/
│   │   │   ├── google_trends_scraper.py
│   │   │   └── tiktok_scraper.py
│   │   ├── serializers.py
│   │   ├── services.py
│   │   ├── tasks.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── common/                 # ♻️ Ortak yardımcı fonksiyonlar
│   │   ├── constants.py
│   │   ├── helpers.py
│   │   └── utils.py
│   │
│   ├── messaging/              # 💬 Mesajlaşma (MVP sonrası)
│   │   ├── templates/
│   │   │   └── messaging/      # 📁 Mesajlaşma sayfaları
│   │   │       └── inbox.html
│   │   └── __init__.py
│   │
│   ├── payment/                # 💰 Ödeme sistemi (MVP sonrası)
│   │   ├── templates/
│   │   │   └── payment/        # 📁 Ödeme sayfaları
│   │   │       └── checkout.html
│   │   └── __init__.py
│   │
│   ├── subscription/           # 🔑 Abonelik sistemi (MVP sonrası)
│   │   ├── templates/
│   │   │   └── subscription/   # 📁 Abonelik sayfaları
│   │   │       └── plans.html
│   │   └── __init__.py
│
│   └── __init__.py
│
├── celerybeat_schedule/        # ⏰ Celery zamanlama verileri
│   ├── __init__.py
│   ├── schedule.db
│   └── schedule.json
│
├── client_secrets/             # 🔒 OAuth istemci json dosyaları
│   ├── ga4_client_secret.json
│   └── youtube_client_secret.json
│
├── docs/                       # 📚 Dokümantasyon, şema ve proje açıklamaları
│   ├── README.md
│   ├── yolharitasi.md
│   └── ...
│
├── infofluencer/               # 🌐 Proje ayarları ve ana yapı
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py             # ⚙️ .env’den DB ayarları ve genel konfig
│   ├── urls.py                 # 🌐 Tüm app URL’lerinin birleştiği yer
│   └── wsgi.py
│
├── migrations/                 # ⚙️ Ortak migration dosyaları
│
├── scripts/                    # ⚡ Tek seferlik script’ler (ör: scraper test)
│   ├── example_scraping.py
│   └── example_token_fetch.py
│
├── tests/                      # 🧪 Genel test dosyaları
│   └── __init__.py
│
├── templates/                  # 🌟 Site genelinde kullanılan ortak HTML’ler
│   ├── base.html               # Ortak şablon (header, footer, vs.)
│   ├── home.html               # Anasayfa (landing page)
│   ├── dashboard.html          # Genel dashboard (influencer/firma ortak)
│   ├── 404.html                # Özel hata sayfası
│   └── ...
│
├── static/                     # 🌟 Ortak statik dosyalar (CSS, JS, img)
│   ├── css/
│   ├── js/
│   └── images/
│
├── .env                        # 🔒 Gizli ortam değişkenleri (repo’da olmaz!)
├── .env.example                # 💡 Ortam değişkenlerinin örneği
├── .gitignore                  # 🚫 İzlenmeyecek dosyalar
├── db.sqlite3                  # 🧪 Lokal geliştirme DB (MVP için yeterli)
├── manage.py                   # 🔧 Django yönetim aracı
├── README.md                   # 📄 Proje tanıtım dosyası
└── requirements.txt            # 📦 Gerekli Python paketleri
