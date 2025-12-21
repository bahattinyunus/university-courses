
# 🧠 **Algoritma Dersi Notları**

---

## 🚀 **1. Algoritma Nedir?**

> **Algoritma**, bir problemi çözmek veya bir görevi yerine getirmek için izlenen **adım adım işlemler dizisidir**.

Bir başka deyişle:

> “Bir işi bilgisayara yaptırmak istiyorsan, önce nasıl yapılacağını algoritma ile tarif etmelisin.”

---

## 🧩 **2. Algoritmanın Özellikleri**

| Özellik                   | Açıklama                                                       |
| ------------------------- | -------------------------------------------------------------- |
| **Başlangıç ve Bitiş**    | Her algoritmanın net bir başlangıç ve bitiş noktası olmalıdır. |
| **Açıklık (Netlik)**      | Adımlar anlaşılır, açık ve çelişkisiz olmalıdır.               |
| **Sonluluk**              | Algoritma, sınırlı sayıda adımda tamamlanmalıdır.              |
| **Girdi (Input)**         | İşlenecek veriler algoritmaya girilir.                         |
| **Çıktı (Output)**        | Algoritma sonunda bir sonuç üretmelidir.                       |
| **Etkinlik (Verimlilik)** | Her adım makul bir sürede gerçekleştirilebilir olmalıdır.      |

---

## ⚙️ **3. Algoritma Nasıl Yazılır?**

Algoritmalar genellikle 3 farklı biçimde ifade edilir:

1. **Doğal dil (Türkçe / İngilizce anlatım)**
2. **Akış diyagramı (Flowchart)**
3. **Sözde kod (Pseudocode)**

---

## 🔁 **4. Akış Diyagramı Sembolleri**

| Sembol | Anlamı            | Görsel Temsil (Metinsel) |
| ------ | ----------------- | ------------------------ |
| ⬛      | Başlangıç / Bitiş | **Start / End**          |
| 🔺     | Karar Verme       | **if / else**            |
| ⬜      | İşlem (Process)   | **x = x + 1**            |
| ⬧      | Giriş / Çıkış     | **Input / Output**       |
| 🔄     | Akış Yönü         | **→ ↓ ↑ ←**              |

---

## 🧮 **5. Temel Algoritma Yapıları**

1. **Sıralı Yapı**

   * İşlemler sırayla yapılır.
   * Örnek:

     ```
     Adım 1: A sayısını al
     Adım 2: B sayısını al
     Adım 3: Toplam = A + B
     Adım 4: Yazdır(Toplam)
     ```

2. **Seçim Yapısı (Karar Verme)**

   * Belirli bir koşula göre farklı yollar izlenir.
   * Örnek:

     ```
     Eğer sayı > 0 ise
         Yaz("Pozitif")
     Değilse
         Yaz("Negatif veya sıfır")
     ```

3. **Döngü Yapısı**

   * Bir işlem belirli koşul sağlanana kadar tekrar edilir.
   * Örnek:

     ```
     i = 1
     While i <= 10
         Yaz(i)
         i = i + 1
     ```

---

## 💡 **6. Örnek Algoritmalar**

### 🧠 Örnek 1: En Büyük Sayıyı Bulma

```
Başla
A, B, C sayılarını al
Eğer A > B ve A > C ise EnBüyük = A
Değilse Eğer B > C ise EnBüyük = B
Değilse EnBüyük = C
Yaz(EnBüyük)
Bitir
```

### 💬 Örnek 2: Faktöriyel Hesaplama

```
Başla
Sayıyı al (n)
Sonuç = 1
i = 1
While i <= n
    Sonuç = Sonuç * i
    i = i + 1
Yaz(Sonuç)
Bitir
```

---

## 🔢 **7. Algoritma Karmaşıklığı (Complexity)**

Bir algoritmanın **hızı ve verimliliği**, iki ölçüte göre değerlendirilir:

| Tür                                        | Açıklama                                  |
| ------------------------------------------ | ----------------------------------------- |
| **Zaman Karmaşıklığı (Time Complexity)**   | Algoritmanın çalışma süresini ifade eder. |
| **Bellek Karmaşıklığı (Space Complexity)** | Kullanılan hafıza miktarını belirtir.     |

> 💬 Örnek:
> “Bir dizideki tüm elemanları gezmek” → **O(n)** zaman karmaşıklığı.

---

## 📚 **8. Algoritma Analizi Örnekleri**

| Algoritma      | Karmaşıklık | Açıklama                              |
| -------------- | ----------- | ------------------------------------- |
| Doğrusal Arama | O(n)        | Tüm elemanlar teker teker aranır.     |
| İkili Arama    | O(log n)    | Sıralı dizilerde hızlı arama yapılır. |
| Bubble Sort    | O(n²)       | Basit sıralama algoritması.           |
| Merge Sort     | O(n log n)  | Verimli sıralama algoritması.         |

---

## 🔍 **9. Gerçek Hayatta Algoritmalar**

| Senaryo                | Algoritma Mantığı       |
| ---------------------- | ----------------------- |
| Google arama sonuçları | Sıralama + filtreleme   |
| Trafik ışıkları        | Karar + döngü           |
| ATM para çekme işlemi  | Girdi → Kontrol → Çıktı |
| Sosyal medya akışı     | Öneri algoritmaları     |

---

## 🧭 **10. Sonuç**

Bir algoritmayı doğru kurmak = programlamanın **yarısını** başarmak demektir.
Kalan yarısı sadece onu bir programlama dilinde (Python, C++, vs.) kodlamaktır.

> **Formül:**
> Düşünce → Algoritma → Kod → Sonuç ✅


# 🧩 **Sözde Koddan Python’a Geçiş Rehberi**

---

## 💡 **1. Sözde Kod Nedir?**

Sözde kod (pseudocode), algoritmanın **programlama diline çok benzeyen ama kuralsız** hâlidir.
Amacı:

> Kod yazmadan önce mantığı planlamak 🧠

Örneğin:

```
Başla
A, B sayılarını al
Toplam = A + B
Yaz(Toplam)
Bitir
```

Bu, **program değil** — sadece düşüncenin düzenli hâli.

---

## 🐍 **2. Python’a Dönüştürme Adımları**

| Sözde Kod     | Python Karşılığı                                |
| ------------- | ----------------------------------------------- |
| Başla / Bitir | Yok (Python’da kod akışı zaten sırayla çalışır) |
| Yaz(...)      | `print(...)`                                    |
| Oku / Al      | `input()`                                       |
| Değer ata     | `=`                                             |
| Eğer ... ise  | `if`                                            |
| Aksi halde    | `else`                                          |
| Döngü         | `for`, `while`                                  |

---

## ⚙️ **3. Örneklerle Dönüşüm**

---

### 🧮 Örnek 1: Toplama İşlemi

**Sözde Kod:**

```
Başla
A, B sayılarını al
Toplam = A + B
Yaz(Toplam)
Bitir
```

**Python Kodu:**

```python
A = int(input("Birinci sayıyı gir: "))
B = int(input("İkinci sayıyı gir: "))
Toplam = A + B
print("Toplam:", Toplam)
```

---

### 🔁 Örnek 2: 1’den 10’a kadar sayıları yazdır

**Sözde Kod:**

```
i = 1
While i <= 10
    Yaz(i)
    i = i + 1
Bitir
```

**Python Kodu:**

```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

---

### ⚖️ Örnek 3: Pozitif / Negatif Kontrolü

**Sözde Kod:**

```
Sayıyı al
Eğer sayı > 0 ise Yaz("Pozitif")
Değilse Eğer sayı < 0 ise Yaz("Negatif")
Aksi halde Yaz("Sıfır")
Bitir
```

**Python Kodu:**

```python
sayi = int(input("Bir sayı gir: "))

if sayi > 0:
    print("Pozitif")
elif sayi < 0:
    print("Negatif")
else:
    print("Sıfır")
```

---

### 💬 Örnek 4: Faktöriyel Hesaplama

**Sözde Kod:**

```
Sayıyı al (n)
Sonuç = 1
i = 1
While i <= n
    Sonuç = Sonuç * i
    i = i + 1
Yaz(Sonuç)
Bitir
```

**Python Kodu:**

```python
n = int(input("Bir sayı gir: "))
sonuc = 1
i = 1

while i <= n:
    sonuc *= i
    i += 1

print("Faktöriyel:", sonuc)
```

---

### 🧠 Örnek 5: En Büyük Sayıyı Bulma

**Sözde Kod:**

```
A, B, C sayılarını al
Eğer A > B ve A > C ise EnBüyük = A
Değilse Eğer B > C ise EnBüyük = B
Aksi halde EnBüyük = C
Yaz(EnBüyük)
Bitir
```

**Python Kodu:**

```python
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

if A > B and A > C:
    en_buyuk = A
elif B > C:
    en_buyuk = B
else:
    en_buyuk = C

print("En büyük sayı:", en_buyuk)
```

---

## 🚀 **4. İleri Seviye Dönüşüm: Liste ve Döngü**

**Sözde Kod:**

```
n adet sayı oku
Bu sayıların ortalamasını bul
```

**Python Kodu:**

```python
n = int(input("Kaç sayı gireceksin? "))
toplam = 0

for i in range(n):
    sayi = float(input(f"{i+1}. sayıyı gir: "))
    toplam += sayi

ortalama = toplam / n
print("Ortalama:", ortalama)
```

---

## 🎯 **5. Özet Tablolar**

| Sözde Kod        | Python                    |
| ---------------- | ------------------------- |
| `Eğer ... ise`   | `if ...:`                 |
| `Değilse`        | `else:`                   |
| `Değilse Eğer`   | `elif ...:`               |
| `While ...`      | `while ...:`              |
| `For i = 1 to n` | `for i in range(1, n+1):` |
| `Yaz(...)`       | `print(...)`              |
| `Oku(...)`       | `input(...)`              |

---

## 💬 **6. Kapanış**

> 💡 **Sözde kod = düşünce**
> 💻 **Python = düşüncenin eyleme dönüşmüş hali**

Yani önce “ne yapacağım”ı düşün, sonra Python’a çevirmek çocuk oyuncağı olur 👶🐍



# 🧠 **Neden Algoritma Öğrenmeliyim?**

---

## 🎯 **1. Çünkü Algoritma, Yazılımın Kalbidir**

> Kod yazmak, sadece sözdizimini bilmek değil; **düşünmeyi sistemleştirmektir.**

Python, C++ veya Java bilmek sana *nasıl yazılır*’ı öğretir.
Ama algoritma, sana *ne yazılmalı ve neden* yazılmalı’yı öğretir.

🧩 **Kısaca:**
Bir programlama dili → kalemdir.
Algoritma → düşüncedir.

> Kalem düşüncesiz işe yaramaz. ✍️

---

## 🚀 **2. Çünkü Problem Çözme Yeteneğini Keskinleştirir**

Her algoritma, bir problem çözme pratiğidir.
Zihnini “mantıksal adımlar”a alıştırırsın.
Bir süre sonra:

* Sorunlara daha sistematik bakarsın,
* Karmaşık şeyleri küçük parçalara ayırmayı öğrenirsin,
* Gerçek hayattaki kararlarını bile daha verimli verirsin (cidden).

> 💬 Yazılımcı olmayan biri bile algoritma öğrenince daha iyi düşünür.

---

## 🔁 **3. Çünkü Kod Yazmayı Kolaylaştırır**

Programlama dillerinin kuralları değişir, ama algoritma **evrensel**dir.
Bir dilde öğrendiğin algoritma, diğerine direkt taşınır.

Örneğin:

* **Faktöriyel hesaplama algoritması**, hem Python’da hem C’de aynıdır.
* Sadece yazım şekli değişir.

Bu yüzden algoritma öğrenen biri, **her dilde hızlı adapte olur.**

---

## 💡 **4. Çünkü Her Şeyin Arkasında Bir Algoritma Var**

Modern dünya algoritmalarla dönüyor:

| Alan            | Kullanılan Algoritmalar        |
| --------------- | ------------------------------ |
| 🌐 Google Arama | Sıralama (PageRank)            |
| 🤖 Yapay Zeka   | Sinir ağları, optimizasyon     |
| 💸 Bankacılık   | Güvenlik, risk analizi         |
| 🎮 Oyun         | Fizik, yol bulma (pathfinding) |
| 📱 Sosyal Medya | Öneri sistemleri, filtreleme   |

Yani **dünyayı yöneten şey**, aslında **matematik + algoritma** kombinasyonu.

---

## 🧩 **5. Çünkü Mülakatlarda, Yarışmalarda, Kariyerde Gerekli**

Birçok yazılım şirketi (Google, Microsoft, Trendyol, Getir...) teknik mülakatlarda algoritma sorar:

> “Bir dizide en büyük iki elemanı O(n) zamanda bul.”

Sadece kod bilmek yetmez; **algoritmik mantık** aranır.
Yani algoritma bilmek = **işe girme anahtarı 🔑**

---

## 🧭 **6. Çünkü Gerçek Hayatta da Kullanıyorsun**

Farkında olmadan zaten her gün algoritma kuruyorsun:

* Sabah hazırlanırken → sıralı algoritma
* Ders seçerken → karar algoritması
* Kahve yaparken bile → giriş, işlem, çıkış var 😄

Bilgisayarlar sadece bu düşünceyi *daha hızlı* ve *hatasız* yapıyor.

---

## 🧘‍♂️ **7. Çünkü Beynini Eğitiyor**

Algoritma, beynini **bir mühendis gibi düşünmeye** alıştırır.
Zamanla:

* Planlı çalışırsın,
* Hataları (bug’ları) daha kolay fark edersin,
* Karmaşık sistemleri daha kolay anlarsın.

> Bir anlamda “**beyin kaslarını çalıştırmak**” gibi. 🧠💪

---

## 💬 **8. Çünkü Gelecek Algoritmaların Üzerine Kurulu**

Yapay zeka, otonom araçlar, veri bilimi…
Hepsinin temeli algoritmadır.
Yani algoritmayı anlamadan bu alanlarda ustalaşmak,
**matematik bilmeden mühendis olmak** gibidir.

---

## 🧩 **Sonuç:**

> “Kod yazmak = konuşmak”
> “Algoritma = düşünmek”

İyi düşünen → iyi kod yazar.
İyi kod yazan → geleceği yazar. 🚀

---
