#!/usr/bin/env python3
"""
Simplified script to update SPIN website pages with modern Tailwind CSS theme
"""

import os
import shutil
from pathlib import Path

# Define the paths
pages_dir = Path("/Users/nagarajm/Work/OS/SPIN/SPIN-Website/pages")

# Read the modern header and footer from the updated login page
with open(pages_dir / "login.html", 'r', encoding='utf-8') as f:
    login_content = f.read()

# Extract header (from <!DOCTYPE to </header>)
header_start = login_content.find('<!DOCTYPE html>')
header_end = login_content.find('</header>') + len('</header>')
modern_header = login_content[header_start:header_end]

# Extract footer (from <!-- Footer --> to </html>)
footer_start = login_content.find('    <!-- Footer -->')
footer_end = login_content.find('</html>') + len('</html>')
modern_footer = login_content[footer_start:footer_end]

# List of pages to update with simple main content
simple_pages = [
    ('signup.html', 'Sign Up', 'Create your SPIN Academics account'),
    ('membership.html', 'Membership', 'Join our community of pediatric neuroradiology professionals'),
    ('education.html', 'Education', 'Explore our educational programs and resources'),
    ('research.html', 'Research', 'Discover our research initiatives and opportunities'),
    ('cortex-club.html', 'Cortex Club', 'Interactive case discussions and learning'),
    ('society-fellowship.html', 'Society Fellowship', 'Comprehensive fellowship program'),
    ('case-of-the-month.html', 'Case of the Month', 'Monthly case studies and discussions'),
    ('green-radiology.html', 'Green Radiology', 'Sustainable radiology practices'),
    ('submit-proposal.html', 'Submit Proposal', 'Submit your research proposals'),
    ('spin-yarn-newsletter.html', 'SPIN Yarn Newsletter', 'Stay updated with our newsletter'),
    ('spin-wfpi.html', 'SPIN-WFPI', 'World Federation partnership'),
    ('spin-reporting-room.html', 'SPIN Reporting Room', 'Advanced reporting resources'),
    ('spin-in-person.html', 'SPIN In Person', 'In-person events and meetings'),
    ('fellowship-part1.html', 'Fellowship Part I', 'Fellowship program requirements'),
    ('fellowship-part2.html', 'Fellowship Part II', 'Advanced fellowship training'),
]

def create_basic_main_content(title, description, page_name):
    """Create basic main content for a page"""
    return f'''    <!-- Main Content -->
    <main class="pt-20 bg-gray-50">
        <!-- Hero Section -->
        <section class="relative bg-gradient-to-br from-primary-600 via-primary-700 to-secondary-600 py-20 overflow-hidden">
            <div class="absolute inset-0 bg-black/20"></div>
            <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <h1 class="text-4xl md:text-6xl font-bold text-white mb-6 animate-fade-in">
                    {title}
                </h1>
                <p class="text-xl md:text-2xl text-blue-100 max-w-3xl mx-auto animate-slide-in">
                    {description}
                </p>
            </div>
        </section>

        <!-- Content Section -->
        <section class="py-20">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="bg-white rounded-2xl shadow-lg p-8 mb-12">
                    <div class="text-center">
                        <div class="w-24 h-24 bg-gradient-to-br from-primary-500 to-secondary-500 rounded-full mx-auto mb-6 flex items-center justify-center">
                            <svg class="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9.5a2.5 2.5 0 00-2.5-2.5H15"></path>
                            </svg>
                        </div>
                        <h2 class="text-3xl font-bold gradient-text mb-6">Coming Soon</h2>
                        <p class="text-gray-600 text-lg mb-8 max-w-2xl mx-auto">
                            We're working hard to bring you the best content for this section. Please check back soon for updates.
                        </p>
                        <div class="flex flex-col sm:flex-row gap-4 justify-center">
                            <a href="../index.html" class="px-8 py-3 bg-gradient-to-r from-primary-500 to-secondary-500 text-white rounded-full font-medium hover:from-primary-600 hover:to-secondary-600 transition-all duration-200 shadow-lg hover:shadow-xl">
                                Back to Home
                            </a>
                            <a href="membership.html" class="px-8 py-3 border-2 border-primary-500 text-primary-600 rounded-full font-medium hover:bg-primary-50 transition-all duration-200">
                                Join SPIN
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Features Grid -->
                <div class="grid md:grid-cols-3 gap-8">
                    <div class="bg-white rounded-xl p-6 shadow-lg card-hover">
                        <div class="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mb-4">
                            <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
                            </svg>
                        </div>
                        <h3 class="text-xl font-semibold text-gray-900 mb-2">Educational Excellence</h3>
                        <p class="text-gray-600">Access to world-class educational resources and programs.</p>
                    </div>
                    <div class="bg-white rounded-xl p-6 shadow-lg card-hover">
                        <div class="w-12 h-12 bg-secondary-100 rounded-lg flex items-center justify-center mb-4">
                            <svg class="w-6 h-6 text-secondary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
                            </svg>
                        </div>
                        <h3 class="text-xl font-semibold text-gray-900 mb-2">Global Community</h3>
                        <p class="text-gray-600">Connect with professionals worldwide in pediatric neuroradiology.</p>
                    </div>
                    <div class="bg-white rounded-xl p-6 shadow-lg card-hover">
                        <div class="w-12 h-12 bg-accent-100 rounded-lg flex items-center justify-center mb-4">
                            <svg class="w-6 h-6 text-accent-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"></path>
                            </svg>
                        </div>
                        <h3 class="text-xl font-semibold text-gray-900 mb-2">Professional Development</h3>
                        <p class="text-gray-600">Advance your career with our fellowship and certification programs.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>'''

def update_page(page_name, title, description):
    """Update a page with modern theme"""
    page_path = pages_dir / page_name
    
    if not page_path.exists():
        print(f"⚠️  Page not found: {page_name}")
        return False
    
    try:
        # Create backup
        backup_path = page_path.with_suffix('.html.backup')
        shutil.copy2(page_path, backup_path)
        
        # Update title in header for this specific page
        page_header = modern_header.replace('Login - SPIN Academics', f'{title} - SPIN Academics')
        
        # Create main content
        main_content = create_basic_main_content(title, description, page_name)
        
        # Combine header + main + footer
        new_content = page_header + '\\n\\n' + main_content + '\\n\\n' + modern_footer
        
        # Write the updated file
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Updated {page_name}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {page_name}: {e}")
        return False

# Update all simple pages
print("🚀 Starting to update pages with modern Tailwind CSS theme...")
print("=" * 60)

updated_count = 0
for page_name, title, description in simple_pages:
    if update_page(page_name, title, description):
        updated_count += 1

print("=" * 60)
print(f"🎉 Updated {updated_count} out of {len(simple_pages)} pages")
print("✨ All pages now have modern Tailwind CSS theme with consistent navigation!")
print("📝 Note: Content for each page has been set to 'Coming Soon' - ready for custom content")
