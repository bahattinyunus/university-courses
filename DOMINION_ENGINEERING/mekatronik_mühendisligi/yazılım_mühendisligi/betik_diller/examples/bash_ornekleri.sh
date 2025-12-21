#!/bin/bash
# Betik Dilleri - Bash Script Örnekleri
# Linux/Unix sistemlerde kullanılan shell script örnekleri

echo "=== Bash Script Örnekleri ==="

# 1. Değişken kullanımı
ISIM="Bahattin"
YAS=24
echo "Merhaba, ben $ISIM, $YAS yaşındayım."

# 2. Koşul ifadeleri
SAYI=10
if [ $SAYI -gt 5 ]; then
    echo "$SAYI, 5'ten büyüktür."
else
    echo "$SAYI, 5'ten küçük veya eşittir."
fi

# 3. Döngü örnekleri
echo -e "\n1'den 5'e kadar sayılar:"
for i in {1..5}; do
    echo "Sayı: $i"
done

# 4. Dosya kontrolü
DOSYA="readme.md"
if [ -f "$DOSYA" ]; then
    echo -e "\n$DOSYA dosyası mevcut."
    echo "Dosya boyutu: $(du -h $DOSYA | cut -f1)"
else
    echo -e "\n$DOSYA dosyası bulunamadı."
fi

# 5. Fonksiyon örneği
topla() {
    SONUC=$(( $1 + $2 ))
    echo "Toplam: $SONUC"
}

echo -e "\nFonksiyon örneği:"
topla 15 25

# 6. Sistem bilgisi
echo -e "\nSistem bilgileri:"
echo "Kullanıcı: $(whoami)"
echo "Mevcut dizin: $(pwd)"
echo "Tarih: $(date)"

# 7. Dosya listeleme
echo -e "\nMevcut dizindeki .py dosyaları:"
ls -lh *.py 2>/dev/null || echo "Python dosyası bulunamadı."

echo -e "\n=== Script tamamlandı ==="

