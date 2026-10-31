#!/usr/bin/env python3
"""
Evrensel Akademik İşletim Sistemi (UAOS) - Repository Management Suite
"""
import os
import sys
import argparse
from pathlib import Path

# Safe stdout/stderr encoding for Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Add scripts directory to sys.path
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPTS_DIR)
sys.path.insert(0, SCRIPTS_DIR)

from final_sanity_check import final_sanity_check
from generate_summary import generate_summary
from generate_encyclopedic_readme import generate_encyclopedic_readme
from search_curriculum import build_index, search_curriculum, print_results, interactive_mode, list_all_research_papers

def print_repo_stats():
    md_count = 0
    pdf_count = 0
    dirs_count = 0
    container_count = 0
    dept_count = 0
    tier_count = 0
    
    EXCLUDE = {'.git', '.vs', '.github', 'scripts', 'assets', 'templates'}
    
    for c in sorted(os.listdir(ROOT_DIR)):
        cp = os.path.join(ROOT_DIR, c)
        if os.path.isdir(cp) and c not in EXCLUDE:
            container_count += 1
            depts = [d for d in os.listdir(cp) if os.path.isdir(os.path.join(cp, d))]
            dept_count += len(depts)
            for d in depts:
                dp = os.path.join(cp, d)
                tiers = [t for t in os.listdir(dp) if os.path.isdir(os.path.join(dp, t)) and t.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_'))]
                tier_count += len(tiers)

    for root, dirs, files in os.walk(ROOT_DIR):
        if '.git' in root or '.vs' in root:
            continue
        dirs_count += len(dirs)
        for f in files:
            if f.endswith('.md'):
                md_count += 1
            elif f.endswith('.pdf'):
                pdf_count += 1

    print("==================================================")
    print("      UAOS / UNIVERSITY COURSES REPO STATS        ")
    print("==================================================")
    print(f"Total Containers        : {container_count}")
    print(f"Total Academic Depts    : {dept_count}")
    print(f"Total Standard Tiers    : {tier_count}")
    print(f"Total Markdown Files    : {md_count}")
    print(f"Total PDF Files         : {pdf_count}")
    print(f"Total Directories       : {dirs_count}")
    print("==================================================")

def main():
    parser = argparse.ArgumentParser(description="UAOS Repository Management Suite")
    parser.add_argument("--stats", action="store_true", help="Display repository statistics")
    parser.add_argument("--verify", action="store_true", help="Run repository sanity checks")
    parser.add_argument("--build-readme", action="store_true", help="Generate README.md")
    parser.add_argument("--build-summary", action="store_true", help="Generate SUMMARY.md")
    parser.add_argument("--build-index", action="store_true", help="Generate assets/curriculum_index.json")
    parser.add_argument("--build-all", action="store_true", help="Run verification and regenerate README, SUMMARY, and Search Index")
    parser.add_argument("--search", "-s", type=str, help="Search curriculum for academic departments or topics")
    parser.add_argument("--research", "-r", action="store_true", help="List all advanced academic and technological research monographs")
    parser.add_argument("--interactive", "-i", action="store_true", help="Launch interactive CLI curriculum search navigator")

    args = parser.parse_args()

    if args.research:
        list_all_research_papers()
        return

    if args.interactive:
        interactive_mode()
        return

    if args.search:
        results = search_curriculum(args.search)
        print_results(results, args.search)
        return

    if len(sys.argv) == 1 or args.build_all:
        print("[1/4] Running repository integrity verification...")
        if not final_sanity_check():
            print("[ERROR] Integrity check failed. Aborting build.")
            sys.exit(1)
        print("[2/4] Generating SUMMARY.md...")
        generate_summary()
        print("[3/4] Generating README.md...")
        generate_encyclopedic_readme()
        print("[4/4] Building assets/curriculum_index.json...")
        build_index()
        print_repo_stats()
        print("\n[SUCCESS] Full repository verification and build completed successfully!")
        return

    if args.stats:
        print_repo_stats()
    if args.verify:
        final_sanity_check()
    if args.build_summary:
        generate_summary()
    if args.build_readme:
        generate_encyclopedic_readme()
    if args.build_index:
        build_index()

if __name__ == "__main__":
    main()
