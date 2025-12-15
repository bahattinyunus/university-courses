import os

def generate_summary(root_dir):
    summary_md = "# 🗂️ Otomatik Ders Dokümantasyon İndeksi\n\n"
    summary_md += "Bu dosya `scripts/generate_summary.py` tarafından otomatik oluşturulmuştur.\n\n"
    
    summary_md += "| Kategori | Ders / Konu | Yol |\n"
    summary_md += "|----------|-------------|-----|\n"

    for root, dirs, files in os.walk(root_dir):
        # Skip hidden and non-content dirs
        if '.git' in root or 'assets' in root or 'scripts' in root or 'templates' in root:
            continue
            
        rel_path = os.path.relpath(root, root_dir)
        path_parts = rel_path.split(os.sep)
        
        if len(path_parts) >= 2:
            category = path_parts[0].replace('_', ' ').title()
            course_name = path_parts[-1].replace('_', ' ').title()
            link = f"[{path_parts[-1]}]({rel_path.replace(os.sep, '/')})"
            
            # Only add if it looks like a course folder (not a parent category folder if possible check)
            # Simple heuristic: if it has files or is deep enough
            if 'mühendislik' in category.lower() and len(path_parts) > 2:
                 summary_md += f"| {category} | {course_name} | {link} |\n"
            elif 'hukuk' in category.lower() or 'vizyon' in category.lower():
                 summary_md += f"| {category} | {course_name} | {link} |\n"

    with open(os.path.join(root_dir, 'SUMMARY.md'), 'w', encoding='utf-8') as f:
        f.write(summary_md)
    print("SUMMARY.md generated successfully.")

if __name__ == "__main__":
    # Run from root
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    generate_summary(root)
