"""
Betik Dilleri - Otomasyon Örnekleri
Python ile günlük işleri otomatikleştirme
"""

import os
import shutil
from datetime import datetime

def dosya_organize_et(klasor_yolu):
    """
    Bir klasördeki dosyaları uzantılarına göre organize eder.
    
    Args:
        klasor_yolu: Organize edilecek klasörün yolu
    """
    # Dosya türlerine göre klasörler
    dosya_turleri = {
        'Resimler': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Videolar': ['.mp4', '.avi', '.mov', '.mkv'],
        'Belgeler': ['.pdf', '.doc', '.docx', '.txt'],
        'Kodlar': ['.py', '.js', '.html', '.css', '.java'],
        'Arsivler': ['.zip', '.rar', '.7z', '.tar']
    }
    
    # Klasör oluştur
    for klasor_adi in dosya_turleri.keys():
        klasor_path = os.path.join(klasor_yolu, klasor_adi)
        if not os.path.exists(klasor_path):
            os.makedirs(klasor_path)
    
    # Dosyaları taşı
    for dosya in os.listdir(klasor_yolu):
        dosya_yolu = os.path.join(klasor_yolu, dosya)
        
        if os.path.isfile(dosya_yolu):
            dosya_uzantisi = os.path.splitext(dosya)[1].lower()
            
            for klasor_adi, uzantilar in dosya_turleri.items():
                if dosya_uzantisi in uzantilar:
                    hedef = os.path.join(klasor_yolu, klasor_adi, dosya)
                    shutil.move(dosya_yolu, hedef)
                    print(f"{dosya} -> {klasor_adi}/")
                    break


def log_tut(metin, dosya_adi="log.txt"):
    """
    İşlemleri bir log dosyasına kaydeder.
    
    Args:
        metin: Kaydedilecek metin
        dosya_adi: Log dosyasının adı
    """
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_mesaji = f"[{zaman}] {metin}\n"
    
    with open(dosya_adi, "a", encoding="utf-8") as f:
        f.write(log_mesaji)
    
    print(f"Log kaydedildi: {metin}")


def toplu_dosya_degistir(klasor_yolu, eski_metin, yeni_metin):
    """
    Bir klasördeki tüm dosyalarda metin değiştirme.
    
    Args:
        klasor_yolu: İşlenecek klasör
        eski_metin: Değiştirilecek metin
        yeni_metin: Yeni metin
    """
    for kok, klasorler, dosyalar in os.walk(klasor_yolu):
        for dosya in dosyalar:
            if dosya.endswith('.txt') or dosya.endswith('.md'):
                dosya_yolu = os.path.join(kok, dosya)
                
                try:
                    with open(dosya_yolu, 'r', encoding='utf-8') as f:
                        icerik = f.read()
                    
                    if eski_metin in icerik:
                        icerik = icerik.replace(eski_metin, yeni_metin)
                        
                        with open(dosya_yolu, 'w', encoding='utf-8') as f:
                            f.write(icerik)
                        
                        print(f"✓ {dosya_yolu} güncellendi")
                except Exception as e:
                    print(f"✗ Hata ({dosya_yolu}): {e}")


# Örnek kullanım
if __name__ == "__main__":
    print("=== Betik Dilleri Otomasyon Örnekleri ===\n")
    
    # Log örneği
    log_tut("Program başlatıldı")
    log_tut("Dosya organizasyonu yapılıyor...")
    
    # Not: Gerçek kullanımda dikkatli olun!
    # dosya_organize_et("C:/Users/Desktop/Karışık_Dosyalar")
    
    print("\nÖrnekler hazır! Gerçek kullanım için yorumları kaldırın.")

