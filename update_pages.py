#!/usr/bin/env python3
"""
Script to update all HTML pages with consistent favicon and footer
"""

import os
import re
import glob

# Standard favicon link
FAVICON_LINE = '    <link rel="icon" type="image/webp" href="../images/spin_logo.webp">'

# Standard footer HTML
FOOTER_HTML = '''    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-4 gap-8">
                <div class="space-y-4">
                    <div class="flex items-center space-x-3">
                        <img src="../images/spin_logo.webp" alt="SPIN Academics" class="h-10 w-10 rounded-full">
                        <div>
                            <h3 class="text-xl font-bold">SPIN Academics</h3>
                            <p class="text-sm text-gray-400">Pediatric Neuroradiology Society</p>
                        </div>
                    </div>
                    <p class="text-gray-300">Society for Pediatric and Investigative Neuroradiology</p>
                </div>
                <div>
                    <h4 class="text-lg font-semibold mb-4">Quick Links</h4>
                    <ul class="space-y-2">
                        <li><a href="about.html" class="text-gray-300 hover:text-white transition-colors">About</a></li>
                        <li><a href="membership.html" class="text-gray-300 hover:text-white transition-colors">Membership</a></li>
                        <li><a href="education.html" class="text-gray-300 hover:text-white transition-colors">Education</a></li>
                        <li><a href="research.html" class="text-gray-300 hover:text-white transition-colors">Research</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-lg font-semibold mb-4">Education</h4>
                    <ul class="space-y-2">
                        <li><a href="society-fellowship-fixed.html" class="text-gray-300 hover:text-white transition-colors">Fellowship Program</a></li>
                        <li><a href="cortex-club.html" class="text-gray-300 hover:text-white transition-colors">Cortex Club</a></li>
                        <li><a href="spin-yarn-newsletter.html" class="text-gray-300 hover:text-white transition-colors">SPIN A Yarn</a></li>
                        <li><a href="spin-wfpi.html" class="text-gray-300 hover:text-white transition-colors">SPIN WFPI</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-lg font-semibold mb-4">Connect</h4>
                    <div class="flex space-x-4">
                        <a href="#" class="text-gray-300 hover:text-white transition-colors">
                            <span class="sr-only">Email</span>
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                            </svg>
                        </a>
                        <a href="#" class="text-gray-300 hover:text-white transition-colors">
                            <span class="sr-only">Twitter</span>
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"/>
                            </svg>
                        </a>
                        <a href="#" class="text-gray-300 hover:text-white transition-colors">
                            <span class="sr-only">YouTube</span>
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                            </svg>
                        </a>
                    </div>
                </div>
            </div>
            <div class="border-t border-gray-800 mt-12 pt-8">
                <p class="text-center text-gray-400">&copy; 2025 SPIN Academics. All rights reserved.</p>
            </div>
        </div>
    </footer>'''

def update_favicon(file_path, content):
    """Add or update favicon in the head section"""
    # Remove existing favicon lines
    content = re.sub(r'    <link rel="icon"[^>]*>', '', content)
    
    # Find the head section and add favicon after title or meta description
    head_pattern = r'(<title>[^<]*</title>|<meta name="description"[^>]*>)'
    if re.search(head_pattern, content):
        content = re.sub(head_pattern, r'\1\n' + FAVICON_LINE, content, count=1)
    
    return content

def update_footer(file_path, content):
    """Update footer to match the standard format"""
    # Find existing footer and replace it
    footer_pattern = r'    <!-- Footer -->\s*<footer.*?</footer>'
    if re.search(footer_pattern, content, re.DOTALL):
        content = re.sub(footer_pattern, FOOTER_HTML, content, flags=re.DOTALL)
    else:
        # If no footer found, add it before the closing body tag
        content = re.sub(r'</body>', FOOTER_HTML + '\n\n</body>', content)
    
    return content

def process_file(file_path):
    """Process a single HTML file"""
    print(f"Processing {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update favicon
        content = update_favicon(file_path, content)
        
        # Update footer
        content = update_footer(file_path, content)
        
        # Write back the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated {file_path}")
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

def main():
    """Main function to process all HTML files"""
    # Get all HTML files in pages directory
    pages_pattern = "pages/*.html"
    html_files = glob.glob(pages_pattern)
    
    # Skip files that are already updated
    skip_files = ['pages/about.html', 'pages/membership.html']
    
    for file_path in html_files:
        if file_path not in skip_files:
            process_file(file_path)
    
    print("✅ All pages have been updated with consistent favicon and footer!")

if __name__ == "__main__":
    main()
