# Indian Art Form — Standalone Cultural Heritage Showcase

An academic and interactive digital archive celebrating traditional Indian art forms, architecture, and indigenous design traditions. This repository hosts **6 independent, standalone assignments**, each deployed to its own dedicated production slot on Vercel with zero cross-dependencies.

---

## Live Deployments Matrix

| Assignment | Production Deployment URL | Primary Domain & Focus | Dedicated Branch | Deployment Status |
| :--- | :--- | :--- | :--- | :---: |
| **Assignment 1** | [indianartformharinish-1.vercel.app](https://indianartformharinish-1.vercel.app/) | **Kalākrama** — Interactive Timeline of Indian Art | `main` | ![Live](https://img.shields.io/badge/Status-Live%20Production-success?style=flat-square) |
| **Assignment 2** | [indianartformharinish-2.vercel.app](https://indianartformharinish-2.vercel.app/) | **Kalābhūmi** — The Art Survey of India | `vercel-project-2` | ![Live](https://img.shields.io/badge/Status-Live%20Production-success?style=flat-square) |
| **Assignment 3** | [indianartformharinish-3.vercel.app](https://indianartformharinish-3.vercel.app/) | **Sangama** — Fusion of Regional Painting Styles | `vercel-project-3` | ![Live](https://img.shields.io/badge/Status-Live%20Production-success?style=flat-square) |
| **Assignment 4** | [indianartformharinish-4.vercel.app](https://indianartformharinish-4.vercel.app/) | **Ajanta Frames** — Cave Walkthrough & Mural Studies | `vercel-project-4` | ![Live](https://img.shields.io/badge/Status-Live%20Production-success?style=flat-square) |
| **Assignment 5** | [indianartformharinish-5.vercel.app](https://indianartformharinish-5.vercel.app/) | **Stone That Speaks** — Mahabalipuram 3D Site Walk | `vercel-project-5` | ![Live](https://img.shields.io/badge/Status-Live%20Production-success?style=flat-square) |
| **Assignment 6** | [indianartformharinish-6.vercel.app](https://indianartformharinish-6.vercel.app/) | **Kolam & Rangoli Studio** — 100 Traditional Designs | `vercel-project-6` | ![Live](https://img.shields.io/badge/Status-Live%20Production-success?style=flat-square) |
| **Base Showcase** | [indianartformharinish.vercel.app](https://indianartformharinish.vercel.app/) | **Kalākrama Showcase** — Primary Web Portal | `main` | ![Live](https://img.shields.io/badge/Status-Live%20Production-success?style=flat-square) |

---

## Detailed Assignment Breakdown

### Assignment 1: Kalākrama — Interactive Timeline of Indian Art
- **Live URL:** [https://indianartformharinish-1.vercel.app](https://indianartformharinish-1.vercel.app/)
- **Git Branch:** `main`
- **Key Features:**
  - Chronological journey across 8 landmark historical epochs: Indus Valley Civilization, Mauryan & Post-Mauryan, Gupta Golden Age, Early Medieval Rock-cut, Chola Bronze Age, Mughal & Rajput Court Painting, Colonial Company Style, and Modernist Revival.
  - Interactive era filtering by medium: Sculpture, Fresco/Mural, Architecture, and Miniature Painting.
  - Classical audio accompaniment player with period ambiance.
  - Built-in visual comparison tool and interactive knowledge check quiz.

### Assignment 2: Kalābhūmi — The Art Survey of India
- **Live URL:** [https://indianartformharinish-2.vercel.app](https://indianartformharinish-2.vercel.app/)
- **Git Branch:** `vercel-project-2`
- **Key Features:**
  - Geographic survey mapping regional folk and classical art schools across North, South, East, West, and Central India.
  - Curated exhibits for Madhubani (Mithila), Warli tribal motifs, Tanjore gold leafing, Odisha Pattachitra, and Rajasthan Pichwai.
  - Material analysis detailing traditional natural pigments (indigo, turmeric, lac, lampblack) and organic binders.

### Assignment 3: Sangama — A Fusion of Regional Painting Styles
- **Live URL:** [https://indianartformharinish-3.vercel.app](https://indianartformharinish-3.vercel.app/)
- **Git Branch:** `vercel-project-3`
- **Key Features:**
  - Interactive synthesis environment exploring the convergence of diverse traditional schools.
  - Side-by-side aesthetic comparison between Pahari miniatures, Deccan court paintings, and Bengal School revivals.
  - Live interactive pigment blender simulating natural earth colors on handmade wasli paper textures.

### Assignment 4: Ajanta Frames — Cave Walkthrough & Mural Studies
- **Live URL:** [https://indianartformharinish-4.vercel.app](https://indianartformharinish-4.vercel.app/)
- **Git Branch:** `vercel-project-4`
- **Key Features:**
  - Virtual exploration of the UNESCO World Heritage rock-cut Buddhist monument caves (Caves 1, 2, 16, 17, and 26).
  - High-resolution thematic analysis of iconic masterpieces including *Padmapani*, *Vajrapani*, and the *Mahajanaka Jataka*.
  - Historical conservation notes detailing tempera painting techniques on mud plaster ground.

### Assignment 5: Stone That Speaks — Mahabalipuram 3D Site Walk
- **Live URL:** [https://indianartformharinish-5.vercel.app](https://indianartformharinish-5.vercel.app/)
- **Git Branch:** `vercel-project-5`
- **Key Features:**
  - 3D interactive monument inspection highlighting 7th-century Pallava granite architecture.
  - Dynamic camera navigation with Drone Aerial, Low-angle Bas-relief, and Cinematic Perspective modes.
  - Dedicated virtual tours of the Shore Temple, Descent of the Ganges (*Arjuna's Penance*), and the Pancha Rathas.
  - Downloadable academic paper: *Thematic Analysis of Mahabalipuram Rock Sculptures*.

### Assignment 6: Kolam & Rangoli Studio — 100 Traditional Designs
- **Live URL:** [https://indianartformharinish-6.vercel.app](https://indianartformharinish-6.vercel.app/)
- **Git Branch:** `vercel-project-6`
- **Key Features:**
  - Comprehensive vector catalog containing 100 mathematically authentic Kolam and Rangoli patterns.
  - Interactive grid studio supporting Sikku Kolam (interlaced loops), Pulli Kolam (dot grids), and freehand geometric Rangoli.
  - Step-by-step stroke-order guide with animated drawing simulation.
  - Custom color palette customizer (Kumkum Red, Turmeric Yellow, Neem Green, Indigo Blue, Rice Flour White) with SVG and PNG export capability.

---

## Technical Architecture

- **Client Runtime:** Pure, self-contained HTML5, CSS3, and modern Vanilla ES6+ JavaScript.
- **Zero Heavy Dependencies:** Zero external build step requirements; runs instantly on any standards-compliant browser.
- **Deployment Platform:** Hosted globally on Vercel Edge CDN nodes for sub-100ms first-contentful paint.
- **Branch Isolation:** Each project maintains its own isolated Git branch on GitHub, preventing unintended cross-contamination of academic submissions.

---

## Local Development & Branch Navigation

To inspect or run any specific assignment locally:

```bash
# Clone the repository
git clone https://github.com/harinish45/indianartformharinish-1.git
cd indianartformharinish-1

# View all assignment branches
git branch -a

# Switch to Assignment 1 (Kalākrama)
git checkout main

# Switch to Assignment 2 (Kalābhūmi)
git checkout vercel-project-2

# Switch to Assignment 3 (Sangama)
git checkout vercel-project-3

# Switch to Assignment 4 (Ajanta Frames)
git checkout vercel-project-4

# Switch to Assignment 5 (Mahabalipuram 3D)
git checkout vercel-project-5

# Switch to Assignment 6 (Kolam & Rangoli Studio)
git checkout vercel-project-6
```

Because each assignment is completely self-contained, you can open `index.html` in any web browser without running a local server:

```bash
# Windows
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

---

## Academic Information

- **Student:** Harinish S V
- **GitHub:** [@harinish45](https://github.com/harinish45)
- **Institution:** SRM Institute of Science and Technology
- **Subject:** Indian Art Forms & Cultural Heritage
