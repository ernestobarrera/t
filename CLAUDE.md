# Proyecto AEPap 2026 — Contexto para Claude Code

## Qué es esto

Presentación Reveal.js: seminario "La IA como Asistente del Pediatra de AP",
22º Congreso AEPap, 3 de marzo de 2026, 120 minutos.
54 slides con audio narrado por TTS ("Paco") + ponente en vivo (Ernesto).

## Archivo principal

`ia-pediatria-aepap-2026.html` — FUENTE DE VERDAD para estructura y layout.
NO reescribir secciones completas. Solo ediciones mínimas (delta).

## Audios

- Carpeta: `aepap-2026/audios/`
- Extensión actual: `.webm`
- Slides #1-#30: audio grabado, NO TOCAR
- Slides #31-#54: en proceso de grabación
- Si falta el .webm, el plugin usa `data-audio-text` como fallback TTS

## Correspondencia audio-src (nombres legacy)

Algunos .webm no coinciden con su número de slide:
- #37 GPTs → 36.webm
- #38 Tu Caja → 37.webm
- #39 IA Agéntica → 49.webm
- #40 RAG → 38.webm
- #42 Síntesis → 40.webm
- #45 Demo Pirámide → 43.webm

El resto: #N usa N.webm.

## Reglas TTS para data-audio-text

- Todo en UNA SOLA LÍNEA (sin \n) — el motor TTS se para con saltos de línea
- Fonética española para siglas: i-a (no IA), erre-a-ge (no RAG),
  ele-ele-eme (no LLM), ge-pe-te (no GPT), yámia (JAMIA), ene-pe-jota (npj)
- Números siempre en letra: "treinta y dos por ciento"
- No usar "último/más reciente/actual" (caduca)
- No "odds" → "probabilidad"

## CSS custom — respetar siempre

glass-panel, text-gradient, assertion-title, grid-2, metric-value,
abbr-tip, source-note, wide-slide, section-intro, clickable-output-card

## Estructura de bloques

| Bloque | Slides | Estado audio |
|--------|--------|-------------|
| 0 Encuadre | #1-#4 | ✅ completo |
| 1 Ruptura | #5-#9 | ✅ completo |
| 2A Fundamentos | #10-#13 | ✅ completo |
| 2B Evidencia | #14-#30 | ✅ completo |
| 2C Aplicaciones | #31-#42 | parcial |
| 3 Demos | #43-#45 | parcial |
| 4 Práctica | #46-#48 | pendiente |
| 5 Cierre | #49-#54 | pendiente |

## Reglas de seguridad

- SIEMPRE backup antes de editar
- Nunca reescribir secciones completas — solo deltas mínimos
- Verificar con grep después de cada cambio
- Si algo falla, restaurar backup y parar
- Ante la duda, PREGUNTAR a Ernesto
