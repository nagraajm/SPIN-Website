#!/usr/bin/env python3
"""
Script to update all SPIN website pages with modern Tailwind CSS theme
"""

import os
import shutil
from pathlib import Path

# Define the paths
pages_dir = Path("/Users/nagarajm/Work/OS/SPIN/SPIN-Website/pages")
homepage_path = Path("/Users/nagarajm/Work/OS/SPIN/SPIN-Website/index.html")

# Read the modern header template from the homepage
with open(homepage_path, 'r', encoding='utf-8') as f:
    homepage_content = f.read()

# Extract the modern header section (from <!DOCTYPE html> to </header>)
header_start = homepage_content.find('<!DOCTYPE html>')
header_end = homepage_content.find('</header>') + len('</header>')
modern_header = homepage_content[header_start:header_end]

# Extract the footer from the homepage
footer_start = homepage_content.find('    <!-- Footer -->')
footer_end = homepage_content.find('</html>') + len('</html>')
modern_footer = homepage_content[footer_start:footer_end]

# List of pages to update
pages_to_update = [
    'case-of-the-month.html',
    'cortex-club.html', 
    'education.html',
    'fellowship-part1.html',
    'fellowship-part2.html',
    'green-radiology.html',
    'login.html',
    'membership.html',
    'research.html',
    'signup.html',
    'society-fellowship.html',
    'spin-in-person.html',
    'spin-reporting-room.html',
    'spin-wfpi.html',
    'spin-yarn-newsletter.html',
    'submit-proposal.html'
]

def update_page(page_path):
    """Update a single page with modern theme"""
    try:
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create backup
        backup_path = page_path.with_suffix('.html.backup')
        shutil.copy2(page_path, backup_path)
        
        # Extract main content between <main> and </main>
        main_start = content.find('<main')
        main_end = content.find('</main>') + len('</main>')
        
        if main_start == -1 or main_end == -1:
            print(f"Could not find main content in {page_path.name}")
            return False
            
        main_content = content[main_start:main_end]
        
        # Create new content with modern header + main + modern footer
        new_content = modern_header + '\n\n' + main_content + '\n\n' + modern_footer
        
        # Write updated content
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"✅ Updated {page_path.name}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {page_path.name}: {e}")
        return False

# Update all pages
print("🚀 Starting to update all pages with modern theme...")
print("=" * 50)

updated_count = 0
for page_name in pages_to_update:
    page_path = pages_dir / page_name
    if page_path.exists():
        if update_page(page_path):
            updated_count += 1
    else:
        print(f"⚠️  Page not found: {page_name}")

print("=" * 50)
print(f"🎉 Updated {updated_count} out of {len(pages_to_update)} pages")
print("✨ All pages now have modern Tailwind CSS theme!")
