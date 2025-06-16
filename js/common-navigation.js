// Common Navigation Component for SPIN Academics
// This creates a consistent navigation across all pages

function createNavigation(currentPage = '') {
    const navigationHTML = `
    <!-- Navigation -->
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
                    <a href="../index.html" class="px-4 py-2 text-sm font-medium ${currentPage === 'home' ? 'text-primary-700 border-b-2 border-primary-600' : 'text-gray-700 hover:text-primary-600'} rounded-lg nav-item">Home</a>
                    
                    <!-- About Dropdown -->
                    <div class="relative group">
                        <button class="px-4 py-2 text-sm font-medium ${currentPage === 'about' ? 'text-primary-700 border-b-2 border-primary-600' : 'text-gray-700 hover:text-primary-600'} rounded-lg nav-item flex items-center space-x-1">
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

                    <a href="membership.html" class="px-4 py-2 text-sm font-medium ${currentPage === 'membership' ? 'text-primary-700 border-b-2 border-primary-600' : 'text-gray-700 hover:text-primary-600'} rounded-lg nav-item">Membership</a>
                    
                    <!-- Education Dropdown -->
                    <div class="relative group">
                        <button class="px-4 py-2 text-sm font-medium ${currentPage === 'education' ? 'text-primary-700 border-b-2 border-primary-600' : 'text-gray-700 hover:text-primary-600'} rounded-lg nav-item flex items-center space-x-1">
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
                        <button class="px-4 py-2 text-sm font-medium ${currentPage === 'research' ? 'text-primary-700 border-b-2 border-primary-600' : 'text-gray-700 hover:text-primary-600'} rounded-lg nav-item flex items-center space-x-1">
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
                <a href="../index.html" class="block px-4 py-2 text-sm ${currentPage === 'home' ? 'font-medium text-primary-600 bg-primary-50' : 'text-gray-700 hover:bg-gray-50'} rounded-lg">Home</a>
                <a href="about.html" class="block px-4 py-2 text-sm ${currentPage === 'about' ? 'font-medium text-primary-600 bg-primary-50' : 'text-gray-700 hover:bg-gray-50'} rounded-lg">About</a>
                <a href="membership.html" class="block px-4 py-2 text-sm ${currentPage === 'membership' ? 'font-medium text-primary-600 bg-primary-50' : 'text-gray-700 hover:bg-gray-50'} rounded-lg">Membership</a>
                <a href="education.html" class="block px-4 py-2 text-sm ${currentPage === 'education' ? 'font-medium text-primary-600 bg-primary-50' : 'text-gray-700 hover:bg-gray-50'} rounded-lg">Education</a>
                <a href="research.html" class="block px-4 py-2 text-sm ${currentPage === 'research' ? 'font-medium text-primary-600 bg-primary-50' : 'text-gray-700 hover:bg-gray-50'} rounded-lg">Research</a>
                <div class="pt-2 border-t border-gray-200">
                    <a href="login.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 rounded-lg">Login</a>
                    <a href="membership.html" class="block px-4 py-2 text-sm font-medium text-white join-btn rounded-lg">Join SPIN</a>
                </div>
            </div>
        </div>
    </nav>
    `;
    
    return navigationHTML;
}

// Function to load navigation and set current page
function loadNavigation(currentPage = '') {
    document.addEventListener('DOMContentLoaded', function() {
        // Find the navigation placeholder or create one
        let navContainer = document.getElementById('navigation-container');
        if (!navContainer) {
            navContainer = document.createElement('div');
            navContainer.id = 'navigation-container';
            document.body.insertBefore(navContainer, document.body.firstChild);
        }
        
        // Insert navigation HTML
        navContainer.innerHTML = createNavigation(currentPage);
        
        // Add mobile menu functionality
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        
        if (mobileMenuBtn && mobileMenu) {
            mobileMenuBtn.addEventListener('click', function() {
                mobileMenu.classList.toggle('hidden');
            });
        }
    });
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { createNavigation, loadNavigation };
}
