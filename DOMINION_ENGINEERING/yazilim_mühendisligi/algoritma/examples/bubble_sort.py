"""
Bubble Sort (Kabarcık Sıralama) Algoritması
Basit ama öğretici bir sıralama algoritması
"""

def bubble_sort(arr):
    """
    Bubble Sort algoritması ile diziyi sıralar.
    
    Args:
        arr: Sıralanacak liste
    
    Returns:
        Sıralanmış liste
    """
    n = len(arr)
    
    # Dizi üzerinde n-1 kez geçiş yap
    for i in range(n):
        # Her geçişte en büyük eleman sona gider
        swapped = False
        for j in range(0, n - i - 1):
            # Eğer önceki eleman sonrakinden büyükse yer değiştir
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Eğer hiç yer değiştirme olmadıysa dizi zaten sıralı
        if not swapped:
            break
    
    return arr


# Örnek kullanım
if __name__ == "__main__":
    # Test verisi
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    print("Sıralanmadan önce:", numbers)
    sorted_numbers = bubble_sort(numbers.copy())
    print("Sıralandıktan sonra:", sorted_numbers)
    
    # Karmaşıklık: O(n²) - Zaman karmaşıklığı
    # En iyi durum: O(n) - Dizi zaten sıralıysa
    # En kötü durum: O(n²) - Dizi ters sıralıysa

