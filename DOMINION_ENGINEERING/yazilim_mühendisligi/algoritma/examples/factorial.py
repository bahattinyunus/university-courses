"""
Faktöriyel Hesaplama
Algoritma dersinde sık kullanılan örnek
"""

def factorial_iterative(n):
    """
    Faktöriyel hesaplama - Döngü ile (iteratif)
    
    Args:
        n: Faktöriyeli alınacak sayı
    
    Returns:
        n! değeri
    """
    if n < 0:
        return None  # Negatif sayıların faktöriyeli yok
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


def factorial_recursive(n):
    """
    Faktöriyel hesaplama - Özyineleme ile (recursive)
    
    Args:
        n: Faktöriyeli alınacak sayı
    
    Returns:
        n! değeri
    """
    # Temel durum (base case)
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    # Özyinelemeli çağrı
    return n * factorial_recursive(n - 1)


# Örnek kullanım
if __name__ == "__main__":
    number = 5
    
    print(f"Faktöriyel hesaplama: {number}!")
    print(f"Döngü ile: {factorial_iterative(number)}")
    print(f"Özyineleme ile: {factorial_recursive(number)}")
    
    # Karmaşıklık: O(n) - Her iki yöntem de
    # Özyineleme daha okunabilir ama daha fazla bellek kullanır

