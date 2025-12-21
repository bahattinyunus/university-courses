# 📡 İLETİŞİM ELEKTRONİĞİ (Communication Electronics)

## ⚙️ Dersin Tanımı
**İletişim Elektroniği**, bilgi (ses, görüntü, veri vb.) içeren sinyallerin **elektronik devrelerle taşınması, işlenmesi ve yeniden elde edilmesi** bilimidir.  
Bu ders, hem **analog** hem de **dijital haberleşme sistemlerinin** temelini oluşturur.  

Temel amaç:
> Bir sinyalin doğduğu yerden (verici) alındığı yere (alıcı) kadar geçen tüm elektronik süreci anlamak.

---

## 🎯 Dersin Amaçları
- Elektronik iletişim sistemlerinin bileşenlerini tanımak  
- Modülasyon ve demodülasyon prensiplerini öğrenmek  
- Gürültünün sinyal üzerindeki etkisini analiz etmek  
- Analog ve dijital haberleşme farkını kavramak  
- Gerçek sistemlerde (radyo, televizyon, uydu, mobil ağ) bu prensiplerin nasıl uygulandığını anlamak  

---

## 🧠 Neden Öğrenmelisin?

1. **Temeli anlamadan teknoloji öğrenilmez.**  
   4G, 5G, Wi-Fi, Bluetooth, hatta Starlink’in bile altında bu prensipler var.  

2. **Elektronikle yazılımın kesiştiği yerdesin.**  
   Yazılım mühendisliği okuyorsan bile, veri nasıl iletiliyor anlamak seni farklılaştırır.  

3. **RF, IoT ve gömülü sistemlerde kariyer için olmazsa olmaz.**  
   Sinyal elektroniğini bilen bir yazılımcı, donanım ekibinin dilinden konuşabilir.  

4. **Mühendis gibi düşünmeyi öğretir.**  
   Her sinyal bir bilgi taşır; o bilgiyi koruyup taşımak için nasıl mücadele edeceğini öğrenirsin.  

---

## 🔬 Dersin Kapsamı

### 1. **Sinyal ve Sistem Temelleri**
Her şey bir **sinyal**le başlar.  
- Sürekli (analog) ve kesikli (dijital) sinyaller  
- Zaman alanı – frekans alanı ilişkisi (Fourier dönüşümü)  
- Genlik, frekans, faz kavramları  
- Dalgalar: sinüs, üçgen, kare dalga  

📘 **Örnek:**  
Bir ses sinyali (örneğin insan sesi) 20 Hz – 20 kHz aralığındadır.  
Bu sinyali doğrudan iletemezsin → taşıyıcı sinyale bindirmen gerekir → işte burada **modülasyon** devreye girer.

---

### 2. **Modülasyon Teknikleri**
Modülasyon, bilginin bir **taşıyıcı dalgaya** bindirilmesidir.  
Amaç: sinyali uzak mesafelere, parazite rağmen gönderebilmek.

#### 🔸 Analog Modülasyonlar
| Tür | Açıklama | Kullanım |
|------|-----------|----------|
| **AM (Amplitude Modulation)** | Genlik bilgiye göre değişir | AM Radyolar |
| **FM (Frequency Modulation)** | Frekans bilgiye göre değişir | FM Radyolar |
| **PM (Phase Modulation)** | Faz bilgiye göre değişir | Modern dijital sistemler |

**Matematiksel ifade (örnek – AM):**  
\[
s(t) = [A_c + m(t)] \cdot \cos(2\pi f_c t)
\]
Burada:
- \( A_c \): taşıyıcı genlik  
- \( m(t) \): bilgi sinyali  
- \( f_c \): taşıyıcı frekansı  

---

#### 🔹 Darbe (Pulse) Modülasyonları
Analog sinyali dijitale dönüştürmeden önce kullanılan ara yöntemlerdir.

| Tür | Açıklama | Kullanım |
|------|-----------|----------|
| **PAM (Pulse Amplitude Modulation)** | Darbelerin genliği bilgiye göre değişir | ADC öncesi aşama |
| **PWM (Pulse Width Modulation)** | Darbe genişliği bilgiye göre değişir | Motor kontrol, ses işleme |
| **PPM (Pulse Position Modulation)** | Darbe konumu bilgiye göre değişir | Optik iletişim, radar |

> 💡 Bu teknikler, “sayısallaştırma” sürecinin temelidir.  
> Yani dijital iletişime geçmeden önce sinyali “darbeler” halinde kodlarsın.

---

### 3. **Demodülasyon (Çözümleme)**
Alıcı tarafta sinyalin içindeki bilgiyi geri çıkarma sürecidir.  
- AM için **zarf dedektörü**  
- FM için **frekans detektörü**  
- Dijital sistemlerde **eşzamanlı örnekleme ve kod çözme**

> 🧩 Yani antenin aldığı karışık sinyali, tekrar anlamlı hale getirirsin.

---

### 4. **Filtreleme ve Gürültü Analizi**
Gerçek dünyada sinyal **hiçbir zaman saf değildir.**
- **Alçak geçiren filtre (LPF)** → Yavaş değişen bileşenleri geçirir  
- **Yüksek geçiren filtre (HPF)** → Hızlı değişen bileşenleri geçirir  
- **Bant geçiren filtre (BPF)** → Belirli bir frekans aralığını geçirir  
- **Gürültü (Noise):** Termal, parazit, kuantizasyon  

📈 Gürültü/sinyal oranı (SNR) iletişim kalitesini belirler:
\[
SNR = \frac{P_{signal}}{P_{noise}}
\]

---

### 5. **Analog vs Dijital Haberleşme**
| Özellik | Analog | Dijital |
|----------|---------|----------|
| Temsil | Sürekli sinyaller | 0 ve 1 |
| Gürültü Direnci | Zayıf | Yüksek |
| İşleme | Kolay | Karmaşık |
| Örnek Teknoloji | FM Radyo | Wi-Fi, Bluetooth, GSM |

> ⚙️ Modern sistemler genellikle “karma”dır:  
> Analogta taşınır, dijitalde işlenir.

---

### 6. **Gerçek Sistem Bileşenleri**
- **Verici (Transmitter)** → Sinyali üretir ve modüle eder  
- **Kanal (Channel)** → Hava, kablo, fiber gibi ortam  
- **Alıcı (Receiver)** → Demodülasyon + filtreleme  
- **Anten** → Sinyali elektromanyetik dalgaya dönüştürür  

> Anten, aslında devrenin “dış dünyaya açılan ağzıdır.”

---

## 🧩 KAM ve PSAM’ın Ayrıntısı

### 🔸 KAM (Genlik Anahtarlamalı Modülasyon)
Bilgi bitleri (0 veya 1), taşıyıcı dalganın **varlığı veya yokluğu** ile temsil edilir.  
Basit ama etkili bir dijital modülasyon türüdür.  

\[
s(t) =
\begin{cases}
A_c \cos(2\pi f_c t), & \text{bit = 1} \\
0, & \text{bit = 0}
\end{cases}
\]

Kullanım: RFID sistemleri, düşük hızlı veri iletimi, sensör haberleşmesi.  

---

### 🔹 PSAM (Pulse Sampled Amplitude Modulation)
Analog sinyali **örnekleme prensibine göre** darbelere dönüştürür.  
Her darbenin genliği, bilgi sinyalinin o andaki değerine eşittir.  

\[
s(t) = \sum_{n=-\infty}^{\infty} m(nT_s) \cdot p(t - nT_s)
\]

Burada:
- \( T_s \): örnekleme periyodu  
- \( p(t) \): darbe sinyali  

> 💡 PSAM, dijital haberleşme sistemlerinde ADC’nin matematiksel temelidir.

---

## 🌍 Gerçek Hayat Uygulamaları

| Sistem | Kullanılan Modülasyon | Açıklama |
|---------|------------------------|-----------|
| **AM/FM Radyolar** | AM, FM | Ses yayınları |
| **Wi-Fi (802.11)** | QAM | Yüksek hızlı veri aktarımı |
| **Bluetooth** | GFSK | Kısa mesafe dijital iletişim |
| **Uydu Sistemleri** | PSK, QAM | Uzay tabanlı haberleşme |
| **Radar** | Pulse Modülasyon | Nesne tespiti |
| **IoT Cihazları** | OOK, FSK | Düşük güçlü veri aktarımı |

---

## 📈 Öğrendiklerin Nerede İşine Yarar?

- 📡 RF ve Haberleşme Sistemleri Tasarımı  
- 🔊 Ses / Görüntü İşleme  
- ⚙️ Sinyal İşleme (DSP)  
- 💾 Gömülü Sistemlerde Veri İletimi  
- 🔐 Güvenli Veri Aktarımı (Şifreleme + Modülasyon)  
- 🚀 Savunma Sanayi (Radar, Telemetri, Uydu)  

---

## 📚 Kaynaklar
- **Simon Haykin – Communication Systems**  
- **B. P. Lathi – Modern Digital and Analog Communication Systems**  
- **Sedra & Smith – Microelectronic Circuits**  
- **John G. Proakis – Digital Communications**  
- **YouTube:** Neso Academy, EEVblog, AllAboutElectronics  

---

## 💬 Son Söz
> “İletişim elektroniği öğrenmek, makinelerin konuşma dilini öğrenmektir.”  
> Artık sadece devrelere bakmayacak, onların nasıl “konuştuğunu” anlayacaksın.  

---

👨‍💻 **Hazırlayan:** Bahattin Yunus Çetin  
🎓 *Software Engineering Student*  
🚀 *Future Data & AI Engineer | Tech Explorer*  
🌍 *Trabzon, Türkiye*
