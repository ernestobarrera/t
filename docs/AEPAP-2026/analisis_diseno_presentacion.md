# Análisis del Diseño de la Presentación AEPap 2026

> Basado en: `informe_presentaciones_cientificas_evidencia.md`

## Estado Actual

La presentación `ia-pediatria-aepap-2026.html` tiene:
- **5 Bloques** correctamente estructurados (120 min)
- **Estilo Glassmorphism** con paleta azul-verde-ámbar
- **Plugins Reveal.js** configurados (audio, menu, chalkboard)

---

## Diagnóstico según Principios del Informe

### ✅ Fortalezas Actuales

| Criterio | Estado |
|----------|--------|
| Estructura narrativa (5 bloques) | ✅ Bien definida |
| Pausas interactivas | ✅ Encuestas y votaciones |
| Elementos visuales (iconos, badges) | ✅ Consistentes |
| Material de apoyo (QR, descargables) | ✅ Planificados |

### ⚠️ Áreas de Mejora Detectadas

| Problema | Principio Violado | Slide(s) Afectadas |
|----------|-------------------|-------------------|
| Titulares tipo "tema" en lugar de "enunciado" | Cadena B: Claridad argumental | Múltiples |
| Listas largas sin evidencia visual | Carga extránea excesiva | Glosario IA, Herramientas |
| Texto redundante con lo que se dice | Efecto de redundancia | Varias |
| Métricas sin contexto visual | Evidencia visual explicativa | Alucinaciones |
| Falta de segmentación progresiva | Interactividad de elementos | RECORD |
| Contraste insuficiente en algunos textos | Diseño perceptivo | `.text-muted` muy tenue |

---

## Mejoras Específicas Propuestas

### 1. Titulares-Enunciado (Prioridad Alta)

**Antes:**
```html
<h2>¿Qué es un LLM?</h2>
```

**Después:**
```html
<h2>Los LLM predicen palabras, no comprenden significados</h2>
<p class="subtitle">Large Language Model = Modelo de Lenguaje Grande</p>
```

### 2. Reducir Densidad de Texto

**Antes:** Glosario con 6 cards de texto
**Después:** Máximo 3-4 conceptos por slide, revelar progresivamente con `class="fragment"`

### 3. Evidencia Visual para Métricas

**Antes:**
```html
<div class="metric-value">60.6%</div>
<div class="metric-label">Referencias fabricadas</div>
```

**Después:** Añadir barra visual o icono que represente la magnitud

### 4. Mejora de Contraste CSS

```css
--text-muted: #94a3b8;  /* Actual - bajo contraste */
--text-muted: #b0c4d8;  /* Propuesto - WCAG AA */
```

### 5. Segmentación del Método RECORD

Actualmente: 6 cards en una sola slide
Propuesta: Revelar paso a paso con animación `appearance`

---

## Checklist de Implementación

- [ ] Convertir titulares clave a formato enunciado
- [ ] Reducir densidad en slides con listas
- [ ] Añadir `class="fragment"` para revelado progresivo
- [ ] Mejorar contraste de `--text-muted`
- [ ] Añadir elementos visuales a métricas
- [ ] Revisar que cada slide tenga UNA idea clara

---

*Documento creado: 2026-01-24*
*Referencia: informe_presentaciones_cientificas_evidencia.md*
