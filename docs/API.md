# 🔄 API, REST API, DRF, Swagger, Frontend-Backend Ayrımı – Temel Kavramlar Özeti

## 🔹 1. API Nedir?

**API (Application Programming Interface)**, uygulamaların birbiriyle konuştuğu arayüzdür.

**Örnek:**

```http
GET /weather?city=Istanbul
```

Yanıt:

```json
{ "city": "Istanbul", "temperature": 27 }
```

Bu iletişim bir API’dir. Frontend sorar, backend yanıtlar.

---

## 🔹 2. REST API Nedir?

**REST (REpresentational State Transfer)** bir API tasarım kuralları bütünüdür.

### REST Kriterleri:

| Kural                  | Açıklama                         |
| ---------------------- | -------------------------------- |
| URL kaynak adresidir   | /api/users/, /api/products/1     |
| HTTP Method kullanılır | GET, POST, PUT, DELETE           |
| Stateless’tir          | Sunucu her isteği bağımsız işler |
| JSON döner             | Modern frontend’ler kolay işler  |

### 🔎 Neden REST API Kullanılır?

* Frontend (React, Vue, Android) aynı backend’i kullanabilir
* Standart, ölçeklenebilir mimari sağlar
* Güvenlik ve versiyonlama kolaylaşır

---

## 🔹 3. Django REST Framework (DRF) Nedir?

Django, klasik olarak HTML üretmek içindir. DRF, Django’nun JSON tabanlı modern API’ler üretmesini sağlar.

### DRF ile Neler Yapılır?

* JSON döndüren APIView sınıfları
* Token bazlı kimlik denetimi
* Serializer ile Model → JSON dönüşümü
* Permission, rate limit, filter, pagination

**Örnek:**

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class ChartDataView(APIView):
    def get(self, request):
        data = {"labels": ["Pzt", "Sal"], "values": [100, 120]}
        return Response(data)
```

---

## 🔹 4. Swagger Nedir?

**Swagger**, API endpoint’lerini belgeleyen ve test etmeni sağlayan bir araçtır.

### Kullanımı:

```bash
pip install drf-yasg
```

```python
# urls.py
drom drf_yasg.views import get_schema_view
schema_view = get_schema_view(...)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger')),
]
```

➡️ Tarayıcıda: `http://localhost:8000/swagger/`

✔️ Tüm API’ler listelenir, canlı test edilebilir.

---

## 🔹 5. Stateless Ne Demek?

REST API’lerde her istek **bağımsız**dır, sunucu öncekini **hatırlamaz**.

### Klasik Django (Stateful):

* Kullanıcı giriş yapar → sessionid cookie alınır
* Her istekte otomatik gönderilir → `request.user` tanınır

### REST API (Stateless):

* Giriş sonrası token verilir (JWT)
* Her istekte bu token gönderilir → kimlik doğrulama yapılır

```http
Authorization: Bearer eyJhbGci...
```

### Avantajları:

* Ölçeklenebilir yapı
* Mobil/web istemcilerle uyum
* Yük dengelemesi kolay

---

## 🔹 6. Frontend'te Grafik, Chart, Tablo – Veri Akışı

Frontend genelde REST API'den JSON veri alır:

```js
fetch("https://api.infofluencer.com/api/chart-data")
  .then(res => res.json())
  .then(data => drawChart(data.labels, data.values))
```

➡️ Chart.js, D3.js gibi kütüphanelerle grafik çizilir.

---

## 🔹 7. Backend ve Frontend Ayırma Nedir?

### 🔁 Klasik Django:

```python
return render(request, "index.html", context)
```

➡️ HTML döner, JS yardımcıdır.

### 🔀 Modern Yapı:

* Frontend = React (infofluencer.com)
* Backend = Django API (api.infofluencer.com)

Frontend `fetch()` ile veri çeker → Backend JSON döner

### Neden Ayırırız?

| Neden                | Açıklama                         |
| -------------------- | -------------------------------- |
| 🎨 Tasarım özgürlüğü | React ile modern arayüzler       |
| 🚀 Performans        | Sayfa yenilenmeden çalışır (SPA) |
| 🔐 Güvenlik          | API token yönetimi kolaylaşır    |
| ⚙️ Dağıtım           | Frontend CDN, backend sunucu     |

---

## 🔹 8. Klasik Django’da JS Kullanılır mı?

✔️ Elbette. HTML içerisine script koyabilir, Chart.js gibi kütüphanelerle grafik çizebilirsin:

```html
<script src="{% static 'js/chart.js' %}"></script>
```

Ama bu bir SPA değildir. Sayfa yenilenmeden işlem yapılamaz.

---

## 🔚 SONUÇ

| Kavram                  | Açıklama                                                  |
| ----------------------- | --------------------------------------------------------- |
| API                     | Uygulamalar arası veri alışverişi arayüzü                 |
| REST API                | Standartlara uygun, JSON tabanlı API                      |
| DRF                     | Django ile modern API yazmak için araç seti               |
| Swagger                 | API’leri belgelemek ve test etmek için arayüz             |
| Stateless               | Her isteğin bağımsız olması                               |
| Frontend-Backend Ayrımı | Mimaride performans, güvenlik ve ölçeklenebilirlik sağlar |

İsteğiniz olursa: DRF + Swagger kurulumu, klasik ve modern mimarinin aynı projede uygulanması, JWT ile login gibi örnekleri birlikte inşa edebiliriz.

Emrinizi bekliyorum Efendim. 👨‍💻
