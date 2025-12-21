# 📁 Veri Tabanı SQL Örnekleri

Bu klasörde veri tabanı dersinde öğrenilen SQL sorguları ve örnekleri bulunmaktadır.

## 📚 İçindekiler

### `ornek_veritabani.sql`
Kapsamlı SQL örnekleri içerir:
- Veritabanı ve tablo oluşturma (CREATE)
- Veri ekleme (INSERT)
- Sorgulama (SELECT)
- JOIN işlemleri (INNER, LEFT, RIGHT)
- Güncelleme (UPDATE)
- Silme (DELETE)
- İleri seviye sorgular (GROUP BY, HAVING, Subquery)

## 🚀 Nasıl Çalıştırılır?

### MySQL/MariaDB:
```bash
mysql -u kullanici_adi -p < ornek_veritabani.sql
```

### MySQL Workbench veya phpMyAdmin:
- SQL dosyasını içe aktarın
- Veya dosya içeriğini kopyalayıp çalıştırın

### SQLite:
```bash
sqlite3 universite.db < ornek_veritabani.sql
```

## 📊 Veritabanı Yapısı

```
ogrenciler (id, ad, soyad, ogrenci_no, email, ...)
    ↓
notlar (id, ogrenci_id, ders_id, vize_notu, final_notu, ...)
    ↓
dersler (id, ders_kodu, ders_adi, kredi, akts)
```

## 💡 Öğrenme İpuçları

1. **Temel Komutlar:**
   - CREATE, INSERT, SELECT, UPDATE, DELETE

2. **JOIN Türleri:**
   - INNER JOIN: Her iki tabloda da eşleşen kayıtlar
   - LEFT JOIN: Sol tablodaki tüm kayıtlar
   - RIGHT JOIN: Sağ tablodaki tüm kayıtlar

3. **Agregasyon Fonksiyonları:**
   - COUNT, SUM, AVG, MAX, MIN

4. **Filtreleme:**
   - WHERE: Satır filtreleme
   - HAVING: Grup filtreleme

## 🔍 Örnek Sorgular

### Basit Sorgu:
```sql
SELECT * FROM ogrenciler WHERE dogum_tarihi > '2000-01-01';
```

### JOIN ile Sorgu:
```sql
SELECT o.ad, d.ders_adi, n.final_notu
FROM ogrenciler o
INNER JOIN notlar n ON o.id = n.ogrenci_id
INNER JOIN dersler d ON n.ders_id = d.id;
```

### Ortalama Hesaplama:
```sql
SELECT AVG(final_notu) AS ortalama FROM notlar;
```

## ⚠️ Önemli Notlar

- FOREIGN KEY kullanırken dikkatli olun
- DELETE işlemlerinde önce ilişkili kayıtları silin
- Büyük veri setlerinde INDEX kullanın
- Transaction kullanarak veri bütünlüğünü koruyun

