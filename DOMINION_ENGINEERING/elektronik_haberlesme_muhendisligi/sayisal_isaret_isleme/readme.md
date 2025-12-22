# ⚙️ Sayısal İşaret İşleme ve Elektrik Devre Temelleri Notları
**Hazırlayan:** Bahattin Yunus Çetin  
**Ders:** Mühendislik Temel Dersleri  
**Bi kahveyle okunacak versiyon ☕**

---

## 🎧 1. Sayısal İşaret İşleme (Sİİ)

### 🌊 Nedir?
**Sayısal İşaret İşleme (Digital Signal Processing - DSP)**, gerçek dünyadan gelen **analog işaretleri (ses, görüntü, sıcaklık, titreşim vb.)** bilgisayarın anlayacağı **sayılara** dönüştürüp üzerinde işlem yapmamızı sağlar.  

👉 Kısaca:  
> “Gerçek dünyayı 0 ve 1’lerle anlamaya çalışma sanatı.”

---

### 🎧 Örnekler
- Mikrofon → ses dalgası → sayısal sinyal  
- Telefon görüşmesi → gürültü azaltma  
- Kamera → görüntü netleştirme  
- Kalp atışı sensörü → veri analizi  

---

### ⚙️ Temel Kavramlar

| Kavram | Anlamı | Örnek |
|---------|--------|--------|
| **İşaret (Signal)** | Bilginin zamana göre değişen hali | Ses dalgası, ECG verisi |
| **Sistem (System)** | İşarete işlem yapan yapı | Hoparlör filtresi, mikrofon devresi |
| **Örnekleme (Sampling)** | Analog sinyali dijitalleştirme | Her 1 ms’de sesi ölçmek |
| **Kuantizasyon (Quantization)** | Ölçülen her değere sayı atama | 0.53V → 1, 0.55V → 2 |
| **Filtreleme (Filtering)** | Gürültü temizleme | Ses netleştirme |
| **Frekans Analizi (Fourier)** | Sinyalin frekans bileşenlerine ayırma | Müzikteki notaları çözmek |

---

### 🧩 Örnekleme (Sampling)
> Sürekli sinyali belli aralıklarla ölçmek.

📸 Her kare bir örnek gibi düşün.  
Örnekleme frekansı: saniyede alınan ölçüm sayısı.  
CD kalitesi ses = 44.1 kHz  

💡 **Nyquist Teoremi:**  
\[
f_s \ge 2 f_{max}
\]  
Sinyali doğru temsil etmek için örnekleme frekansı, en yüksek frekansın en az 2 katı olmalı.

---

### 🧩 Kuantizasyon (Quantization)
> Her örneğe dijital sayı karşılığı atama.  
Küçük yuvarlama hataları → **kuantizasyon hatası**.

---

### 🧮 Matematiksel Temeller

| Kavram | Açıklama | Örnek |
|---------|-----------|--------|
| **Genlik** | Sinyalin yüksekliği | Sesin şiddeti |
| **Frekans** | Tekrarlama hızı | Pes/tiz farkı |
| **Faz** | Başlama zamanı | Aynı sinyalin farklı anı |
| **Periyodik Sinyal** | Belirli aralıklarla tekrar eden | Nota sesi |
| **Aperiyodik Sinyal** | Tek seferlik olay | El çırpma sesi 👏 |

---

### 🎛️ Filtreleme Türleri

| Tür | Özellik | Örnek |
|-----|-----------|--------|
| **Alçak Geçiren (Low-pass)** | Yavaş değişen sinyalleri geçirir | Bas sesler |
| **Yüksek Geçiren (High-pass)** | Hızlı değişenleri geçirir | Tiz sesler |
| **Bant Geçiren (Band-pass)** | Belirli aralık | Radyo frekansları |

**FIR** (Finite Impulse Response): stabil, basit  
**IIR** (Infinite Impulse Response): güçlü, dikkatli ayar ister

---

### 🔁 Fourier Dönüşümü

> “Bir sinyali zaman yerine frekansla anlatmak.”

\[
X(f) = \int x(t)e^{-j2\pi ft} dt
\]

📊 Sesin içinde hangi frekanslar var görmek için kullanılır.  
Telefon, mikrofon, müzik analizleri hep Fourier’e dayanır.

---

### 🧩 SKFD (Sürekli-Kesikli Fourier Dönüşümü)

> Analog sinyali örnekleyip dijital frekans alanına dönüştürme işlemidir.

| Kısaltma | Açılım | Açıklama |
|-----------|---------|-----------|
| **SFT** | Sürekli Fourier Dönüşümü | Sürekli sinyaller için |
| **KFT** | Kesikli Fourier Dönüşümü | Sayısal sinyaller için |
| **SKFD** | Sürekli-Kesikli Fourier Dönüşümü | Analog → Dijital geçiş |
| **DFT** | Discrete Fourier Transform | Bilgisayar versiyonu |
| **FFT** | Fast Fourier Transform | DFT’nin hızlı algoritması ⚡ |

---

### 🧠 Uygulama Alanları

| Alan | Kullanım |
|------|-----------|
| Ses | Gürültü azaltma, ekolayzır |
| Görüntü | Kenar bulma, netleştirme |
| Tıp | Kalp sinyali (ECG) analizi |
| Uydu | Sinyal güçlendirme |
| Yapay Zeka | Sensör verisi ön işleme |

---

### 💡 Özet
> Sayısal İşaret İşleme, analog dünyayı sayılara dönüştürüp anlamlandırma sanatıdır 🎨  
Matematikle yazılımın buluştuğu noktadır 💻✨

---

## ⚡ 2. Elektrik Devre Temelleri

### 1. Temel Kavramlar
- Elektrik akımı (I)  
- Gerilim / Voltaj (V)  
- Güç (P) ve Enerji (W)  
- Direnç (R), İletkenlik, Ohm Kanunu  
- Birimler: Volt, Amper, Ohm, Watt  

---

### 2. Devre Elemanları
- **Pasif elemanlar:** Direnç, Kondansatör (C), Bobin (L)  
- **Aktif elemanlar:** Gerilim / Akım kaynakları  
- Bağlantılar: Seri, Paralel, Karma  
- Eşdeğer devre hesapları  

---

### 3. Devre Yasaları
- **Ohm Kanunu:** V = I × R  
- **Kirchhoff Akım Kanunu (KCL):** Düğüme giren akımların toplamı = çıkanların toplamı  
- **Kirchhoff Gerilim Kanunu (KVL):** Kapalı çevrede gerilimlerin toplamı = 0  

---

### 4. Devre Çözüm Yöntemleri
- Düğüm (Node) analizi  
- Mesh (Çevre) analizi  
- Süper düğüm / süper mesh  
- Eşdeğer devre oluşturma  

---

### 5. Lineer Devre Teoremleri
- Süperpozisyon  
- Thevenin Teoremi  
- Norton Teoremi  
- Maksimum Güç Transferi  
- Karşılıklı Bağımlılık Teoremi  

---

### 6. Kapasitör ve Endüktör Davranışı
- Kapasitör: Gerilime karşı enerji depolar  
- Endüktör: Akıma karşı enerji depolar  
- RC, RL, RLC devreleri  
- Zaman sabiti (τ = RC veya L/R)

---

### 7. Zamanla Değişen Devreler
- Geçici durum analizi  
- Üstel davranış  
- Başlangıç koşulları  

---

### 8. Sinüzoidal (AC) Devre Analizi
- AC sinyaller (genlik, faz, frekans)  
- Fazör yöntemi  
- Empedans (Z) ve Reaktans (X)  
- Güç türleri:  
  - Gerçek (P), Reaktif (Q), Görünür (S)  
  - Güç faktörü (cosφ)  

---

### 9. Rezonans ve Filtreleme
- Seri / Paralel rezonans  
- Rezonans frekansı  
- Bant genişliği, Q faktörü  
- Filtre tipleri:  
  - Alçak geçiren  
  - Yüksek geçiren  
  - Bant geçiren  
  - Bant durduran  

---

### 10. Üç Fazlı Sistemler
- Yıldız (Y) ve Üçgen (Δ) bağlantılar  
- Hat-faz gerilim ilişkileri  
- Denge ve dengesizlik durumları  

---

### 11. Frekans Alanı Analizi (İleri Seviye)
- Fourier serileri  
- Laplace dönüşümü  
- Transfer fonksiyonu  
- Sistem kararlılığı  

---

### 12. Pratik Devre Uygulamaları
- Gerilim bölücü, akım bölücü  
- Ölçüm teknikleri  
- Breadboard kurulumu  
- AC-DC güç kaynakları, osiloskop kullanımı  

---

## 🧠 Genel Özet

| Ders | Temel Amaç | Ne Öğretir? |
|------|--------------|--------------|
| **Sayısal İşaret İşleme** | Analog bilgiyi dijitale çevirme | Ses, görüntü, sensör verisi analizi |
| **Elektrik Devre Temelleri** | Elektriğin davranışını anlama | Akım, gerilim, güç hesapları |

---

> “Matematiği anlamak, fiziği görmek gibidir.  
> Devreleri çözmek ve sinyalleri işlemek, mühendisliğin kalp atışıdır.” ⚡💻
