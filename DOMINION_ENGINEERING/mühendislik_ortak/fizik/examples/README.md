# 📁 Fizik Hesaplama Kodları

Bu klasörde fizik dersinde öğrenilen temel formüllerin Python implementasyonları bulunmaktadır.

## 📚 İçindekiler

### `fizik_hesaplamalari.py`
Kapsamlı fizik hesaplamaları içerir:

1. **Mekanik:**
   - Hız hesaplama
   - İvme hesaplama
   - Newton'un 2. Yasası
   - Serbest düşme

2. **Elektrik ve Manyetizma:**
   - Ohm Kanunu
   - Elektrik gücü
   - Elektrik enerjisi

3. **Termodinamik:**
   - Sıcaklık dönüşümleri
   - Isı enerjisi

4. **Dalgalar ve Optik:**
   - Dalga boyu
   - Frekans hesaplama

5. **Modern Fizik:**
   - Einstein'ın E=mc² formülü

## 🚀 Nasıl Çalıştırılır?

```bash
python fizik_hesaplamalari.py
```

## 📐 Formüller

### Mekanik:
- Hız: `v = s / t`
- İvme: `a = (v - v₀) / t`
- Newton 2. Yasa: `F = m × a`
- Serbest düşme: `h = (1/2) × g × t²`

### Elektrik:
- Ohm Kanunu: `V = I × R`
- Güç: `P = V × I`
- Enerji: `E = P × t`

### Termodinamik:
- Isı: `Q = m × c × ΔT`
- Sıcaklık: `K = °C + 273.15`

### Dalgalar:
- Dalga boyu: `λ = c / f`
- Frekans: `f = c / λ`

### Modern Fizik:
- Enerji-Kütle: `E = m × c²`

## 💡 Kullanım Örnekleri

```python
from fizik_hesaplamalari import ohm_kanunu, einstein_enerji_kutle

# Ohm Kanunu
akim = ohm_kanunu(12, 4)  # 12V, 4Ω -> 3A

# Einstein formülü
enerji = einstein_enerji_kutle(1)  # 1 kg -> Joule
```

## 🔬 Geliştirme Fikirleri

- Grafik çizimi (matplotlib ile)
- İnteraktif hesaplayıcı (GUI)
- Fizik simülasyonları
- Veri analizi örnekleri

