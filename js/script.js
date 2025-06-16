// SPIN Academics JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initMobileMenu();
    initHeroCarousel();
    initAccordion();
    initForms();
    initAnimations();
});

// Mobile Menu Toggle with Dropdown Support
function initMobileMenu() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');
    const dropdowns = document.querySelectorAll('.dropdown');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
            
            // Close all dropdowns when menu toggles
            dropdowns.forEach(dropdown => {
                dropdown.classList.remove('active');
            });
        });

        // Handle dropdown toggles on mobile
        dropdowns.forEach(dropdown => {
            const dropdownToggle = dropdown.querySelector('.dropdown-toggle');
            const dropdownMenu = dropdown.querySelector('.dropdown-menu');
            
            if (dropdownToggle && dropdownMenu) {
                dropdownToggle.addEventListener('click', function(e) {
                    // On mobile, prevent default link behavior and toggle dropdown
                    if (window.innerWidth <= 768) {
                        e.preventDefault();
                        dropdown.classList.toggle('active');
                        
                        // Close other dropdowns
                        dropdowns.forEach(otherDropdown => {
                            if (otherDropdown !== dropdown) {
                                otherDropdown.classList.remove('active');
                            }
                        });
                    }
                });
            }
        });

        // Close menu when clicking on a regular link (not dropdown toggle)
        navLinks.forEach(link => {
            if (!link.classList.contains('dropdown-toggle')) {
                link.addEventListener('click', function() {
                    navToggle.classList.remove('active');
                    navMenu.classList.remove('active');
                });
            }
        });

        // Close dropdown links on mobile
        document.querySelectorAll('.dropdown-link').forEach(link => {
            link.addEventListener('click', function() {
                if (window.innerWidth <= 768) {
                    navToggle.classList.remove('active');
                    navMenu.classList.remove('active');
                    dropdowns.forEach(dropdown => {
                        dropdown.classList.remove('active');
                    });
                }
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navToggle.contains(event.target) || navMenu.contains(event.target);
            
            if (!isClickInsideNav) {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                dropdowns.forEach(dropdown => {
                    dropdown.classList.remove('active');
                });
            }
        });

        // Handle window resize
        window.addEventListener('resize', function() {
            if (window.innerWidth > 768) {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                dropdowns.forEach(dropdown => {
                    dropdown.classList.remove('active');
                });
            }
        });
    }
}

// Hero Carousel
function initHeroCarousel() {
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    if (slides.length === 0) return;

    let currentSlide = 0;
    let autoSlideInterval;

    function showSlide(index) {
        // Remove active class from all slides and dots
        slides.forEach(slide => slide.classList.remove('active'));
        dots.forEach(dot => dot.classList.remove('active'));

        // Add active class to current slide and dot
        if (slides[index]) {
            slides[index].classList.add('active');
        }
        if (dots[index]) {
            dots[index].classList.add('active');
        }

        currentSlide = index;
    }

    function nextSlide() {
        const next = (currentSlide + 1) % slides.length;
        showSlide(next);
    }

    function prevSlide() {
        const prev = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(prev);
    }

    function startAutoSlide() {
        autoSlideInterval = setInterval(nextSlide, 5000); // Change slide every 5 seconds
    }

    function stopAutoSlide() {
        clearInterval(autoSlideInterval);
    }

    // Event listeners for navigation buttons
    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            stopAutoSlide();
            nextSlide();
            startAutoSlide();
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            stopAutoSlide();
            prevSlide();
            startAutoSlide();
        });
    }

    // Event listeners for dots
    dots.forEach((dot, index) => {
        dot.addEventListener('click', function() {
            stopAutoSlide();
            showSlide(index);
            startAutoSlide();
        });
    });

    // Pause auto-slide on hover
    const carouselContainer = document.querySelector('.carousel-container');
    if (carouselContainer) {
        carouselContainer.addEventListener('mouseenter', stopAutoSlide);
        carouselContainer.addEventListener('mouseleave', startAutoSlide);
    }

    // Keyboard navigation
    document.addEventListener('keydown', function(event) {
        if (event.key === 'ArrowLeft') {
            stopAutoSlide();
            prevSlide();
            startAutoSlide();
        } else if (event.key === 'ArrowRight') {
            stopAutoSlide();
            nextSlide();
            startAutoSlide();
        }
    });

    // Touch/swipe support for mobile
    let touchStartX = 0;
    let touchEndX = 0;

    if (carouselContainer) {
        carouselContainer.addEventListener('touchstart', function(event) {
            touchStartX = event.changedTouches[0].screenX;
        });

        carouselContainer.addEventListener('touchend', function(event) {
            touchEndX = event.changedTouches[0].screenX;
            handleSwipe();
        });
    }

    function handleSwipe() {
        const swipeThreshold = 50;
        const swipeDistance = touchEndX - touchStartX;

        if (Math.abs(swipeDistance) > swipeThreshold) {
            stopAutoSlide();
            if (swipeDistance > 0) {
                prevSlide();
            } else {
                nextSlide();
            }
            startAutoSlide();
        }
    }

    // Initialize carousel
    showSlide(0);
    startAutoSlide();
}

// Accordion functionality
function initAccordion() {
    const accordionHeaders = document.querySelectorAll('.accordion-header');

    accordionHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const content = this.nextElementSibling;
            const icon = this.querySelector('.accordion-icon');
            const isActive = this.classList.contains('active');

            // Close all accordion items
            accordionHeaders.forEach(h => {
                h.classList.remove('active');
                h.nextElementSibling.classList.remove('active');
            });

            // If the clicked item wasn't active, open it
            if (!isActive) {
                this.classList.add('active');
                content.classList.add('active');
            }
        });
    });
}

// Form handling
function initForms() {
    // Newsletter form
    const newsletterForm = document.getElementById('newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(event) {
            event.preventDefault();
            handleNewsletterSubmission(this);
        });
    }

    // Proposal form
    const proposalForm = document.getElementById('proposal-form');
    if (proposalForm) {
        proposalForm.addEventListener('submit', function(event) {
            event.preventDefault();
            handleProposalSubmission(this);
        });
    }

    // Contact forms
    const contactForms = document.querySelectorAll('.contact-form');
    contactForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            handleContactFormSubmission(this);
        });
    });

    // Notify me forms
    const notifyForms = document.querySelectorAll('.notify-form');
    notifyForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            handleNotifyFormSubmission(this);
        });
    });

    // Login form
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            handleLoginSubmission(this);
        });
    }

    // Signup form
    const signupForm = document.getElementById('signup-form');
    if (signupForm) {
        signupForm.addEventListener('submit', function(event) {
            event.preventDefault();
            handleSignupSubmission(this);
        });
    }
}

// Newsletter form submission
function handleNewsletterSubmission(form) {
    const email = form.querySelector('input[name="email"]').value;
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;

    // Show loading state
    submitBtn.innerHTML = '<span class="loading"></span> Subscribing...';
    submitBtn.disabled = true;

    // Simulate API call
    setTimeout(() => {
        showSuccessMessage(form, 'Thank you for subscribing to SPIN A Yarn newsletter!');
        form.reset();
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }, 1500);
}

// Proposal form submission
function handleProposalSubmission(form) {
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;

    // Show loading state
    submitBtn.innerHTML = '<span class="loading"></span> Submitting...';
    submitBtn.disabled = true;

    // Simulate API call
    setTimeout(() => {
        showSuccessMessage(form, 'Your proposal has been submitted successfully! We will review it and get back to you soon.');
        form.reset();
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }, 2000);
}

// Contact form submission
function handleContactFormSubmission(form) {
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;

    // Show loading state
    submitBtn.innerHTML = '<span class="loading"></span> Sending...';
    submitBtn.disabled = true;

    // Simulate API call
    setTimeout(() => {
        showSuccessMessage(form, 'Your message has been sent successfully! We will get back to you soon.');
        form.reset();
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }, 1500);
}

// Notify form submission
function handleNotifyFormSubmission(form) {
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;

    // Show loading state
    submitBtn.innerHTML = '<span class="loading"></span> Submitting...';
    submitBtn.disabled = true;

    // Simulate API call
    setTimeout(() => {
        showSuccessMessage(form, 'Thank you! We will notify you when registration opens.');
        form.reset();
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }, 1500);
}

// Login form submission
function handleLoginSubmission(form) {
    const email = form.querySelector('input[name="email"]').value;
    const password = form.querySelector('input[name="password"]').value;
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;

    // Basic validation
    if (!email || !password) {
        showErrorMessage(form, 'Please fill in all required fields.');
        return;
    }

    // Show loading state
    submitBtn.innerHTML = '<span class="loading"></span> Signing in...';
    submitBtn.disabled = true;

    // Simulate API call
    setTimeout(() => {
        // In a real app, you would validate credentials here
        showSuccessMessage(form, 'Login successful! Redirecting...');
        setTimeout(() => {
            window.location.href = 'index.html';
        }, 1000);
    }, 1500);
}

// Signup form submission
function handleSignupSubmission(form) {
    const password = form.querySelector('input[name="password"]').value;
    const confirmPassword = form.querySelector('input[name="confirm-password"]').value;
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;

    // Password validation
    if (password !== confirmPassword) {
        showErrorMessage(form, 'Passwords do not match.');
        return;
    }

    if (password.length < 6) {
        showErrorMessage(form, 'Password must be at least 6 characters long.');
        return;
    }

    // Show loading state
    submitBtn.innerHTML = '<span class="loading"></span> Creating account...';
    submitBtn.disabled = true;

    // Simulate API call
    setTimeout(() => {
        showSuccessMessage(form, 'Account created successfully! Please check your email for verification.');
        form.reset();
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }, 2000);
}

// Utility functions
function showSuccessMessage(form, message) {
    removeExistingMessages(form);
    const messageDiv = document.createElement('div');
    messageDiv.className = 'success-message fade-in';
    messageDiv.textContent = message;
    form.appendChild(messageDiv);

    // Remove message after 5 seconds
    setTimeout(() => {
        if (messageDiv.parentNode) {
            messageDiv.remove();
        }
    }, 5000);
}

function showErrorMessage(form, message) {
    removeExistingMessages(form);
    const messageDiv = document.createElement('div');
    messageDiv.className = 'error-message fade-in';
    messageDiv.textContent = message;
    form.appendChild(messageDiv);

    // Remove message after 5 seconds
    setTimeout(() => {
        if (messageDiv.parentNode) {
            messageDiv.remove();
        }
    }, 5000);
}

function removeExistingMessages(form) {
    const existingMessages = form.querySelectorAll('.success-message, .error-message');
    existingMessages.forEach(msg => msg.remove());
}

// Animation on scroll
function initAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    // Observe elements that should animate
    const animatedElements = document.querySelectorAll('.about-card, .feedback-quote, .section-title');
    animatedElements.forEach(element => {
        observer.observe(element);
    });
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Search functionality (if needed)
function initSearch() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');

    if (searchInput && searchResults) {
        let searchTimeout;

        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            const query = this.value.trim();

            if (query.length < 2) {
                searchResults.innerHTML = '';
                searchResults.style.display = 'none';
                return;
            }

            searchTimeout = setTimeout(() => {
                performSearch(query);
            }, 300);
        });

        // Close search results when clicking outside
        document.addEventListener('click', function(event) {
            if (!searchInput.contains(event.target) && !searchResults.contains(event.target)) {
                searchResults.style.display = 'none';
            }
        });
    }
}

function performSearch(query) {
    // This would typically make an API call to search content
    // For now, we'll simulate search results
    const searchResults = document.getElementById('search-results');
    
    // Mock search results
    const mockResults = [
        { title: 'SPIN Fellowship Program', url: 'pages/society-fellowship.html' },
        { title: 'Cortex Club', url: 'pages/cortex-club.html' },
        { title: 'SPIN A Yarn Newsletter', url: 'pages/spin-yarn-newsletter.html' },
        { title: 'Green Radiology Initiative', url: 'pages/green-radiology.html' }
    ];

    const filteredResults = mockResults.filter(result => 
        result.title.toLowerCase().includes(query.toLowerCase())
    );

    if (filteredResults.length > 0) {
        searchResults.innerHTML = filteredResults.map(result => 
            `<div class="search-result">
                <a href="${result.url}">${result.title}</a>
            </div>`
        ).join('');
        searchResults.style.display = 'block';
    } else {
        searchResults.innerHTML = '<div class="no-results">No results found</div>';
        searchResults.style.display = 'block';
    }
}

// Tab functionality for WFPI page
function initTabs() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetTab = this.getAttribute('data-tab');

            // Remove active class from all tabs and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            // Add active class to clicked tab and corresponding content
            this.classList.add('active');
            const targetContent = document.getElementById(targetTab);
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });
}

// Initialize tabs if they exist
if (document.querySelector('.tab-button')) {
    initTabs();
}

// Initialize search if search elements exist
if (document.getElementById('search-input')) {
    initSearch();
}

// Utility function to format dates
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

// Utility function to validate email
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Print functionality
function printPage() {
    window.print();
}

// Export functionality for downloadable content
function downloadContent(content, filename, contentType) {
    const a = document.createElement('a');
    const file = new Blob([content], { type: contentType });
    a.href = URL.createObjectURL(file);
    a.download = filename;
    a.click();
    URL.revokeObjectURL(a.href);
}

// Copy to clipboard functionality
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        // Show success message
        const toast = document.createElement('div');
        toast.className = 'toast success-message';
        toast.textContent = 'Copied to clipboard!';
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.remove();
        }, 3000);
    }, function(err) {
        console.error('Could not copy text: ', err);
    });
}

// Back to top functionality
function addBackToTop() {
    const backToTopBtn = document.createElement('button');
    backToTopBtn.innerHTML = '↑';
    backToTopBtn.className = 'back-to-top';
    backToTopBtn.setAttribute('aria-label', 'Back to top');
    document.body.appendChild(backToTopBtn);

    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopBtn.style.display = 'block';
        } else {
            backToTopBtn.style.display = 'none';
        }
    });
}

// Initialize back to top button
addBackToTop();
