"""
Fizik Hesaplamaları
Temel fizik formüllerinin Python implementasyonları
"""

import math

# ============================================
# 1. MEKANİK - HAREKET
# ============================================

def hiz_hesapla(mesafe, zaman):
    """
    Hız hesaplama: v = s / t
    
    Args:
        mesafe: Alınan yol (metre)
        zaman: Geçen süre (saniye)
    
    Returns:
        Hız (m/s)
    """
    return mesafe / zaman


def ivme_hesapla(ilk_hiz, son_hiz, zaman):
    """
    İvme hesaplama: a = (v - v₀) / t
    
    Args:
        ilk_hiz: Başlangıç hızı (m/s)
        son_hiz: Son hız (m/s)
        zaman: Geçen süre (saniye)
    
    Returns:
        İvme (m/s²)
    """
    return (son_hiz - ilk_hiz) / zaman


def newton_ikinci_yasa(kuvvet, kutle):
    """
    Newton'un 2. Yasası: F = m × a
    İvme hesaplama: a = F / m
    
    Args:
        kuvvet: Uygulanan kuvvet (Newton)
        kutle: Kütle (kg)
    
    Returns:
        İvme (m/s²)
    """
    return kuvvet / kutle


def serbest_dusme_yukseklik(zaman, g=9.81):
    """
    Serbest düşme yükseklik: h = (1/2) × g × t²
    
    Args:
        zaman: Düşme süresi (saniye)
        g: Yerçekimi ivmesi (m/s²) - varsayılan 9.81
    
    Returns:
        Yükseklik (metre)
    """
    return 0.5 * g * (zaman ** 2)


# ============================================
# 2. ELEKTRİK VE MANYETİZMA
# ============================================

def ohm_kanunu(gerilim, direnc):
    """
    Ohm Kanunu: V = I × R
    Akım hesaplama: I = V / R
    
    Args:
        gerilim: Voltaj (Volt)
        direnc: Direnç (Ohm)
    
    Returns:
        Akım (Amper)
    """
    return gerilim / direnc


def elektrik_gucu(gerilim, akim):
    """
    Elektrik Gücü: P = V × I
    
    Args:
        gerilim: Voltaj (Volt)
        akim: Akım (Amper)
    
    Returns:
        Güç (Watt)
    """
    return gerilim * akim


def elektrik_enerjisi(guc, zaman):
    """
    Elektrik Enerjisi: E = P × t
    
    Args:
        guc: Güç (Watt)
        zaman: Süre (saniye)
    
    Returns:
        Enerji (Joule)
    """
    return guc * zaman


# ============================================
# 3. TERMODİNAMİK
# ============================================

def celsius_to_kelvin(celsius):
    """
    Celsius'tan Kelvin'e dönüşüm: K = °C + 273.15
    
    Args:
        celsius: Sıcaklık (Celsius)
    
    Returns:
        Sıcaklık (Kelvin)
    """
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    """
    Fahrenheit'tan Celsius'a dönüşüm: °C = (°F - 32) × 5/9
    
    Args:
        fahrenheit: Sıcaklık (Fahrenheit)
    
    Returns:
        Sıcaklık (Celsius)
    """
    return (fahrenheit - 32) * 5 / 9


def isi_enerjisi(kutle, oz_isi, sicaklik_farki):
    """
    Isı Enerjisi: Q = m × c × ΔT
    
    Args:
        kutle: Kütle (kg)
        oz_isi: Özgül ısı (J/kg·K)
        sicaklik_farki: Sıcaklık farkı (Kelvin)
    
    Returns:
        Isı enerjisi (Joule)
    """
    return kutle * oz_isi * sicaklik_farki


# ============================================
# 4. DALGALAR VE OPTİK
# ============================================

def dalga_boyu(frekans, hiz=3e8):
    """
    Dalga boyu: λ = c / f
    
    Args:
        frekans: Frekans (Hz)
        hiz: Dalga hızı (m/s) - varsayılan ışık hızı
    
    Returns:
        Dalga boyu (metre)
    """
    return hiz / frekans


def frekans_hesapla(dalga_boyu, hiz=3e8):
    """
    Frekans: f = c / λ
    
    Args:
        dalga_boyu: Dalga boyu (metre)
        hiz: Dalga hızı (m/s)
    
    Returns:
        Frekans (Hz)
    """
    return hiz / dalga_boyu


# ============================================
# 5. MODERN FİZİK
# ============================================

def einstein_enerji_kutle(kutle, isik_hizi=3e8):
    """
    Einstein'ın ünlü formülü: E = m × c²
    
    Args:
        kutle: Kütle (kg)
        isik_hizi: Işık hızı (m/s) - varsayılan 3×10⁸
    
    Returns:
        Enerji (Joule)
    """
    return kutle * (isik_hizi ** 2)


# ============================================
# ÖRNEK KULLANIM
# ============================================

if __name__ == "__main__":
    print("=== Fizik Hesaplamaları Örnekleri ===\n")
    
    # Mekanik örnekleri
    print("1. MEKANİK:")
    print(f"   Hız: {hiz_hesapla(100, 10):.2f} m/s")
    print(f"   İvme: {ivme_hesapla(0, 20, 5):.2f} m/s²")
    print(f"   Newton 2. Yasa: {newton_ikinci_yasa(50, 10):.2f} m/s²")
    print(f"   Serbest düşme (2 saniye): {serbest_dusme_yukseklik(2):.2f} m\n")
    
    # Elektrik örnekleri
    print("2. ELEKTRİK:")
    print(f"   Ohm Kanunu (12V, 4Ω): {ohm_kanunu(12, 4):.2f} A")
    print(f"   Elektrik Gücü (12V, 3A): {elektrik_gucu(12, 3):.2f} W")
    print(f"   Enerji (36W, 3600s): {elektrik_enerjisi(36, 3600)/1000:.2f} kJ\n")
    
    # Termodinamik örnekleri
    print("3. TERMODİNAMİK:")
    print(f"   25°C = {celsius_to_kelvin(25):.2f} K")
    print(f"   100°F = {fahrenheit_to_celsius(100):.2f}°C")
    print(f"   Isı enerjisi (1kg su, 50K): {isi_enerjisi(1, 4186, 50)/1000:.2f} kJ\n")
    
    # Dalgalar örnekleri
    print("4. DALGALAR:")
    print(f"   Dalga boyu (100 MHz): {dalga_boyu(100e6):.2f} m")
    print(f"   Frekans (λ=0.5m): {frekans_hesapla(0.5)/1e6:.2f} MHz\n")
    
    # Modern fizik örnekleri
    print("5. MODERN FİZİK:")
    print(f"   E=mc² (1 kg): {einstein_enerji_kutle(1)/1e16:.2e} × 10¹⁶ J")

