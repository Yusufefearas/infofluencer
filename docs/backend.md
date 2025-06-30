# 📆 TEMİZ & GÜVENLİ DJANGO BACKEND’İN TEMELLERİ

---

## 🔹 1. CORS Nedir? Ne İşe Yarar?

### 🌍 CORS: Cross-Origin Resource Sharing

Tarayıcı, **farklı domain'den** gelen isteklere **güvenlik gereği izin vermez**, ta ki siz açıkça "izin veriyorum" diyene kadar.

### 🧪 Örnek:

* API: `https://api.infofluencer.com`
* Frontend: `https://frontend.infofluencer.com`

Tarayıcı der ki: “Bu başka bir origin, izin vermem.”

### ✅ Çözüm:

```bash
pip install django-cors-headers
```

```python
# settings.py\INSTALLED_APPS += ["corsheaders"]
MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware"] + MIDDLEWARE
CORS_ALLOWED_ORIGINS = [
    "https://frontend.infofluencer.com",
    "http://localhost:3000"
]
```

---

## 🔹 2. Frontend’e Hangi Formatlarda Veri Sunulur?

### 🥇 JSON (En yaygın)

```json
{
  "labels": ["01", "02", "03"],
  "values": [120, 150, 98]
}
```

Tüm modern frontend yapıları (React, Vue, Chart.js) JSON sever.

### 🥈 Alternatifler:

| Format | Kullanım             | Örnek             |
| ------ | -------------------- | ----------------- |
| CSV    | Excel ve veri işleme | `text/csv`        |
| XML    | Legacy sistemler     | `application/xml` |
| HTML   | Django template'te   | Dahili kullanım   |
| PDF    | Rapor/Fatura         | `application/pdf` |

---

## 🔹 3. Güvenlik Temelleri

### 🔐 Kim API'ye erişebilir?

```python
@login_required
def get_chart_data(request):
    stats = DailyStats.objects.filter(user=request.user)
```

### 🔒 Token kullanımı:

```
GET /api/chart-data
Authorization: Bearer eyJhbGciOi...
```

```python
from rest_framework.permissions import IsAuthenticated
class MyChartView(APIView):
    permission_classes = [IsAuthenticated]
```

---

## 🔹 4. Net Veri Modeli Yazımı

### ❌ Kötü:

```python
class D(models.Model):
    x = models.CharField(max_length=100)
```

### ✅ İyi:

```python
class DailyStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(help_text="Veri tarihi")
    followers = models.IntegerField(help_text="O günkü takipçi sayısı")
```

---

## 🔹 5. API Dökümantasyonu Hazırlamak

### ✅ JSON örneği:

```json
{
  "labels": ["2025-06-28", "2025-06-29"],
  "values": [14200, 14500]
}
```

### ✅ Swagger kurulumu:

```bash
pip install drf-yasg
```

Tarayıcıda: `localhost:8000/swagger/`

---

## 🔹 6. Standart Hata Kodları

| Durum           | Kod | Mesaj                                |
| --------------- | --- | ------------------------------------ |
| Yetkisiz        | 401 | {"error": "Authentication required"} |
| Yetki yok       | 403 | {"error": "Permission denied"}       |
| Eksik parametre | 400 | {"error": "start\_date is required"} |
| Bulunamadı      | 404 | {"error": "Data not found"}          |

### Django örneği:

```python
if not start_date:
    return JsonResponse({"error": "start_date is required"}, status=400)
```

---

## 🔹 7. Frontend Ekipleri İçin Hazır Olmalısın

| Bilgi           | Açıklama                              |
| --------------- | ------------------------------------- |
| API endpoint    | `/api/influencer-stats/`              |
| Parametreler    | `?start=2025-01-01&end=2025-06-30`    |
| Auth            | Token gerekiyor mu?                   |
| Response şemasi | `{"labels": [...], "values": [...]}`  |
| Hatalar         | Ne zaman, ne mesaj dönülür?           |
| Veri tazeliği   | Celery ile ne sıklıkta güncelleniyor? |

---

# 🧠 SONUÇ: TEMİZ DJANGO BACKEND = MODÜlER + GÜVENLİ + AÇIK

| Gereken                | Açıklama                          |
| ---------------------- | --------------------------------- |
| ✅ JSON API             | Hızlı, yaygın veri aktarımı       |
| ✅ CORS ayarı           | Farklı domain'lerden erişim için  |
| ✅ Net endpoint yapısı  | `/api/stats/` gibi sade yollar    |
| ✅ Parametre denetimi   | Girdi temizliği, `cleaned_data`   |
| ✅ Hata kontrolü        | Kod + açık mesaj                  |
| ✅ Model okunabilirliği | Yardımcı metinler ve adlar        |
| ✅ Yetkilendirme        | Kim, neye erişebilir belli olmalı |


