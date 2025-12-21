# 📁 Görüntü İşleme Kod Örnekleri

Bu klasörde görüntü işleme dersinde öğrenilen OpenCV örnekleri bulunmaktadır.

## 📚 İçindekiler

### 1. `yuz_algilama.py`
- Fotoğraftan yüz algılama
- Kameradan canlı yüz algılama
- Haar Cascade kullanımı
- Kenar tespiti (Canny)

### 2. `renk_filtreleme.py`
- HSV renk uzayında filtreleme
- Belirli renkleri tespit etme
- Kameradan renk takibi
- Kontur analizi

## 🚀 Nasıl Çalıştırılır?

### Gerekli Kütüphaneler:
```bash
pip install opencv-python numpy
```

### Çalıştırma:
```bash
python yuz_algilama.py
python renk_filtreleme.py
```

## 📸 Kullanım Örnekleri

### Yüz Algılama:
```python
from yuz_algilama import yuz_algila_fotograf, yuz_algila_kamera

# Fotoğraftan
yuz_algila_fotograf("foto.jpg")

# Kameradan
yuz_algila_kamera()
```

### Renk Filtreleme:
```python
from renk_filtreleme import renk_filtreleme_hsv, renk_takibi_kamera

# Fotoğraftan
renk_filtreleme_hsv("foto.jpg", "kirmizi")

# Kameradan
renk_takibi_kamera("yesil")
```

## 💡 Öğrenme İpuçları

1. **Renk Uzayları:**
   - RGB: Kırmızı, Yeşil, Mavi
   - HSV: Ton, Doygunluk, Parlaklık (daha iyi filtreleme)

2. **Yüz Algılama:**
   - Haar Cascade: Hızlı ama basit
   - DNN (Deep Neural Network): Daha doğru ama yavaş

3. **Görüntü İşleme Adımları:**
   - Yükleme → Dönüşüm → Filtreleme → Tespit → Gösterim

## 🔧 Geliştirme Fikirleri

- Yüz tanıma (face recognition)
- Nesne takibi (object tracking)
- Görüntü filtreleri (blur, sharpen)
- Histogram eşitleme
- Görüntü dönüştürme (rotation, scaling)

## ⚠️ Önemli Notlar

- Kamera erişimi için izin gerekebilir
- Haar Cascade XML dosyaları OpenCV ile birlikte gelir
- HSV renk aralıkları farklı ışık koşullarında ayarlanmalıdır

