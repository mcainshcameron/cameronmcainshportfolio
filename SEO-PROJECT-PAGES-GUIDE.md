# SEO Optimization Guide for Individual Project Pages

This guide provides the essential SEO elements needed for each project page to ensure optimal search engine visibility and proper linking back to your portfolio.

---

## 1. Essential Meta Tags

### Basic Meta Tags
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="[Project Name] - [Brief description with key features and technologies]. Created by Cameron McAinsh.">
<meta name="keywords" content="[Project Name], [Tech Stack Keywords], Cameron McAinsh, [Category Keywords]">
<meta name="author" content="Cameron McAinsh">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="[Project URL]">
```

### Open Graph (Facebook/LinkedIn)
```html
<meta property="og:type" content="website">
<meta property="og:url" content="[Project URL]">
<meta property="og:title" content="[Project Name] | Cameron McAinsh">
<meta property="og:description" content="[Compelling description for social sharing]">
<meta property="og:image" content="[URL to project screenshot/logo - min 1200x630px]">
<meta property="og:site_name" content="Cameron McAinsh Portfolio">
```

### Twitter Cards
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:url" content="[Project URL]">
<meta name="twitter:title" content="[Project Name] | Cameron McAinsh">
<meta name="twitter:description" content="[Brief description]">
<meta name="twitter:image" content="[URL to project screenshot/logo]">
```

### Title Tag
```html
<title>[Project Name] | Cameron McAinsh - [Brief descriptor]</title>
```

---

## 2. Structured Data (JSON-LD)

Add this in the `<head>` section:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "[Project Name]",
  "url": "[Project URL]",
  "description": "[Detailed description of the project]",
  "applicationCategory": "[Category: e.g., WebApplication, MobileApplication, BusinessApplication]",
  "operatingSystem": "[e.g., Web Browser, iOS, Android, Cross-platform]",
  "author": {
    "@type": "Person",
    "name": "Cameron McAinsh",
    "url": "https://cameronmcainsh.com"
  },
  "image": "[URL to project screenshot/logo]",
  "screenshot": "[URL to project screenshot]",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  },
  "datePublished": "[YYYY-MM-DD]",
  "keywords": "[comma, separated, keywords]"
}
</script>

<!-- Add Breadcrumb Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://cameronmcainsh.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Projects",
      "item": "https://cameronmcainsh.com/#projects"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "[Project Name]",
      "item": "[Project URL]"
    }
  ]
}
</script>
```

---

## 3. Essential On-Page Content

### Page Structure

```html
<header>
  <!-- Navigation with link back to portfolio -->
  <nav aria-label="Main navigation">
    <a href="https://cameronmcainsh.com" aria-label="Back to Cameron McAinsh Portfolio">
      CM
    </a>
    <!-- Other nav items -->
  </nav>
</header>

<main>
  <!-- Hero Section -->
  <section class="hero">
    <h1>[Project Name]</h1>
    <p class="tagline">[Brief compelling tagline]</p>
  </section>

  <!-- Project Overview -->
  <section class="overview">
    <h2>Overview</h2>
    <p>[What the project does and why it exists]</p>
  </section>

  <!-- Key Features -->
  <section class="features">
    <h2>Key Features</h2>
    <ul>
      <li>[Feature 1]</li>
      <li>[Feature 2]</li>
      <li>[Feature 3]</li>
    </ul>
  </section>

  <!-- Technology Stack -->
  <section class="tech-stack">
    <h2>Technology Stack</h2>
    <ul>
      <li>[Technology 1]</li>
      <li>[Technology 2]</li>
    </ul>
  </section>

  <!-- Screenshots/Demo -->
  <section class="gallery">
    <h2>Screenshots</h2>
    <!-- Add alt text to all images -->
    <img src="[screenshot.jpg]" alt="[Descriptive alt text of what's shown]" loading="lazy">
  </section>

  <!-- Development Story (optional but good for SEO) -->
  <section class="story">
    <h2>Development Story</h2>
    <p>[Why you built it, challenges faced, lessons learned]</p>
  </section>
</main>

<footer>
  <p>&copy; 2026 Cameron McAinsh</p>
  <p>
    <a href="https://cameronmcainsh.com">Back to Portfolio</a> |
    <a href="https://linkedin.com/in/cameronmcainsh" rel="noopener noreferrer">LinkedIn</a> |
    <a href="https://github.com/mcainshcameron" rel="noopener noreferrer">GitHub</a>
  </p>
</footer>
```

---

## 4. Important Links Back to Portfolio

### In Navigation
```html
<nav>
  <a href="https://cameronmcainsh.com" class="back-link">
    ← Back to Portfolio
  </a>
  <!-- Or -->
  <a href="https://cameronmcainsh.com#projects" class="back-link">
    ← All Projects
  </a>
</nav>
```

### In Footer
```html
<footer>
  <p>Part of <a href="https://cameronmcainsh.com">Cameron McAinsh's Portfolio</a></p>
  <p>View <a href="https://cameronmcainsh.com#projects">more projects</a></p>
</footer>
```

### Author Attribution
```html
<section class="author">
  <p>Created by <a href="https://cameronmcainsh.com" rel="author">Cameron McAinsh</a></p>
</section>
```

---

## 5. SEO-Friendly URLs

### Best Practices
- Use descriptive URLs: `yoursite.com/solo-pro-league` ✓
- Avoid: `yoursite.com/project1` ✗
- Keep URLs short and readable
- Use hyphens to separate words (not underscores)

---

## 6. Image Optimization

### Requirements
1. **Alt Text**: Descriptive text for every image
   ```html
   <img src="dashboard.png" alt="Solo Pro League player dashboard showing match statistics and rankings">
   ```

2. **File Names**: Use descriptive names
   - Good: `solo-pro-league-dashboard.png`
   - Bad: `IMG_1234.png`

3. **Dimensions**: Specify width and height
   ```html
   <img src="image.png" alt="..." width="1200" height="800">
   ```

4. **Format**: Use modern formats (WebP with PNG/JPG fallback)

5. **Open Graph Image**: 1200x630px minimum for social sharing

---

## 7. Internal Linking Strategy

### Link to Portfolio
```html
<!-- In content -->
<p>This project is part of my <a href="https://cameronmcainsh.com#projects">portfolio of experimental projects</a>.</p>

<!-- Related projects -->
<section class="related-projects">
  <h2>More Projects</h2>
  <ul>
    <li><a href="https://cameronmcainsh.com#projects">View all projects</a></li>
    <li><a href="[other-project-url]">Another Project Name</a></li>
  </ul>
</section>
```

### Link FROM Portfolio (already done)
Make sure your portfolio links to project pages with descriptive anchor text:
```html
<a href="[project-url]">Learn more about [Project Name]</a>
```

---

## 8. Content Requirements

### Minimum Content for SEO
Each project page should have:

1. **Unique Title** (60 characters max for search results)
2. **Meta Description** (155-160 characters, compelling summary)
3. **H1 Heading** (Project name)
4. **300+ words of unique content** (more is better)
5. **H2/H3 subheadings** for structure
6. **Alt text** for all images
7. **Internal links** back to portfolio
8. **External links** to live demo/GitHub (if applicable)

### Content Ideas
- Problem the project solves
- Target audience/users
- Key features and benefits
- Technology choices and why
- Development challenges
- Future improvements
- Lessons learned
- Call-to-action (try demo, view code, etc.)

---

## 9. Technical SEO Checklist

- [ ] Mobile-responsive design
- [ ] Fast loading speed (< 3 seconds)
- [ ] HTTPS enabled
- [ ] Valid HTML
- [ ] Semantic HTML5 elements
- [ ] robots.txt allows crawling
- [ ] XML sitemap includes project pages
- [ ] Structured data validates (test with Google Rich Results Test)
- [ ] No broken links
- [ ] Proper 301 redirects if URLs change

---

## 10. Project-Specific Templates

### Solo Pro League Example

```html
<title>Solo Pro League | Amateur Football Performance Tracking Platform</title>
<meta name="description" content="Solo Pro League - A platform for tracking amateur football matches, player performance, and generating balanced teams using ML algorithms. Built with Odoo, n8n, and Supabase by Cameron McAinsh.">
<meta name="keywords" content="Solo Pro League, Football Analytics, Amateur Sports Platform, Team Balancing, ML Workflows, Odoo, n8n, Supabase, Cameron McAinsh">
```

```json
{
  "@type": "SoftwareApplication",
  "name": "Solo Pro League",
  "applicationCategory": "WebApplication",
  "description": "Platform for collecting and analyzing data from amateur football matches, focused on player performance and balanced teams",
  "operatingSystem": "Web Browser",
  "keywords": "football, analytics, sports, team management, machine learning"
}
```

### Serra Vano Example

```html
<title>Serra Vano | Milano - AI-Generated Conceptual Kitchen Design</title>
<meta name="description" content="Serra Vano - An automated content pipeline generating intentionally impractical kitchen objects as high-end design products. Inspired by The Uncomfortable. Built with n8n, LLMs, and Fal.ai by Cameron McAinsh.">
<meta name="keywords" content="Serra Vano, AI Art, Conceptual Design, LLM Art, n8n Automation, Generative Design, Cameron McAinsh">
```

```json
{
  "@type": "SoftwareApplication",
  "name": "Serra Vano | Milano",
  "applicationCategory": "WebApplication",
  "description": "Automated system generating conceptual impractical kitchen objects presented as high-end design products",
  "keywords": "conceptual design, AI art, generative design, automation"
}
```

---

## 11. Performance Optimization

### Critical for SEO
```html
<!-- Preload critical resources -->
<link rel="preload" as="image" href="hero-image.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">

<!-- Lazy load images below fold -->
<img src="image.jpg" loading="lazy" alt="...">

<!-- Defer non-critical JavaScript -->
<script src="script.js" defer></script>
```

---

## 12. Analytics & Tracking

### Add to each project page
```html
<!-- Google Analytics or your preferred analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

---

## 13. Update Main Portfolio Sitemap

After creating project pages, update `sitemap.xml`:

```xml
<url>
  <loc>https://soloproleague.com/</loc>
  <lastmod>2026-01-04</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
<url>
  <loc>https://mcainshcameron.github.io/SerraVano/</loc>
  <lastmod>2026-01-04</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
<!-- Add others... -->
```

---

## 14. Cross-Linking Strategy

### Portfolio → Project Pages
- Link from portfolio project cards to dedicated project pages
- Use descriptive anchor text: "Learn more about Solo Pro League"
- Not: "Click here" or "Read more"

### Project Pages → Portfolio
- Prominent "Back to Portfolio" link in navigation
- Footer link: "View more projects by Cameron McAinsh"
- Author bio with portfolio link

### Project Pages → Other Projects
- "Related Projects" section
- Links to projects with similar tech stack
- "You might also like" section

---

## 15. Content Update Strategy

### Keep Projects Fresh
- Add new screenshots as features are added
- Update "Last Updated" date in footer
- Add case studies or user testimonials
- Document new features
- Keep technology stack list current

---

## Quick Checklist for Each Project Page

- [ ] Unique meta title and description
- [ ] All images have alt text
- [ ] H1 tag with project name
- [ ] At least 300 words of unique content
- [ ] Link back to portfolio homepage
- [ ] Link to live demo (if available)
- [ ] Link to GitHub repo (if public)
- [ ] Structured data (JSON-LD) added
- [ ] Open Graph tags for social sharing
- [ ] Mobile responsive
- [ ] Fast loading (test with PageSpeed Insights)
- [ ] Valid HTML (test with W3C validator)
- [ ] Added to sitemap.xml
- [ ] Tested in Google Search Console

---

## Tools for Testing

1. **Google Search Console** - Submit pages, check indexing
2. **Google Rich Results Test** - Validate structured data
3. **PageSpeed Insights** - Check performance
4. **W3C Markup Validator** - Validate HTML
5. **Screaming Frog** - Crawl your site for issues
6. **Ahrefs/SEMrush** - Track rankings and backlinks

---

## Priority Order

1. **High Priority**: Solo Pro League, Serra Vano (most impressive projects)
2. **Medium Priority**: Weekend English, Vestal, PQL Study App
3. **Low Priority**: xlsonic, No Scrolls Given (conceptual/simple projects)

Focus on the high-priority projects first to get the best SEO ROI.
