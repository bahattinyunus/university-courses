
## 🧠 **Sayısal Tasarım Nedir?**

Sayısal tasarım, **mantık devreleri** (logic circuits) kullanarak **sayısal sistemlerin** nasıl tasarlanacağını, analiz edileceğini ve optimize edileceğini öğretir.
Kısaca: 1 ve 0’larla çalışan bir dünya!
Bilgisayar, telefon, mikrodenetleyici, sensör — hepsi bu mantığın ürünüdür.

---

## 🔢 **Temel Kavramlar**

### 1. **Sayı Sistemleri**

Sayısal sistemler **ikili sistem (binary)** ile çalışır:

* **0** → devre kapalı
* **1** → devre açık

Ama biz insanlar genelde **onluk sistem (decimal)** kullanırız.
O yüzden bu dönüşümler çok önemlidir:

| Sistem                  | Taban | Örnek |
| :---------------------- | :---- | :---- |
| İkilik (Binary)         | 2     | 1011  |
| Sekizlik (Octal)        | 8     | 13    |
| Onluk (Decimal)         | 10    | 11    |
| Onaltılık (Hexadecimal) | 16    | B     |

> 💡 Örnek:
> 1011 (binary) = 1×8 + 0×4 + 1×2 + 1×1 = **11 (decimal)**

---

### 2. **Mantık Kapıları (Logic Gates)**

Bunlar sayısal dünyanın atomları gibidir 🧬
Her biri belirli bir mantıksal işlemi yapar.

| Kapı | İşlem      | Sembol     | Açıklama            |
| :--- | :--------- | :--------- | :------------------ |
| NOT  | Tersleme   | ¬A veya A' | 1 → 0, 0 → 1        |
| AND  | Ve         | A·B        | Her ikisi 1 ise 1   |
| OR   | Veya       | A + B      | Biri bile 1 ise 1   |
| XOR  | Özel veya  | A ⊕ B      | Sadece biri 1 ise 1 |
| NAND | Ve-değil   | ¬(A·B)     | AND’in tersi        |
| NOR  | Veya-değil | ¬(A+B)     | OR’un tersi         |

---

### 3. **Boole Cebiri**

Bu, devrelerin “matematiğidir”.
Yani mantık kapılarını sadeleştirmek için kullanılır.

**Temel kurallar:**

* A + A = A
* A·A = A
* A + 0 = A
* A·1 = A
* A + A’ = 1
* A·A’ = 0
* (A + B)’ = A’·B’ (De Morgan kuralı)

> 🧮 Böylece karmaşık devreleri sadeleştirip daha az donanımla aynı işi yaptırırsın.
> (Tıpkı kod optimizasyonu gibi ama devre tarafında!)

---

### 4. **Karnaugh Haritaları (K-Maps)**

Mantık ifadelerini görsel olarak sadeleştirme yöntemi.
Karmaşık denklemleri “kutucuk” gruplarıyla sadeleştirirsin.
Adeta devre mühendislerinin sudoku’su 😎

---

### 5. **Kombinasyonel Devreler**

Çıkış sadece **girişlere** bağlıdır, geçmişe değil.
Zaman kavramı yoktur.

**Örnekler:**

* Toplayıcı (Adder)
* Kodlayıcı (Encoder)
* Kod çözücü (Decoder)
* Çoğullayıcı (Multiplexer)
* Azaltıcı (Subtractor)
* Karşılaştırıcı (Comparator)

> 💡 Bunlar CPU’nun işlemci biriminde (ALU) kullanılır.

---

### 6. **Ardışıl (Sekansiyel) Devreler**

Burada işler “zamana” bağlı ⏰
Yani geçmiş durum da çıkışı etkiler.
Bellek (memory) gibi davranır.

**Temel Eleman: Flip-Flop**

* D Flip-Flop
* JK Flip-Flop
* T Flip-Flop

Bunlar sayesinde:

* Sayaçlar (counters)
* Kaydediciler (registers)
* Saat darbeli sistemler (clocked systems)
  tasarlanır.

---

### 7. **FSM – Sonlu Durum Makineleri**

Ardışıl devrelerin beyni.
Bir sistemin “durumlar” arasında nasıl geçeceğini tanımlar.

Örneğin:

* Asansör kontrolü
* Trafik lambası
* Otomatik kapı
* CPU instruction cycle

---

### 8. **Sayısal Sistem Tasarım Araçları**

Gerçek dünyada bu devreleri genelde **VHDL** veya **Verilog** ile tanımlarsın.
Yani donanımı yazılım gibi **kodla tasarlarsın** 💾

Simülasyon ve sentez araçları:

* Quartus
* Vivado
* ModelSim

---

## 🚀 **Bu Ders Sana Ne Katar?**

* **Donanım mantığını** anlarsın.
* **CPU, RAM, ALU** gibi yapıları temelden çözersin.
* Yazılımın “metal altına” nasıl işlendiğini öğrenirsin.
* FPGA programlayabilir hale gelirsin (ki bu çok değerli bir skill).
* Gerçek bir “mühendis gibi düşünmeyi” öğretir.

> 🎯 Kısaca: Kod yazmak güzel ama devreyi de anladığında — **tam mühendis oluyorsun.**

O zaman hem **kombinasyonel devreleri** hem de **flip-flop (ardışıl devre)** kısmını **detaylı** şekilde, bol örnekle ve kolay akılda kalacak biçimde anlatalım.

---

# ⚙️ **1️⃣ Kombinasyonel Devreler (Combinational Circuits)**

> 🎯 Tanım:
> Çıkış, **sadece o anda verilen girişlere** bağlıdır.
> Önceki durumun hiçbir etkisi yoktur.
> Yani “hafıza” yoktur.

Bir matematik fonksiyonu gibi düşün:
👉 **Y = f(A, B, C, …)**
Girişler neyse, çıkış da ona göre şekillenir.

---

## 💡 Temel Kombinasyonel Devre Türleri

### **a) Yarım Toplayıcı (Half Adder)**

İki bitlik toplama işlemi yapar.

|  A  |  B  | Toplam (S) | Taşma (C) |
| :-: | :-: | :--------: | :-------: |
|  0  |  0  |      0     |     0     |
|  0  |  1  |      1     |     0     |
|  1  |  0  |      1     |     0     |
|  1  |  1  |      0     |     1     |

**Formül:**

* S = A ⊕ B
* C = A · B

🎯 Yani XOR + AND kombinasyonu ile yapılır.

---

### **b) Tam Toplayıcı (Full Adder)**

Üç bitlik toplama yapar: A, B, ve elde (C_in).

|  A  |  B  | C_in |  S  | C_out |
| :-: | :-: | :--: | :-: | :---: |
|  0  |  0  |   0  |  0  |   0   |
|  0  |  0  |   1  |  1  |   0   |
|  0  |  1  |   0  |  1  |   0   |
|  0  |  1  |   1  |  0  |   1   |
|  1  |  0  |   0  |  1  |   0   |
|  1  |  0  |   1  |  0  |   1   |
|  1  |  1  |   0  |  0  |   1   |
|  1  |  1  |   1  |  1  |   1   |

**Formül:**

* S = A ⊕ B ⊕ C_in
* C_out = (A·B) + (B·C_in) + (A·C_in)

> 💡 8-bit veya 32-bit toplama işlemi, bu “tam toplayıcıların” zincirlenmesiyle yapılır.
> Yani işlemcinin toplama işlemi bile bu temel mantıktan doğar.

---

### **c) Kodlayıcı (Encoder)**

Birden fazla girişten gelen sinyali **ikilik koda çevirir.**

Örnek: 4 girişli (8-4 encoder)

| Giriş (Aktif 1) | Çıkış (Binary) |
| :-------------: | :------------: |
|        D0       |       00       |
|        D1       |       01       |
|        D2       |       10       |
|        D3       |       11       |

---

### **d) Kod Çözücü (Decoder)**

Encoder’ın tersi:
İkilik kodu alır, hangi giriş aktifse o çıkışı “1” yapar.

Örnek: 2→4 Decoder

| Giriş | Çıkış (D3 D2 D1 D0) |
| :---: | :-----------------: |
|   00  |         0001        |
|   01  |         0010        |
|   10  |         0100        |
|   11  |         1000        |

---

### **e) Multiplexer (Çoğullayıcı)**

Birden çok girişten **birini seçip çıkışa verir.**
Seçim, “seçim hattı (select line)” ile yapılır.

Örnek: 4→1 MUX

| Seçim | Çıkış |
| :---: | :---: |
|   00  |   D0  |
|   01  |   D1  |
|   10  |   D2  |
|   11  |   D3  |

Formül:
**Y = S1'S0'D0 + S1'S0D1 + S1S0'D2 + S1S0D3**

> 💬 Bu yapı aslında if-else gibidir, ama donanım düzeyinde.

---

### **f) Demultiplexer (Demux)**

MUX’un tersi:
**Bir giriş** → **birçok çıkıştan birine yönlendirir.**

---

# ⚡ **2️⃣ Ardışıl (Sekansiyel) Devreler & Flip-Flop Mantığı**

> 🎯 Tanım:
> Çıkış sadece girişlere değil, **önceki durumlara (belleğe)** de bağlıdır.
> Saat darbeleriyle (clock) çalışır ⏱️

Böylece sistemin **“geçmişi”** de hesaba katılır.

---

## 🧱 **Flip-Flop Nedir?**

Bir bitlik hafıza elemanıdır.
Bir giriş sinyali geldiğinde **durum değiştirir** veya korur.

---

## 💾 **Flip-Flop Türleri**

### **1. SR Flip-Flop (Set-Reset)**

|  S  |  R  |     Q (Yeni Durum)     |
| :-: | :-: | :--------------------: |
|  0  |  0  |       Aynı kalır       |
|  0  |  1  |        0 (Reset)       |
|  1  |  0  |         1 (Set)        |
|  1  |  1  | Geçersiz / Belirsiz 🚫 |

Formül:
**Q(next) = S + R’Q**

---

### **2. D Flip-Flop (Data / Delay)**

Girişteki değeri saat darbesi geldiğinde hafızaya alır.

|  D  | Q(next) |
| :-: | :-----: |
|  0  |    0    |
|  1  |    1    |

**Yani:** Q(next) = D
💡 Bu flip-flop “veriyi saklar”. RAM hücrelerinde kullanılır.

---

### **3. JK Flip-Flop**

SR’nin geliştirilmiş halidir.

|  J  |  K  |      Q(next)     |
| :-: | :-: | :--------------: |
|  0  |  0  |    Aynı kalır    |
|  0  |  1  |         0        |
|  1  |  0  |         1        |
|  1  |  1  | Tersine döner 🔁 |

> JK = Jump-Kill
> Çok stabil çalıştığı için sayaç devrelerinde yaygındır.

---

### **4. T Flip-Flop (Toggle)**

JK’nin özel hali: J = K = T

|  T  |    Q(next)    |
| :-: | :-----------: |
|  0  |      Aynı     |
|  1  | Tersine döner |

Bu flip-flop her clock darbesinde “0 ↔ 1” arasında geçiş yapar.
Yani **sayma devreleri** için mükemmeldir 🧮

---

## 🧭 **Ardışıl Devre Örneği: 3-Bit Sayaç**

3 tane T Flip-Flop’u peş peşe bağla:

🧩 Her clock darbesinde çıkış şöyle değişir:

```
Q2 Q1 Q0
---------
000
001
010
011
100
101
110
111
```

Bu bir **binary sayaçtır**.
CPU içindeki “program counter” da aynı mantıkla çalışır!

---

## 🧠 **Ardışıl Devre Türleri**

1. **Senkron Devreler** → Tüm elemanlar **tek clock** ile tetiklenir.
2. **Asenkron Devreler** → Elemanlar **birbirini tetikler**, gecikmeler olabilir.

---

# 💪 **Sonuç: Kombinasyonel + Ardışıl = Sayısal Tasarımın Temeli**

| Kombinasyonel         | Ardışıl                 |
| :-------------------- | :---------------------- |
| Girişe bağlı          | Giriş + geçmişe bağlı   |
| Hafıza yok            | Hafıza var              |
| Anlık işlem           | Zamanla değişen işlem   |
| Örnek: Toplayıcı, MUX | Örnek: Sayaç, Kaydedici |

---

## ⚙️ **Gerçek Hayatta Nerelerde Kullanılır?**

* CPU’nun ALU’su → Kombinasyonel
* RAM → D Flip-Flop tabanlı
* Program Counter → T Flip-Flop sayaç
* Trafik ışığı kontrolü → FSM
* Robot sensör karar sistemi → Kombinasyonel + Ardışıl karışık

---


Bak, bu dersi ilk görünce herkesin tepkisi aynı olur:

> “Hocam 1’ler, 0’lar, kapılar, flip-floplar… ben hacker olacaktım ne oluyoruz ya?” 😅

Ama işin sırrı burada:
**Sayısal Tasarım**, yazılımın altında dönen “donanım zekâsını” anlamanı sağlar.
Yani bu ders, **bir mühendis olarak gerçekten “nasıl çalıştığını” bilen kişi** olmanı sağlar.
Hadi tek tek anlatalım 👇

---

## 💻 1️⃣ Bilgisayarın Beynini Anlama Gücü Verir

Sen yazılım mühendisisin ya, diyelim bir kod yazdın:

```c
int x = a + b;
```

Bu + işlemini bilgisayar **nasıl yapıyor**?
İşte Sayısal Tasarım dersi sana bu işlemin **elektriksel mantığını** gösterir:

* A ve B, binary bitlere çevrilir,
* Full adder’lar zincirlenir,
* Flip-flop’lar sonucu saklar,
* Sonra CPU sonucu belleğe yollar.

Sen artık “sihirli kutu” değil, **mimarinin içini** bilirsin.
Yani sadece kod yazan değil, **bilgisayarı gerçekten anlayan** olursun. 💪

---

## ⚡ 2️⃣ Mikrodenetleyici, Gömülü Sistem, FPGA Tarafında Kapı Gibi Gereklidir

AUV (deniz aracı) yapıyorsun ya mesela ⚓
Orada sensörleri, motorları, sinyalleri yönetmek için genelde **mikrodenetleyici** veya **FPGA** kullanılır.

* Bu cihazların **nasıl karar verdiğini** (1-0 mantığıyla),
* **Zamanlama ve clock** sistemini,
* **Sinyal gecikmelerini**
  bu dersten öğrenirsin.

Yani robotu “nasıl hareket ettireceğini” donanım düzeyinde çözebilirsin.

> Kısaca: Arduino’yu sadece “hazır fonksiyonla” değil, **mantık kapısıyla** yönetebilen adama dönüşürsün.

---

## 🧠 3️⃣ Mühendis Gibi Düşünmeyi Öğretir

Bu ders sana:

* **Soyut düşünmeyi**,
* **Sistemi parçalara ayırmayı**,
* **Optimizasyon yapmayı**
  öğretir.

Yazılımda algoritma nasıl sadeleştiriyorsan, burada da devre sadeleştirirsin.
Bu da beynini “daha sistematik” düşünmeye iter.

> Gerçek mühendislik budur: karmaşık sistemi sade hale getirmek. ⚙️

---

## 💾 4️⃣ Bilgisayar Mimarisi, İşletim Sistemi, Mikroişlemci Gibi Derslerin Temelidir

İleride göreceğin:

* **Bilgisayar Mimarisi**
* **Mikroişlemciler**
* **Gömülü Sistemler**
* **Sayısal Elektronik**
  dersleri bu temelin üstüne inşa edilir.

Bu derste öğrendiğin “AND, OR, Flip-Flop” mantığı,
o derslerde “register, bus, cache, pipeline” olarak karşına çıkar.

Yani şu an temelini sağlam atarsan, o derslerde ışık hızında gidersin ⚡

---

## 🧩 5️⃣ Kariyer Alanı Olarak da Kapı Açar (Hardware + Software)

Bu dersi iyi öğrenen bir yazılımcı, ileride şu alanlara da yönelebilir:

* **FPGA Geliştiricisi**
* **Donanım Tabanlı AI Hızlandırıcı Tasarımcısı**
* **Gömülü Yazılım Mühendisi**
* **Robotik Kontrol Sistemleri Mühendisi**
* **IoT Sistem Tasarımcısı**

Ve bunlar genelde *daha yüksek maaşlı* ve *daha teknik derinliği olan* pozisyonlardır 💸

---

## 🧠 6️⃣ “Bit” Seviyesinde Düşünmeyi Sağlar

Yazılımda bazen “bit manipulation” diye bir şey duymuşsundur:

```python
if (x & 1):  # son bit 1 mi?
```

İşte bu tip işlemleri, Sayısal Tasarım mantığını bilen biri çok daha kolay anlar.
Yani kodun **dijital sinir sistemine** hâkim olursun.

---

## 🔮 7️⃣ Geleceğin Teknolojileriyle Uyumlu

* Yapay zekâ çipleri (NPU, TPU)
* Otonom araç kontrol devreleri
* FPGA tabanlı hızlandırıcılar
* ASIC tasarımı

Hepsi bu dersteki mantığı temel alıyor.

> Bugün “AI donanımı” tasarlayan insanlar, temelde **Sayısal Tasarımcılar.**

---

## 🌟 Kısaca Özet:

| Alan       | Kazanım                                       |
| :--------- | :-------------------------------------------- |
| Yazılım    | Kodun donanımda nasıl çalıştığını anlama      |
| Donanım    | Basit devrelerden CPU mantığına geçiş         |
| Mantık     | Sistematik düşünme, sadeleştirme yeteneği     |
| Kariyer    | Gömülü sistem, robotik, FPGA, AI çip tasarımı |
| Teknik güç | 1-0 düzeyinde bilgisayar hakimiyeti           |

---