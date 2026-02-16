# CMC Portfolio - Martina Caputo
## Product Requirements Document

### Problema Originale
Perfezionamento di un sito portfolio HTML statico per esame universitario. Il sito era stato creato con Manus ma la qualità non era soddisfacente. Richiesto miglioramento di:
- Animazioni e transizioni
- Tipografia
- Spaziature e allineamenti
- Interattività (hover, click effects)
- Responsive design

**Vincoli**: Mantenere colori originali (oro #cda741, sfondo #0F0F0F) e layout di base.

---

### Architettura
- **Frontend**: HTML5 + CSS3 + JavaScript vanilla
- **Backend**: FastAPI (serve file statici)
- **Hosting**: File serviti su `/api/site/`

### Struttura File
```
/app/site/
├── index.html          # Homepage
├── chi-sono.html       # About page
├── progetti.html       # Projects page
├── cv.html             # CV/Resume page
├── contatti.html       # Contact page
├── css/
│   ├── styles.css      # Main styles
│   └── animations.css  # Animation library
├── js/
│   └── main.js         # JavaScript interactions
├── images/             # Logo e immagini
└── assets/             # CV PDF e PDF progetti
```

---

### User Personas
1. **Professore/Esaminatore**: Valuta qualità tecnica del sito
2. **Potenziale Cliente/Datore**: Cerca designer UX/UI
3. **Recruiter**: Valuta competenze e portfolio

### Core Requirements
- [x] Sito responsive mobile-first
- [x] Animazioni fluide e professionali
- [x] Navigazione intuitiva
- [x] Download CV funzionante
- [x] Form contatti validato
- [x] Link social funzionanti
- [x] SEO base (meta tags, OG tags)

---

### Implementato (16 Feb 2026)

#### Miglioramenti CSS
- CSS Variables per tema coerente
- Custom scrollbar stilizzata
- Smooth scroll behavior
- Focus states per accessibilità
- Gradient text e button effects
- Box-shadow e glow effects

#### Animazioni
- Logo float animation con glow
- Scroll reveal (fadeInUp, fadeInLeft, fadeInRight)
- Staggered animations per grids
- Ripple effect sui buttons
- Hover transitions su cards e buttons
- Skills carousel con pause on hover
- FAQ accordion smoothing

#### Tipografia
- Font pairing: Cinzel (headings) + Montserrat (body)
- Line-height e letter-spacing ottimizzati
- Text shadow per headings

#### Interattività
- Menu hamburger animato con overlay
- FAQ accordion
- Form validation con feedback
- Hover effects sofisticati

---

### Test Results
- Backend: 100% ✓
- Frontend: 98% ✓
- All pages accessible
- Navigation working
- Forms validated
- Animations functional

---

### Backlog / Future Improvements

#### P0 (Critical)
- Nessuno

#### P1 (Important)
- Aggiungere foto profilo reale in chi-sono.html
- Aggiungere immagini preview dei progetti

#### P2 (Nice to have)
- Dark/Light mode toggle
- Multilingua (IT/EN)
- Loading animation iniziale
- Particle effects sfondo
- Cookie banner GDPR

---

### URL Preview
`https://cmc-portfolio.preview.emergentagent.com/api/site/index.html`

### Repository Originale
`https://github.com/martinacaputo93-design/CMC`
