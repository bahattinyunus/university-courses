# ⚙️ Analog Elektronik Nedir?

**Analog elektronik**, elektriksel büyüklüklerin **sürekli değiştiği** sistemlerle ilgilenir.  
Yani **voltaj (gerilim)** ve **akım (current)** gibi değerler zamanla değişir — dijitaldeki gibi **0 ya da 1** değildir.

---

## 🔊 Örnek Analog Sinyaller
- 🎙️ Ses sinyali (mikrofon çıkışı)  
- ☀️ Işık sensörü voltajı  
- ❤️ Kalp atış sinyali  

Hepsi **analog sinyallerdir.**

---

## 🔌 Temel Bileşenler

### 1. Direnç (Resistor - R)
- Akımı sınırlar.  
- **Ohm Kanunu:**  
  \[
  V = I \times R
  \]
- Bir nevi *trafik polisi* gibidir; akımın ne kadar geçeceğini belirler.  
- Kullanım: gerilim bölücü, filtre, akım sınırlama.

---

### 2. Kapasitör (Capacitor - C)
- Elektrik yükünü depolar, zamanla **dolup boşalır.**  
- **Formül:**  
  \[
  I = C \times \frac{dV}{dt}
  \]
- **Kullanım:** sinyal filtreleme, zamanlama, ses devrelerinde “gürültü süzgeci”.

---

### 3. Bobin (İndüktör - L)
- Manyetik alan oluşturur, akım değişimlerine karşı çıkar.  
- **Formül:**  
  \[
  V = L \times \frac{dI}{dt}
  \]
- Akımı “yavaşlatır”.  
- Genellikle güç devrelerinde ve filtrelerde kullanılır.

---

### 4. Diyot
- Akımı **tek yönde geçirir** 🔁  
- Elektriğin tek yönlü otoyol kapısı gibidir.  
- **Kullanım:** doğrultma (AC → DC), sinyal koruma.

---

### 5. Transistör
- Elektroniğin kalbi 💓  
- Hem **anahtar** hem **yükselteç (amplifikatör)** olarak kullanılır.  

**Basitçe:**  
Küçük bir sinyali girişe verirsin → çıkışta büyümüş olarak alırsın.

**Formül (BJT için):**  
\[
V_{out} = -\beta \times V_{in}
\]
- **β:** transistör kazancı

---

### 6. Op-Amp (Operational Amplifier)
- Yüksek kazançlı, fark alabilen yükselteçtir.  
- Girişleri: (+) non-inverting, (−) inverting  
- **Kullanım alanları:**
  - Sinyal yükseltme  
  - Filtreleme  
  - Matematiksel işlemler (toplama, çıkarma, entegrasyon)

---

## 📈 Analog Devre Türleri

### 1. Yükselteç (Amplifier) Devreleri
**Amaç:** Sinyali büyütmek.

**Tipleri:**
- Ortak Emiter (BJT)
- Ortak Kaynak (MOSFET)
- Op-Amp (Operational Amplifier)

**Uygulama:** ses sistemleri, radyo devreleri, sensör çıkışları.

---

### 2. Filtre Devreleri
**Amaç:** Belirli frekansları geçirmek veya engellemek.

| Tür | Özellik | Kullanım |
|-----|----------|-----------|
| Alçak geçiren (Low-pass) | Yavaş sinyalleri geçirir, gürültüyü engeller | Bas filtreleri |
| Yüksek geçiren (High-pass) | Hızlı değişen sinyalleri geçirir | Tiz filtreleri |
| Band geçiren (Band-pass) | Belirli frekans aralığını geçirir | Radyo, müzik sentezi |

---

### 3. Osilatör Devreleri
- Kendi kendine sinyal üretir 🔄  
- **Dalga türleri:** sinüs, kare, üçgen  
- **Kullanım:** radyo frekansları, saat darbeleri, müzik sentezleme

---

### 4. Doğrultma ve Güç Devreleri
- **AC → DC** çevirir.  
- Diyot köprüleri ve kapasitörlerle DC gerilimi dengeler.

---

## 🧮 Temel Yasalar

### 1. Ohm Kanunu
\[
V = I \times R
\]

### 2. Kirchhoff Akım Yasası (KCL)
Bir düğümde **giren akımların toplamı = çıkan akımların toplamı.**

### 3. Kirchhoff Gerilim Yasası (KVL)
Bir kapalı döngüde **tüm gerilimlerin toplamı = 0.**

---

## ⚡ Neden Öğrenmelisin?

Çünkü analog elektronik bilmek:
- Devrelerin **gerçek dünyayla nasıl konuştuğunu** anlamanı sağlar.  
- Sensör, mikrofon, kamera gibi **giriş/çıkış sistemlerini çözmeni** sağlar.  
- Yazılımcı olarak **IoT, gömülü sistemler, robotik** gibi alanlarda fark yaratmanı sağlar.  

---

# 🔧 Uygulama: Ortak Emiter (BJT) Yükselteç Devresi

## 1️⃣ Devreyi Tanıyalım
**Amaç:** Küçük bir AC sinyali (örneğin mikrofon çıkışı) alıp daha büyük bir AC sinyale dönüştürmek.

**Bileşenler:**
- NPN Transistör (BC547)
- R1, R2 (bias), RC (kolektör), RE (emiter)
- C1 (giriş), C2 (çıkış)
- Besleme: Vcc = 12V

---

## 2️⃣ Devre Şeması
    Vcc
     |
    RC
     |
     |----> Vout (Çıkış)
     |
    C
    |\

---

## 3️⃣ Devre Analizi
### Biasing (Çalışma Noktası)
Transistörün doğru çalışması için base gerilimi ayarlanır.

\[
V_B = V_{CC} \times \frac{R2}{R1 + R2}
\]
\[
V_E \approx V_B - 0.7V
\]

---

### AC Sinyal Yükseltme
- Giriş sinyali **C1** ile base’e geçer.  
- Base akımındaki küçük değişim → kolektörde büyük voltaj değişimi.  
- Çıkış **RC** üzerinden alınır.

---

### Kapasitörler
- **C1:** AC sinyali geçirir, DC’yi engeller.  
- **C2:** Çıkışta DC’yi bloke eder.

---

## 4️⃣ Örnek Hesaplama
Varsayalım:
- Vcc = 12V  
- RC = 2 kΩ  
- RE = 500 Ω  
- β = 100  

\[
V_B \approx 2V, \quad V_E \approx 1.3V
\]
\[
V_C = 12V - (2mA \times 2kΩ) = 8V
\]

✅ Transistör aktif bölgede, sinyal doğru şekilde yükselir.

---

## 5️⃣ Devre Çıkışı
- Giriş: 100 mV  
- Çıkış: 2–3 V  
- Faz: 180° **terslenmiş** çıkış  

---

## 6️⃣ Simülasyon
**LTspice / Multisim** kullan:
1. BJT ve dirençleri ekle  
2. Giriş sinyali: 100 mV  
3. Run → Vout’u gözlemle  
4. Çıkış sinyali büyümüş ve fazı ters olmalı

---

# 🔧 Non-Inverting Op-Amp Yükselteç Devresi

## 1️⃣ Devreyi Tanıyalım
**Amaç:** Küçük bir AC sinyali büyütmek — faz terslemesi olmadan.

**Bileşenler:**
- Op-Amp (LM741)
- R1 (feedback), R2 (ground)
- C1 (giriş)
- Besleme: ±12V veya 0–12V

---

## 2️⃣ Devre Şeması

---

## 3️⃣ Devre Analizi
### Kazanç Hesabı
\[
A_v = 1 + \frac{R1}{R2}
\]

**Örnek:** R1 = 10kΩ, R2 = 1kΩ  
\[
A_v = 1 + 10 = 11
\]
➡️ Sinyal 11 kat büyür.

---

### AC Sinyal Davranışı
- **C1:** DC’yi engeller, AC sinyali geçirir.  
- Çıkış, girişle **aynı fazda**.

---

### Avantajları
✅ Yüksek giriş empedansı  
✅ Lineer kazanç  
✅ Faz terslemesi yok  

---

## 4️⃣ Örnek Hesap
\[
V_{in} = 100mV, \quad A_v = 11
\]
\[
V_{out} = 0.1V \times 11 = 1.1V
\]

➡️ BJT’ye göre daha temiz ve lineer yükseltme.

---

## 5️⃣ Simülasyon
1. **LTspice** aç  
2. Op-Amp ve dirençleri yerleştir  
3. Vin = 100 mV AC sinyal ver  
4. Run → Vout’u gözlemle  

Fazın **aynı yönde** kaldığını göreceksin 🎧

---

## 💡 Not
| Devre Tipi | Faz Durumu | Kazanç Ayarı | Özellik |
|-------------|-------------|--------------|----------|
| BJT Yükselteç | 180° ters | Transistör β’sına bağlı | Faz tersleme, dinamik |
| Op-Amp Yükselteç | Aynı faz | Direnç oranına bağlı | Kararlı, temiz çıkış |

---

> 🔭 **Sonuç:**  
> Analog elektronik, gerçek dünyadaki sinyalleri anlamanın dilidir.  
> Her volt, her Hertz bir hikâye anlatır — sen de o hikâyeyi okumayı öğreniyorsun. ⚡
