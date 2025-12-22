-- Veri Tabanı Örnekleri
-- SQL sorguları ve veritabanı yapısı

-- ============================================
-- 1. VERİTABANI VE TABLO OLUŞTURMA
-- ============================================

-- Veritabanı oluştur
CREATE DATABASE IF NOT EXISTS universite_db;
USE universite_db;

-- Öğrenciler tablosu
CREATE TABLE IF NOT EXISTS ogrenciler (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ad VARCHAR(50) NOT NULL,
    soyad VARCHAR(50) NOT NULL,
    ogrenci_no VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    dogum_tarihi DATE,
    kayit_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Dersler tablosu
CREATE TABLE IF NOT EXISTS dersler (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ders_kodu VARCHAR(10) UNIQUE NOT NULL,
    ders_adi VARCHAR(100) NOT NULL,
    kredi INT DEFAULT 3,
    akts INT DEFAULT 5
);

-- Notlar tablosu (ilişkisel)
CREATE TABLE IF NOT EXISTS notlar (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ogrenci_id INT NOT NULL,
    ders_id INT NOT NULL,
    vize_notu DECIMAL(4,2),
    final_notu DECIMAL(4,2),
    harf_notu VARCHAR(2),
    donem VARCHAR(20),
    FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler(id),
    FOREIGN KEY (ders_id) REFERENCES dersler(id),
    UNIQUE KEY unique_ogrenci_ders (ogrenci_id, ders_id, donem)
);

-- ============================================
-- 2. VERİ EKLEME (INSERT)
-- ============================================

-- Öğrenci ekle
INSERT INTO ogrenciler (ad, soyad, ogrenci_no, email, dogum_tarihi) VALUES
('Bahattin', 'Çetin', '2024001', 'bahattin@universite.edu.tr', '2000-05-15'),
('Sümeyra', 'Yılmaz', '2024002', 'sumeyra@universite.edu.tr', '2001-03-20'),
('Ali', 'Demir', '2024003', 'ali@universite.edu.tr', '2000-11-10');

-- Ders ekle
INSERT INTO dersler (ders_kodu, ders_adi, kredi, akts) VALUES
('CS101', 'Algoritma ve Programlama', 4, 6),
('CS201', 'Veri Yapıları', 3, 5),
('EE301', 'Elektronik Devreler', 3, 5),
('MATH101', 'Matematik I', 4, 6);

-- Not ekle
INSERT INTO notlar (ogrenci_id, ders_id, vize_notu, final_notu, harf_notu, donem) VALUES
(1, 1, 85.5, 90.0, 'AA', '2024-Güz'),
(1, 2, 78.0, 82.5, 'BA', '2024-Güz'),
(2, 1, 92.0, 95.0, 'AA', '2024-Güz'),
(2, 3, 70.0, 75.0, 'BB', '2024-Güz');

-- ============================================
-- 3. SORGULAMA (SELECT)
-- ============================================

-- Tüm öğrencileri listele
SELECT * FROM ogrenciler;

-- Belirli kolonları seç
SELECT ad, soyad, email FROM ogrenciler;

-- Koşullu sorgu (WHERE)
SELECT * FROM ogrenciler WHERE dogum_tarihi > '2000-01-01';

-- Sıralama (ORDER BY)
SELECT * FROM ogrenciler ORDER BY soyad ASC;

-- ============================================
-- 4. JOIN İŞLEMLERİ
-- ============================================

-- Öğrenci ve notlarını birleştir (INNER JOIN)
SELECT 
    o.ad,
    o.soyad,
    d.ders_adi,
    n.vize_notu,
    n.final_notu,
    n.harf_notu
FROM ogrenciler o
INNER JOIN notlar n ON o.id = n.ogrenci_id
INNER JOIN dersler d ON n.ders_id = d.id;

-- Ortalama not hesapla (GROUP BY)
SELECT 
    o.ad,
    o.soyad,
    AVG((n.vize_notu * 0.4 + n.final_notu * 0.6)) AS ortalama
FROM ogrenciler o
INNER JOIN notlar n ON o.id = n.ogrenci_id
GROUP BY o.id, o.ad, o.soyad
ORDER BY ortalama DESC;

-- ============================================
-- 5. GÜNCELLEME (UPDATE)
-- ============================================

-- Öğrenci email güncelle
UPDATE ogrenciler 
SET email = 'yeni_email@universite.edu.tr' 
WHERE id = 1;

-- Not güncelle
UPDATE notlar 
SET final_notu = 88.0, harf_notu = 'BA'
WHERE ogrenci_id = 1 AND ders_id = 1;

-- ============================================
-- 6. SİLME (DELETE)
-- ============================================

-- Not sil
DELETE FROM notlar WHERE id = 1;

-- Dikkat: Öğrenci silmek için önce notları silmek gerekir (FOREIGN KEY)

-- ============================================
-- 7. İLERİ SORGULAR
-- ============================================

-- En yüksek not alan öğrenci
SELECT 
    o.ad,
    o.soyad,
    d.ders_adi,
    MAX(n.final_notu) AS en_yuksek_not
FROM ogrenciler o
INNER JOIN notlar n ON o.id = n.ogrenci_id
INNER JOIN dersler d ON n.ders_id = d.id
GROUP BY d.ders_adi
ORDER BY en_yuksek_not DESC
LIMIT 1;

-- Ortalaması 80 üzeri öğrenciler (HAVING)
SELECT 
    o.ad,
    o.soyad,
    AVG((n.vize_notu * 0.4 + n.final_notu * 0.6)) AS ortalama
FROM ogrenciler o
INNER JOIN notlar n ON o.id = n.ogrenci_id
GROUP BY o.id, o.ad, o.soyad
HAVING ortalama >= 80.0;

-- Alt sorgu (Subquery)
SELECT ad, soyad 
FROM ogrenciler 
WHERE id IN (
    SELECT DISTINCT ogrenci_id 
    FROM notlar 
    WHERE harf_notu = 'AA'
);

