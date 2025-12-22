# 📡 Antenler ve Propagasyon

## 📋 Ders Hakkında
**Bölüm:** Elektronik ve Haberleşme Mühendisliği  
**Dönem:** 3. Sınıf / Bahar  
**İçerik:** Bu ders, elektromanyetik dalgaların yayılımı, anten parametreleri (kazanç, yönlülük) ve link bütçesi hesaplamalarını kapsar. Haberleşme sistemlerinin fiziksel katmanı için temel niteliğindedir.

---

## 📚 Konu Başlıkları & İçerik

| Hafta | Konu | İlgili Dosya | Detay |
|-------|------|--------------|-------|
| 1 | Giriş: Anten Nedir? | `README.md#1-giris-anten-nedir` | Anten tanımı ve türleri |
| 2 | Maxwell Denklemleri & Dalga Yayılımı | `README.md#2-propagasyon` | Yayılım modları |
| 3 | Anten Parametreleri (Gain, Directivity) | `README.md#3-temel-kavramlar` | $G = \eta D$ |
| 4 | Friis İletim Denklemi | `README.md#7-friis` | Güç hesabı |
| 5 | Link Bütçesi ve Kayıplar | `README.md#8-sorunlar` | Fading, Path Loss |

---

## 🎨 Görselleştirme: Sinyal Yayılımı

Aşağıdaki diyagram bir vericiden alıcıya sinyal gidişatını özetler:

```mermaid
graph LR
    A[Verici (Tx)] -->|Elektrik Sinyali| B(Verici Anten)
    B -.->|EM Dalga| C{Propagasyon Kanalı}
    C -.->|Yansıma/Kırılma| D(Alıcı Anten)
    D -->|Elektrik Sinyali| E[Alıcı (Rx)]
    
    style A fill:#f9f,stroke:#333
    style E fill:#bfb,stroke:#333
    style C fill:#ff9,stroke:#f66,stroke-dasharray: 5 5
```

---

## ⚙️ 3. Temel Kavramlar ve Formüller

### 📏 Frekans ve Dalga Boyu İlişkisi
$$ \lambda = \frac{c}{f} $$
*   $c$: Işık hızı ($3 \times 10^8$ m/s)
*   $f$: Frekans (Hz)

### 📡 Friis İletim Denklemi
İki anten arasındaki güç transferini ifade eder:

$$ P_r = P_t G_t G_r \left( \frac{\lambda}{4\pi R} \right)^2 $$

> **Not:** Mesafe ($R$) iki katına çıkarsa, alınan güç ($P_r$) dört kat düşer (6 dB azalır).

---

## 📊 4. Anten Parametreleri

### Yönlülük (Directivity)
Antenin enerjiyi belirli bir yöne ne kadar odakladığının ölçüsüdür.
$$ D = \frac{U_{max}}{U_{avg}} $$

### Verimlilik (Efficiency)
$$ \eta = \frac{P_{rad}}{P_{in}} $$
*   İdeal antende $\eta = 1$ (%100).

---

## 🛠️ Simülasyon Araçları
Bu dersin uygulamaları için aşağıdaki yazılımlar önerilir:
- **MATLAB (Phased Array System Toolbox):** Anten dizileri simülasyonu.
- **CST Studio Suite / HFSS:** 3D elektromanyetik alan simülasyonu.
- **4NEC2:** Ücretsiz anten modelleme aracı.

---

## 📝 Pratik Notlar
- Dikey polarizasyonlu bir antenle yatay polarizasyonlu bir anten haberleşemez (Polarization Mismatch Loss $\approx \infty$).
- Yüksek frekanslarda (örn: 60 GHz), atmosferik sönümleme (yağmur, oksijen emilimi) çok daha yüksektir.

---

## 📎 Kaynaklar ve İleri Okuma
- **Kitap:** *Antenna Theory: Analysis and Design* - Constantine A. Balanis
- **Makale:** IEEE Antennas and Propagation Magazine
