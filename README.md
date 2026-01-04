# Portfolio Website

Personal portfolio website for Cameron McAinsh showcasing projects, skills, and contact information.

## Project Structure

```
Portfolio/
├── index.html              # Main HTML file
├── robots.txt             # Search engine directives
├── llms.txt               # LLM context file
├── README.md              # This file
└── assets/
    ├── css/
    │   └── styles.css     # Main stylesheet
    ├── js/
    │   └── script.js      # JavaScript functionality
    └── images/            # All project images (PNG + WebP)
        ├── Solo Pro League.png/webp
        ├── Serra Vano.png/webp
        ├── weekend-english-high-resolution-logo-transparent.png/webp
        ├── xlsonics.png/webp
        ├── NoScrollzGiven.png/webp
        ├── vestal.png/webp
        └── PQL.png/webp
```

## Features

- Responsive design for all screen sizes
- Optimized image loading with WebP format + PNG fallbacks
- Lazy loading for below-the-fold images
- Smooth animations and transitions
- Interactive project cards
- Mobile-friendly navigation

## Performance Optimizations

- **WebP Images**: Modern browsers load WebP format (47% smaller) with PNG fallbacks
- **Lazy Loading**: Images load only when visible in viewport
- **Preloading**: Critical first image preloaded for faster initial render
- **Async Decoding**: Images decode asynchronously to prevent blocking
- **Layout Stability**: Width/height attributes prevent layout shifts

## Local Development

Simply open `index.html` in a web browser, or serve with any static file server:

```bash
# Python
python -m http.server 8000

# Node.js (with http-server)
npx http-server

# PHP
php -S localhost:8000
```

## Technologies

- HTML5
- CSS3 (Custom Properties, Flexbox, Grid)
- Vanilla JavaScript (ES6+)
- WebP image format with fallbacks

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

---

Built by Cameron McAinsh | 2026
