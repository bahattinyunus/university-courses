
# ⚙️ **İŞLETİM SİSTEMLERİ DERSİ - TAM REHBER**

---

## 🧠 1. İşletim Sistemi Nedir?

Bir bilgisayarın donanımıyla kullanıcı arasında duran, tüm kaynakları yöneten **ana yazılımdır**.
Kısaca:

> **İşletim sistemi = Bilgisayarın patronu.**

O, belleği kimin kullanacağına karar verir, hangi işlemcinin neyle uğraşacağını ayarlar, dosyaları düzenler ve kullanıcıya “kullanımı kolay” bir arayüz sunar.

💬 Basitçe:

* Donanım: “Nasıl yapacağım?” der.
* Kullanıcı: “Şunu yap!” der.
* İşletim Sistemi: “Tamam, ben hallederim.” der.

---

## 🧩 2. İşletim Sisteminin Görevleri

| Görev                             | Açıklama                                                                  |
| --------------------------------- | ------------------------------------------------------------------------- |
| **1️⃣ Bellek Yönetimi**           | RAM’in kim tarafından, ne kadar kullanılacağını belirler.                 |
| **2️⃣ İşlem Yönetimi**            | CPU üzerinde çalışan programların sırasını, süresini, önceliğini ayarlar. |
| **3️⃣ Dosya Yönetimi**            | Verileri diskte organize eder, kaydeder, siler, erişir.                   |
| **4️⃣ Girdi/Çıktı Yönetimi**      | Klavye, fare, yazıcı, monitör gibi cihazlarla etkileşimi sağlar.          |
| **5️⃣ Kullanıcı Arayüzü**         | Komut satırı (CLI) ya da grafik arayüz (GUI) sunar.                       |
| **6️⃣ Güvenlik ve Hata Yönetimi** | Yetkisiz erişimleri engeller, sistem çökmelerini yönetir.                 |

---

## 🖥️ 3. İşletim Sistemi Türleri

### 💡 1. **Tek Kullanıcılı - Tek Görevli**

Bir anda sadece bir program çalıştırır.
🧮 Örnek: Eski MS-DOS.

### 💡 2. **Tek Kullanıcılı - Çok Görevli**

Aynı anda birden fazla program çalışabilir.
💻 Örnek: Windows, macOS.

### 💡 3. **Çok Kullanıcılı Sistemler**

Birden fazla kullanıcı aynı anda sistemi kullanabilir.
🖧 Örnek: UNIX, Linux sunucuları.

### 💡 4. **Gerçek Zamanlı İşletim Sistemleri (RTOS)**

Zaman hassas uygulamalarda kullanılır (örnek: uçuş kontrol sistemleri, robotlar).
⚙️ Örnek: VxWorks, FreeRTOS.

### 💡 5. **Gömülü İşletim Sistemleri**

Mikrodenetleyicilerde, IoT cihazlarında kullanılır.
📱 Örnek: Android, RTOS türevleri.

---

## 🧬 4. İşlem (Process) ve Thread Kavramı

* **Process (İşlem):** Çalışan bir programın RAM üzerindeki hali.
* **Thread (İş Parçacığı):** Bir işlemin içindeki küçük, bağımsız yürütme birimleri.

🎯 Örnek:
Bir tarayıcı (process),
→ sekmeler (thread) gibidir.
Biri kilitlenirse, diğeri çalışmaya devam eder.

---

## ⚡ 5. CPU Zamanlama (Scheduling)

Birden fazla işlem varsa, CPU kime öncelik verir?
Bu işin kuralları vardır:

| Algoritma                         | Açıklama                               | Örnek                              |
| --------------------------------- | -------------------------------------- | ---------------------------------- |
| **FCFS (First Come First Serve)** | İlk gelen ilk işler.                   | Banka kuyruğu gibi.                |
| **SJF (Shortest Job First)**      | En kısa işi önce yap.                  | Hızlı işleri öne alır.             |
| **Round Robin**                   | Herkese belli süre (time slice) verir. | Adil paylaşım.                     |
| **Priority Scheduling**           | Önceliği yüksek olan önce.             | Gerçek zamanlı sistemlerde yaygın. |

---

## 💾 6. Bellek Yönetimi Teknikleri

| Yöntem                            | Açıklama                                          |
| --------------------------------- | ------------------------------------------------- |
| **Paging (Sayfalama)**            | Belleği sayfalara böler, verimli kullanım sağlar. |
| **Segmentation (Bölütleme)**      | Belleği mantıksal bölümlere ayırır.               |
| **Virtual Memory (Sanal Bellek)** | RAM yetersizse diski geçici RAM gibi kullanır.    |

💡 RAM dolunca sistem “swap” yapar — yavaşlar ama çökmez.

---

## 🗂️ 7. Dosya Sistemi

Dosyaların nasıl saklandığı, isimlendirildiği ve erişildiğini belirler.

| Dosya Sistemi | Özellik                         | Kullanıldığı Yer |
| ------------- | ------------------------------- | ---------------- |
| **FAT32**     | Basit, eski ama evrensel.       | USB bellekler    |
| **NTFS**      | Güvenlik + büyük dosya desteği. | Windows          |
| **ext4**      | Hızlı, sağlam.                  | Linux            |
| **APFS**      | Şifreleme + performans.         | macOS            |

---

## 🔒 8. Güvenlik & Erişim Kontrolü

* **Kullanıcı hesapları** oluşturulur (admin, guest vs).
* **Dosya izinleri** (okuma, yazma, çalıştırma) belirlenir.
* **Firewall** ve **şifreleme** teknikleri kullanılır.

🎭 Yani işletim sistemi, “herkes her şeyi göremez” ilkesine göre çalışır.

---

## 🌐 9. Modern İşletim Sistemleri

| İşletim Sistemi                    | Kullanım Alanı                         |
| ---------------------------------- | -------------------------------------- |
| **Windows**                        | Genel kullanıcı, oyun, ofis işleri     |
| **Linux (Ubuntu, Debian, Fedora)** | Sunucular, yazılım geliştirme          |
| **macOS**                          | Yaratıcı işler, tasarım, stabil sistem |
| **Android**                        | Mobil cihazlar                         |
| **iOS**                            | Apple ekosistemi                       |
| **FreeBSD / UNIX**                 | Sunucular, güvenlik sistemleri         |

---

## 🚀 10. İşletim Sistemlerinin Geleceği

* **Bulut tabanlı OS’ler:** (ChromeOS gibi) her şey online.
* **Yapay zekâ destekli kaynak yönetimi:** Sistem, sen fark etmeden optimizasyon yapacak.
* **Quantum işletim sistemleri:** Kuantum işlemcilerle yeni paradigma.
* **Tam entegrasyon:** Mobil + masaüstü + IoT birleşimi tek platformda.

💫 Geleceğin işletim sistemi “nerede çalıştığın değil, nasıl bağlandığınla” ilgilenecek.

---

## 💡 11. Bu Dersi Öğrenmenin Sana Katkısı

* Bilgisayarın **iç mekanizmasını** anlarsın.
* Yazılım geliştirirken “donanım neden böyle davranıyor?” sorusuna cevap bulursun.
* **Kernel, thread, scheduling** gibi sistemsel kavramlar sana artık sıradan gelir.
* Sistem tasarlarken **verimlilik + güvenlik + kontrol** senin elinde olur.

🎯 Kısaca:

> “İşletim sistemlerini anlayan yazılımcı, sadece kod yazmaz — sistemi yönetir.”

---

## 💬 Son Söz

İşletim sistemleri, bilgisayar biliminin **görünmez kahramanıdır**.
Eğer onları anlarsan, artık sadece kullanıcı değil, **bilgisayarın diliyle konuşan bir mühendis** olursun. 💻✨


---

# 🧩 **İŞLETİM SİSTEMİ ÇEKİRDEĞİ (KERNEL) & PROCESS MANAGEMENT**

---

## ⚙️ 1. Kernel Nedir?

Kernel, işletim sisteminin **beyni**, **çekirdeği**, **temel parçasıdır**.
Bilgisayar açıldığında ilk çalışan kısımdır ve sistem kapanana kadar aktif kalır.

🎯 Görevi:
Donanım kaynaklarını yönetmek, uygulamalara servis sunmak.

🧠 Kısaca:

> Kernel, “arka plandaki sihirbaz”tır — kullanıcı fark etmeden her şeyi yönetir.

---

## 🧱 2. Kernel Türleri

| Kernel Türü           | Açıklama                                                                                           | Örnek                 |
| --------------------- | -------------------------------------------------------------------------------------------------- | --------------------- |
| **Monolithic Kernel** | Tüm modüller tek bir yapıdadır, hızlıdır ama hata riski yüksek.                                    | Linux, Unix           |
| **Microkernel**       | Minimum fonksiyon çekirdekte, geri kalanlar modül olarak eklenir. Daha güvenlidir ama biraz yavaş. | Minix, QNX            |
| **Hybrid Kernel**     | İki yapının dengeli karışımıdır.                                                                   | Windows NT, macOS XNU |
| **Exokernel**         | Donanımı doğrudan uygulamalara açar.                                                               | MIT deneysel OS’ler   |

💡 **Monolithic = kaslı ama riskli**,
**Microkernel = zeki ama sabırlı.**

---

## 🧠 3. Kernel’in Ana Görevleri

| Görev                          | Açıklama                                                 |
| ------------------------------ | -------------------------------------------------------- |
| **1️⃣ Process Management**     | İşlemlerin oluşturulması, yürütülmesi, bitirilmesi.      |
| **2️⃣ Memory Management**      | RAM’in paylaşımı, swap işlemleri.                        |
| **3️⃣ Device Management**      | G/Ç cihazlarının sürücülerle konuşması.                  |
| **4️⃣ File System Management** | Dosyaların fiziksel olarak nasıl saklanacağını belirler. |
| **5️⃣ System Calls**           | Kullanıcı programlarıyla kernel arasındaki arabirimdir.  |

---

## 💬 4. System Call Nedir?

Uygulama, donanıma doğrudan erişemez.
Kernel’e “bir şey yap” demesi gerekir.
İşte bu iletişim kanalına **system call** denir.

📞 Örnek system call’lar:

* `read()` → Dosyadan oku
* `write()` → Dosyaya yaz
* `fork()` → Yeni işlem oluştur
* `exec()` → Yeni program çalıştır
* `exit()` → İşlemi sonlandır

💬 **Uygulama → System Call → Kernel → Donanım**

---

## 🔄 5. Process Management (İşlem Yönetimi)

Her çalışan program bir **process (işlem)** olarak görülür.
Kernel, tüm işlemlerin:

* **Yaşam döngüsünü**,
* **Kaynak kullanımını**,
* **Zamanlamasını** yönetir.

---

### 🔹 Process’in Yaşam Döngüsü

```
NEW → READY → RUNNING → WAITING → TERMINATED
```

| Durum          | Açıklama                 |
| -------------- | ------------------------ |
| **NEW**        | Yeni oluşturulmuş işlem. |
| **READY**      | CPU zamanı bekliyor.     |
| **RUNNING**    | CPU’da çalışıyor.        |
| **WAITING**    | G/Ç işlemi bekliyor.     |
| **TERMINATED** | İş tamamlandı.           |

💡 Bir işlem “bekliyorken” bile RAM’de yer kaplar. Kernel bu yüzden optimize eder.

---

### 🔹 Process Oluşturma (fork)

UNIX tabanlı sistemlerde, yeni bir işlem oluşturmak için **`fork()`** çağrısı yapılır.
Bu, mevcut işlemin bir **kopyasını** oluşturur.
Ardından `exec()` ile başka bir program yüklenebilir.

📚 Örnek:

```c
pid_t pid = fork();
if (pid == 0)
    exec("ls"); // Çocuk işlem "ls" komutunu çalıştırır
else
    wait();     // Ana işlem bekler
```

Bu yapı, modern işletim sistemlerinin çoklu görev mimarisinin temelidir.

---

### 🔹 Process’ler Arası İletişim (IPC)

İşlemler bazen birbirleriyle konuşmak ister.
Kernel buna **IPC (Inter Process Communication)** mekanizmalarıyla izin verir:

| Yöntem                   | Açıklama                                     |
| ------------------------ | -------------------------------------------- |
| **Pipes (Boru Hatları)** | Bir işlemin çıktısı, diğerinin girdisi olur. |
| **Message Queue**        | İşlemler mesaj gönderir/alır.                |
| **Shared Memory**        | Aynı bellek alanı paylaşılır.                |
| **Semaphore & Mutex**    | Eşzamanlı erişim kontrolü.                   |

💬 Basit örnek:
Bir program veri üretir (producer), diğeri tüketir (consumer). Kernel ortada trafik polisi gibi düzenler.

---

## ⏱️ 6. CPU Scheduling (İşlem Zamanlama)

Kernel’in en önemli işi:

> “Hangi işlem CPU’yu şimdi kullanacak?”

Bir sistemde yüzlerce process olabilir ama CPU aynı anda sadece **birini** çalıştırabilir.
Kernel, bu sıralamayı zamanlayıcı algoritmalarla yapar.

### ⚡ Kısa Hatırlatma:

* **Round Robin:** Herkese sırayla kısa süre verir.
* **Priority Scheduling:** Önceliği yüksek olan öne geçer.
* **Multilevel Queue:** İşlemleri kategorilere ayırır (etkileşimli, sistem, batch).

🧩 Hedef: Maksimum CPU kullanımı + minimum bekleme süresi.

---

## 🧠 7. Thread’ler (İş Parçacıkları)

Bir process içinde **birden fazla işin aynı anda yapılmasını** sağlar.
Aynı process’in thread’leri:

* Aynı belleği paylaşır,
* Fakat bağımsız yürürler.

🎯 Örnek:
Bir tarayıcıda:

* Sekme 1 → Video oynatıyor,
* Sekme 2 → Chat çalıştırıyor,
* Sekme 3 → Dosya indiriyor.

Hepsi aynı programın thread’leri.

---

## 🧩 8. Kernel Mode vs User Mode

İşletim sistemleri güvenlik için iki modda çalışır:

| Mod             | Açıklama                                               | Erişim    |
| --------------- | ------------------------------------------------------ | --------- |
| **User Mode**   | Uygulama kodu burada çalışır. Kernel’e sınırlı erişim. | Sınırlı   |
| **Kernel Mode** | Donanım ve sistem çağrıları buradan yapılır.           | Tam yetki |

💡 Eğer bir program doğrudan kernel moduna geçmeye kalkarsa?
➡️ Sistem çöker veya “Blue Screen of Death” gelir 😬

---

## 🔒 9. Deadlock (Kilitlenme)

İki veya daha fazla işlem, birbirinin tuttuğu kaynağı bekliyorsa, sistem **kilitlenir.**

🎭 Örnek:

* Process A yazıcıyı tuttu, disk bekliyor.
* Process B diski tuttu, yazıcı bekliyor.
  İkisi de bekliyor = sonsuz kilitlenme.

💡 Kernel, bu durumu önlemek için **deadlock prevention** veya **detection** mekanizmaları kullanır.

---

## 🚀 10. Kernel’in Modern Gelişim Yönleri

* **Modüler kernel yapısı (Linux modülleri gibi):** Sürücüler “plug-in” gibi takılıp çıkarılabiliyor.
* **Realtime destek:** Gecikmesiz işlem garantisi.
* **Security Hardening:** Kernel exploit’lerine karşı koruma.
* **Energy-aware scheduling:** Mobil cihazlarda enerji tasarruflu işlem planlama.

---

## 🧭 11. Neden Kernel ve Process Management Öğrenmelisin?

* Donanımın nasıl “yönetildiğini” anlarsın.
* Yazılım geliştirirken sistem kaynaklarını optimize edebilirsin.
* Multi-threading, concurrency, async işlemler artık gözünü korkutmaz.
* Sistem çökmelerinde hata loglarını **bir hacker gibi** analiz edebilirsin.

🎯 Kısaca:

> “Kernel’i anlayan mühendis, bilgisayarı sadece kullanmaz, **komuta eder.**”

---


# 💾 **BELLEK YÖNETİMİ (MEMORY MANAGEMENT) - DERİN ANLATIM**

---

## 🧠 1. Bellek Yönetimi Nedir?

Bellek yönetimi, **RAM’in etkin ve adil kullanımını** sağlayan işletim sistemi mekanizmasıdır.

Bir bilgisayarda aynı anda onlarca işlem çalışır.
Herkes “bana biraz RAM ver” der.
İşletim sistemi de adeta bir **RAM bankeri** gibi, kimin ne kadar alacağını hesaplar.

💬 Kısaca:

> “Bellek yönetimi, bilgisayarın trafik polisi gibidir — kim nerede, ne kadar duracak, o karar verir.”

---

## ⚙️ 2. Bellek Türleri

| Tür                               | Açıklama                                           | Örnek            |
| --------------------------------- | -------------------------------------------------- | ---------------- |
| **ROM (Read Only Memory)**        | Kalıcı bellektir, sistem açılışında BIOS burada.   | BIOS/UEFI        |
| **RAM (Random Access Memory)**    | Geçici, hızlı bellektir. İşlemler burada yürür.    | DDR4, DDR5       |
| **Cache**                         | CPU’ya en yakın, çok hızlı bellek.                 | L1, L2, L3 Cache |
| **Virtual Memory (Sanal Bellek)** | RAM yetmezse diskin bir kısmı RAM gibi kullanılır. | Swap / Pagefile  |

---

## 🧩 3. Bellek Yönetiminin Görevleri

| Görev                                  | Açıklama                                         |
| -------------------------------------- | ------------------------------------------------ |
| **1️⃣ Tahsis (Allocation)**            | Her işleme belirli miktarda bellek ayırır.       |
| **2️⃣ Koruma (Protection)**            | İşlemler birbirinin alanına karışamaz.           |
| **3️⃣ Paylaşım (Sharing)**             | Ortak kodlar (DLL, kütüphaneler) paylaşılabilir. |
| **4️⃣ Sanallaştırma (Virtualization)** | Her işlem kendine ait sanal adres alanı sanır.   |
| **5️⃣ Geri Alma (Deallocation)**       | İşlem bitince bellek geri alınır.                |

---

## 🧮 4. Bellek Adresleme Kavramı

İşlemciler iki tür adres kullanır:

| Tür                                   | Açıklama                         |
| ------------------------------------- | -------------------------------- |
| **Logical Address (Mantıksal Adres)** | Programın gördüğü adres. (Sanal) |
| **Physical Address (Fiziksel Adres)** | Gerçekte RAM’deki konum.         |

🔁 **Memory Management Unit (MMU)**, bu iki adres arasında çeviri yapar.

📦 Yani uygulama sanır ki adres `0x0000A3F2`,
ama kernel der ki: “Aslında o 0xFFF23B10’da.” 😎

---

## 🧱 5. Bellek Dağıtım Teknikleri

### 🟩 1. **Contiguous Allocation (Bitisik Dağıtım)**

Bellek, ardışık bloklar halinde ayrılır.

🧩 Dezavantaj:

* **Fragmentation (Parçalanma)** oluşur.

  * *Internal fragmentation:* Tahsis edilen alanın bir kısmı boşa gider.
  * *External fragmentation:* Kullanılabilir alanlar dağılır, birleşemez.

---

### 🟨 2. **Paging (Sayfalama)**

Modern sistemlerin favorisi ❤️
RAM, **sabit boyutlu bloklara** bölünür:

* RAM → **Frame’ler**
* Process → **Page’ler**

🧠 Page Table (Sayfa Tablosu) ile sanal adresler fiziksel adreslere çevrilir.

📊 Örnek:

| Page | Frame |
| ---- | ----- |
| 0    | 5     |
| 1    | 9     |
| 2    | 2     |

💬 Yani process sayfa 1’i istediğinde, aslında RAM’in 9. bloğuna gider.
Fragmentation azalır, bellek kullanımı artar.

---

### 🟦 3. **Segmentation (Bölütleme)**

Program, **mantıksal parçalara** (segmentlere) bölünür:

* Kod (Code Segment)
* Veri (Data Segment)
* Stack (Yığın Segmenti)

📦 Her segment farklı boyuttadır, sayfalamadan farkı budur.
Ama birleşirse: **Segmented Paging** sistemi oluşur → Windows & Linux bunu kullanır.

---

## 🌌 6. Virtual Memory (Sanal Bellek)

Fiziksel RAM yetmezse, işletim sistemi diskin bir kısmını **RAM gibi davranan alan** haline getirir.
Bu alana **swap alanı** veya **page file** denir.

📉 Dezavantaj: Disk RAM’den çok daha yavaştır.
Ama sistem çökmez — çalışmaya devam eder.

🧠 Yani RAM dolsa bile “Ben çökmem, yavaşlarım” stratejisi 😅

---

## 🔁 7. Swapping (Bellek Takası)

Sistem aktif işlem sayısını azaltmak için bazı işlemleri RAM’den diske taşır.
Bu işlem **swap-in** ve **swap-out** döngüsüyle gerçekleşir.

🌀 RAM <-> Disk arasında sürekli veri taşınır.
Fazla olursa “thrashing” denilen felaket ortaya çıkar.

💀 **Thrashing =** Sürekli swap yapan, çalışmaya fırsat bulamayan sistem.

---

## ⚡ 8. Cache Bellek

Cache, CPU’nun “mini RAM”idir.
İşletim sistemi değil, işlemci kontrol eder ama bellek yönetimiyle entegredir.

| Seviye       | Özellik                                           |
| ------------ | ------------------------------------------------- |
| **L1 Cache** | En hızlı, en küçük. CPU çekirdeğine en yakın.     |
| **L2 Cache** | Daha büyük, biraz yavaş.                          |
| **L3 Cache** | Çok büyük, tüm çekirdekler tarafından paylaşılır. |

💡 Amaç: CPU, RAM’e gitmeden önce veriyi cache’te bulsun.
Eğer bulursa: **Cache Hit**, bulamazsa: **Cache Miss.**

---

## 🧩 9. Page Replacement Algoritmaları

RAM dolduğunda kernel karar verir: “Hangi sayfa dışarı atılsın?”
İşte burada strateji devreye girer.

| Algoritma                     | Mantık                               | Açıklama             |
| ----------------------------- | ------------------------------------ | -------------------- |
| **FIFO (First In First Out)** | İlk gelen sayfa, ilk çıkar.          | Basit ama verimsiz.  |
| **LRU (Least Recently Used)** | En uzun süredir kullanılmayan çıkar. | Gerçekçi ve yaygın.  |
| **Optimal**                   | Gelecekte en geç kullanılacak çıkar. | Teorik mükemmellik.  |
| **Clock (Second Chance)**     | FIFO’nun akıllı versiyonu.           | Linux’ta kullanılır. |

💬 Gerçek sistemler genelde **LRU + Clock hybrid** kullanır.

---

## 🔒 10. Bellek Koruma Mekanizmaları

Kernel, her işleme “adres alanı sınırı” verir.
Bir işlem başka bir işlem alanına girerse? → **Segmentation Fault 💥**

🧱 Koruma yöntemleri:

* **Base Register:** Başlangıç adresi.
* **Limit Register:** İzin verilen uzunluk.
* **Access Control Bits:** Okuma / Yazma / Çalıştırma izinleri.

💬 Bu yüzden yanlış pointer kullanan C programları “Segmentation Fault” verir.

---

## 🧠 11. Bellek Paylaşımı (Shared Memory)

Bazı işlemler aynı veriyi kullanmak ister.
İşletim sistemi, belirli RAM alanlarını “ortak kullanım”a açar.

Örnek:

* Web tarayıcı sekmeleri aynı motoru (render engine) paylaşır.
* DLL dosyaları her program için kopyalanmaz, ortak alan kullanır.

💡 Bu yöntem RAM tasarrufu sağlar ve performansı artırır.

---

## ⚡ 12. Modern Bellek Yönetim Teknikleri

* **NUMA (Non-Uniform Memory Access):** Çok çekirdekli sistemlerde her çekirdeğin kendi RAM bölgesi vardır.
* **Memory Compression:** Sık kullanılmayan veriler sıkıştırılarak RAM’de daha çok yer açılır.
* **Demand Paging:** Sayfa sadece gerçekten ihtiyaç duyulduğunda yüklenir.
* **Copy-on-Write (COW):** Process kopyalanırken sayfalar paylaşılır, biri değiştirirse o zaman ayrılır.

---

## 🌟 13. Neden Öğrenmelisin?

* Yazdığın yazılımlar RAM dostu olur 💚
* Performans optimizasyonlarını profesyonel düzeyde anlarsın.
* “Out of Memory” hatalarının arkasındaki sebebi bilir, çözersin.
* Donanım-yazılım arası köprüyü kurarsın.

🎯 Kısaca:

> “Bellek yönetimini anlayan yazılımcı, sadece kod değil — **bilinçli sistem** yazar.”

---

## 💬 Son Söz

Bellek yönetimi, işletim sisteminin **en karmaşık ama en zekice** parçasıdır.
RAM dolduğunda çökmeden yola devam edebilmek, işte o sanat! 🎨
Ve sen artık bu sanatın perde arkasını biliyorsun.

---

