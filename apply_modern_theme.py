#!/usr/bin/env python3
"""
Apply modern Tailwind CSS theme to all SPIN Academics pages
"""

import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path("/Users/nagarajm/Work/OS/SPIN/SPIN-Website")
PAGES_DIR = BASE_DIR / "pages"

# Modern navigation HTML
MODERN_NAV = '''    <!-- Navigation -->
    <nav class="fixed top-0 w-full z-50 bg-white/80 backdrop-blur-md border-b border-gray-200/50 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <!-- Logo -->
                <div class="flex items-center space-x-3">
                    <img src="../images/spin_logo.webp" alt="SPIN Academics Logo" class="h-10 w-10 rounded-full shadow-sm">
                    <div class="hidden sm:block">
                        <h1 class="text-xl font-bold gradient-text">SPIN Academics</h1>
                        <p class="text-xs text-gray-600">Pediatric Neuroradiology Society</p>
                    </div>
                </div>

                <!-- Desktop Navigation -->
                <div class="hidden lg:flex items-center space-x-1">
                    <a href="../index.html" class="px-4 py-2 text-sm font-medium text-gray-700 hover:text-primary-600 rounded-lg nav-item">Home</a>
                    
                    <!-- About Dropdown -->
                    <div class="relative group">
                        <button class="px-4 py-2 text-sm font-medium text-gray-700 hover:text-primary-600 rounded-lg nav-item flex items-center space-x-1">
                            <span>About</span>
                            <svg class="w-4 h-4 transition-transform group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div class="absolute top-full left-0 mt-1 w-64 bg-white rounded-xl shadow-lg border border-gray-200 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 transform group-hover:translate-y-0 translate-y-2">
                            <div class="p-2">
                                <a href="about.html#presidents-welcome" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">President's Welcome</a>
                                <a href="about.html#founding-members" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">Founding Members</a>
                                <a href="about.html#executive-committee" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">Executive Committee</a>
                                <a href="about.html#scientific-committee" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">Scientific Committee</a>
                                <a href="about.html#research-admin-team" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">Research & Admin Team</a>
                                <a href="about.html#rising-stars" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">Rising Stars</a>
                            </div>
                        </div>
                    </div>

                    <a href="membership.html" class="px-4 py-2 text-sm font-medium text-gray-700 hover:text-primary-600 rounded-lg nav-item">Membership</a>
                    
                    <!-- Education Dropdown -->
                    <div class="relative group">
                        <button class="px-4 py-2 text-sm font-medium text-gray-700 hover:text-primary-600 rounded-lg nav-item flex items-center space-x-1">
                            <span>Education</span>
                            <svg class="w-4 h-4 transition-transform group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div class="absolute top-full left-0 mt-1 w-64 bg-white rounded-xl shadow-lg border border-gray-200 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 transform group-hover:translate-y-0 translate-y-2">
                            <div class="p-2">
                                <a href="society-fellowship.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">Society Fellowship</a>
                                <a href="education.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">Education Offerings</a>
                                <a href="cortex-club.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">Cortex Club</a>
                                <a href="spin-yarn-newsletter.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">SPIN Yarn Newsletter</a>
                                <a href="spin-wfpi.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">SPIN-WFPI</a>
                                <a href="spin-reporting-room.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">SPIN Reporting Room</a>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Research Dropdown -->
                    <div class="relative group">
                        <button class="px-4 py-2 text-sm font-medium text-gray-700 hover:text-primary-600 rounded-lg nav-item flex items-center space-x-1">
                            <span>Research</span>
                            <svg class="w-4 h-4 transition-transform group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div class="absolute top-full left-0 mt-1 w-64 bg-white rounded-xl shadow-lg border border-gray-200 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 transform group-hover:translate-y-0 translate-y-2">
                            <div class="p-2">
                                <a href="case-of-the-month.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">Case of the Month</a>
                                <a href="submit-proposal.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">Submit a Proposal</a>
                                <a href="green-radiology.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 rounded-lg">Green Radiology</a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- CTA Button -->
                <div class="hidden lg:flex items-center space-x-3">
                    <a href="login.html" class="text-sm font-medium text-gray-700 hover:text-primary-600">Login</a>
                    <a href="membership.html" class="join-btn text-white px-6 py-3 rounded-xl text-sm font-semibold transition-all">Join SPIN</a>
                </div>

                <!-- Mobile Menu Button -->
                <button id="mobile-menu-btn" class="lg:hidden p-2 rounded-lg hover:bg-gray-100">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
        </div>

        <!-- Mobile Menu -->
        <div id="mobile-menu" class="lg:hidden hidden border-t border-gray-200 bg-white">
            <div class="px-4 py-3 space-y-2">
                <a href="../index.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 rounded-lg">Home</a>
                <a href="about.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 rounded-lg">About</a>
                <a href="membership.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 rounded-lg">Membership</a>
                <a href="education.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 rounded-lg">Education</a>
                <a href="research.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 rounded-lg">Research</a>
                <div class="pt-2 border-t border-gray-200">
                    <a href="login.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 rounded-lg">Login</a>
                    <a href="membership.html" class="block px-4 py-2 text-sm font-medium text-white join-btn rounded-lg">Join SPIN</a>
                </div>
            </div>
        </div>
    </nav>'''

# Modern footer HTML
MODERN_FOOTER = '''    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-4 gap-8">
                <!-- Logo and Description -->
                <div class="md:col-span-2">
                    <div class="flex items-center space-x-3 mb-4">
                        <img src="../images/spin_logo.webp" alt="SPIN Academics" class="h-10 w-10 rounded-full">
                        <div>
                            <h3 class="text-xl font-bold">SPIN Academics</h3>
                            <p class="text-gray-400 text-sm">Pediatric Neuroradiology Society</p>
                        </div>
                    </div>
                    <p class="text-gray-400 mb-6 max-w-md">Society for Pediatric and Investigative Neuroradiology - Advancing education, research, and collaboration in pediatric neuroimaging worldwide.</p>
                    <div class="flex space-x-4">
                        <a href="#" class="text-gray-400 hover:text-white transition-colors">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
                            </svg>
                        </a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                            </svg>
                        </a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors">
                            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/>
                            </svg>
                        </a>
                    </div>
                </div>

                <!-- Quick Links -->
                <div>
                    <h4 class="text-lg font-semibold mb-4">Quick Links</h4>
                    <ul class="space-y-2">
                        <li><a href="about.html" class="text-gray-400 hover:text-white transition-colors">About</a></li>
                        <li><a href="membership.html" class="text-gray-400 hover:text-white transition-colors">Membership</a></li>
                        <li><a href="education.html" class="text-gray-400 hover:text-white transition-colors">Education</a></li>
                        <li><a href="research.html" class="text-gray-400 hover:text-white transition-colors">Research</a></li>
                    </ul>
                </div>

                <!-- Programs -->
                <div>
                    <h4 class="text-lg font-semibold mb-4">Programs</h4>
                    <ul class="space-y-2">
                        <li><a href="society-fellowship.html" class="text-gray-400 hover:text-white transition-colors">Fellowship</a></li>
                        <li><a href="cortex-club.html" class="text-gray-400 hover:text-white transition-colors">Cortex Club</a></li>
                        <li><a href="spin-yarn-newsletter.html" class="text-gray-400 hover:text-white transition-colors">Newsletter</a></li>
                        <li><a href="green-radiology.html" class="text-gray-400 hover:text-white transition-colors">Green Radiology</a></li>
                    </ul>
                </div>
            </div>

            <div class="border-t border-gray-800 mt-12 pt-8">
                <div class="flex flex-col md:flex-row justify-between items-center">
                    <p class="text-gray-400">&copy; 2025 SPIN Academics. All rights reserved.</p>
                    <div class="flex space-x-6 mt-4 md:mt-0">
                        <a href="#" class="text-gray-400 hover:text-white transition-colors text-sm">Privacy Policy</a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors text-sm">Terms of Service</a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors text-sm">Contact</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>'''

# Modern head section
MODERN_HEAD = '''<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - SPIN Academics</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        primary: {{
                            50: '#e6f3ff',
                            100: '#cce7ff',
                            200: '#99cfff',
                            300: '#66b7ff',
                            400: '#339fff',
                            500: '#0087ff',
                            600: '#006bcc',
                            700: '#004f99',
                            800: '#003366',
                            900: '#001733',
                            950: '#000d1a'
                        }},
                        secondary: {{
                            50: '#e6f9f7',
                            100: '#ccf2ef',
                            200: '#99e6df',
                            300: '#66d9cf',
                            400: '#33ccbf',
                            500: '#00bfaf',
                            600: '#00998c',
                            700: '#007369',
                            800: '#004d46',
                            900: '#002623',
                            950: '#001311'
                        }},
                        accent: {{
                            50: '#f8fafc',
                            100: '#f1f5f9',
                            200: '#e2e8f0',
                            300: '#cbd5e1',
                            400: '#94a3b8',
                            500: '#64748b',
                            600: '#475569',
                            700: '#334155',
                            800: '#1e293b',
                            900: '#0f172a',
                            950: '#020617'
                        }}
                    }},
                    fontFamily: {{
                        'sans': ['Poppins', 'system-ui', 'sans-serif'],
                    }},
                    animation: {{
                        'fade-in': 'fadeIn 0.5s ease-in-out',
                        'slide-in': 'slideIn 0.6s ease-out',
                        'float': 'float 6s ease-in-out infinite',
                        'pulse-slow': 'pulse 3s ease-in-out infinite',
                    }},
                    keyframes: {{
                        fadeIn: {{
                            '0%': {{ opacity: '0', transform: 'translateY(10px)' }},
                            '100%': {{ opacity: '1', transform: 'translateY(0)' }},
                        }},
                        slideIn: {{
                            '0%': {{ opacity: '0', transform: 'translateX(-10px)' }},
                            '100%': {{ opacity: '1', transform: 'translateX(0)' }},
                        }},
                        float: {{
                            '0%, 100%': {{ transform: 'translateY(0px)' }},
                            '50%': {{ transform: 'translateY(-10px)' }},
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .gradient-bg {{
            background: linear-gradient(135deg, #0087ff 0%, #00bfaf 100%);
        }}
        .gradient-text {{
            background: linear-gradient(135deg, #0087ff, #00bfaf);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .glass-effect {{
            background: rgba(0, 135, 255, 0.1);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 135, 255, 0.2);
        }}
        .hero-glass {{
            background: rgba(0, 135, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(0, 135, 255, 0.1);
        }}
        .hero-pattern {{
            background-image: radial-gradient(circle at 1px 1px, rgba(0, 135, 255, 0.1) 1px, transparent 0);
            background-size: 30px 30px;
        }}
        .nav-active {{
            position: relative;
        }}
        .nav-active::after {{
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #0087ff, #00bfaf);
            border-radius: 2px;
        }}
        .nav-item {{
            position: relative;
        }}
        .nav-item::after {{
            content: '';
            position: absolute;
            bottom: -2px;
            left: 50%;
            transform: translateX(-50%);
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, #0087ff, #00bfaf);
            border-radius: 2px;
            transition: width 0.3s ease;
        }}
        .nav-item:hover::after {{
            width: 80%;
        }}
        .join-btn {{
            background: linear-gradient(135deg, #0087ff 0%, #00bfaf 100%);
            box-shadow: 0 4px 15px rgba(0, 135, 255, 0.3);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }}
        .join-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 135, 255, 0.4);
            background: linear-gradient(135deg, #006bcc 0%, #00998c 100%);
        }}
        .dropdown-item {{
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}
        .dropdown-item::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(0, 135, 255, 0.1), transparent);
            transition: left 0.6s ease;
        }}
        .dropdown-item:hover::before {{
            left: 100%;
        }}
        .dropdown-item:hover {{
            background: linear-gradient(135deg, rgba(0, 135, 255, 0.08), rgba(0, 191, 175, 0.08));
            transform: translateX(8px);
            border-left: 3px solid;
            border-image: linear-gradient(135deg, #0087ff, #00bfaf) 1;
        }}
        .card-hover {{
            transition: all 0.3s ease;
        }}
        .card-hover:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }}
    </style>
</head>'''

MODERN_SCRIPT = '''    <script>
        // Mobile menu toggle
        document.getElementById('mobile-menu-btn').addEventListener('click', function() {
            const mobileMenu = document.getElementById('mobile-menu');
            mobileMenu.classList.toggle('hidden');
        });

        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            });
        });
    </script>'''

def update_page(filepath, page_name):
    """Update a single page with modern theme"""
    print(f"Updating {page_name}...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title from existing content
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).replace(' - SPIN Academics', '')
        else:
            title = page_name.replace('.html', '').replace('-', ' ').title()
        
        # Extract main content (everything between nav and footer)
        # Look for the main content section
        main_content_pattern = r'(<main.*?</main>|<div[^>]*class[^>]*container.*?</div>|<section.*?</section>)'
        main_content = re.search(main_content_pattern, content, re.DOTALL | re.IGNORECASE)
        
        if not main_content:
            # If no main content found, extract body content
            body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
            if body_match:
                body_content = body_match.group(1)
                # Remove existing nav and footer
                body_content = re.sub(r'<nav.*?</nav>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
                body_content = re.sub(r'<footer.*?</footer>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
                body_content = re.sub(r'<script.*?</script>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
                main_content_text = f'<main class="pt-16">{body_content.strip()}</main>'
            else:
                main_content_text = f'''<main class="pt-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <h1 class="text-4xl font-bold text-gray-900 mb-8">{title}</h1>
        <p class="text-gray-600">Content coming soon...</p>
    </div>
</main>'''
        else:
            main_content_text = main_content.group(0)
            # Ensure main has proper classes
            if not 'pt-16' in main_content_text:
                main_content_text = re.sub(r'<main([^>]*)>', r'<main\1 class="pt-16">', main_content_text)
        
        # Create the new page
        new_content = f'''<!DOCTYPE html>
<html lang="en">
{MODERN_HEAD.format(title=title)}
<body class="font-sans bg-gray-50">
{MODERN_NAV}

{main_content_text}

{MODERN_FOOTER}

{MODERN_SCRIPT}
</body>
</html>'''
        
        # Write the updated content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ {page_name} updated successfully")
        
    except Exception as e:
        print(f"❌ Error updating {page_name}: {str(e)}")

def main():
    """Update all pages with modern theme"""
    print("🚀 Starting modern theme application to all pages...")
    
    # Get all HTML files in pages directory
    html_files = list(PAGES_DIR.glob("*.html"))
    
    print(f"Found {len(html_files)} pages to update:")
    for file in html_files:
        print(f"  - {file.name}")
    
    print("\n" + "="*50)
    
    # Update each page
    for html_file in html_files:
        update_page(html_file, html_file.name)
    
    print("\n" + "="*50)
    print(f"🎉 Successfully updated {len(html_files)} pages with modern theme!")
    print("\nFeatures applied:")
    print("✅ Modern Tailwind CSS theme")
    print("✅ Poppins font")
    print("✅ Glassmorphism effects")
    print("✅ Animated navigation with gradient lines")
    print("✅ Enhanced dropdown menus")
    print("✅ Gradient Join SPIN button")
    print("✅ Professional footer")
    print("✅ Mobile responsive design")

if __name__ == "__main__":
    main()
