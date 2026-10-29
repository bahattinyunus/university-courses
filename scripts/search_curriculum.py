#!/usr/bin/env python3
"""
University Courses (UC) - Evrensel Akademik Arama ve Müfredat İndeksleyici
Bu araç 21 konteyner, 374 akademik disiplin ve 2618 kademeyi anında tarar, arar ve indeksler.
"""

import os
import sys
import json
import argparse
import unicodedata
from pathlib import Path

# Safe stdout encoding for Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPTS_DIR)
INDEX_PATH = os.path.join(ROOT_DIR, 'assets', 'curriculum_index.json')

CONTAINER_TITLES = {
    'epistemik': '👁️ Epistemik Vizyon & Bilgi Felsefesi',
    'meta_muhendislik': '🛠️ Mühendislik & İleri Teknoloji Bilimleri',
    'mimarlik_ve_tasarim': '🏛️ Mimarlık, Tasarım & Mekânsal Şehircilik',
    'guzel_sanatlar': '🖼️ Güzel Sanatlar, Estetik & Görsel Kültür',
    'saglik': '🩺 Sağlık Bilimleri, Klinik Tıp & Yaşam',
    'ogretmenlik': '🎓 Eğitim Fakültesi, Pedagoji & Didaktik',
    'spor_bilimleri': '🏅 Spor Bilimleri, Kinetik & Fiziksel Performans',
    'sosyal_ve_beseri_bilimler': '⚖️ Sosyal, Beşeri, İdari & Davranışsal Bilimler',
    'temel_bilimler': '🧪 Temel Fen Bilimleri (Fizik, Kimya, Matematik)',
    'edebiyat_ve_diller': '📚 Filoloji, Dilbilim & Dünya Edebiyatı',
    'iletisim': '📡 İletişim, Medya Ekolojisi & Dijital Anlatı',
    'turizm_ve_gastronomi': '🏨 Turizm, Ağırlama & Gastronomi Sanatı',
    'tarim_ve_ziraat_bilimleri': '🌱 Tarım, Ziraat, Biyosistem & Doğa Bilimleri',
    'askeri_bilimler_ve_savunma_teknolojileri': '⚔️ Savunma Sanayii, Harp Doktrini & Askeri Strateji',
    'hukuk_bilimi': '⚖️ Adalet, Hukuk Kuramı & Yasal Düzen',
    'ilahiyat_ve_din': '📚 İlahiyat, Dinler Tarihi & Karşılaştırmalı Felsefe',
    'on_lisans_programlari': '📋 Mesleki Yüksekokul & Uygulamalı Teknik Disiplinler',
    'ozel_arastirma_alanlari': '🔬 Özel Araştırma, Füzyon & Sınır Disiplinler',
    'kariyer_ve_sertifikasyonlar': '🚀 Kariyer, Portfolyo, Standartlar & Sertifikasyon',
    'meta_yetkinlikler_ve_gelisim': '🧠 Meta-Zihin, Otonom İrade & Bilişsel Disiplin',
    'genel': '📂 Genel Metodoloji, Arşiv & Ortak Alanlar'
}

TIER_NAMES = {
    '00': 'Akademik Hazırlık ve Dil',
    '01': 'Temel Bilimler ve Seminerler',
    '02': 'Alan Dersleri ve Pratik',
    '03': 'Seçmeli ve İleri Uygulama',
    '04': 'Araştırma ve Bitirme',
    '05': 'Lisansüstü ve Akademik Kariyer',
    '06': 'Sertifikasyon ve Endüstriyel Standartlar'
}

def normalize_text(text: str) -> str:
    """Türkçe karakterleri ve aksanları arama için normalize eder."""
    tr_map = {
        'ı': 'i', 'İ': 'i', 'I': 'i',
        'ğ': 'g', 'Ğ': 'g',
        'ü': 'u', 'Ü': 'u',
        'ş': 's', 'Ş': 's',
        'ö': 'o', 'Ö': 'o',
        'ç': 'c', 'Ç': 'c'
    }
    for tr_char, eng_char in tr_map.items():
        text = text.replace(tr_char, eng_char)
    return text.lower()

def format_dept_name(d: str) -> str:
    dept_name = d.replace('_', ' ').title()
    dept_name = (dept_name
                 .replace('Muhendisligi', 'Mühendisliği')
                 .replace('Insaat', 'İnşaat')
                 .replace('Isletme', 'İşletme')
                 .replace('Ulasim', 'Ulaşım')
                 .replace('Bilisim', 'Bilişim')
                 .replace('Sagligi', 'Sağlığı')
                 .replace('Egitimi', 'Eğitimi')
                 .replace('Ogretmenligi', 'Öğretmenliği')
                 .replace('Programciligi', 'Programcılığı')
                 .replace('Iktisat', 'İktisat')
                 .replace('Iletisim', 'İletişim'))
    return dept_name

def build_index() -> list:
    """Tüm repository ağacını tarar ve yapılandırılmış JSON indeksi oluşturur."""
    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
    index_data = []

    for container_key in sorted(CONTAINER_TITLES.keys()):
        c_path = os.path.join(ROOT_DIR, container_key)
        if not os.path.isdir(c_path):
            continue

        depts = sorted([d for d in os.listdir(c_path) if os.path.isdir(os.path.join(c_path, d)) and not d.startswith('.')])
        for dept_slug in depts:
            dept_path = os.path.join(c_path, dept_slug)
            rel_path = f"{container_key}/{dept_slug}"
            name = format_dept_name(dept_slug)

            # Discover tiers
            tiers = []
            for t_dir in sorted(os.listdir(dept_path)):
                tp = os.path.join(dept_path, t_dir)
                if os.path.isdir(tp) and t_dir.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_')):
                    tier_code = t_dir[:2]
                    tier_label = TIER_NAMES.get(tier_code, t_dir[3:].replace('_', ' '))
                    tiers.append({
                        "code": tier_code,
                        "dir": t_dir,
                        "label": tier_label,
                        "path": f"{rel_path}/{t_dir}"
                    })

            # Generate search tokens
            tokens = set()
            tokens.update(dept_slug.lower().split('_'))
            tokens.update(normalize_text(name).split())
            tokens.add(container_key.lower())
            tokens.add(normalize_text(CONTAINER_TITLES[container_key]))

            entry = {
                "slug": dept_slug,
                "name": name,
                "container": container_key,
                "container_title": CONTAINER_TITLES.get(container_key, container_key),
                "path": rel_path,
                "tier_count": len(tiers),
                "tiers": tiers,
                "tokens": sorted(list(tokens))
            }
            index_data.append(entry)

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    return index_data

def load_index() -> list:
    if os.path.exists(INDEX_PATH):
        try:
            with open(INDEX_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return build_index()

def search_curriculum(query: str, container_filter: str = None, limit: int = 20) -> list:
    """Sorgu ile disiplinleri arar."""
    index = load_index()
    norm_query = normalize_text(query).strip()
    words = norm_query.split()

    results = []
    for item in index:
        if container_filter and item['container'] != container_filter:
            continue

        item_str = normalize_text(f"{item['name']} {item['slug']} {item['container_title']}")
        # Score calculation
        score = 0
        if norm_query in item_str:
            score += 10
        for w in words:
            if w in item_str:
                score += 3
            if any(w in t for t in item['tokens']):
                score += 2

        if score > 0:
            results.append((score, item))

    results.sort(key=lambda x: x[0], reverse=True)
    return [r[1] for r in results[:limit]]

def print_results(results: list, query: str):
    print("=" * 70)
    print(f" 🔍 ARAMA SONUÇLARI: '{query}' ({len(results)} Eşleşme)")
    print("=" * 70)

    if not results:
        print("  Belirtilen kriterlere uygun akademik disiplin bulunamadı.")
        print("  İpucu: 'bilgisayar', 'felsefe', 'mimarlık', 'kuantum', 'yapay zeka' gibi anahtar kelimeler deneyin.")
        print("=" * 70)
        return

    for idx, item in enumerate(results, 1):
        print(f"\n[{idx}] 🎓 {item['name']}")
        print(f"    Konteyner: {item['container_title']}")
        print(f"    Konum    : ./{item['path']}/")
        print(f"    Kademeler: {item['tier_count']} Standart Kademe (00-06)")
        print(f"    Dizin    : https://github.com/bahattinyunus/university-courses/tree/main/{item['path']}")
    print("\n" + "=" * 70)

def interactive_mode():
    print("=" * 70)
    print(" 🌌 UAOS INTERAKTIF MÜFREDAT VE DİSİPLİN ARAMA TERMINALI")
    print(" Çıkmak için 'q' veya 'exit' yazın.")
    print("=" * 70)
    
    while True:
        try:
            query = input("\n🔎 Aramak istediğiniz kavram veya alan: ").strip()
            if query.lower() in ('q', 'exit', 'quit'):
                print("Görüşmek üzere!")
                break
            if not query:
                continue
            results = search_curriculum(query)
            print_results(results, query)
        except (KeyboardInterrupt, EOFError):
            print("\nÇıkış yapıldı.")
            break

def main():
    parser = argparse.ArgumentParser(description="UAOS Curriculum Search and Navigation Tool")
    parser.add_argument("query", nargs="?", default="", help="Arama sorgusu")
    parser.add_argument("--container", "-c", help="Konteyner filtresi (örn: meta_muhendislik, saglik)")
    parser.add_argument("--build-index", action="store_true", help="Arama indeksini (curriculum_index.json) yeniden oluştur")
    parser.add_argument("--interactive", "-i", action="store_true", help="İnteraktif terminal arama modunu başlat")
    parser.add_argument("--limit", "-l", type=int, default=15, help="Maksimum sonuç sayısı")
    parser.add_argument("--json", action="store_true", help="Sonuçları JSON formatında çıktı ver")

    args = parser.parse_args()

    if args.build_index:
        index = build_index()
        print(f"[SUCCESS] Search index built with {len(index)} departments at {INDEX_PATH}")
        return

    if args.interactive or (not args.query and not args.build_index):
        interactive_mode()
        return

    results = search_curriculum(args.query, container_filter=args.container, limit=args.limit)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print_results(results, args.query)

if __name__ == "__main__":
    main()
