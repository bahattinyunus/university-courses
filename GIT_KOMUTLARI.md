# 🔧 Git ve UAOS Yönetim Komutları Rehberi

Bu belge, **University Courses (UC) / Evrensel Akademik İşletim Sistemi (UAOS)** deposunun yerel yönetimi, arama araçları, indeksleme otomasyonu ve GitHub iş akışı için pratik rehberdir.

---

## 🚀 UAOS Yönetim Araçları (CLI)

Repository içerisinde yerleşik olarak gelen Python yönetim araçlarını kullanarak repo durumunu kontrol edebilir, arama yapabilir ve indeksleri yeniden üretebilirsiniz:

### 1. Müfredatta Anlık Arama Yapma
```bash
# Anahtar kelime ile arama
python scripts/manage_repo.py --search "yapay zeka"
python scripts/manage_repo.py --search "kuantum"

# Doğrudan arama aracıyla
python scripts/search_curriculum.py "robotik"
```

### 2. İnteraktif Terminal Arama Gezgini
```bash
python scripts/manage_repo.py --interactive
# veya
python scripts/search_curriculum.py --interactive
```

### 3. Repository Bütünlük Doğrulama ve Tam İndeksleme
```bash
# CI/CD öncesinde tüm düğümleri doğrular ve README/SUMMARY/İndeksi üretir
python scripts/manage_repo.py --build-all
```

### 4. İstatistikleri Görüntüleme
```bash
python scripts/manage_repo.py --stats
```

---

## 📋 Git İş Akışı ve GitHub'a Yükleme

### 1. Terminalde Repository Dizinine Gidin
```bash
cd "g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\universty-courses"
```

### 2. Git Durumunu Kontrol Edin
```bash
git status
```

### 3. Değişiklikleri Sahneye Ekleyin
```bash
git add .
```

### 4. Anlamlı Bir Commit Mesajı ile Kaydedin
```bash
git commit -m "feat(core): comprehensive academic normalization, search engine, and polymathic ontology"
```

### 5. GitHub'a Gönderin (Push)
```bash
git push origin main
```

---

## 🛡️ Otomatik CI Doğrulaması

Yapılan her push sonrasında GitHub Actions (`.github/workflows/validate.yml`) şu kontrolleri otomatik olarak çalıştırır:
1. `python scripts/final_sanity_check.py` (21 Konteyner, 374 Disiplin, 2618 Kademe varlığı)
2. `python scripts/manage_repo.py --build-all` (Otomatik derleme senkronizasyonu)
3. `git status --porcelain` (Temiz ve senkronize durum kontrolü)
