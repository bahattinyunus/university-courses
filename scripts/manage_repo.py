import os
from pathlib import Path

def get_repo_stats(root_dir):
    md_count = 0
    pdf_count = 0
    dirs_count = 0
    
    print(f"Analyzing {root_dir}...\n")
    print("--- Directory Structure ---")

    for root, dirs, files in os.walk(root_dir):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        
        dirs_count += len(dirs)
        
        for file in files:
            if file.endswith('.md'):
                md_count += 1
            elif file.endswith('.pdf'):
                pdf_count += 1

    print("\n--- Summary ---")
    print(f"Total Markdown Files: {md_count}")
    print(f"Total PDF Files: {pdf_count}")
    print(f"Total Directories: {dirs_count}")

if __name__ == "__main__":
    # Assumes script is in root/scripts/
    root_path = Path(__file__).parent.parent
    get_repo_stats(str(root_path))
