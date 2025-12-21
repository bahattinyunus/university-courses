"""
Görüntü İşleme - Yüz Algılama
OpenCV ile basit yüz algılama örneği
"""

# Not: opencv-python kütüphanesi gerekli
# Kurulum: pip install opencv-python

try:
    import cv2
except ImportError:
    print("OpenCV yüklü değil!")
    print("Kurulum: pip install opencv-python")
    exit(1)


def yuz_algila_fotograf(dosya_yolu):
    """
    Fotoğraftan yüz algılama
    
    Args:
        dosya_yolu: İşlenecek görüntü dosyasının yolu
    """
    # Görüntüyü yükle
    img = cv2.imread(dosya_yolu)
    
    if img is None:
        print(f"Hata: {dosya_yolu} dosyası bulunamadı!")
        return
    
    # Gri tonlamaya çevir (yüz algılama algoritması gri tonlama ile çalışır)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Haar Cascade yüz tanıma modeli yükle
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    
    # Yüzleri tespit et
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,      # Görüntü ölçeklendirme faktörü
        minNeighbors=5,       # Minimum komşu sayısı
        minSize=(30, 30)      # Minimum yüz boyutu
    )
    
    # Tespit edilen yüzlerin etrafına dikdörtgen çiz
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, 'Yuz', (x, y-10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Sonucu göster
    print(f"{len(faces)} yüz tespit edildi!")
    cv2.imshow('Yuz Algilama', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Sonucu kaydet
    cv2.imwrite('yuz_algilama_sonuc.jpg', img)
    print("Sonuç 'yuz_algilama_sonuc.jpg' olarak kaydedildi.")


def yuz_algila_kamera():
    """
    Kameradan canlı yüz algılama
    """
    # Kamera aç
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Hata: Kamera açılamadı!")
        return
    
    # Haar Cascade modeli yükle
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    
    print("Kamera açıldı. Çıkmak için 'q' tuşuna basın.")
    
    while True:
        # Kameradan frame oku
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Gri tonlamaya çevir
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Yüzleri tespit et
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        
        # Yüzlerin etrafına dikdörtgen çiz
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f'Yuz ({w}x{h})', (x, y-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Frame'i göster
        cv2.imshow('Canli Yuz Algilama', frame)
        
        # 'q' tuşuna basılırsa çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Temizlik
    cap.release()
    cv2.destroyAllWindows()
    print("Kamera kapatıldı.")


def kenar_bulma(dosya_yolu):
    """
    Görüntüde kenar tespiti (Canny Edge Detection)
    
    Args:
        dosya_yolu: İşlenecek görüntü dosyasının yolu
    """
    # Görüntüyü yükle
    img = cv2.imread(dosya_yolu, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print(f"Hata: {dosya_yolu} dosyası bulunamadı!")
        return
    
    # Canny kenar tespiti
    edges = cv2.Canny(img, 100, 200)  # Eşik değerleri
    
    # Sonuçları göster
    cv2.imshow('Orijinal', img)
    cv2.imshow('Kenarlar', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Örnek kullanım
if __name__ == "__main__":
    print("=== Görüntü İşleme - Yüz Algılama ===\n")
    print("1. Fotoğraftan yüz algılama")
    print("2. Kameradan canlı yüz algılama")
    print("3. Kenar tespiti\n")
    
    secim = input("Seçiminiz (1/2/3): ")
    
    if secim == "1":
        dosya = input("Görüntü dosyası yolu: ")
        yuz_algila_fotograf(dosya)
    elif secim == "2":
        yuz_algila_kamera()
    elif secim == "3":
        dosya = input("Görüntü dosyası yolu: ")
        kenar_bulma(dosya)
    else:
        print("Geçersiz seçim!")

