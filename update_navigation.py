#!/usr/bin/env python3
"""
Script to update navigation menus across all HTML pages with dropdown menus
"""

import os
import re
from pathlib import Path

# Base navigation template for pages in the 'pages' directory
base_nav_template = '''            <nav class="nav" role="navigation">
                <button class="nav-toggle" aria-label="Toggle navigation">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
                <ul class="nav-menu">
                    <li><a href="../index.html" class="nav-link">Home</a></li>
                    <li class="nav-item dropdown">
                        <a href="about.html" class="nav-link dropdown-toggle{about_active}">About <i class="dropdown-arrow">▼</i></a>
                        <ul class="dropdown-menu">
                            <li><a href="about.html#presidents-welcome" class="dropdown-link">President's Welcome</a></li>
                            <li><a href="about.html#founding-members" class="dropdown-link">Founding Members</a></li>
                            <li><a href="about.html#executive-committee" class="dropdown-link">Executive Committee</a></li>
                            <li><a href="about.html#scientific-committee" class="dropdown-link">Scientific Committee</a></li>
                            <li><a href="about.html#research-admin-team" class="dropdown-link">Research and Admin Team</a></li>
                            <li><a href="about.html#rising-stars" class="dropdown-link">Rising Stars</a></li>
                        </ul>
                    </li>
                    <li><a href="membership.html" class="nav-link{membership_active}">Membership</a></li>
                    <li class="nav-item dropdown">
                        <a href="education.html" class="nav-link dropdown-toggle{education_active}">Education <i class="dropdown-arrow">▼</i></a>
                        <ul class="dropdown-menu">
                            <li><a href="society-fellowship.html" class="dropdown-link">Society Fellowship</a></li>
                            <li><a href="education.html" class="dropdown-link">Education Offerings</a></li>
                            <li><a href="cortex-club.html" class="dropdown-link">Cortex Club</a></li>
                            <li><a href="spin-yarn-newsletter.html" class="dropdown-link">SPIN Yarn Newsletter</a></li>
                            <li><a href="spin-wfpi.html" class="dropdown-link">SPIN-WFPI</a></li>
                            <li><a href="spin-reporting-room.html" class="dropdown-link">SPIN Reporting Room</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a href="research.html" class="nav-link dropdown-toggle{research_active}">Research <i class="dropdown-arrow">▼</i></a>
                        <ul class="dropdown-menu">
                            <li><a href="case-of-the-month.html" class="dropdown-link">Case of the Month Submission</a></li>
                            <li><a href="submit-proposal.html" class="dropdown-link">Submit a Proposal</a></li>
                            <li><a href="green-radiology.html" class="dropdown-link">Green Radiology</a></li>
                        </ul>
                    </li>
                    <li><a href="login.html" class="nav-link login-btn">Login</a></li>
                </ul>
            </nav>'''

# Define which pages belong to which categories
page_categories = {
    'about': ['about.html'],
    'membership': ['membership.html'],
    'education': [
        'education.html', 'society-fellowship.html', 'cortex-club.html', 
        'spin-yarn-newsletter.html', 'spin-wfpi.html', 'spin-reporting-room.html',
        'fellowship-part1.html', 'fellowship-part2.html'
    ],
    'research': [
        'research.html', 'case-of-the-month.html', 'submit-proposal.html', 
        'green-radiology.html'
    ],
    'other': ['login.html', 'signup.html', 'spin-in-person.html']
}

def get_page_category(filename):
    """Determine which category a page belongs to"""
    for category, pages in page_categories.items():
        if filename in pages:
            return category
    return 'other'

def update_navigation(file_path):
    """Update navigation in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        filename = os.path.basename(file_path)
        category = get_page_category(filename)
        
        # Set active states
        about_active = ' active' if category == 'about' else ''
        membership_active = ' active' if category == 'membership' else ''
        education_active = ' active' if category == 'education' else ''
        research_active = ' active' if category == 'research' else ''
        
        # Format the navigation template
        new_nav = base_nav_template.format(
            about_active=about_active,
            membership_active=membership_active,
            education_active=education_active,
            research_active=research_active
        )
        
        # Find and replace the navigation section
        nav_pattern = r'<nav class="nav"[^>]*>.*?</nav>'
        updated_content = re.sub(nav_pattern, new_nav, content, flags=re.DOTALL)
        
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"Updated: {file_path}")
        else:
            print(f"No changes needed: {file_path}")
            
    except Exception as e:
        print(f"Error updating {file_path}: {e}")

def main():
    """Main function to update all pages"""
    pages_dir = Path('pages')
    
    if not pages_dir.exists():
        print("Pages directory not found!")
        return
    
    # Get all HTML files in the pages directory
    html_files = list(pages_dir.glob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to update...")
    
    for html_file in html_files:
        update_navigation(html_file)
    
    print("Navigation update complete!")

if __name__ == "__main__":
    main()
