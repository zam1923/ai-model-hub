# AI Info Catalog - Agent Instructions (Zero-Touch Operations)

This repository is designed as a "Zero-Touch" autonomous AI information portal. It requires no manual human intervention for daily updates.

## 1. Project Philosophy & Architecture
- **Framework:** Astro (latest) with Content Collections API (using `glob` loader).
- **Styling:** Tailwind CSS v4.
- **Data Source:** Git-based Markdown files stored in `src/content/{models,labs,researchers}/`.
- **Zero-Touch Principle:** All new data must be programmatically generated via scheduled scripts (GitHub Actions) using LLMs (e.g., Gemini API), committed directly to the `main` branch, and automatically deployed without human PR reviews.

## 2. Content Collections Schema Definition (`src/content.config.ts`)
When generating new data, agents MUST adhere strictly to the following frontmatter definitions:

### Models (`src/content/models/*.md`)
```yaml
---
title: "String (Model Name)"
lab: "String (Lab Name, must exactly match a lab's name field)"
releaseDate: YYYY-MM-DD
contextWindow: "String (e.g., '128k')"
license: "String (e.g., 'Proprietary', 'MIT', 'Apache 2.0')"
description: "String (Short Japanese description, 1-2 sentences)"
officialUrl: "URL String (Optional)"
paperUrl: "URL String (Optional)"
modalities: ["Text", "Image", "Audio"] # Array of strings, Optional
---
Markdown body with a detailed Japanese summary.
```

### Labs (`src/content/labs/*.md`)
```yaml
---
name: "String (Lab Name)"
location: "String (Location)"
description: "String (Short Japanese description)"
website: "URL String (Optional)"
---
Markdown body with detailed lab information.
```

### Researchers (`src/content/researchers/*.md`)
```yaml
---
name: "String (Researcher Name)"
lab: "String (Lab Name)"
role: "String (Role/Title)"
famousFor: "String (What they are known for)"
links: # Optional
  x: "URL String (Optional)"
  github: "URL String (Optional)"
  scholar: "URL String (Optional)"
---
Markdown body with detailed researcher information.
```

## 3. Automation Workflow Guidelines
- **Update Script:** `scripts/auto_update.py` is executed via GitHub Actions to poll RSS feeds (like arXiv) or scrape news.
- **LLM Usage:** The script uses the Gemini API (via `GEMINI_API_KEY`) to parse English/Japanese source texts, extract entities (Models, Labs, Researchers), and output strictly formatted Markdown files matching the schemas above.
- **Cross-Linking:** When generating a Model, if a new Lab or Researcher is detected, the script should simultaneously generate their respective Markdown files to maintain relational integrity.
- **Idempotency:** Scripts should check if an entity already exists (by checking file existence in `src/content/`) before creating duplicates.

## 4. UI/UX Guidelines
- Maintain a clean, dark-theme-ready design (`class="dark"` is applied globally).
- Ensure client-side interactions (like search and filtering) are implemented with lightweight Vanilla JS to keep the static site performance optimal. No heavy frameworks (React/Vue) unless strictly necessary.

## 5. Next Steps for Autonomous Agents
When you are assigned a task to improve this repository, follow these rules:
1. Always test `npm run build` locally after making structural changes.
2. If modifying schemas, ensure `scripts/auto_update.py` and `src/content.config.ts` are updated in sync.
3. Respect the existing Tailwind styling and do not introduce conflicting CSS methodologies.
4. Use standard Pull Requests for your changes. The environment restricts direct pushes to the `main` branch.
