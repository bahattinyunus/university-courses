# 🛡️ Yapay Zeka Çağında Veri Koruma: KVKK ve GDPR

## 1. Büyük Veri ve AI İlişkisi
Yapay zeka modelleri (özellikle Deep Learning), öğrenmek için devasa verilere ihtiyaç duyar. Ancak bu verilerin önemli bir kısmı **kişisel veri** içerebilir (yüz fotoğrafları, ses kayıtları, sağlık verileri).

## 2. Unutulma Hakkı (Right to be Forgotten)
KVKK ve GDPR'da "Unutulma Hakkı" vardır. Bir kişi verisinin silinmesini isteyebilir.
*   **Sorun:** Bir AI modeli eğitildikten sonra, o kişinin verisini modelin "hafızasından" silmek teknik olarak çok zordur (Machine Unlearning). Modelin parametrelerini tamamen değiştirmek gerekebilir.

## 3. Black Box (Kara Kutu) Sorunu ve Açıklanabilirlik
Hukuk, kararların gerekçeli olmasını ister. Ancak Karmaşık Sinir Ağları (DNN), bir kararı (örn: kredi reddi) neden verdiğini her zaman açıklayamaz.
*   **GDPR Madde 22:** Otomatik karar vermeye itiraz hakkı tanır ve "kararın mantığının açıklanmasını" talep eder.

## 4. Algoritmik Ayrımcılık (Bias)
Eğer eğitim verisi önyargılıysa, yapay zeka da ırkçı veya cinsiyetçi kararlar verebilir.
*   *Örnek:* İşe alım algoritmasının, geçmiş verilerde erkekler çoğunlukta olduğu için kadın adayları elemesi.
*   Hukuki olarak bu durum, eşitlik ilkesine aykırıdır ve tazminat sorumluluğu doğurur.

## 5. Çözüm Önerileri
*   **Privacy-Preserving AI:** Diferansiyel gizlilik teknikleri kullanmak.
*   **XAI (Explainable AI):** Açıklanabilir yapay zeka modellerine öncelik vermek.
