# Infofluencer MVP Geliştirme Yol Haritası

Güncellenme Tarihi: 2025-05-29

## Amaçlar
1. Firma, GA4 hesabını bağlayarak hedef kitlesini analiz edecek veya manuel filtreleme ile influencer arayacak.
2. Influencer, Instagram ve YouTube hesaplarını OAuth ile bağlayacak.
3. API'den gelen veriler veri tabanına kaydedilecek, daha sonra background task'lar ile güncellenecek.
4. Firma, influencer’ları platform üzerinden filtreleyip eşleştirecek.
5. Mesajlaşma ve ödeme MVP'de yer almayacak, ancak mimariye uygun şekilde planlanacak.

---

## Ortak Altyapı ve Başlangıç

### Yapılacaklar
- GitHub repo oluştur: `main`, `dev`, `feature/x` branch yapısı
- Sanal ortam kurulumu:
  ```bash
  python -m venv venv && source venv/bin/activate
  ```
- `requirements.txt` içerikleri: Django, Celery, Redis, psycopg2, python-dotenv, requests
- `.gitignore`: `.env`, `client_secrets/`, `__pycache__`, `*.pyc`
- `.env.example`: tüm çevresel değişken örnekleri
- PostgreSQL kurulumu: `infofluencer_db` veritabanı ve kullanıcı ayarları

---

## 🔐 1. HAFTA – Kullanıcı Sistemleri (accounts app)

### Yapılacaklar
- `accounts` app oluştur
- `CustomUser`, `Company`, `InfluencerProfile` modelleri
- Giriş/Kayıt servisleri (`services.py`)
- Admin panel ayarları

---

## 2. HAFTA – OAuth ve Token Saklama (oauth app)

### Yapılacaklar
- `oauth` app oluştur
- Instagram, GA4, YouTube token alma servisleri (`services.py`)
- `client_secrets/` dizini + `.env` yapılandırması
- Token modelleri ve güvenli şifreleme (örn: Fernet)

---

## 3. HAFTA – Veri Çekme ve Normalize Etme (influencers + data_processors)

### Yapılacaklar
- `influencers` app oluştur
- `InstagramProfile`, `YouTubeProfile` modelleri
- `data_processors/`: gelen veriyi normalize et
- Test token’larla örnek veri çekme ve kaydetme

---

## 4. HAFTA – Celery Task'ları ve Zamanlanmış Güncelleme (tasks + Celery)

### Yapılacaklar
- `celery.py` yapılandırması
- Redis kurulumu ve broker bağlantısı
- `tasks/`: `update_instagram_data`, `refresh_youtube_data`
- (Opsiyonel) Celery Beat ile görev zamanlama

---

## 5. HAFTA – Firma GA4 Analizi ve Filtreleme (analytics app)

### Yapılacaklar
- `analytics` app oluştur
- GA4 verilerini alma ve kaydetme servisleri
- Influencer filtreleme kriterleri (yaş, cinsiyet, ilgi alanı vb.)

---

## 6. HAFTA – Son Rötuşlar ve Yayına Hazırlık

### Yapılacaklar
- Admin panelden içerik doğrulama
- `tests/`: temel fonksiyonların testleri
- `README.md`, `.env.example` güncellenmesi
- Hata loglama, yedekleme ve deployment notları

---

## Geçiş Notları (İsteğe Bağlı Teknolojiler)

| Teknoloji | Kullanım Zamanı | Hazırlık Notu |
|----------|------------------|----------------|
| DRF | API katmanı gerekiyorsa | `serializers.py`, `APIView`, `router`, auth |
| React | Dashboard UI gerekiyorsa | DRF endpoint'leri hazır olmalı |
| Docker | Ortam taşınabilirliği için | `Dockerfile`, `docker-compose.yml` |
| Celery Beat | Zamanlanmış görevler için | `celerybeat_schedule/` dizini |
| Sentry | Prod ortamında loglama için | Opsiyonel hata izleme aracı |

---

## Ortak Geliştirme Notları

- `.env` her geliştiricinin lokalinde olmalı, `.env.example` paylaşılmalı
- PostgreSQL bağlantı bilgileri aynı olmalı
- Kodlar `feature/` branch’lerinde geliştirilmeli
- Merge işlemleri test sonrası `dev` üzerinden yapılmalı

---

## Sonuç

Bu plan sayesinde Infofluencer:
- OAuth tabanlı güvenli bağlantı sağlar
- GA4, Instagram ve YouTube verisini işler
- Firma–influencer eşleştirmesini optimize eder
- Modüler, genişletilebilir ve profesyonel bir yapıya sahiptir
