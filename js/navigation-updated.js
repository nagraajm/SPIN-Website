// Common Navigation Component for SPIN Academics Website
// This component provides consistent navigation across all pages

function createNavigation(currentPage = '') {
    return `
    <!-- Header -->
    <header class="bg-white/95 backdrop-blur-md shadow-sm fixed w-full top-0 z-50 border-b border-gray-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <!-- Logo -->
                <div class="flex items-center space-x-3">
                    <img src="../images/spin_logo.webp" alt="SPIN Academics" class="h-12 w-12 rounded-full ring-2 ring-primary-200">
                    <div>
                        <h1 class="text-xl font-bold gradient-text">SPIN Academics</h1>
                        <p class="text-xs text-gray-500">Pediatric Neuroradiology</p>
                    </div>
                </div>

                <!-- Desktop Navigation -->
                <nav class="hidden lg:flex items-center space-x-8">
                    <a href="../index.html" class="nav-item text-gray-700 hover:text-primary-600 font-medium transition-colors duration-200 ${currentPage === 'home' ? 'nav-active text-primary-600' : ''}">Home</a>
                    
                    <!-- About Dropdown -->
                    <div class="nav-item group relative">
                        <button class="text-gray-700 hover:text-primary-600 font-medium transition-colors duration-200 flex items-center space-x-1 ${currentPage === 'about' ? 'nav-active text-primary-600' : ''}">
                            <span>About</span>
                            <svg class="w-4 h-4 transition-transform group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div class="absolute left-0 mt-2 w-64 bg-white/95 backdrop-blur-md rounded-2xl shadow-xl border border-gray-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 transform translate-y-2 group-hover:translate-y-0">
                            <div class="py-3">
                                <a href="about.html#presidents-welcome" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200">President's Welcome</a>
                                <a href="about.html#founding-members" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200">Founding Members</a>
                                <a href="about.html#executive-committee" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200">Executive Committee</a>
                                <a href="about.html#scientific-committee" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200">Scientific Committee</a>
                                <a href="about.html#research-admin-team" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200">Research & Admin Team</a>
                                <a href="about.html#rising-stars" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200">Rising Stars</a>
                            </div>
                        </div>
                    </div>

                    <a href="membership.html" class="nav-item text-gray-700 hover:text-primary-600 font-medium transition-colors duration-200 ${currentPage === 'membership' ? 'nav-active text-primary-600' : ''}">Membership</a>
                    
                    <!-- Education Dropdown -->
                    <div class="nav-item group relative">
                        <button class="text-gray-700 hover:text-primary-600 font-medium transition-colors duration-200 flex items-center space-x-1 ${currentPage === 'education' || currentPage === 'society-fellowship' || currentPage === 'cortex-club' || currentPage === 'spin-yarn-newsletter' || currentPage === 'spin-wfpi' || currentPage === 'spin-reporting-room' ? 'nav-active text-primary-600' : ''}">
                            <span>Education</span>
                            <svg class="w-4 h-4 transition-transform group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div class="absolute left-0 mt-2 w-64 bg-white/95 backdrop-blur-md rounded-2xl shadow-xl border border-gray-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 transform translate-y-2 group-hover:translate-y-0">
                            <div class="py-3">
                                <a href="society-fellowship.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200 ${currentPage === 'society-fellowship' ? 'text-primary-600 bg-primary-50' : ''}">Society Fellowship</a>
                                <a href="education.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200 ${currentPage === 'education' ? 'text-primary-600 bg-primary-50' : ''}">Education Offerings</a>
                                <a href="cortex-club.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200 ${currentPage === 'cortex-club' ? 'text-primary-600 bg-primary-50' : ''}">Cortex Club</a>
                                <a href="spin-yarn-newsletter.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200 ${currentPage === 'spin-yarn-newsletter' ? 'text-primary-600 bg-primary-50' : ''}">SPIN Yarn Newsletter</a>
                                <a href="spin-wfpi.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200 ${currentPage === 'spin-wfpi' ? 'text-primary-600 bg-primary-50' : ''}">SPIN-WFPI</a>
                                <a href="spin-reporting-room.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200 ${currentPage === 'spin-reporting-room' ? 'text-primary-600 bg-primary-50' : ''}">SPIN Reporting Room</a>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Research Dropdown -->
                    <div class="nav-item group relative">
                        <button class="text-gray-700 hover:text-primary-600 font-medium transition-colors duration-200 flex items-center space-x-1 ${currentPage === 'research' || currentPage === 'case-of-the-month' || currentPage === 'submit-proposal' || currentPage === 'green-radiology' ? 'nav-active text-primary-600' : ''}">
                            <span>Research</span>
                            <svg class="w-4 h-4 transition-transform group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div class="absolute left-0 mt-2 w-64 bg-white/95 backdrop-blur-md rounded-2xl shadow-xl border border-gray-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 transform translate-y-2 group-hover:translate-y-0">
                            <div class="py-3">
                                <a href="case-of-the-month.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200 ${currentPage === 'case-of-the-month' ? 'text-primary-600 bg-primary-50' : ''}">Case of the Month</a>
                                <a href="submit-proposal.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200 ${currentPage === 'submit-proposal' ? 'text-primary-600 bg-primary-50' : ''}">Submit a Proposal</a>
                                <a href="green-radiology.html" class="dropdown-item block px-4 py-3 text-sm text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-all duration-200 ${currentPage === 'green-radiology' ? 'text-primary-600 bg-primary-50' : ''}">Green Radiology</a>
                            </div>
                        </div>
                    </div>
                    
                    <a href="login.html" class="px-6 py-2 bg-gradient-to-r from-primary-500 to-secondary-500 text-white rounded-full font-medium hover:from-primary-600 hover:to-secondary-600 transition-all duration-200 shadow-lg hover:shadow-xl">Login</a>
                </nav>

                <!-- Mobile menu button -->
                <button id="mobile-menu-btn" class="lg:hidden flex items-center justify-center w-10 h-10 rounded-lg bg-gray-100 hover:bg-gray-200 transition-colors duration-200">
                    <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>

            <!-- Mobile Navigation Menu -->
            <div id="mobile-menu" class="lg:hidden hidden absolute top-full left-0 right-0 bg-white/95 backdrop-blur-md border-t border-gray-100 shadow-lg">
                <div class="py-4 px-4 space-y-2">
                    <a href="../index.html" class="block py-3 px-4 text-gray-700 hover:text-primary-600 hover:bg-primary-50 rounded-lg transition-colors duration-200 ${currentPage === 'home' ? 'text-primary-600 bg-primary-50 font-medium' : ''}">Home</a>
                    <a href="about.html" class="block py-3 px-4 text-gray-700 hover:text-primary-600 hover:bg-primary-50 rounded-lg transition-colors duration-200 ${currentPage === 'about' ? 'text-primary-600 bg-primary-50 font-medium' : ''}">About</a>
                    <a href="membership.html" class="block py-3 px-4 text-gray-700 hover:text-primary-600 hover:bg-primary-50 rounded-lg transition-colors duration-200 ${currentPage === 'membership' ? 'text-primary-600 bg-primary-50 font-medium' : ''}">Membership</a>
                    <a href="education.html" class="block py-3 px-4 text-gray-700 hover:text-primary-600 hover:bg-primary-50 rounded-lg transition-colors duration-200 ${currentPage === 'education' || currentPage === 'society-fellowship' || currentPage === 'cortex-club' || currentPage === 'spin-yarn-newsletter' || currentPage === 'spin-wfpi' || currentPage === 'spin-reporting-room' ? 'text-primary-600 bg-primary-50 font-medium' : ''}">Education</a>
                    <a href="research.html" class="block py-3 px-4 text-gray-700 hover:text-primary-600 hover:bg-primary-50 rounded-lg transition-colors duration-200 ${currentPage === 'research' || currentPage === 'case-of-the-month' || currentPage === 'submit-proposal' || currentPage === 'green-radiology' ? 'text-primary-600 bg-primary-50 font-medium' : ''}">Research</a>
                    <a href="login.html" class="block py-3 px-4 bg-gradient-to-r from-primary-500 to-secondary-500 text-white rounded-lg font-medium text-center">Login</a>
                </div>
            </div>
        </div>
    </header>
    `;
}

// Function to create common HTML head section
function createCommonHead(title, description = "Educational programs and resources from SPIN Academics") {
    return `
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} - SPIN Academics</title>
    <meta name="description" content="${description}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: {
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
                        },
                        secondary: {
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
                        }
                    },
                    fontFamily: {
                        'sans': ['Poppins', 'system-ui', 'sans-serif'],
                    },
                    animation: {
                        'fade-in': 'fadeIn 0.5s ease-in-out',
                        'slide-in': 'slideIn 0.6s ease-out',
                        'float': 'float 6s ease-in-out infinite',
                    },
                    keyframes: {
                        fadeIn: {
                            '0%': { opacity: '0', transform: 'translateY(10px)' },
                            '100%': { opacity: '1', transform: 'translateY(0)' },
                        },
                        slideIn: {
                            '0%': { opacity: '0', transform: 'translateX(-10px)' },
                            '100%': { opacity: '1', transform: 'translateX(0)' },
                        },
                        float: {
                            '0%, 100%': { transform: 'translateY(0px)' },
                            '50%': { transform: 'translateY(-10px)' },
                        }
                    }
                }
            }
        }
    </script>
    <style>
        .gradient-text {
            background: linear-gradient(135deg, #0087ff, #00bfaf);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .glass-effect {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .glass-card:hover {
            background: rgba(255, 255, 255, 0.9);
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 135, 255, 0.1);
        }
        .nav-item {
            position: relative;
        }
        .nav-item:hover::after {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 80%;
            height: 2px;
            background: linear-gradient(90deg, #0087ff, #00bfaf);
            border-radius: 2px;
        }
        .nav-active::after {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 80%;
            height: 2px;
            background: linear-gradient(90deg, #0087ff, #00bfaf);
            border-radius: 2px;
        }
        .dropdown-item {
            position: relative;
            overflow: hidden;
        }
        .dropdown-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(0, 135, 255, 0.2), transparent);
            transition: left 0.5s;
        }
        .dropdown-item:hover::before {
            left: 100%;
        }
        .card-hover {
            transition: all 0.3s ease;
        }
        .card-hover:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 135, 255, 0.1);
        }
    </style>
    `;
}

// Mobile menu toggle functionality
function initializeNavigation() {
    document.addEventListener('DOMContentLoaded', function() {
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        
        if (mobileMenuBtn && mobileMenu) {
            mobileMenuBtn.addEventListener('click', function() {
                mobileMenu.classList.toggle('hidden');
            });
        }
    });
}

// Initialize navigation when the script loads
initializeNavigation();
