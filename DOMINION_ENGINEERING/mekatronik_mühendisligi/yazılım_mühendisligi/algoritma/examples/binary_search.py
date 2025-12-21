"""
Binary Search (İkili Arama) Algoritması
Sıralı dizilerde çok hızlı arama yapar
"""

def binary_search(arr, target):
    """
    Binary Search ile hedef değeri arar.
    
    Args:
        arr: Sıralı liste (küçükten büyüğe)
        target: Aranacak değer
    
    Returns:
        Eğer bulunursa indeks, bulunamazsa -1
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Ortadaki elemanı bul
        mid = (left + right) // 2
        
        # Ortadaki eleman hedef mi?
        if arr[mid] == target:
            return mid
        
        # Eğer hedef ortadaki elemandan küçükse, sol yarıya bak
        elif arr[mid] > target:
            right = mid - 1
        
        # Eğer hedef ortadaki elemandan büyükse, sağ yarıya bak
        else:
            left = mid + 1
    
    # Bulunamadı
    return -1


# Özyinelemeli (Recursive) versiyon
def binary_search_recursive(arr, target, left=0, right=None):
    """
    Binary Search'in özyinelemeli versiyonu
    """
    if right is None:
        right = len(arr) - 1
    
    # Temel durum: arama aralığı geçersiz
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


# Örnek kullanım
if __name__ == "__main__":
    # Sıralı dizi (binary search için dizi sıralı olmalı!)
    sorted_list = [2, 5, 8, 12, 16, 23, 38, 45, 67, 78, 99]
    
    target = 23
    result = binary_search(sorted_list, target)
    
    if result != -1:
        print(f"{target} değeri {result}. indekste bulundu!")
    else:
        print(f"{target} değeri bulunamadı!")
    
    # Karmaşıklık: O(log n) - Çok hızlı!
    # Linear search: O(n) - Yavaş
    # Binary search: O(log n) - Hızlı

