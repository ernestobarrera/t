# Creación de Audios con OpenTTS

Guía para generar audios de narración para presentaciones Reveal.js usando el servicio [OpenTTS.ai](https://www.opentts.ai/).

## Configuración Recomendada

| Parámetro | Valor |
|-----------|-------|
| **URL** | https://www.opentts.ai/ |
| **Voice** | Google ESPAÑOL |
| **Rate** | 1.1 |
| **Pitch** | 1.0 |

## Flujo de Trabajo

1. **Preparar textos**: Usar la herramienta `opentts_textos_audio.html` que extrae y formatea los textos de cada diapositiva
2. **Generar audios**: Copiar cada texto, pegarlo en OpenTTS.ai con la configuración indicada
3. **Descargar y nombrar**: Guardar cada audio con el nombre indicado en la herramienta
4. **Organizar archivos**: Colocar los audios en la carpeta correspondiente de `assets/`

## Archivos de Referencia

- [`opentts_textos_audio.html`](../../opentts_textos_audio.html) — Herramienta web con los textos listos para copiar
- [`plantilla_opentts.html`](./plantilla_opentts.html) — Plantilla para crear nuevas herramientas de extracción

## Notas

- El formato `.webm` es ideal para web por su compresión eficiente
- También se puede usar `.mp3` si se prefiere compatibilidad universal
- La herramienta incluye seguimiento de progreso con localStorage