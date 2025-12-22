"""
Betik Dilleri - Web Scraping Örneği
Python ile web'den veri çekme
"""

# Not: requests ve beautifulsoup4 kütüphaneleri gerekli
# Kurulum: pip install requests beautifulsoup4

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Gerekli kütüphaneler yüklü değil!")
    print("Kurulum: pip install requests beautifulsoup4")
    exit(1)


def basit_web_scraping(url):
    """
    Basit web scraping örneği - başlıkları çeker.
    
    Args:
        url: İşlenecek web sitesi URL'i
    
    Returns:
        Başlıklar listesi
    """
    try:
        # Web sayfasını indir
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Hata kontrolü
        
        # HTML'i parse et
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Tüm başlıkları bul (h1, h2, h3)
        basliklar = []
        for tag in ['h1', 'h2', 'h3']:
            for baslik in soup.find_all(tag):
                basliklar.append(baslik.get_text().strip())
        
        return basliklar
    
    except requests.RequestException as e:
        print(f"Hata: {e}")
        return []


def haber_basliklari_cek(url="https://www.example.com"):
    """
    Örnek: Haber sitesinden başlıkları çeker.
    (Gerçek kullanımda robots.txt ve kullanım şartlarına dikkat edin!)
    """
    basliklar = basit_web_scraping(url)
    
    print(f"\n{url} sitesinden {len(basliklar)} başlık bulundu:\n")
    for i, baslik in enumerate(basliklar[:10], 1):  # İlk 10 başlık
        print(f"{i}. {baslik}")
    
    return basliklar


# Örnek kullanım
if __name__ == "__main__":
    print("=== Web Scraping Örneği ===\n")
    print("Not: Gerçek bir URL ile test etmek için kodu güncelleyin.")
    print("Önemli: Web scraping yaparken robots.txt ve kullanım şartlarına uyun!\n")
    
    # Örnek (gerçek kullanımda dikkatli olun)
    # haber_basliklari_cek("https://www.example-news-site.com")

