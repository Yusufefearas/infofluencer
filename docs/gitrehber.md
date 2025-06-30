**🌐 Django Projesi - 2 Kisilik Takim icin GitHub Is Akisi Rehberi**

Bu belge, Django tabanli bir web projesinde iki gelistirici tarafindan profesyonel, guvenli ve temiz bir sekilde calisilmasi icin gereken tum Git komutlarini ve is akisini kronolojik olarak aciklar.

---

## 🏠 1. Ilk Kurulum (Birinci Gelistirici)

### 1.1. Yeni GitHub Reposu Olustur

* GitHub.com'da yeni bir repo ac: `infofluencer`
* .gitignore olarak `Python` sec
* README.md ekle

### 1.2. Yerelde Projeyi Olustur

```bash
# Reposu klonla
git clone https://github.com/Yusufefearas/infofluencer.git
cd infofluencer

# Sanal ortam kur
python -m venv .venv
source .venv/bin/activate

# Django yukle ve proje baslat
pip install django
django-admin startproject infofluencer .

# Degisiklikleri ekle ve push et
git add .
git commit -m "Django project initialized"
git push origin main
```

---

## 🔗 2. Ikinci Gelistirici Projeye Katilir

```bash
git clone https://github.com/Yusufefearas/infofluencer.git
cd infofluencer
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # varsa
```

---

## 🔄 3. Gunluk Is Akisi (Her Gelistirici Icin)

### 3.1. Yeni Gun Baslangici

```bash
git checkout main
git pull origin main
```

### 3.2. Yeni Gorev Icin Branch Olustur

```bash
git checkout -b feature/login-api
```

### 3.3. Kodunu Yaz ve Commit Et

```bash
git add .
git commit -m "Login API endpoint created"
```

### 3.4. Ana Branch ile Senkron Olmak (Gerekirse)

```bash
git checkout main
git pull origin main

git checkout feature/login-api
git merge main
```

> ⚡þ Conflict olursa:
>
> * Dosyalari duzenle
> * `git add .`
> * `git commit -m "Conflict resolved"`

### 3.5. Islemi Push Et

```bash
git push origin feature/login-api
```

### 3.6. GitHub'da PR (Pull Request) Ac

* GitHub'da "Compare & Pull Request" sec
* Aciklayici baslik ve yorum ekle
* Diger gelistirici kodu kontrol edip onaylar
* Merge edilir

---

## ⛔️ 4. YAPILMAMASI GEREKENLER

| Hatali Davranis                      | Dogrusu                                  |
| ------------------------------------ | ---------------------------------------- |
| `main` uzerinde direkt kod yazmak    | Her is icin `feature/` branch kullanmak  |
| `git push --force`                   | Gerekirse `--force-with-lease` kullanmak |
| Ortak dosyalarda uyarisiz degisiklik | Once haberlesmek ve ayristirmak          |

---

## 🔄 5. Ortak Dosyada Calisirken

* Farkli fonksiyonlara bolunun
* Is basinda haber verin ("Ben login'i aldim")
* `git pull` yapmadan `commit` yapmayin

---

## ⚖️ 6. Ek Tavsiyeler

* `.env`, `__pycache__`, `.sqlite3` gibi dosyalari `.gitignore` ile disarda tutun
* `requirements.txt` dosyasini guncel tutun:

```bash
pip freeze > requirements.txt
```

* Commit mesajlari anlamli ve kisa olsun:

```bash
git commit -m "Fix: mobile navbar not loading"
```

---

## 🏆 7. Ideal Branch Yapisi

```
main
 |
 |-- feature/login-api
 |-- feature/ui-design
 |-- bugfix/login-error
```

---

Bu belgeyi proje dizinine `docs/git-workflow.md` olarak eklemeniz tavsiye edilir. Herkesin bu is akisini izlemesi, projenizin stabil, okunabilir ve profesyonel kalmasini saglayacaktir.
