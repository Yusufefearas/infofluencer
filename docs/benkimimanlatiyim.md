Sen bir yazılım geliştirici yardımcısısın. Aşağıdaki proje üzerinde çalışıyorum. Amacım bu projenin geliştirme sürecini hızlandırmak, öneriler almak, eksikleri görüp çözüm üretmek ve gerektiğinde kod yazdırmak.

## 🔷 PROJE ADI:
Infofluencer

## 🎯 PROJE AMACI:
Firmalar ile sosyal medya fenomenlerini (influencer) eşleştiren bir platform geliştiriyorum. Amaç:
1. Firmaların kendi GA4 verileri ile hedef kitle analizlerini yapabilmesi.
2. Influencer’ların Instagram ve YouTube hesaplarını OAuth ile bağlayarak analiz verilerinin alınabilmesi.
3. Firma ile influencer verilerinin eşleştirilmesi (filtreleme, hedef kitle uyumu).
4. Verilerin veri tabanına ilk bağlantıda kaydedilmesi, daha sonra Celery gibi araçlarla periyodik olarak güncellenmesi.
5. MVP’de ödeme ve mesajlaşma sistemi yer almayacak ancak mimariye uygun olarak dizin yapısında planlandı.

## 🛠️ TEKNOLOJİLER:
- **Backend:** Django (şu an DRF kullanılmıyor ama ileride eklenebilir)
- **Database:** PostgreSQL
- **Task Queue:** Celery + Redis
- **OAuth:** Instagram Graph API, YouTube OAuth 2.0, GA4 OAuth 2.0
- **Scraping:** TikTok ve Google Trends için manuel veri çekme veya PyTrends
- **Deployment:** Şimdilik lokal, ileride AWS veya DigitalOcean düşünülebilir

## 🔐 GÜVENLİK ve ORTAM:
- Tüm API bilgileri `.env` içinde saklanıyor.
- `client_secrets/` klasöründe `client_secret.json` dosyaları var.
- Bu klasör `.gitignore` ile koruma altında.
- Token’lar `access_token`, `refresh_token`, `expires_at` şeklinde şifreli veya güvenli alanlarda saklanıyor.

## 📁 PROJE DOSYA YAPISI:
Proje yapısı ve içeriği aşağıdaki ek olan "dosyadizini.md" içeriğinde mevcut.

## 🤝 ORTAK ÇALIŞMA:
Projeyi iki backend geliştirici birlikte geliştiriyoruz.
- Her geliştirici `.env` dosyasını kendi lokalinde tutuyor.
- PostgreSQL bağlantı ayarlarımız ortak.
- Branch yapımız: `main`, `dev`, `feature/x`

## 📦 .ZIP DOSYASI:
Bir Django projesi olarak tam dosya yapısı hazırlanmıştır. Örnek kodlar, yorumlu yapılar ve yapısal boş klasörler (messaging, subscription gibi) ileriye dönük genişleme için hazır.

---

**Lütfen:**  
- 

