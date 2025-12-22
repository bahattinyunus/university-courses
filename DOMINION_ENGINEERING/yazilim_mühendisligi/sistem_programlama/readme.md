# 🧠 Sistem Programlama Ders Notları

> Yazılım Mühendisliği Bölümü  
> Düşük seviyeli sistem yazılımlarının temelleri  
> İşletim sistemiyle doğrudan konuşan programlar geliştirme dersi 👾

---

## 📘 1. Giriş: Sistem Programlama Nedir?

**Sistem Programlama**, bilgisayar donanımıyla **işletim sistemi üzerinden** doğrudan etkileşim kuran yazılımların geliştirilmesini inceleyen derstir.

Uygulama programlarından farkı:
- Donanım ve işletim sistemi arasındaki köprüyü kurar.
- Sistem kaynaklarını (bellek, dosyalar, CPU, I/O) doğrudan kontrol eder.

### 💡 Örnek Sistem Yazılımları
- Derleyiciler (Compilers)
- İşletim sistemleri (Operating Systems)
- Sürücüler (Drivers)
- Linker / Loader’lar
- Dosya sistemleri
- Sistem araçları (Terminal, Shell)

---

## ⚙️ 2. Sistem Yazılımı Katmanları

| Katman | Açıklama | Örnek |
|--------|----------|-------|
| **Uygulama Yazılımları** | Kullanıcıyla doğrudan etkileşen yazılımlar | Word, Chrome |
| **Sistem Yazılımları** | Uygulama ile donanım arasındaki arayüz | İşletim sistemi, derleyici |
| **Donanım (Hardware)** | Fiziksel bileşenler | CPU, RAM, Disk |

🧩 Sistem programlama, bu iki katman arasındaki “gizli dünya”dır.

---

## 🧰 3. Derleyici, Assembler, Linker, Loader

Bu bileşenler sistem yazılımlarının kalbidir.

### 🔹 Derleyici (Compiler)
Kaynak kodu yüksek seviyeli dilden (C, C++) makine diline dönüştürür.

### 🔹 Assembler
Assembly dilini makine koduna çevirir (örneğin `.asm` → `.obj`).

### 🔹 Linker
Farklı dosyaları birleştirip çalışabilir dosya (`.exe`, `.out`) oluşturur.

### 🔹 Loader
Oluşturulan programı belleğe yükler ve çalıştırır.

📚 **Derleme Akışı:**
    
---

## 🧩 4. Sistem Çağrıları (System Calls)

Sistem çağrıları, kullanıcı programlarının işletim sistemi çekirdeği (kernel) ile iletişim kurmasını sağlar.  
Yani sistem kaynaklarına erişmek için kullanılan fonksiyonlardır.

### 💬 Örnek Tanım
> “Kardeşim, şu dosyayı açabilir miyim?” — Programın işletim sistemine yaptığı istektir.

### ⚙️ Yaygın Sistem Çağrıları

| Sistem Çağrısı | Görevi |
|----------------|--------|
| `open()` | Dosya açar |
| `read()` | Dosyadan veri okur |
| `write()` | Dosyaya veri yazar |
| `fork()` | Yeni bir process oluşturur |
| `exec()` | Yeni bir program çalıştırır |
| `exit()` | İşlemi sonlandırır |
| `wait()` | Alt işlemin bitmesini bekler |

### 🧪 Örnek Kod (C)

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Merhaba, dünya!\n");
    fork();  // Yeni bir process oluşturur
    printf("Ben bir process'im!\n");
    return 0;
}
Merhaba, dünya!
Ben bir process'im!
Ben bir process'im!
fork() çağrısından sonra iki ayrı işlem (parent ve child) oluşur 👨‍👦

⚙️ 5. İşlem Yönetimi (Process Management)

İşletim sistemi aynı anda birden fazla program çalıştırabilir.
Her çalışan program bir işlem (process) olarak adlandırılır.

🔄 Process’in Yaşam Döngüsü

New (Yeni) → İşlem oluşturuluyor

Ready (Hazır) → CPU bekliyor

Running (Çalışıyor) → CPU işlemi yürütüyor

Waiting (Bekliyor) → G/Ç işlemi bekliyor

Terminated (Sonlandı) → İşlem tamamlandı

🧮 Zamanlayıcı (Scheduler)

CPU’nun hangi işlemi çalıştıracağına karar verir.

Kullanılan algoritmalar:

FCFS (First Come First Serve)

SJF (Shortest Job First)

Round Robin

Priority Scheduling

🧠 6. Bellek Yönetimi (Memory Management)

Birden fazla program aynı anda çalışırken bellek (RAM) yönetimi hayati önem taşır.

🧩 Temel Kavramlar
Terim	Açıklama
Logical Address	Program tarafından kullanılan adres
Physical Address	RAM’deki gerçek adres
MMU (Memory Management Unit)	Bu adres dönüşümünü yapar
🧱 Bellek Yönetim Teknikleri
Teknik	Açıklama
Paging	Bellek sabit boyutlu sayfalara bölünür (örnek: 4 KB)
Segmentation	Bellek anlamlı parçalara ayrılır (kod, veri, stack)
Virtual Memory	Disk, RAM’in uzantısı gibi davranır (swap alanı)

💡 Örnek:

8 GB RAM’in var ama 12 GB’lık bir program açabiliyorsan → sanal bellek (swap) sayesinde!

📁 7. Dosya Sistemleri (File Systems)

Dosya sistemi, verilerin nasıl saklandığını ve erişildiğini belirler.

📂 Görevleri

Dosyaları mantıksal olarak organize eder.

Erişim izinlerini yönetir.

Diskteki blokları takip eder.

Klasör (directory) yapısını sağlar.

🔹 Yaygın Dosya Sistemleri

FAT32 → Basit, taşınabilir (USB’lerde yaygın)

NTFS → Windows’un varsayılanı

EXT4 → Linux’un modern dosya sistemi

APFS → macOS dosya sistemi

⚡ 8. G/Ç (I/O) Yönetimi

Input/Output Management, işletim sisteminin cihazlarla iletişimini düzenler.

🎧 Örnek Cihazlar

Klavye, fare

Diskler

Ekran, ses kartı

Yazıcı, ağ kartı

⚙️ G/Ç Katmanları

Uygulama seviyesi (örnek: dosya okuma)

Sistem çağrısı seviyesi

Sürücü seviyesi (device driver)

Donanım seviyesi

🧩 Buffering, Spooling, Caching gibi tekniklerle performans artırılır.

🔧 9. Sistem Programlama Dersinin Diğer Adları

Bazı üniversitelerde bu ders farklı isimlerle geçer 👇

Ders Adı	Açıklama
Sistem Yazılımı (System Software)	Derleyici, assembler, linker odaklı
İşletim Sistemi Uygulamaları	System call pratikleriyle işletim sistemi birleşimi
Düşük Seviyeli Programlama (Low-Level Programming)	Donanım ve bellek kontrolü içerir
UNIX/Linux Sistem Programlama	C diliyle Linux üzerinde sistem çağrıları
Sistem Seviyesinde Programlama (System-Level Programming)	Modern versiyon, C/C++ veya Rust ile yapılır
İşletim Sistemi ve Sistem Programlama	Teori + pratik birleşik ders biçimi
💪 10. Kazandırdığı Beceriler

İşletim sistemi ve donanım etkileşimini anlama

C dilinde sistem düzeyinde programlama

Bellek, işlem ve dosya yönetimini kavrama

Performans optimizasyonu yapabilme

Gerçek zamanlı sistem mantığını öğrenme

Yazılım ile donanım arasındaki sınırları fark etme

🧩 11. Özet

Sistem Programlama, bilgisayarın iç organlarını tanıma dersidir.
Uygulama değil, sistemin kendisini programlarsın. ⚡

Kodun donanıma en yakın hâliyle konuştuğu, “arka plandaki büyünün” nasıl çalıştığını anlamanı sağlar.

📚 12. Önerilen Kaynaklar

Operating System Concepts — Silberschatz, Galvin

Modern Operating Systems — Andrew S. Tanenbaum

Advanced Programming in the UNIX Environment — W. Richard Stevens

Linux Manual Pages (man 2 fork, man 2 exec, man 2 open)