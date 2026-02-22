---
description: Sincronización obligatoria de cambios entre presentación HTML y guiones de audio TTS
---

# Regla de sincronización: Presentación ↔ Audio Scripts

## Regla fundamental

**Todo cambio de contenido, estructura u orden en `ia-pediatria-aepap-2026.html` DEBE reflejarse también en:**

1. **`opentts_aepap_audios.html`** — array `audios[]` con los textos TTS
2. **`guion_locuciones_aepap_2026.md`** — guion en markdown

## Qué cambios disparan la sincronización

- Añadir, eliminar o reordenar slides
- Modificar datos, cifras o referencias en una slide existente
- Cambiar el `data-audio-text` de una slide
- Renombrar secciones o bloques
- Añadir contenido conceptual nuevo (incluso dentro de una slide existente)

## Cómo sincronizar

1. Identificar la slide afectada por su número secuencial (00-72+)
2. Actualizar el texto en `opentts_aepap_audios.html` (campo `text` del objeto correspondiente)
3. Actualizar el mismo texto en `guion_locuciones_aepap_2026.md` (sección correspondiente)
4. Si se añaden/eliminan slides, renumerar el array `audios[]` y actualizar `guion_locuciones_aepap_2026.md`
5. **Recordar al usuario** que los archivos de audio ya generados pueden necesitar regeneración

## Convenciones de los textos TTS

- Sin abreviaturas: escribir todo expandido
- Números < 10 en letra; > 10 en formato "X con Y" para decimales
- Sin marcadores `[PAUSA]` — usar puntuación natural
- Adaptar contenido interactivo para escucha offline
