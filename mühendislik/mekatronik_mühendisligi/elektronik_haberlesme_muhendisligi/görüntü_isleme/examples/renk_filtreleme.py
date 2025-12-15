"""
Görüntü İşleme - Renk Filtreleme
Belirli bir rengi tespit etme ve filtreleme
"""

try:
    import cv2
    import numpy as np
except ImportError:
    print("OpenCV ve NumPy yüklü değil!")
    print("Kurulum: pip install opencv-python numpy")
    exit(1)


def renk_filtreleme_hsv(dosya_yolu, renk='kirmizi'):
    """
    HSV renk uzayında renk filtreleme
    
    Args:
        dosya_yolu: İşlenecek görüntü dosyasının yolu
        renk: Filtrelenecek renk ('kirmizi', 'yesil', 'mavi')
    """
    # Görüntüyü yükle
    img = cv2.imread(dosya_yolu)
    
    if img is None:
        print(f"Hata: {dosya_yolu} dosyası bulunamadı!")
        return
    
    # BGR'den HSV'ye dönüştür
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Renk aralıklarını belirle
    renk_araliklari = {
        'kirmizi': [
            np.array([0, 50, 50]),      # Alt sınır
            np.array([10, 255, 255])    # Üst sınır
        ],
        'yesil': [
            np.array([40, 50, 50]),
            np.array([80, 255, 255])
        ],
        'mavi': [
            np.array([100, 50, 50]),
            np.array([130, 255, 255])
        ]
    }
    
    if renk not in renk_araliklari:
        print(f"Hata: '{renk}' rengi desteklenmiyor!")
        return
    
    # Renk maskesi oluştur
    alt_sinir, ust_sinir = renk_araliklari[renk]
    mask = cv2.inRange(hsv, alt_sinir, ust_sinir)
    
    # Maskeyi görüntüye uygula
    sonuc = cv2.bitwise_and(img, img, mask=mask)
    
    # Sonuçları göster
    cv2.imshow('Orijinal', img)
    cv2.imshow('Renk Maskesi', mask)
    cv2.imshow(f'{renk.capitalize()} Filtre', sonuc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def renk_takibi_kamera(renk='kirmizi'):
    """
    Kameradan belirli bir rengi takip etme
    """
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Hata: Kamera açılamadı!")
        return
    
    # Renk aralıkları
    renk_araliklari = {
        'kirmizi': [
            np.array([0, 50, 50]),
            np.array([10, 255, 255])
        ],
        'yesil': [
            np.array([40, 50, 50]),
            np.array([80, 255, 255])
        ],
        'mavi': [
            np.array([100, 50, 50]),
            np.array([130, 255, 255])
        ]
    }
    
    if renk not in renk_araliklari:
        print(f"Hata: '{renk}' rengi desteklenmiyor!")
        return
    
    alt_sinir, ust_sinir = renk_araliklari[renk]
    
    print(f"{renk.capitalize()} renk takibi başladı. Çıkmak için 'q' tuşuna basın.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # HSV'ye dönüştür
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Renk maskesi
        mask = cv2.inRange(hsv, alt_sinir, ust_sinir)
        
        # Gürültüyü azalt
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        
        # Konturları bul
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, 
                                      cv2.CHAIN_APPROX_SIMPLE)
        
        # En büyük konturu bul ve işaretle
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest_contour) > 100:  # Minimum alan
                x, y, w, h = cv2.boundingRect(largest_contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, f'{renk.capitalize()} Nesne', (x, y-10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Sonuçları göster
        cv2.imshow('Renk Takibi', frame)
        cv2.imshow('Mask', mask)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


# Örnek kullanım
if __name__ == "__main__":
    print("=== Görüntü İşleme - Renk Filtreleme ===\n")
    print("1. Fotoğraftan renk filtreleme")
    print("2. Kameradan renk takibi\n")
    
    secim = input("Seçiminiz (1/2): ")
    renk = input("Renk (kirmizi/yesil/mavi): ").lower()
    
    if secim == "1":
        dosya = input("Görüntü dosyası yolu: ")
        renk_filtreleme_hsv(dosya, renk)
    elif secim == "2":
        renk_takibi_kamera(renk)
    else:
        print("Geçersiz seçim!")

