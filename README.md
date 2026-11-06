# 💄 Faberlic Partner — Promo & Content Management Platform

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4+-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![HTMX](https://img.shields.io/badge/HTMX-1.9+-3366CC?style=for-the-badge&logo=htmx&logoColor=white)](https://htmx.org/)
[![Alpine.js](https://img.shields.io/badge/Alpine.js-3.x-8BC0D0?style=for-the-badge&logo=alpinedotjs&logoColor=black)](https://alpinejs.dev/)
[![Nginx](https://img.shields.io/badge/Nginx-Production-009639?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/)

A responsive, high-performance web platform built for an official Faberlic brand partner. Designed with a **Server-Side Rendered (SSR)** architecture optimized for top search engine ranking (SEO), combined with lightweight reactive frontend technologies (**HTMX + Alpine.js**) to provide a seamless Single-Page-Application (SPA) user experience.

---

## 🌟 Live Demo
- **Production URL:** [https://faberlic-sales.com](https://faberlic-sales.com)

---

## 🎯 Architectural Highlights & Key Features

### 1. Frontend & UX/UI
* **DHA Stack (Django + HTMX + Alpine.js):** Replaces heavy JavaScript SPAs (React/Vue), achieving **sub-second page loads** and 100% crawlable server-rendered HTML for search bots.
* **Tailwind CSS Integration:** Modern utility-first design completely customized to the official Faberlic color palette.
* **Mobile-First Responsive Layout:**
  * **Desktop:** Magazine-style split-layouts (2+3 grid arrangements, sticky sidebars).
  * **Mobile:** Slide-over navigation drawers, adaptive content stacking, and touch-optimized components.
* **Alpine.js Interactive Components:**
  * **Global Lightbox Modal:** Full-screen high-resolution image preview with smooth GPU-accelerated zoom animations and keyboard (`Esc`) controls.
  * **Dynamic Content Clamping:** Intelligent "Read more..." logic with font-rendering awareness and fallback handling across different mobile browser engines (iOS WebKit / Android Chromium).
* **HTMX Infinite Pagination:** Asynchronous partial rendering for dynamic deals on the homepage - users can load additional records without full page reloads.

### 2. Backend & CMS (Django)
* **Custom Admin Panel:** Styled with **Django Jazzmin** and branded with corporate accents for a clean CRM-like feel.
* **WYSIWYG Rich-Text Editing:** Integrated **Summernote** allowing the client to inject rich text, lists, and referral hyperlinks anywhere within page content.
* **Singleton Admin Architecture:** Enforced single-record configurations for key landing blocks, preventing accidental duplicate setups.
* **Database Optimization:** PostgreSQL backend with indexes, explicit schema configurations, and optimized query slicing.

### 3. SEO & Discoverability
* **Dynamic Sitemap (`sitemap.xml`):** Automatically aggregates and calculates URLs, update frequencies, and priority levels using `django.contrib.sitemaps`.
* **Robots Configuration (`robots.txt`):** Route-managed directives preventing crawler overload and blocking administrative/editor endpoints.
* **Smart Open Graph (OG) Pipeline:** Context-aware social sharing tags for Telegram, WhatsApp, and VK. Dynamically pulls content excerpts (`striptags` + truncation) and featured images, falling back to corporate branded defaults.
* **Search Console Integrations:** Verified on both **Yandex.Webmaster** and **Google Search Console**; fully connected to **Yandex.Metrika** (including WebVisor session replay).

### 4. Infrastructure & Production Deployment
* **Operating System:** Ubuntu Linux VPS.
* **WSGI / App Server:** **Gunicorn** managed via systemd sockets and background service daemons (3 parallel worker processes).
* **Reverse Proxy:** **Nginx** acting as reverse proxy, request buffer, security firewall, and direct static/media file server.
* **SSL/TLS:** Free automated certificates via **Let's Encrypt (Certbot)** with forced HTTPS redirection.
* **Low-Memory Optimization:** 2 GB SWAP space configured on SSD to guarantee zero out-of-memory (OOM) failures under 1 GB physical RAM.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.11+, Django 5 |
| **Frontend** | Tailwind CSS, HTMX, Alpine.js |
| **Database** | PostgreSQL |
| **Rich-Text Engine** | Django Summernote |
| **Admin UI** | Django Jazzmin |
| **Web Server / Proxy** | Nginx |
| **WSGI Server** | Gunicorn |
| **Monitoring / Analytics** | Yandex.Metrika, Google Search Console, Yandex.Webmaster |

---

## 📂 Project Structure

```text
.
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── logging_config.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_familyshopping_moneybyphone_workasleader.py
│   │   ├── 0003_alter_familyshopping_title_alter_moneybyphone_title_and_more.py
│   │   ├── 0004_home.py
│   │   ├── 0005_homedealoffer_homegiftssection_homestartersection_and_more.py
│   │   └── __init__.py
│   ├── models.py
│   ├── sitemaps.py
│   ├── static
│   │   └── images
│   │       ├── favicon.png
│   │       └── og-faberlic.png
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── pyproject.toml
├── README.md
├── static
│   └── admin
│       └── js
│           └── dynamic_image_preview.js
├── templates
│   └── core
│       ├── about-products.html
│       ├── base.html
│       ├── family-shopping.html
│       ├── home.html
│       ├── money-by-phone.html
│       ├── news.html
│       ├── partials
│       │   └── deals_chunk.html
│       ├── robots.txt
│       └── work-as-leader.html
├── theme
│   ├── apps.py
│   ├── __init__.py
│   ├── static
│   │   └── css
│   │       └── dist
│   │           └── styles.css
│   ├── static_src
│   │   └── src
│   │       └── styles.css
│   └── templates
│       └── base.html
└── uv.lock
```

## 🚀 Local Development Setup
### 1. Prerequisites

Ensure you have the following installed locally:

- Python 3.10+

- PostgreSQL

- Node.js (v18+)

### 2. Clone and Setup Environment

```bash
git clone https://github.com/NikolayRom/Elena-Faberlic.git
cd Elena-Faberlic

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a .env file in the project root:

```bash
cp .env.ex .env
```

### 4. Database Initialization & Tailwind Setup

```bash
python manage.py migrate

python manage.py createsuperuser

python manage.py tailwind install
```

### 5. Running the Project

In two separate terminal windows:

```bash
python manage.py tailwind start

python manage.py runserver
```

Visit http://127.0.0.1:8000 in your browser.