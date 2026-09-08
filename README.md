<div align="center">

# 🎨 Kalākrama (KalaBhumi)

**Interactive Digital Heritage, Chronological Timeline & Regional Taxonomy of Indian Traditional Art**

[![HTML5](https://img.shields.io/badge/HTML5-Semantic-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-Custom_Design_System-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Typography](https://img.shields.io/badge/Typography-Rozha_One_%26_Work_Sans-D9B36A?style=for-the-badge)](https://fonts.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

</div>

---

## 🌟 Executive Summary

**Kalākrama (KalaBhumi)** is a digital humanities curation and interactive web portal dedicated to preserving and celebrating traditional Indian art forms. Spanning millennia of cultural evolution—from prehistoric rock shelters to classical court miniatures and indigenous tribal expressions—Kalākrama presents an accessible, chronologically indexed timeline accompanied by high-resolution visual analysis and regional geographical mappings.

---

## 🏛️ Cultural & Art Traditions Featured

```mermaid
graph TD
    subgraph AncientEra ["Prehistoric & Ancient Foundations"]
        Bhimbetka["Bhimbetka Petroglyphs (10,000 BCE)"]
        IndusSeal["Indus Valley Terracotta & Seals (2500 BCE)"]
        Ajanta["Ajanta Murals & Frescoes (2nd C. BCE)"]
    end

    subgraph MedievalRenaissance ["Classical & Court Traditions"]
        Chola["Chola Bronzes & Temple Sculpture"]
        Mughal["Mughal & Rajput Miniatures"]
        Tanjore["Thanjavur Gold Leaf Paintings"]
    end

    subgraph TribalFolk ["Living Tribal & Regional Folk Arts"]
        Madhubani["Mithila / Madhubani (Bihar)"]
        Warli["Warli Tribal Art (Maharashtra)"]
        Pattachitra["Pattachitra Scroll Painting (Odisha)"]
        Gond["Gond Folk Art (Madhya Pradesh)"]
        Kalamkari["Kalamkari Block Print & Pen Art (Andhra)"]
    end

    AncientEra --> MedievalRenaissance --> TribalFolk
```

---

## ✨ Key Capabilities

- **Fluid Chronological Timeline:** Seamlessly navigate between major epochs of Indian artistic history with smooth hardware-accelerated transitions.
- **Bespoke Heritage Design System:** Tailored dark-paper palette (`#0e1016` background with `#d9b36a` gold accents), radial ambient glows, and paired Devanagari typography (`Rozha One` display and `Work Sans` body).
- **Interactive Art Gallery & Modal Inspector:** High-definition inspection of stylistic motifs, natural pigment techniques (indigo, lampblack, ochre, vermilion), and regional materials.
- **Zero-Dependency Architecture:** Pure semantic HTML5, modern CSS3 variables, and vanilla ES6 JavaScript—instant loading with zero build steps or npm baggage.

---

## 📂 Repository Structure

```
indianartformharinish-1/
├── index.html                  # Main interactive timeline & portal experience (Kalākrama)
├── kalabhumi.html              # Comprehensive regional folk art directory & showcase
├── AGENTS.md                   # AI pair-programming & design tokens guide
├── PRD.md                      # Product Requirements Document
├── TODO.md                     # Actionable engineering tasks
└── LICENSE                     # MIT License
```

---

## 🚀 Quick Start

No package manager or build pipeline required!

### Option 1: Direct Browser Launch
Simply double-click `index.html` or open it in any modern web browser:
```bash
start index.html # On Windows
```

### Option 2: Local HTTP Server
```bash
npx serve .
# Or using Python:
python -m http.server 8000
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.
