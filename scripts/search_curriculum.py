#!/usr/bin/env python3
"""
University Courses (UC) - Evrensel Akademik Arama, İnceleme ve Müfredat İndeksleyici
Bu araç 21 konteyner, 374 akademik disiplin, 2618 kademe ve 30 ileri araştırma monografını tarar, arar ve inceler.
"""

import os
import sys
import re
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

            # Discover tiers & research monographs
            tiers = []
            research_papers = []
            tokens = set()
            tokens.update(dept_slug.lower().split('_'))
            tokens.update(normalize_text(name).split())
            tokens.add(container_key.lower())
            tokens.add(normalize_text(CONTAINER_TITLES[container_key]))

            for t_dir in sorted(os.listdir(dept_path)):
                tp = os.path.join(dept_path, t_dir)
                if os.path.isdir(tp) and t_dir.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_')):
                    tier_code = t_dir[:2]
                    tier_label = TIER_NAMES.get(tier_code, t_dir[3:].replace('_', ' '))
                    
                    tier_files = []
                    for tf in sorted(os.listdir(tp)):
                        if tf.endswith('.md') and tf.lower() != 'readme.md':
                            f_path = f"{rel_path}/{t_dir}/{tf}"
                            tier_files.append({"filename": tf, "path": f_path})
                            if tf.startswith('arastirma_'):
                                full_fpath = os.path.join(tp, tf)
                                title = tf.replace('arastirma_', '').replace('.md', '').replace('_', ' ').title()
                                try:
                                    with open(full_fpath, 'r', encoding='utf-8') as rf:
                                        for line in rf:
                                            line_s = line.strip()
                                            if line_s.startswith('# '):
                                                raw_t = re.sub(r'^#\s*[^\w\s]*\s*', '', line_s)
                                                if raw_t:
                                                    title = raw_t
                                                break
                                except Exception:
                                    pass

                                research_papers.append({
                                    "title": title,
                                    "filename": tf,
                                    "path": f_path,
                                    "tier": tier_code
                                })
                                tokens.update(normalize_text(title).split())
                                tokens.update(tf.replace('.md', '').split('_'))
                    
                    tiers.append({
                        "code": tier_code,
                        "dir": t_dir,
                        "label": tier_label,
                        "path": f"{rel_path}/{t_dir}",
                        "files": tier_files
                    })

            entry = {
                "slug": dept_slug,
                "name": name,
                "container": container_key,
                "container_title": CONTAINER_TITLES.get(container_key, container_key),
                "path": rel_path,
                "tier_count": len(tiers),
                "tiers": tiers,
                "research_papers": research_papers,
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

def get_all_research_papers():
    """Tüm depodaki araştırma monograflarını sıralı liste olarak döndürür."""
    index = load_index()
    all_papers = []
    for item in index:
        for rp in item.get("research_papers", []):
            all_papers.append((item, rp))
    # Sort deterministically by container then title
    all_papers.sort(key=lambda x: (x[0]['container'], x[1]['title']))
    return all_papers

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
        if item.get("research_papers"):
            print(f"    🔬 Özgün Araştırma Monografları ({len(item['research_papers'])} Adet):")
            for rp in item["research_papers"]:
                print(f"       • {rp['title']} (./{rp['path']})")
        print(f"    Dizin    : https://github.com/bahattinyunus/university-courses/tree/main/{item['path']}")
    print("\n" + "=" * 70)

def list_all_research_papers():
    """Tüm depodaki ileri seviye araştırma monograflarını listeler."""
    all_papers = get_all_research_papers()
    print("=" * 75)
    print(f" 📚 UAOS İLERİ AKADEMİK VE TEKNOLOJİK ARAŞTIRMA MONOGRAFLARI ({len(all_papers)} Eser)")
    print("=" * 75)
    for idx, (item, rp) in enumerate(all_papers, 1):
        print(f"[{idx:02d}] 📑 {rp['title']}")
        print(f"     Disiplin : {item['name']} ({item['container_title']})")
        print(f"     Dosya    : ./{rp['path']}")
    print("=" * 75)
    print(" 💡 İpucu: Monograf içeriğini doğrudan okumak için: python scripts/search_curriculum.py --read <NO>")
    print("=" * 75)

def print_statistics():
    """Depo genelindeki istatistikleri ve konteyner dağılımını gösterir."""
    index = load_index()
    all_papers = get_all_research_papers()
    
    total_depts = len(index)
    total_tiers = sum(item.get("tier_count", 0) for item in index)
    total_papers = len(all_papers)
    
    container_stats = {}
    for item in index:
        c_key = item['container']
        if c_key not in container_stats:
            container_stats[c_key] = {
                "title": item['container_title'],
                "depts": 0,
                "tiers": 0,
                "papers": 0
            }
        container_stats[c_key]["depts"] += 1
        container_stats[c_key]["tiers"] += item.get("tier_count", 0)
        container_stats[c_key]["papers"] += len(item.get("research_papers", []))

    print("=" * 78)
    print(" 📊 UNIVERSITY COURSES (UAOS) - EVRENSEL DİSİPLİN MATRİS İSTATİSTİKLERİ")
    print("=" * 78)
    print(f"  🏛️ Toplam Konteyner Sayısı         : {len(container_stats)} Tematik Fakülte & Küme")
    print(f"  🎓 Toplam Akademik Disiplin       : {total_depts} Alan")
    print(f"  📦 Toplam Yapılandırılmış Kademe   : {total_tiers} Modüler Kademe (00-06)")
    print(f"  🔬 İleri Araştırma Monografları    : {total_papers} Derin Bilimsel Monograf")
    print("=" * 78)
    print(f" {'#':<3} {'KONTEYNER / FAKÜLTE':<45} {'ALAN':<8} {'MONOGRAF':<9}")
    print("-" * 78)
    for idx, (c_key, s) in enumerate(sorted(container_stats.items(), key=lambda x: x[1]['depts'], reverse=True), 1):
        clean_title = s['title']
        if len(clean_title) > 42:
            clean_title = clean_title[:39] + "..."
        print(f" {idx:<3} {clean_title:<45} {s['depts']:<8} {s['papers']:<9}")
    print("=" * 78)

def print_discipline_tree(query: str):
    """Bir disiplinin kademe ve dosya ağacını ASCII formatında terminale yazdırır."""
    results = search_curriculum(query, limit=1)
    if not results:
        print(f"[!] '{query}' ile eşleşen bir disiplin bulunamadı.")
        return

    item = results[0]
    dept_full_path = os.path.join(ROOT_DIR, item['path'])

    print("=" * 75)
    print(f" 🌳 AKADEMİK DİSİPLİN AĞACI: {item['name']}")
    print(f"    Konteyner: {item['container_title']}")
    print(f"    Konum    : ./{item['path']}/")
    print("=" * 75)
    print(f"└── {item['slug']}/")

    if not os.path.isdir(dept_full_path):
        print("    [!] Dizin bulunamadı.")
        return

    subdirs = sorted([d for d in os.listdir(dept_full_path) if os.path.isdir(os.path.join(dept_full_path, d))])
    for s_idx, s_dir in enumerate(subdirs):
        is_last_s = (s_idx == len(subdirs) - 1)
        s_pref = "    └── " if is_last_s else "    ├── "
        c_pref = "        " if is_last_s else "    │   "
        
        # Check tier label
        t_code = s_dir[:2]
        label = TIER_NAMES.get(t_code, s_dir)
        print(f"{s_pref}{s_dir}/ ({label})")

        subpath = os.path.join(dept_full_path, s_dir)
        files = sorted([f for f in os.listdir(subpath) if os.path.isfile(os.path.join(subpath, f)) and not f.startswith('.')])
        for f_idx, fn in enumerate(files):
            is_last_f = (f_idx == len(files) - 1)
            f_pref = c_pref + ("└── " if is_last_f else "├── ")
            icon = "📑 [MONOGRAF]" if fn.startswith("arastirma_") else "📄"
            print(f"{f_pref}{icon} {fn}")
    print("=" * 75)

def read_research_paper(target: str):
    """Numara veya başlık ile seçilen araştırma monografını terminalde görüntüler."""
    all_papers = get_all_research_papers()
    selected_paper = None
    selected_dept = None

    if target.isdigit():
        num = int(target)
        if 1 <= num <= len(all_papers):
            selected_dept, selected_paper = all_papers[num - 1]
        else:
            print(f"[!] Geçersiz monograf numarası: {num}. Geçerli aralık: 1-{len(all_papers)}")
            return
    else:
        norm_t = normalize_text(target)
        for dept, paper in all_papers:
            if norm_t in normalize_text(paper['title']) or norm_t in normalize_text(paper['filename']):
                selected_dept, selected_paper = dept, paper
                break

    if not selected_paper:
        print(f"[!] '{target}' ile eşleşen bir araştırma monografı bulunamadı.")
        return

    full_path = os.path.join(ROOT_DIR, selected_paper['path'])
    if not os.path.isfile(full_path):
        print(f"[!] Dosya bulunamadı: {full_path}")
        return

    print("\n" + "=" * 80)
    print(f" 📖 MONOGRAF OKUYUCU: {selected_paper['title']}")
    print(f" 🏛️ Disiplin : {selected_dept['name']} ({selected_dept['container_title']})")
    print(f" 📂 Konum    : ./{selected_paper['path']}")
    print("=" * 80 + "\n")

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(content)
        print("\n" + "=" * 80)
        print(" [SON] Monograf sonuna ulaşıldı.")
        print("=" * 80 + "\n")
    except Exception as e:
        print(f"[!] Dosya okunurken hata oluştu: {e}")

def interactive_mode():
    print("=" * 70)
    print(" 🌌 UAOS INTERAKTİF MÜFREDAT VE DİSİPLİN ARAMA TERMİNALİ")
    print(" Komutlar:")
    print("   :stats, :s       - Depo istatistiklerini görüntüle")
    print("   :research, :r    - Tüm 30 araştırma monografını listele")
    print("   :read <NO>       - Belirtilen numaralı monografı oku")
    print("   :tree <disiplin> - Disiplinin kademe ve dosya ağacını göster")
    print("   :quit, :q        - Çıkış yap")
    print("   <arama terimi>   - Disiplin veya kavram ara")
    print("=" * 70)
    
    while True:
        try:
            query = input("\n🔎 Aramak istediğiniz kavram veya komut: ").strip()
            if not query:
                continue
            if query.lower() in (':q', ':quit', 'q', 'exit', 'quit'):
                print("Görüşmek üzere!")
                break
            if query.lower() in (':s', ':stats'):
                print_statistics()
                continue
            if query.lower() in (':r', ':research'):
                list_all_research_papers()
                continue
            if query.startswith((':read ', ':o ')):
                arg = query.split(maxsplit=1)[1]
                read_research_paper(arg)
                continue
            if query.startswith((':tree ', ':t ')):
                arg = query.split(maxsplit=1)[1]
                print_discipline_tree(arg)
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
    parser.add_argument("--research", "-r", action="store_true", help="Tüm ileri araştırma monograflarını listele")
    parser.add_argument("--stats", "-s", action="store_true", help="Depo genelindeki istatistikleri ve dağılımı göster")
    parser.add_argument("--tree", "-t", help="Belirtilen disiplinin ağaç yapısını göster")
    parser.add_argument("--read", "-o", help="Numara veya başlık ile araştırma monografını oku")

    args = parser.parse_args()

    if args.stats:
        print_statistics()
        return

    if args.research:
        list_all_research_papers()
        return

    if args.read:
        read_research_paper(args.read)
        return

    if args.tree:
        print_discipline_tree(args.tree)
        return

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
