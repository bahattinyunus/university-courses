# 💡 **Neden Analog ve Dijital Haberleşmeyi Öğrenmelisin**

## 🧠 **1️⃣ Gerçek Dünyadaki Tüm İletişim Buradan Geçiyor**

Telefonunla konuşuyorsun → sesin analog başlıyor, dijitale çevriliyor, kablosuz modülasyonla taşınıyor.
Wi-Fi, Bluetooth, 4G, 5G, hatta uzay iletişimi bile bu temeller üzerine kurulu.

> “Bugün internete bağlanan her cihaz — analog ve dijital haberleşme yasalarına itaat eder.”

Bunu bilmek, teknolojinin **içini görmek** demek.
Sadece kullanan değil, **yaratan** olursun.

---

## 🛰️ **2️⃣ Yazılımcıysan, Bu Bilgi Seni Diğerlerinden Ayırır**

Sen yazılımcısın 🧑‍💻
Ama yazılım artık sadece ekranda değil:

* Robotlar
* IoT cihazları
* Otonom araçlar
* Dronlar
* Gömülü sistemler

Hepsi sensörlerden **analog sinyal** alır, dijital veriye çevirir, sonra kablosuz iletir.
Bu dersi bilen bir yazılımcı, sadece kod yazmaz — **donanımın nabzını tutar.**

> “Kod yazan çok, sistemi anlayan az.”

---

## ⚙️ **3️⃣ Elektronik + Yazılım + Fizik → Senin Süper Gücün**

Bu ders, bu üç alanı birleştiren köprü gibi.

* Elektronik: Sinyal devreleri nasıl çalışır
* Fizik: Dalga ve enerji nasıl yayılır
* Yazılım: Sinyali nasıl işler, gönderir, çözeriz

Bunları birlikte anlayınca, sadece “programcı” değil, **mühendis gibi düşünen programcı** oluyorsun.
Ve bu fark, seni 10 adım öne taşır 🚀

---

## 💬 **4️⃣ Röportajlarda, Projelerde, Start-up’larda Çok İşine Yarar**

💼 İş görüşmesinde:

> “Sinyal işleme, haberleşme protokolleri veya modülasyon türleri hakkında bilgi sahibi misiniz?”

Bilen biri olarak:

* Donanım ve ağ ekipleriyle aynı dili konuşursun
* IoT / robotik / telekom projelerinde aktif rol alırsın
* Kodladığın sistemin nasıl “gerçek dünyaya ulaştığını” bilirsin

---

## 🧬 **5️⃣ Düşünme Biçimini Değiştirir**

Bu ders sadece bilgi değil, **mantık disiplini** kazandırır:

* “Sinyal bozulduysa neden?”
* “Veri kaybolduysa hata hangi katmanda?”
* “İletim süresini nasıl optimize ederim?”

Bu, seni sadece bir yazılımcı değil, **sistem düşünen** biri yapar.

---

## 💥 **6️⃣ Geleceğin Teknolojileri Buradan Doğuyor**

| Teknoloji             | Temelinde Ne Var                  |
| --------------------- | --------------------------------- |
| 5G / 6G               | Dijital modülasyon, kanal kodlama |
| Uydu İnterneti        | Analog-dijital dönüşüm            |
| Yapay Zeka Sensörleri | Analog giriş, dijital işleme      |
| Kuantum İletişimi     | Dalga temelli bilgi aktarımı      |

Geleceği inşa eden mühendisler bu temelleri **ezbere değil, özümseyerek** biliyor.

---

## 🌍 **7️⃣ Basitçe: Her Şey Sinyaldir**

İnsan beyni bile elektriksel sinyallerle çalışır.
Yani bu dersi öğrenmek = doğayı, makineleri ve teknolojiyi aynı anda anlamak.

> “Haberleşme öğrenmek, doğanın konuşma dilini çözmektir.”

---

## ⚡ **Kısacası:**

* Dijital çağın arkasındaki bilimi öğrenirsin
* Kodladığın şeyin neden ve nasıl çalıştığını bilirsin
* IoT, robotik, yapay zeka, siber güvenlik gibi alanlara sağlam temel atarsın
* Sadece kullanıcı değil, **yaratıcı mühendis** olursun 💪



# 📡 **Analog Haberleşme Dersi**

## 🎯 **Dersin Amacı**

Analog haberleşme, **bilginin (ses, görüntü, veri)** sürekli değişen (analog) sinyallerle taşınmasını inceler. Bu ders, temel sinyal teorisinden başlayarak, **modülasyon teknikleri**, **gürültü analizi** ve **iletim sistemlerinin performansını** anlamayı hedefler.

---

## ⚙️ **1. Temel Kavramlar**

### 🔸 Sinyal Nedir?

Bir fiziksel büyüklüğün zamanla değişimine **sinyal** denir.

* **Analog sinyal:** Sürekli değer alır (örnek: ses dalgası).
* **Sayısal sinyal:** Kesikli değer alır (örnek: 0 ve 1).

### 🔸 Sistem Nedir?

Girdiyi (input) alıp, belirli kurallara göre çıktıya (output) dönüştüren yapıdır.
Örnek: Mikrofon → elektrik sinyali üretir.

---

## 📈 **2. Sinyallerin Temsili**

### 🧮 Zaman Bölgesi Gösterimi

Sinyal doğrudan zaman ekseninde ifade edilir:
( x(t) )

### 🌊 Frekans Bölgesi Gösterimi

Sinyalin frekans bileşenlerini gösterir:
( X(f) )

> Fourier Dönüşümü burada devreye girer:
> [
> X(f) = \int_{-\infty}^{\infty} x(t)e^{-j2\pi ft}dt
> ]

---

## 🧭 **3. Analog Haberleşme Süreci**

Bilgi → Modülasyon → Kanal → Demodülasyon → Bilgi

```
[Bilgi] → [Taşıyıcıya bindirme] → [Kanal üzerinden iletim]
             ↓
        [Alıcı - çözme]
```

---

## 🔊 **4. Modülasyon Teknikleri**

Modülasyon: Bilgi sinyalini yüksek frekanslı taşıyıcıya bindirme işlemidir.

### 🌀 **4.1. Genlik Modülasyonu (AM)**

Taşıyıcının **genliği** bilgi sinyaline göre değişir.

* Avantaj: Basit donanım
* Dezavantaj: Gürültüye hassas

📘 **AM sinyali:**
[
s(t) = A_c[1 + k_a m(t)] \cos(2\pi f_c t)
]

---

### 🌊 **4.2. Frekans Modülasyonu (FM)**

Bilgi sinyali, taşıyıcının **frekansını** değiştirir.

* Avantaj: Gürültüye dayanıklı
* Dezavantaj: Daha geniş bant genişliği ister

📘 **FM sinyali:**
[
s(t) = A_c \cos[2\pi f_c t + k_f \int m(t)dt]
]

---

### ⚡ **4.3. Faz Modülasyonu (PM)**

Bilgi sinyali taşıyıcının **fazını** değiştirir.
FM’e oldukça benzer ama faz üzerinden çalışır.

📘 **PM sinyali:**
[
s(t) = A_c \cos[2\pi f_c t + k_p m(t)]
]

---

## 🧠 **5. Demodülasyon (Çözme)**

Taşıyıcıdan bilgi sinyalinin geri elde edilmesi işlemidir.

* AM → Zarf dedektörü
* FM → Frekans detektörü
* PM → Faz detektörü

---

## 🌐 **6. Gürültü (Noise)**

Gerçek sistemlerde **gürültü kaçınılmazdır**.
Gürültü, iletilen sinyali bozarak bilgi kaybına yol açar.

* **Termal Gürültü:** Direnç kaynaklı rastgele gürültü
* **Parazit Gürültü:** Elektriksel cihazlardan kaynaklanır
* **Atmosferik Gürültü:** Yıldırım, güneş vb. doğal olaylardan

📊 **Sinyal-Gürültü Oranı (SNR):**
[
SNR = \frac{P_{sinyal}}{P_{gürültü}}
]

---

## 📶 **7. Bant Genişliği ve Kanal Kapasitesi**

Bir sinyalin iletilebilmesi için gereken frekans aralığına **bant genişliği** denir.
📏 **Shannon Kapasite Teoremi:**
[
C = B \log_2 (1 + SNR)
]

---

## ⚡ **8. Uygulama Alanları**

* Radyo yayıncılığı (AM/FM)
* Televizyon sistemleri
* Telefon haberleşmesi
* Havacılık ve denizcilik iletişimi
* Analog sensör sistemleri

---

## 🧩 **9. Dijital ile Farkı**

| Özellik                | Analog Haberleşme | Dijital Haberleşme     |
| ---------------------- | ----------------- | ---------------------- |
| Sinyal Tipi            | Sürekli           | Kesikli                |
| Gürültüye Dayanıklılık | Düşük             | Yüksek                 |
| Donanım Karmaşıklığı   | Basit             | Karmaşık               |
| Örnekleme              | Yok               | Var                    |
| Kullanım Alanı         | Radyo, TV         | İnternet, Cep telefonu |

---

## 🧭 **10. Dersin Kazanımları**

Bu dersi bitirdiğinde;

* Analog sinyallerin matematiksel modelini kurabilir,
* Modülasyon ve demodülasyon prensiplerini açıklayabilir,
* Gürültünün etkilerini analiz edebilir,
* Haberleşme sistemlerinin performansını ölçebilirsin.

---

## 🧩 **Ekstra Not:**

> Analog haberleşme, dijitalin atasıdır.
> Onu anlamadan dijital haberleşmeye tam hâkim olunmaz ⚙️



# 🎛️ **Analog Modülasyonların Görsel ve Örnekli Anlatımı**

## 🧩 **1. Taşıyıcı, Bilgi ve Modüleli Sinyaller**

Bir modülasyon sisteminde üç temel sinyal vardır:

| Sinyal Türü                 | Tanım                                                       | Örnek             |
| --------------------------- | ----------------------------------------------------------- | ----------------- |
| **Bilgi Sinyali (m(t))**    | İletilmek istenen sinyaldir. Genellikle düşük frekanslıdır. | Ses dalgası       |
| **Taşıyıcı Sinyali (c(t))** | Bilgiyi taşımak için kullanılan yüksek frekanslı sinyaldir. | Radyo taşıyıcısı  |
| **Modüleli Sinyal (s(t))**  | Bilginin taşıyıcıya bindirilmiş hali.                       | Yayınlanan sinyal |

---

## 📊 **2. AM, FM, PM Görsel Benzetimleri**

### 🌀 **A. Genlik Modülasyonu (AM)**

**Genlik değişir**, frekans sabit kalır.

```
Bilgi:    ~~~____~~~~____~~~~
Taşıyıcı: /\/\/\/\/\/\/\/\/\/\
Modüleli: /\/\/\____/\/\/\____/
```

📘 Matematiksel Gösterim:
[
s(t) = A_c[1 + k_a m(t)] \cos(2\pi f_c t)
]

🧠 **Yorum:** AM sinyallerde bilgi **genlikte** taşınır.
Bu yüzden gürültüye (örneğin elektriksel parazite) çok duyarlıdır.

---

### 🌊 **B. Frekans Modülasyonu (FM)**

**Frekans değişir**, genlik sabittir.

```
Bilgi:    ~~~____~~~~____~~~~
Taşıyıcı: /\/\/\/\/\/\/\/\/\/\
Modüleli: //\\/\\//\\//\\//\\/
```

📘 Matematiksel Gösterim:
[
s(t) = A_c \cos[2\pi f_c t + k_f \int m(t)dt]
]

🧠 **Yorum:** Gürültüye karşı dayanıklıdır çünkü bilgi **frekans** değişimindedir.
Radyo yayınlarında FM tercih edilmesinin nedeni budur.

---

### ⚡ **C. Faz Modülasyonu (PM)**

**Faz değişir**, genlik ve frekans sabittir.

```
Bilgi:    ~~~____~~~~____~~~~
Modüleli: /\/\/\/  \/\/\/  \/\
```

📘 Matematiksel Gösterim:
[
s(t) = A_c \cos[2\pi f_c t + k_p m(t)]
]

🧠 **Yorum:** FM ile benzer, ancak frekans yerine faz değişimi söz konusudur.
Sayısal dünyada bu tekniğin dijital hali **PSK (Phase Shift Keying)** olarak kullanılır.

---

## ⚖️ **3. AM vs FM Karşılaştırma Tablosu**

| Özellik                | **AM (Genlik Modülasyonu)** | **FM (Frekans Modülasyonu)** |
| ---------------------- | --------------------------- | ---------------------------- |
| Bilgi Nerede Taşınır   | Genlikte                    | Frekansta                    |
| Gürültüye Dayanıklılık | Düşük                       | Yüksek                       |
| Bant Genişliği         | Dar                         | Geniş                        |
| Donanım Karmaşıklığı   | Basit                       | Karmaşık                     |
| Güç Kullanımı          | Verimsiz                    | Daha verimli                 |
| Örnek Kullanım         | AM Radyo                    | FM Radyo                     |

---

## 🔬 **4. Örnek Problem 1: AM Sinyali**

Verilenler:

* Taşıyıcı genliği ( A_c = 5V )
* Modülasyon indeksi ( m = 0.5 )
* Bilgi sinyali ( m(t) = \sin(2\pi 100t) )
* Taşıyıcı frekansı ( f_c = 1,kHz )

📘 Çözüm:
[
s(t) = 5[1 + 0.5\sin(2\pi 100t)]\cos(2\pi 1000t)
]

🧠 Bu sinyalde genlik, bilgiye göre %50 oranında değişir.
%100’ü aşarsa (m > 1), **aşırı modülasyon (overmodulation)** oluşur ve sinyal bozulur.

---

## 🧮 **5. Örnek Problem 2: FM Sinyali**

Verilenler:

* ( f_c = 100,kHz )
* ( k_f = 50,Hz/V )
* ( m(t) = 2\sin(2\pi 500t) )

📘 Çözüm:
[
s(t) = A_c \cos[2\pi 100000t + 2\pi(50)(2\sin(2\pi 500t))]
]

🧠 Burada frekans, bilgi sinyaline göre ±100 Hz değişir.
Frekans sapması = ( \Delta f = k_f A_m = 100 Hz )

---

## 📻 **6. Gerçek Hayat Bağlantıları**

| Sistem         | Kullanılan Modülasyon | Neden                       |
| -------------- | --------------------- | --------------------------- |
| AM Radyo       | Genlik Modülasyonu    | Basit alıcı devresi         |
| FM Radyo       | Frekans Modülasyonu   | Gürültüye dayanıklı         |
| Analog TV      | AM (video) + FM (ses) | Karma sistem                |
| CB Telsiz      | AM                    | Kolay iletim                |
| Uçak İletişimi | AM                    | Gürültüden çok yön avantajı |

---

## 🚀 **7. Ekstra Bilgi: Modülasyon İndeksi**

Modülasyon derinliğini gösterir.

### **AM’de:**

[
m = \frac{A_m}{A_c}
]
0 ≤ m ≤ 1 olmalı.
m > 1 → **Overmodulation (taşma)** olur.

### **FM’de:**

[
\beta = \frac{\Delta f}{f_m}
]
Bu değer arttıkça FM sinyali daha kaliteli ama daha geniş bantlı olur.

---

## 🧭 **8. Özet Şema**

```
m(t) -----> Modülatör -----> s(t) -----> Kanal -----> Demodülatör -----> m(t)
```

* **Modülatör:** Bilgiyi taşıyıcıya ekler.
* **Kanal:** İletim ortamı (hava, kablo vs).
* **Demodülatör:** Taşıyıcıdan bilgiyi çözer.


# 💻 **Analogdan Dijitale Geçiş (Sayısal Haberleşmeye Giden Yol)**

## 🚀 **1. Neden Dijitale Geçildi?**

Analog sistemler güzeldi ama…

* Gürültüye dayanıksızdı 😣
* Uzun mesafede kalite düşüyordu
* İşleme, depolama ve şifreleme zor oluyordu

📈 Dijital sistemler ise:
✅ Gürültüye daha dayanıklı
✅ Depolama kolay
✅ Şifreleme, sıkıştırma ve hata düzeltme mümkün
✅ Mikrodenetleyici, bilgisayar, yazılım ile mükemmel uyumlu

---

## 🧭 **2. Geçiş Süreci: Analog → Dijital**

Bir analog sinyalin dijitale dönüşmesi **3 aşamada** gerçekleşir:

```
Analog Sinyal
     ↓
1️⃣ Örnekleme (Sampling)
     ↓
2️⃣ Nicemleme (Quantization)
     ↓
3️⃣ Kodlama (Encoding)
     ↓
Sayısal Sinyal (Binary)
```

---

## 🎚️ **3. 1️⃣ Örnekleme (Sampling)**

Analog sinyalden belli aralıklarla örnek alınır.
Örnekleme frekansı ( f_s ), sinyalin değişim hızına bağlıdır.

📘 **Nyquist Teoremi:**

> Sinyalin en yüksek frekansı ( f_{max} ) ise,
> kayıpsız örnekleme için ( f_s ≥ 2f_{max} ) olmalı.

🎯 **Örnek:**
Ses sinyali ( f_{max} = 20,kHz )
→ ( f_s ≥ 40,kHz )
CD kalitesi = 44.1 kHz (bu yüzden seçilmiştir!)

---

## 📏 **4. 2️⃣ Nicemleme (Quantization)**

Örneklenen sinyalin genliği **yakın bir sayısal değere** yuvarlanır.
Her seviye, belirli bir bit kombinasyonuna denk gelir.

```
Gerçek Değer:  2.67V
Nicemlenmiş:   2.5V (en yakın seviye)
```

📊 Bit sayısı (n) arttıkça hassasiyet artar:
[
\text{Nicemleme Seviyesi} = 2^n
]
🎯 8-bit → 256 seviye
🎯 16-bit → 65.536 seviye (yüksek ses kalitesi)

---

## 🔢 **5. 3️⃣ Kodlama (Encoding)**

Nicemlenmiş her değer, **ikili (binary)** formda ifade edilir.

Örnek:

```
Nicemlenmiş değer = 3 → 011
Nicemlenmiş değer = 7 → 111
```

💡 Artık sinyal **0 ve 1’lerden** oluşur → Dijital dünyaya hazırdır!

---

## 🎧 **6. PCM (Pulse Code Modulation)**

Bu üç adımın birleştiği klasik yöntemdir.

📘 **PCM Aşamaları:**

1. Örnekleme
2. Nicemleme
3. Kodlama

PCM ses sistemlerinde, telefon hatlarında ve ses kartlarında kullanılır.

🧠 **PCM Avantajları:**

* Gürültüden az etkilenir
* Dijital devrelerle uyumlu
* Hata düzeltme yapılabilir

---

## 🔁 **7. DPCM (Differential PCM)**

PCM’in geliştirilmiş versiyonudur.
Tam sinyali değil, **ardışık örnekler arasındaki farkı** kodlar.

🎯 **Avantajı:** Daha az bit kullanılır → daha az bant genişliği.
Yani veri sıkıştırmanın ilk adımı!

---

## 🪄 **8. ADC ve DAC Dönüştürücüler**

| Dönüştürücü                           | Görev                           | Yön              |
| ------------------------------------- | ------------------------------- | ---------------- |
| **ADC (Analog-to-Digital Converter)** | Analog sinyali dijitale çevirir | Analog → Dijital |
| **DAC (Digital-to-Analog Converter)** | Dijital sinyali analoga çevirir | Dijital → Analog |

🎮 **Gerçek örnek:**

* Mikrofon → ADC → Bilgisayar
* Bilgisayar → DAC → Hoparlör

---

## 🧠 **9. Dijital Sinyalin Yeniden Üretimi**

Dijital sinyalde, gürültü sinyali bozmaz çünkü

> sadece “0” ve “1”’ler vardır.

Eğer bozulma olursa, **eşikleme (thresholding)** işlemiyle sinyal eski haline getirilir.

```
0.8V → 1
0.3V → 0
```

Sonuç: Mükemmel sinyal geri döner 💪

---

## ⚡ **10. Analog vs Dijital Karşılaştırma**

| Özellik      | Analog         | Dijital            |
| ------------ | -------------- | ------------------ |
| Temel Eleman | Sürekli sinyal | 0 ve 1             |
| Gürültü      | Etkilenir      | Etkilenmez         |
| İşleme       | Zor            | Kolay (yazılımla)  |
| Donanım      | Basit          | Karmaşık           |
| Depolama     | Zor            | Kolay              |
| Şifreleme    | Zor            | Güçlü algoritmalar |
| Örnek        | AM/FM Radyo    | Bluetooth, Wi-Fi   |

---

## 🧭 **11. Dijital Haberleşmeye Giden Yol**

Analog sistemlerden sonra artık:

* **PCM** → klasik dijital ses
* **DPCM / ADPCM** → sıkıştırılmış versiyonlar
* **Delta Modülasyon** → fark sinyaline dayalı teknik
* **Dijital Modülasyonlar:** ASK, FSK, PSK gibi (bir sonraki seviye 🚀)

---

## 💬 **Özetle:**

> Analogdan dijitale geçiş,
> “sürekli dalgaları”
> “sayısal verilere” dönüştürme sanatıdır.

Bugün kullandığın her şey — telefondaki ses, internetteki veri, Wi-Fi sinyali — bu dönüşümün sonucudur 🌍💡



# ⚙️ **Dijital Modülasyon Teknikleri**

## 🎯 **Amaç:**

Dijital veriyi (0 ve 1’leri), iletim için **analog taşıyıcı sinyale** dönüştürmek.
Yani:

```
Dijital veri → Analog taşıyıcı → Kanal → Analog → Dijital veri
```

Her bit (0 veya 1), taşıyıcı sinyalin **genliği**, **frekansı** ya da **fazı** değiştirilerek temsil edilir.

---

## 🧩 **1️⃣ Amplitude Shift Keying (ASK) — Genlik Kaydırmalı Anahtarlama**

### 📘 Tanım:

Taşıyıcının **genliği**, gönderilen bite göre değiştirilir.

| Bit | Taşıyıcı Genliği |
| --- | ---------------- |
| 1   | Yüksek (A)       |
| 0   | Düşük (veya 0)   |

📊 **Matematiksel Gösterim:**
[
s(t) = A_i \cos(2\pi f_c t)
]
Burada ( A_i ) = 0 veya A.

```
Bit: 1 0 1 1 0
Sinyal: /\/\/\/\____/\/\/\/\____
```

### ⚡ Özellikler:

* Basit donanım
* Gürültüye karşı zayıf
* Kısa mesafeli sistemlerde (IR, basit RF) kullanılır

🛰️ **Gerçek örnek:**
Kızılötesi uzaktan kumandalar, RFID sistemleri.

---

## 🌀 **2️⃣ Frequency Shift Keying (FSK) — Frekans Kaydırmalı Anahtarlama**

### 📘 Tanım:

Taşıyıcının **frekansı**, gönderilen bite göre değiştirilir.

| Bit | Frekans |
| --- | ------- |
| 1   | ( f_1 ) |
| 0   | ( f_2 ) |

📊 **Matematiksel Gösterim:**
[
s(t) =
\begin{cases}
A \cos(2\pi f_1 t), & \text{bit = 1} \
A \cos(2\pi f_2 t), & \text{bit = 0}
\end{cases}
]

```
Bit: 1 0 1
Sinyal: /\/\/\/\/\/\  /\/\/\/\  /\/\/\/\/\/\
```

### ⚡ Özellikler:

* Gürültüye dayanıklı
* Daha geniş bant genişliği gerektirir
* **Modemler** ve **Bluetooth** iletişiminde kullanılır

🛰️ **Gerçek örnek:**
Bluetooth → **Gaussian FSK (GFSK)** kullanır 💙

---

## 🔄 **3️⃣ Phase Shift Keying (PSK) — Faz Kaydırmalı Anahtarlama**

### 📘 Tanım:

Taşıyıcının **fazı**, gönderilen bite göre değiştirilir.

| Bit | Faz (derece) |
| --- | ------------ |
| 1   | 0°           |
| 0   | 180°         |

📊 **Matematiksel Gösterim:**
[
s(t) = A \cos(2\pi f_c t + \phi_i)
]

Burada ( \phi_i = 0 ) veya ( \pi ).

```
Bit: 1 0 1 0
Sinyal: /\/\/\/\____\/\/\/\/
          ↑ faz kayması ↑
```

### ⚡ Özellikler:

* Gürültüye oldukça dayanıklı
* Senkronizasyon gerektirir (alıcı taşıyıcı fazını bilmelidir)
* Wi-Fi, GSM, GPS gibi modern sistemlerde kullanılır

---

## 🔸 **3.1. Binary PSK (BPSK)**

Her bit bir faz değeriyle temsil edilir:

* 0 → 0°
* 1 → 180°

🧠 **Avantaj:** Gürültüye en dayanıklı dijital modülasyonlardan biri.
🧩 **Dezavantaj:** Bit başına yalnızca 1 bilgi birimi taşır → düşük hız.

---

## 🔸 **3.2. Quadrature PSK (QPSK)**

Her sembolde **2 bit** taşınır.
Faz dört farklı değer alır:

| Bit Çifti | Faz  |
| --------- | ---- |
| 00        | 45°  |
| 01        | 135° |
| 11        | 225° |
| 10        | 315° |

🧮 **Verimlilik:**
Aynı bant genişliğinde iki kat bilgi taşınır.

> BPSK → 1 bit/simge
> QPSK → 2 bit/simge

📡 **Gerçek örnek:**
Wi-Fi (802.11b), 3G ve 4G hücresel ağlar QPSK tabanlıdır.

---

## 🔸 **3.3. 8-PSK, 16-PSK**

Daha fazla faz değeriyle daha fazla bit taşınabilir.

| Modülasyon | Bit/Sembol |
| ---------- | ---------- |
| 8-PSK      | 3 bit      |
| 16-PSK     | 4 bit      |

> Ama dikkat: Faz aralıkları daraldıkça **hata riski artar** (faz farkı algılanamazsa bit hatası olur).

---

## 🔮 **4️⃣ QAM (Quadrature Amplitude Modulation) — Genlik + Faz**

Son seviye canavar 💪
Hem **genlik** hem **faz** aynı anda değiştirilir.

| Modülasyon | Bit/Sembol | Kullanım   |
| ---------- | ---------- | ---------- |
| 16-QAM     | 4 bit      | Wi-Fi, DVB |
| 64-QAM     | 6 bit      | LTE, 4G    |
| 256-QAM    | 8 bit      | 5G         |

📘 Örnek:
16-QAM, 4 bit’i temsil eden 16 farklı sinyal noktası üretir.

🧠 **Avantaj:** Yüksek veri hızı
⚠️ **Dezavantaj:** Gürültüye daha hassas

---

## 🧠 **5️⃣ Dijital Modülasyon Karşılaştırması**

| Özellik          | ASK   | FSK       | PSK        | QAM        |
| ---------------- | ----- | --------- | ---------- | ---------- |
| Gürültü Dayanımı | Düşük | Orta      | Yüksek     | Orta       |
| Bant Genişliği   | Dar   | Geniş     | Orta       | Geniş      |
| Veri Hızı        | Düşük | Orta      | Yüksek     | Çok yüksek |
| Karmaşıklık      | Basit | Orta      | Orta       | Yüksek     |
| Kullanım Alanı   | RFID  | Bluetooth | Wi-Fi, GSM | LTE, 5G    |

---

## 🔭 **6️⃣ Özet Şema**

```
Dijital Veri → [Modülatör] → Analog Sinyal → [Kanal] → [Demodülatör] → Dijital Veri
```

Her modülasyon türü, hız / dayanıklılık / bant genişliği arasında bir **denge oyunudur** 🎮

---

## 💬 **Kısa Özet:**

> Analog haberleşme duygusal sanat ise,
> dijital haberleşme onun mühendislik versiyonudur ⚙️

ASK — basit ama zayıf
FSK — orta seviye
PSK — akıllı, güçlü
QAM — profesyonel, 5G’nin bel kemiği 📡

---
