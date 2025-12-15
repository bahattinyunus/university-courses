# ⚙️ Elektronik Devreler Dersi Notları

## 1. 📘 Giriş: Elektronik Devre Nedir?

**Elektronik devre**, elektrik akımının belirli bir düzen içinde akmasını sağlayan, direnç, kapasitör, endüktör, diyot, transistör gibi elemanların oluşturduğu yapıdır.

Bir devre genelde iki kısımdan oluşur:

- **Kaynak (Source):** Gerilimi (voltajı) sağlar.  
- **Yük (Load):** Bu enerjiyi kullanan bileşendir (örneğin LED, motor, hoparlör).

### Devre Türleri

- **Analog devreler:** Sürekli değişen sinyallerle çalışır.  
- **Dijital devreler:** 0 ve 1 (binary) seviyelerinde çalışır.  
- **Karma devreler:** Hem analog hem dijital kısımları içerir (örnek: mikrodenetleyiciler).

---

## 2. ⚡ Temel Kavramlar

### 2.1 Akım (I)
- Elektronların devre boyunca hareketidir.  
- **Birimi:** Amper (A)  
- **Yönü:** Artı kutuptan eksi kutba doğru varsayılan akış yönü.

### 2.2 Gerilim (V)
- İki nokta arasındaki potansiyel farktır.  
- **Birimi:** Volt (V)  
- **Formül:**  
  \[
  V = I \times R
  \]

### 2.3 Direnç (R)
- Akıma karşı gösterilen zorluktur.  
- **Birimi:** Ohm (Ω)  
- **Formül:**  
  \[
  R = \frac{V}{I}
  \]

### 2.4 Güç (P)
- Enerji dönüşüm hızıdır.  
- **Birimi:** Watt (W)  
- **Formül:**  
  \[
  P = V \times I
  \]

---

## 3. 🔌 Devre Elemanları

### 3.1 Direnç (Resistor)
- Akımı sınırlar.  
- Renk kodlarıyla değer okunur (örnek: **kahverengi-siyah-kırmızı = 1kΩ**).  
- **Kullanım:** Akım sınırlama, gerilim bölücü, yükleme direnci.

### 3.2 Kondansatör (Capacitor)
- Elektrik yükünü depolayan elemandır.  
- **Birimi:** Farad (F)  
- **Formül:**  
  \[
  Q = C \times V
  \]

#### Türleri:
- **Elektrolitik:** Kutuplu, yüksek kapasite.  
- **Seramik:** Kutupsuz, düşük kapasite.  
- **Tantalum:** Küçük boyutlu, yüksek performans.

### 3.3 Bobin (Inductor)
- Manyetik alan oluşturur.  
- **Birimi:** Henry (H)  
- **Kullanım:** Filtreler, motor sürücüleri, enerji depolama.

### 3.4 Diyot (Diode)
- Akımı tek yönde iletir.  
- **İleri yön (Forward bias):** İletir.  
- **Ters yön (Reverse bias):** İletmez.  

#### Örnekler:
- **Zener Diyot:** Gerilim regülasyonu  
- **LED:** Işık yayan diyot  
- **Schottky Diyot:** Hızlı anahtarlama

### 3.5 Transistör (BJT - FET)
Elektrik akımını kontrol eder; anahtar veya yükselteç olarak kullanılır.

#### BJT (Bipolar Junction Transistor)
- **Terminalleri:** Base, Emitter, Collector  
- **Türleri:** NPN / PNP  
- Akım kontrollü elemandır.

#### FET (Field Effect Transistor)
- **Terminalleri:** Gate, Drain, Source  
- Gerilim kontrollü elemandır.

---

## 4. 🔁 Devre Bağlantı Türleri

### 4.1 Seri Bağlantı
- Akım aynıdır.  
- Gerilim bölünür.  
- **Toplam direnç:**  
  \[
  R_{toplam} = R_1 + R_2 + R_3 + \dots
  \]

### 4.2 Paralel Bağlantı
- Gerilim aynıdır.  
- Akım bölünür.  
- **Toplam direnç:**  
  \[
  \frac{1}{R_{toplam}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots
  \]

---

## 5. 🧮 Temel Devre Kanunları

### 5.1 Ohm Kanunu
\[
V = I \times R
\]

### 5.2 Kirchhoff Akım Kanunu (KCL)
Bir düğüme giren akımların toplamı, çıkan akımların toplamına eşittir.
\[
\sum I_{giren} = \sum I_{çıkan}
\]

### 5.3 Kirchhoff Gerilim Kanunu (KVL)
Bir kapalı döngüdeki tüm gerilimlerin cebirsel toplamı sıfırdır.
\[
\sum V = 0
\]

---

## 6. 🔋 Gerilim ve Akım Kaynakları

### 6.1 Gerilim Kaynağı
Sabit bir potansiyel farkı sağlar (örnek: **5V pil**).

### 6.2 Akım Kaynağı
Sabit bir akım sağlar (örnek: **1mA akım kaynağı**).

### 6.3 Bağımlı (Controlled) Kaynaklar
Çıkış değeri başka bir devre büyüklüğüne bağlıdır:

| Kısaltma | Açıklama |
|-----------|-----------|
| VCVS | Gerilim kontrollü gerilim kaynağı |
| CCVS | Akım kontrollü gerilim kaynağı |
| VCCS | Gerilim kontrollü akım kaynağı |
| CCCS | Akım kontrollü akım kaynağı |

---

## 7. 🧩 Devre Analizi Yöntemleri

### 7.1 Düğüm (Node) Gerilimi Yöntemi
Düğüm noktalarındaki potansiyelleri bulmak için **KCL** kullanılır.

### 7.2 Mesh (Kapsam) Akımı Yöntemi
Kapanımlar (loop’lar) üzerinde **KVL** uygulanır.

### 7.3 Süperpozisyon Teoremi
Birden fazla kaynak varsa, her biri ayrı ayrı etkilenip sonuçlar toplanır.

### 7.4 Thevenin Teoremi
Karmaşık devreyi tek bir **gerilim kaynağı + seri direnç** ile temsil eder.

### 7.5 Norton Teoremi
Karmaşık devreyi tek bir **akım kaynağı + paralel direnç** ile temsil eder.

---

## 8. 🔀 AC Devre Analizi

Alternatif akım (AC), zamanla yön değiştirir.  
Genel formu:
\[
v(t) = V_m \sin(\omega t + \phi)
\]

### 8.1 Fazör Temsili
Sinüzoidal işaretler fazör (vektör) formunda gösterilir.

### 8.2 Empedans (Z)
Direnç, kapasitans ve endüktans etkilerini birleştirir:
\[
Z = R + jX
\]

| Eleman | Empedans Formülü |
|---------|------------------|
| Direnç (R) | \( Z_R = R \) |
| Kapasitör (C) | \( Z_C = \frac{1}{j\omega C} \) |
| Bobin (L) | \( Z_L = j\omega L \) |

---

## 9. 🔉 Filtreler

Filtreler belirli frekansları geçirir veya engeller.

| Tür | Özellik |
|------|----------|
| Alçak Geçiren (Low Pass) | Düşük frekansları geçirir. |
| Yüksek Geçiren (High Pass) | Yüksek frekansları geçirir. |
| Bant Geçiren (Band Pass) | Belirli bir aralığı geçirir. |
| Bant Durduran (Band Stop) | Belirli bir aralığı engeller. |

---

## 10. ⚙️ Uygulama Alanları

- **Güç devreleri:** Enerji aktarımı, regülasyon.  
- **Ses devreleri:** Amplifikatörler, filtreler.  
- **Sinyal işleme:** Ölçüm sistemleri, sensör devreleri.  
- **Mikrodenetleyici tabanlı sistemler:** Arduino, Raspberry Pi devreleri.

---

## 11. 🧠 İpucu Kutusu

- Multimetre kullanmayı iyi öğren: Gerilim, akım, direnç ölçmeden devre anlamak imkânsız.  
- Simülasyon yazılımlarıyla (**Proteus, Multisim, Tinkercad**) sanal deneyler yap.  
- Breadboard üzerinde pratik yap: **Direnç + LED + transistör = temel laboratuvar seti 💡**  
- Devreyi çizmeyi alışkanlık haline getir — *“çizmek, anlamaktır.”*

---

## 12. 🔚 Sonuç

Elektronik devreler, mühendisliğin **“görünmeyen dili”** gibidir.  
Yazılım mühendisliğinde bile donanımı anlamak; gömülü sistemlerden yapay zekâ donanımlarına kadar seni bir seviye yukarı taşır.  
**Kısacası:** Elektroniği bilen yazılımcı, kodun ötesini görür. 🚀
