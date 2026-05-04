# Erasmus Guide Static Website

This repository contains a static informational website for Erasmus students. It includes six pages:

- `index.html` — Home
- `about.html` — About Us
- `consulting.html` — Consulting
- `opportunities.html` — Opportunities
- `blog.html` — Blog
- `contact.html` — Contact

## Hosting with GitHub Pages

1. Create a GitHub repository for this project.
2. Initialize git locally:
   ```bash
   git init
   git add .
   git commit -m "Add Erasmus Guide static site"
   git remote add origin https://github.com/your-username/your-repo.git
   git branch -M main
   git push -u origin main
   ```
3. In GitHub repository settings, enable GitHub Pages and set the source to:
   - Branch: `main`
   - Folder: `/docs`
4. Your site will be published at `https://your-username.github.io/your-repo/`.

## Alternative free hosting

- Netlify: Drag and drop the `docs/` folder into Netlify Sites.
- Cloudflare Pages: Connect the repository and publish the `docs` folder.

## Notes

- The live website can be hosted as a static site because it is informational only.
- If you want a server-backed version later, the Flask app is still available in `app.py`.
