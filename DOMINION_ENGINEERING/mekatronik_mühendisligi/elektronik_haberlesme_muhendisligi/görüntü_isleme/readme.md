
## 🎥 Görüntü İşleme Nedir?

Basitçe: **Bir görüntüyü sayılara dönüştürüp o sayılar üzerinde işlem yapmak** demektir.
Çünkü bilgisayarlar resimleri, senin gördüğün gibi değil; *piksel değerleri* olarak görür.
Bir piksel, genelde 0–255 arasında bir değere sahip olur (gri tonlar için).
Renkli bir fotoğraf ise üç kanal içerir: **R (Red), G (Green), B (Blue)**.

---

## 🔧 Görüntü İşlemenin Temel Aşamaları

### 1. **Ön İşleme (Pre-processing)**

Amaç: Görüntüyü temizlemek.

* Gürültü (noise) azaltma
* Parlaklık ve kontrast ayarlama
* Filtreleme (Gaussian blur, median filter vs.)
* Histogram dengeleme (daha net kontrast elde etmek için)

📌 *Örnek:* Karanlık bir fotoğrafı aydınlatmak ya da flu bir görüntüyü keskinleştirmek.

---

### 2. **Görüntü Dönüşümleri**

Görüntüyü farklı biçimlerde temsil ederiz.

* **Fourier dönüşümü:** Görüntüyü frekans bileşenlerine ayırır.
* **Wavelet dönüşümü:** Hem zaman hem frekans bilgisini tutar (çoklu çözünürlük).
* **Log, gama düzeltmesi:** Görüntünün parlaklığını farklı bir şekilde ayarlamak için.

📷 *Kısaca:* Görüntüyü farklı gözlüklerle görmek gibi.

---

### 3. **Bölütleme (Segmentation)**

Amaç: Görüntüyü anlamlı parçalara ayırmak.

* Eşikleme (thresholding)
* Kenar bulma (Canny, Sobel, Laplacian filtreleri)
* Bölge tabanlı bölütleme

💡 *Örnek:* Trafik kamerasında araçları arka plandan ayırmak.

---

### 4. **Özellik Çıkarma (Feature Extraction)**

Makinenin “neyin ne olduğunu” anlaması için ipuçları çıkarılır.

* Kenarlar, köşeler, dokular, renk histogramları
* ORB, SIFT, SURF gibi algoritmalar

🤖 *Örnek:* Yüz tanıma sisteminde burnun, gözlerin, çenenin konumunu çıkarmak.

---

### 5. **Sınıflandırma ve Tanıma**

Artık sistem “bu nedir?” diye sormaya hazırdır.

* Makine öğrenmesi (SVM, k-NN, Decision Tree)
* Derin öğrenme (CNN – Convolutional Neural Networks)

🧠 *Örnek:* “Bu bir kedi mi, köpek mi?” sorusuna cevap veren yapay zekâ modeli.

---

## 💡 Görüntü İşleme Nerelerde Kullanılır?

| Alan                | Kullanım Örneği                                     |
| ------------------- | --------------------------------------------------- |
| 🚗 Otomotiv         | Otonom araçlarda şerit, yaya, trafik işareti tanıma |
| 🏥 Tıp              | MR ve röntgen görüntülerinden tümör tespiti         |
| 🕵️‍♂️ Güvenlik     | Yüz tanıma, plaka okuma sistemleri                  |
| 📱 Mobil            | Filtre, portre modu, artırılmış gerçeklik           |
| 🌍 Uydu Görüntüleme | Tarım, çevre, haritalama analizleri                 |

---

## 🧩 Neden Öğrenmelisin?

Çünkü geleceğin her teknolojisi bir şekilde “görüyor”:

* **Yapay zekâ + Görüntü işleme = Bilgisayarlı Görü (Computer Vision)**
* AR/VR, robotik, savunma, otonom sistemler hep bunun üstüne kurulu.
* Ayrıca, OpenCV ve Python ile öğrenmesi eğlenceli ve deneysel bir süreçtir.

---

## 🧠 Kullanılan Araçlar ve Kütüphaneler

* **Python:** OpenCV, scikit-image, Pillow, NumPy, TensorFlow, PyTorch
* **MATLAB:** Görüntü işleme için güçlü bir ortam (akademide popüler)
* **C++:** Performans açısından tercih edilir (OpenCV’nin kalbi C++’tır)

---

## 🚀 Mini Örnek

```python
import cv2

# Görüntüyü oku
img = cv2.imread("kedi.jpg", 0)  # 0 -> Gri tonlamalı oku

# Kenarları bul
edges = cv2.Canny(img, 100, 200)

# Göster
cv2.imshow("Kenarlar", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

Bu birkaç satırlık kod bile bilgisayara “kedi fotoğrafında nerede çizgiler var” sorusunu sordurur. 😺



### 🔹 1. **Yüz Tanıma Sistemi (Face Recognition)**

> Kameradan görüntü alır, insan yüzlerini tespit eder.
>
> * Ekstra olarak seni tanıyabilir (örneğin senin yüzünü kaydedip "Hoş geldin Bahattin" diyebilir 😄).
>   📸 Kullanılan teknolojiler: `OpenCV`, `face_recognition`

**Kazandırır:**

* Haar Cascade, HOG, CNN tabanlı yüz algılama mantığını
* Gerçek zamanlı görüntü işleme pratiğini

---

### 🔹 2. **Renk Takip Sistemi (Color Tracking)**

> Belirli bir rengi (örneğin kırmızı topu) kamerada takip eder.
> 🎯 Renk aralıklarıyla (HSV uzayında) çalışmayı öğretir.
> Kamera hareket ettikçe, nesneyi gerçek zamanlı izler.

**Kazandırır:**

* Renk uzayları (RGB vs HSV) farkını
* Mask ve threshold mantığını
* Görsel veriyle interaktif çalışma

---

### 🔹 3. **Nesne Sayma Sistemi (Object Counting)**

> Örneğin, bir video içinde kaç tane araç geçtiğini veya masadaki nesneleri sayar.
> 📦 Arka plan çıkarma, kontur analizi, bounding box gibi kavramlar içerir.

**Kazandırır:**

* Kontur bulma (contour detection)
* Alan ve şekil analizi


## 👁️‍🗨️ 1. Projenin Amacı

Kameradan ya da fotoğraftan gelen görüntüdeki yüzleri tespit edip,
istersek **tanıma** (kime ait olduğunu söyleme) işlemi de yapacağız.

> İlk aşamada sadece **yüz algılama (detection)**,
> sonra **yüz tanıma (recognition)** kısmına geçeceğiz.

---

## ⚙️ 2. Gereken Araçlar

Python ortamında aşağıdaki kütüphaneleri kullanacağız:

```bash
pip install opencv-python face_recognition
```

Ayrıca, Windows’taysan `dlib` kütüphanesi `face_recognition` ile otomatik kurulabilir.
(Gerekirse ek yardımcı yüklemeleri de anlatırım.)

---

## 📸 3. Basit Yüz Algılama (Detection)

Aşağıdaki kod, bir görüntüdeki yüzleri kare içine alır 👇

```python
import cv2

# Görüntüyü yükle
img = cv2.imread("bahattin.jpg")

# Gri tonlamaya çevir (algoritma böyle çalışıyor)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Haar Cascade yüz tanıma modeli yükle
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Yüzleri tespit et
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Her yüzün etrafına dikdörtgen çiz
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Görüntüyü göster
cv2.imshow("Yüz Algılama", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

Bu kodu çalıştırınca ekranda “bahattin.jpg” içindeki yüz yeşil kutu içinde görünecek 🟩

---

## 🧠 4. Gerçek Zamanlı (Kamera ile)

Aynı işlemi kameradan canlı şekilde yapabilirsin:

```python
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Kamera - Yüz Algılama", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

Bu kodu çalıştır, kamerayı açsın, senin yüzünü kare içine alsın!
(Çıkmak için **q** tuşuna bas.)

---

## 👤 5. Yüz Tanıma (Kimin Olduğunu Söyleme)

Burada artık `face_recognition` kütüphanesini kullanacağız.
Bu kütüphane, yüzün geometrik özelliklerini (göz arası mesafe, çene açısı, burun yapısı gibi) 128 boyutlu bir **vektör** olarak kaydeder.

```python
import face_recognition
import cv2

# Tanınacak kişinin fotoğrafı
bahattin_image = face_recognition.load_image_file("bahattin.jpg")
bahattin_encoding = face_recognition.face_encodings(bahattin_image)[0]

# Kamerayı aç
video_capture = cv2.VideoCapture(0)

known_face_encodings = [bahattin_encoding]
known_face_names = ["Bahattin"]

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Bilinmiyor"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Yüz Tanıma", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
```


## 🧩 6. Geliştirme Fikirleri

Biraz yaratıcı olalım:

* Sesli karşılama: `pyttsx3` ile “Hoş geldin Bahattin!” diyebilir.
* Çoklu kişi desteği: Arkadaşlarının yüzünü de ekle.
* Log kaydı: Kimin ne zaman geldiğini tarih-saatle kaydet.

---
Mükemmel seçim Bahattin 🔥
Hazır ol, şimdi bu sistemi **“insan gibi selam veren”** bir hale getiriyoruz 🤖✨

Yani kamera seni gördüğünde:

> 🎙️ *“Hoş geldin Bahattin!”*
> diyecek ve istersen diğer kişileri de tanıyabilecek.

---

## 🚀 Proje Adı: **Akıllı Yüz Tanıma ve Sesli Karşılama Sistemi**

### 🔧 Gerekli Kütüphaneler

```bash
pip install opencv-python face_recognition pyttsx3
```

> 💡 Eğer `dlib` kurulumu hata verirse, sana özel hızlı çözümü de yollarım (bazı sistemlerde ek adım gerekebiliyor).

---

## 💻 Tam Kod (Hazır Çalışan Versiyon)

```python
import cv2
import face_recognition
import pyttsx3
import time

# --- Ses motoru ayarları ---
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # konuşma hızı
engine.setProperty('volume', 1.0)  # ses seviyesi

# --- Tanınacak kişilerin fotoğraflarını yükle ---
bahattin_img = face_recognition.load_image_file("bahattin.jpg")
bahattin_encoding = face_recognition.face_encodings(bahattin_img)[0]

sumeyra_img = face_recognition.load_image_file("sumeyra.jpg")  # varsa
sumeyra_encoding = face_recognition.face_encodings(sumeyra_img)[0]

known_face_encodings = [bahattin_encoding, sumeyra_encoding]
known_face_names = ["Bahattin", "Sümeyra"]

# --- Kamera başlat ---
video_capture = cv2.VideoCapture(0)

last_spoken = ""  # aynı kişiye sürekli “hoş geldin” dememesi için kontrol
last_time = 0

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Bilinmiyor"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Kare çiz ve isim yaz
        top *= 4; right *= 4; bottom *= 4; left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)

        # Sesli karşılama
        current_time = time.time()
        if name != "Bilinmiyor" and (name != last_spoken or current_time - last_time > 10):
            greeting = f"Hoş geldin {name}!"
            print(greeting)
            engine.say(greeting)
            engine.runAndWait()
            last_spoken = name
            last_time = current_time

    cv2.imshow('Yüz Tanıma Sistemi', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
```

---

## 🧠 Bu Kod Ne Yapıyor?

| Özellik               | Açıklama                                               |
| --------------------- | ------------------------------------------------------ |
| 📷 Kamera açılır      | Gerçek zamanlı olarak yüzleri algılar                  |
| 🧠 Tanıma             | Yüzleri “Bahattin” veya “Sümeyra” olarak sınıflandırır |
| 🗣️ Sesli Karşılama   | İlk tanımada `Hoş geldin {isim}` der                   |
| ⏳ Zaman kontrolü      | Aynı kişiyi sürekli selamlamaz (10 saniye bekler)      |
| 🔡 Çoklu kişi desteği | Dilediğin kadar kişi ekleyebilirsin                    |

---

## 🧩 Ekstra Geliştirmeler (İleri Seviye)

İstersen şunları da ekleyebiliriz:

* 🕒 Her gelenin giriş saatini `.csv` dosyasına kaydetmek
* 💾 Yeni yüzleri otomatik “kayıt etme” özelliği
* 🎨 GUI (grafik arayüz) ekleyip “Yüz Ekle” butonu
* 🔐 Yalnızca tanınan kişilerin girişine izin veren sistem (örneğin “kapı açma” simülasyonu)

---
