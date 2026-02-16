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
├── chi-sono.html       # About page (senza foto profilo)
├── progetti.html       # Projects page (4 card solo icone)
├── cv.html             # CV/Resume page
├── contatti.html       # Contact page
├── css/
│   ├── styles.css      # Main styles + Cookie banner
│   └── animations.css  # Animation library
├── js/
│   └── main.js         # JavaScript + Cookie consent
├── images/             # Logo CMC aggiornato
└── assets/             # CV PDF e PDF progetti
```

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

#### Modifiche Finali
- ✅ Logo SVG aggiornato (scritta allineata)
- ✅ Rimossa foto profilo da Chi Sono
- ✅ Rimossa anteprima immagine Grafica
- ✅ Cookie banner GDPR con bordo oro
- ✅ Footer invariato

---

### Test Results - FINALE
- Frontend: 98% ✓
- Tutte le pagine accessibili ✓
- Navigazione funzionante ✓
- Cookie banner visibile ✓
- Form validati ✓
- Animazioni funzionanti ✓

---

### URL Preview
`https://cmc-portfolio.preview.emergentagent.com/api/site/index.html`

### Pagine
- Home: `/api/site/index.html`
- Chi Sono: `/api/site/chi-sono.html`
- Progetti: `/api/site/progetti.html`
- CV: `/api/site/cv.html`
- Contatti: `/api/site/contatti.html`
