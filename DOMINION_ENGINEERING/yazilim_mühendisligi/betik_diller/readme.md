# Betik Diller (Scripting Languages) Ders Notları

## 1. Betik Dili Nedir?

Betik dili, genellikle **uygulamaları kontrol etmek, otomasyon yapmak veya hızlı prototip geliştirmek** için kullanılan programlama dilleridir.

* Çoğunlukla **yorumlayıcı (interpreter)** ile çalışır, yani kod yazıldıktan sonra derlenmeden çalıştırılır.
* Hedefi **hızlı geliştirme ve esneklik** sağlamaktır, performans kritikse genellikle ana dilde (C/C++, Java) yazılır.

### Öne Çıkan Özellikler:

* **Yorumlanır:** Kod satır satır çalıştırılır.
* **Dinamik tip:** Değişken tipleri runtime’da belirlenir.
* **Hızlı geliştirme:** Küçük projelerde derleme gerektirmez.
* **Platform bağımsız:** Genellikle işletim sisteminden bağımsız çalışabilir.

---

## 2. Betik Dillerin Kullanım Alanları

* Web geliştirme (**JavaScript, PHP, Python**)
* Sistem yönetimi ve otomasyon (**Bash, PowerShell, Python**)
* Veri analizi ve yapay zeka (**Python, R**)
* Oyun geliştirme ve modifikasyon (**Lua, Python**)
* Test otomasyonu ve CI/CD (**Python, Groovy**)

---

## 3. Popüler Betik Dilleri

| Dil        | Kullanım Alanı                          | Avantajları                                 |
| ---------- | --------------------------------------- | ------------------------------------------- |
| Python     | Web, veri bilimi, otomasyon, yapay zeka | Kolay sözdizimi, çok kütüphane desteği      |
| JavaScript | Web, frontend, backend                  | Tarayıcı desteği, popüler                   |
| PHP        | Web geliştirme                          | Sunucu tarafı script, geniş hosting desteği |
| Bash       | Linux/Unix sistem yönetimi              | Sistem yönetimi ve otomasyon                |
| PowerShell | Windows sistem yönetimi                 | Windows otomasyon ve script yönetimi        |
| Lua        | Oyun geliştirme, gömülü sistemler       | Hafif, gömülü sistemler için uygun          |

---

## 4. Betik Dillerin Avantajları

* Hızlı prototip geliştirme
* Küçük ve orta ölçekli projelerde daha az kod
* Platform bağımsızlık
* Otomasyon ve sistem yönetimi kolaylığı

### Dezavantajları

* Performans genellikle derlenen dillere göre düşük
* Büyük projelerde yönetimi zorlaşabilir
* Tip hataları runtime’da ortaya çıkabilir

---

## 5. Betik Dili vs Derlenen Dil

| Özellik              | Betik Dili      | Derlenen Dil                     |
| -------------------- | --------------- | -------------------------------- |
| Çalıştırma şekli     | Yorumlayıcı     | Derleyici                        |
| Tip kontrolü         | Dinamik         | Statik                           |
| Geliştirme hızı      | Hızlı           | Daha yavaş                       |
| Performans           | Orta/düşük      | Yüksek                           |
| Platform bağımsızlık | Genellikle evet | İşletim sistemine bağlı olabilir |

---

## 6. Örnek Betik Dilleri Kodları

### Python

```python
# Basit bir toplama işlemi
a = 5
b = 10
print("Toplam:", a + b)
```

### JavaScript

```javascript
// Basit bir toplama işlemi
let a = 5;
let b = 10;
console.log("Toplam: " + (a + b));
```

### Bash

```bash
#!/bin/bash
# Basit bir toplama işlemi
a=5
b=10
echo "Toplam: $((a+b))"
```

---

## 7. Betik Dili Öğrenirken Dikkat Edilecekler

* Değişken tiplerini ve scope’u iyi öğren
* Dosya okuma/yazma ve sistem komutlarını öğren
* Hata ayıklamayı ve logging’i kullan
* Modülleri ve kütüphaneleri keşfet



## 1. Hızlı Prototip ve Çözüm Üretimi

* Betik dilleri, Python veya JavaScript gibi dillerle **fikirden koda hızla geçebilirsin**.
* Örneğin bir fikir geldi: “Sitedeki tüm görselleri indirip isimlerini değiştireyim.” Python ile 10 satırda çözersin, C++ ile saatler sürer.

---

## 2. Otomasyon ve Verimlilik

* Günlük tekrarlayan işler mi var? Dosya taşıma, rapor çıkarma, web site veri çekme…
* Betik dilleri ile **tek tuşla halledersin**.
* Yani hayatını kolaylaştırır ve seni zaman canavarı olmaktan kurtarır.

---

## 3. Veri ve Web Dünyasında Vazgeçilmez

* Veri bilimi, AI, makine öğrenimi, web geliştirme… hepsi betik dillerini kullanıyor.
* Python öğrenmek = yapay zekaya bir adım atmak.
* JavaScript = webin dili. Bunu bilmeden modern yazılım dünyasında var olamazsın.

---

## 4. Platform Bağımsızlık ve Esneklik

* Windows, Linux, macOS fark etmez.
* Bir script yazarsın, çoğu yerde çalıştırabilirsin.
* Yani bir dili öğrenmek = kodlarını bir çok yerde kullanabilmek.

---

## 5. Kariyer ve İş Fırsatları

* Yazılımcılar arasında **en çok talep edilen becerilerden biri** betik dili bilmek.
* DevOps, test otomasyonu, web geliştirme, veri analizi… Hepsi için lazım.
* Bunu bilmek seni rakiplerinden öne geçirir.

---

## 6. Güçlü Ama Öğrenmesi Kolay

* Python, Bash, JavaScript gibi dillerin **öğrenmesi çok kolay**.
* Hızlı başarı hissi verir → motivasyon yükselir → diğer zor konulara geçmek kolaylaşır.

---

Özetle: Betik dilleri **zaman kazandırır, hayatı kolaylaştırır ve kariyer yolunu açar**. Hatta şöyle düşünebilirsin: Bir yazılımcı için betik dili bilmemek, kılıç kullanmayı bilmeyen bir şövalye gibi.



# Yazılım Dilleri Sınıflandırması

## 1. Derlenen ve Yorumlanan Diller

### a) Derlenen (Compiled) Diller

* **Tanım:** Kod, çalıştırılmadan önce derleyici (compiler) tarafından makine diline çevrilir.
* **Avantaj:** Performans çok yüksek, hata ayıklama derleme aşamasında yapılabilir.
* **Dezavantaj:** Kod değiştiğinde tekrar derlenmesi gerekir, geliştirme süresi daha uzun.
* **Örnekler:** C, C++, Go, Rust

### b) Yorumlanan (Interpreted) Diller

* **Tanım:** Kod satır satır yorumlayıcı (interpreter) tarafından çalıştırılır.
* **Avantaj:** Hızlı geliştirme, platform bağımsız, esnek.
* **Dezavantaj:** Performans düşük, bazı hatalar runtime’da ortaya çıkar.
* **Örnekler:** Python, Ruby, JavaScript, PHP, Bash

> Not: Python gibi bazı diller **yarı derlenmiş (bytecode)** çalışır ama genellikle yorumlanan dil olarak sınıflandırılır.

---

## 2. Amaçlarına Göre Yazılım Dilleri

| Tür                    | Açıklama                              | Örnekler                 |
| ---------------------- | ------------------------------------- | ------------------------ |
| Sistem Dilleri         | İşletim sistemi, donanım kontrolü     | C, C++, Rust             |
| Uygulama Dilleri       | Masaüstü, mobil veya web uygulamaları | Java, C#, Swift, Kotlin  |
| Betik Dilleri          | Otomasyon, web, hızlı prototip        | Python, Bash, JavaScript |
| Sorgulama Dilleri      | Veritabanı sorguları                  | SQL, GraphQL             |
| Fonksiyonel Diller     | Fonksiyon mantığıyla programlama      | Haskell, Elixir, Lisp    |
| Nesne Yönelimli Diller | Nesneler üzerinden programlama        | Java, Python, C++        |
| Mantıksal Diller       | Kurallara dayalı problem çözümü       | Prolog                   |

---

## 3. Düşük ve Yüksek Seviyeli Diller

### a) Düşük Seviyeli Diller

* Makineye yakın, donanım üzerinde daha fazla kontrol sağlar.
* **Avantaj:** Performans ve donanım kontrolü yüksek.
* **Dezavantaj:** Öğrenmesi zor, yazması uzun.
* **Örnek:** Assembly, C

### b) Yüksek Seviyeli Diller

* İnsan diline yakın, okunabilirlik yüksek.
* **Avantaj:** Daha hızlı geliştirme, öğrenmesi kolay.
* **Dezavantaj:** Performans düşük, donanımı doğrudan kontrol edemez.
* **Örnek:** Python, Java, Ruby

---

## 4. Programlama Paradigmalarına Göre

| Paradigma            | Açıklama                                      | Örnekler          |
| -------------------- | --------------------------------------------- | ----------------- |
| Nesne Yönelimli      | Nesneler ve sınıflar üzerinden programlama    | Java, Python, C++ |
| Fonksiyonel          | Fonksiyonları temel alır, yan etkiler minimal | Haskell, Lisp     |
| Prosedürel / Yapısal | Adım adım komut çalıştırma                    | C, Pascal         |
| Mantıksal            | Kurallar ve mantık üzerinden problem çözme    | Prolog            |
| Betik / Scripting    | Otomasyon ve hızlı geliştirme                 | Python, Bash      |

---

### Özet

* **İki ana kategori:** Derlenen ve yorumlanan diller
* **Paradigmalar ve kullanım alanları** ile çeşitlenir.
* Her dilin **kendine uygun kullanım alanı ve avantajı** vardır.



## 1. Betik Dillerin Temel Kavramları

* **Yorumlayıcı (Interpreter):** Kodun satır satır çalıştırılmasını sağlar.
* **Dinamik Tip:** Değişken tipleri runtime’da belirlenir.
* **Platform Bağımsızlık:** Kod çoğu işletim sisteminde çalışabilir.
* **Modülerlik:** Fonksiyonlar, modüller ve kütüphaneler sayesinde tekrar kullanılabilir.

> Yani özetle: Betik dili hızlı, esnek ve insan dostudur, ama performans için optimize edilmez.

---

## 2. Betik Dillerin Kullanım Amaçları

* **Otomasyon:** Dosya taşıma, rapor çıkarma, test otomasyonu.
* **Web Geliştirme:** Frontend ve backend geliştirme.
* **Veri İşleme ve Analiz:** Pandas, NumPy, veri görselleştirme.
* **Sistem Yönetimi:** Linux, Windows yönetimi, cron ve görev planlama.
* **Oyun ve Script Modları:** Oyun içi kontrol ve modifikasyon.

> Buradaki mantık: Betik dili **küçük ama çok yönlü işler için** ideal.

---

## 3. Betik Dili Özellikleri – Bilmen Gerekenler

* **Değişken Tanımlama ve Dinamik Tip Kullanımı**
* **Koşul ve Döngü Yapıları**
* **Fonksiyonlar ve Parametre Kullanımı**
* **Modüller ve Kütüphaneler**
* **Hata Yakalama (Try/Except)**
* **Dosya İşlemleri ve Sistem Komutları**

> Yani sınavda çıkarsa “bir betik dilinde dosya nasıl okunur?” veya “try/except ne işe yarar?” gibi sorular rahat gelir.

---

## 4. Betik Dilleri ile İlgili İleri Konular

* **Otomasyon Scriptleri Yazabilme:** Cron job, Windows Task Scheduler
* **API Kullanımı:** Web servislerinden veri çekme
* **Veri Analizi:** CSV, JSON, Excel dosyalarını işleme
* **Test ve CI/CD:** Jenkins veya GitHub Actions ile otomasyon testleri
* **Web Scraping:** Python’da BeautifulSoup veya Selenium ile veri toplama

> İşin pratiği burada başlıyor: Betik dili sadece kod yazmak değil, iş ve veri süreçlerini kolaylaştırmak için kullanılır.

---

## 5. Betik Dilleri ile İlgili Sınav ve Teorik Bilgiler

* Betik dilleri **yorumlanan diller**dir.
* **Performansı derlenen dillere göre düşüktür.**
* **Platform bağımsızdır.**
* **Dinamik tip kullanır.**
* Küçük ve orta ölçekli projeler için uygundur.
* Örnekleri: Python, Bash, JavaScript, PHP, Lua, PowerShell

> Bu kısım genelde sınavlarda soru olur, mantığı kafanda net tut.

---

## 6. Pratik Tavsiyeler

* Python veya Bash ile **küçük otomasyonlar yap**: dosya taşımak, rapor yazdırmak, web verisi çekmek.
* JavaScript ile **basit web scriptleri yaz**: butona basınca değişen mesajlar, basit hesap makineleri.
* **Modülleri ve kütüphaneleri dene:** math, os, sys, requests…
* **Hata yakalamayı öğren:** try/except ile runtime hatalarını yönetebil.

---
