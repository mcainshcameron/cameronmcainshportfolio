// Navigation scroll effect
const nav = document.getElementById('nav');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 50) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }

    lastScroll = currentScroll;
});

// Mobile menu toggle
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');

navToggle.addEventListener('click', () => {
    const isActive = navMenu.classList.toggle('active');
    navToggle.classList.toggle('active');
    navToggle.setAttribute('aria-expanded', isActive);
});

// Close mobile menu when clicking a link
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        navToggle.classList.remove('active');
        navToggle.setAttribute('aria-expanded', false);
    });
});

// Smooth scroll with offset for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offsetTop = target.offsetTop - 80;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Intersection Observer for project cards
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.classList.add('visible');
            }, index * 100);
        }
    });
}, observerOptions);

// Observe all project cards
document.querySelectorAll('.project-card').forEach(card => {
    observer.observe(card);
});

// Active nav link on scroll
const sections = document.querySelectorAll('section[id]');

function updateActiveNavLink() {
    const scrollY = window.pageYOffset;

    sections.forEach(section => {
        const sectionHeight = section.offsetHeight;
        const sectionTop = section.offsetTop - 100;
        const sectionId = section.getAttribute('id');
        const navLink = document.querySelector(`.nav-link[href="#${sectionId}"]`);

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            navLinks.forEach(link => link.classList.remove('active'));
            if (navLink) navLink.classList.add('active');
        }
    });
}

window.addEventListener('scroll', updateActiveNavLink);

// Parallax effect for gradient orbs
window.addEventListener('mousemove', (e) => {
    const { clientX, clientY } = e;
    const centerX = window.innerWidth / 2;
    const centerY = window.innerHeight / 2;

    const moveX = (clientX - centerX) / 50;
    const moveY = (clientY - centerY) / 50;

    document.querySelectorAll('.gradient-orb').forEach((orb, index) => {
        const speed = (index + 1) * 0.5;
        orb.style.transform = `translate(${moveX * speed}px, ${moveY * speed}px)`;
    });
});

// Add typing effect to hero title (optional enhancement)
const heroName = document.querySelector('.hero-name');
if (heroName) {
    const text = heroName.textContent;
    heroName.textContent = '';
    heroName.style.opacity = '1';

    let index = 0;
    function typeWriter() {
        if (index < text.length) {
            heroName.textContent += text.charAt(index);
            index++;
            setTimeout(typeWriter, 80);
        }
    }

    // Start typing after page loads
    setTimeout(typeWriter, 800);
}


// Cursor trail effect (subtle)
let cursorTrail = [];
const trailLength = 20;

document.addEventListener('mousemove', (e) => {
    cursorTrail.push({ x: e.clientX, y: e.clientY, time: Date.now() });

    if (cursorTrail.length > trailLength) {
        cursorTrail.shift();
    }
});

// Add easter egg: Konami code
let konamiCode = [];
const konamiSequence = [
    'ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown',
    'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight',
    'b', 'a'
];

document.addEventListener('keydown', (e) => {
    konamiCode.push(e.key);
    konamiCode = konamiCode.slice(-10);

    if (konamiCode.join('') === konamiSequence.join('')) {
        document.body.style.animation = 'rainbow 2s linear infinite';
        setTimeout(() => {
            document.body.style.animation = '';
        }, 5000);
    }
});

// Add CSS for rainbow animation
const style = document.createElement('style');
style.textContent = `
    @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
`;
document.head.appendChild(style);

// Performance: Reduce animations on lower-end devices
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('*').forEach(el => {
        el.style.animation = 'none';
        el.style.transition = 'none';
    });
}

// ===== ZenQuotes API Integration =====
let quotesCache = [];
const CACHE_DURATION = 3600000; // 1 hour in milliseconds
const API_URL = "https://zenquotes.io/api/quotes";

// Fetch quotes from ZenQuotes API
async function fetchQuotes() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error('Failed to fetch quotes');
        }
        const data = await response.json();

        // Store quotes in cache with timestamp
        quotesCache = data;
        localStorage.setItem('zenquotes_cache', JSON.stringify(data));
        localStorage.setItem('zenquotes_timestamp', Date.now().toString());

        return data;
    } catch (error) {
        console.error('Error fetching quotes:', error);
        // Return a fallback quote if API fails
        return [{
            q: "The only way to do great work is to love what you do.",
            a: "Steve Jobs"
        }];
    }
}

// Load quotes from cache or fetch new ones
async function loadQuotes() {
    const cachedQuotes = localStorage.getItem('zenquotes_cache');
    const cachedTimestamp = localStorage.getItem('zenquotes_timestamp');
    const now = Date.now();

    // Check if cache exists and is still valid
    if (cachedQuotes && cachedTimestamp && (now - parseInt(cachedTimestamp)) < CACHE_DURATION) {
        quotesCache = JSON.parse(cachedQuotes);
    } else {
        // Cache expired or doesn't exist, fetch new quotes
        quotesCache = await fetchQuotes();
    }

    // Display a random quote
    displayRandomQuote();
}

// Display a random quote from the cache
function displayRandomQuote() {
    if (quotesCache.length === 0) return;

    // Get a random quote
    const randomIndex = Math.floor(Math.random() * quotesCache.length);
    const quote = quotesCache[randomIndex];

    const quoteText = document.getElementById('zenquote-text');
    const quoteAuthor = document.getElementById('zenquote-author');

    if (quoteText && quoteAuthor) {
        // Add fade-out animation
        quoteText.style.opacity = '0';
        quoteAuthor.style.opacity = '0';

        setTimeout(() => {
            quoteText.textContent = `"${quote.q}"`;
            quoteAuthor.textContent = `— ${quote.a}`;

            // Fade back in
            quoteText.style.opacity = '1';
            quoteAuthor.style.opacity = '1';
        }, 300);
    }
}

// Initialize quotes on page load
document.addEventListener('DOMContentLoaded', () => {
    loadQuotes();
});
