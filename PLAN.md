# Plan: Lo que queda para mañana (1 marzo) y post-congreso

## Estado actual después de la sesión del 28/02

### Completado hoy:
- Reorden B5: Sándwich → Test1 → Test2 → Takeaways → Gracias
- 12 data-audio-src insertados (35, 36, 44, 46-54)
- data-audio-text actualizado para #41-#54
- Timing B5 cambiado de 20 a 10 minutos
- Test 1/2: respuesta oculta hasta clic (reveal-correct)
- Texto visible #42 msg2 limpiado
- Push a rama `claude/edit-revealjs-presentation-aglRI`

### Lo que falta:

---

## A. AUDIOS PENDIENTES DE GRABAR (3 archivos .webm)

Faltan los archivos para las 3 últimas slides. Sin ellos, usarán TTS fallback.

| Slide | Archivo | data-audio-text ya listo |
|-------|---------|-------------------------|
| Pregunta Test 2 | `52.webm` | "Segunda pregunta. ¿Cuál es el riesgo principal de la paradoja humano más i-a?" |
| Lo que nos llevamos | `53.webm` | "Tres mensajes para llevaros a casa..." (texto largo, ~30s) |
| Gracias | `54.webm` | "Ha sido un placer acompañaros..." |

**Prioridad**: ALTA si quieres que suenen con la voz de Paco y no con TTS genérico.
Los textos ya están definidos en el HTML. Solo hay que grabarlos.

---

## B. REVISIÓN data-audio-text #1-#30 vs LIBRETO

Los .webm de #1-#30 están grabados y no se tocan. Pero los `data-audio-text`
(fallback TTS) podrían no coincidir con lo que dice el libreto/plot twist de Paco.

### ¿Es urgente?
- **Para el congreso del 3 de marzo: NO.** Si los .webm funcionan, el TTS
  fallback nunca se activa. Los data-audio-text solo importan si falla un .webm.
- **Para post-congreso: SÍ** (ver sección D).

### Para hacerlo necesitamos:
1. El libreto (`libreto_v2_produccion.md`) — está en la memoria del proyecto
   Claude, no en el repo. Habría que pegarlo o compartirlo.
2. Comparar slide a slide los textos de 🤖 PACO del libreto con los
   data-audio-text actuales del HTML.
3. Actualizar los que difieran (respetando reglas TTS: una línea, fonética).

### Estimación: ~14 slides podrían diferir
Las slides #1-#4 (encuadre), #5 (ruptura), #6 (encuesta), #9 (historias),
#19 (pausa) son las más probables por tener narrativa de Paco con personalidad.

---

## C. PROBLEMA SLIDE #28: FRAGMENT LEÍDO POR TTS

### El problema:
La slide "Sesgos Algorítmicos" (#28) tiene un `<div class="glass-panel fragment">`
(línea 4454) con texto "Ejemplos pediátricos: dermatitis en piel oscura...".
Cuando el .webm falla y el TTS lee, este div genera una segunda lectura automática
al hacer clic.

### Solución propuesta:
El plugin `audio-slideshow` de Reveal.js **SÍ soporta audio en fragments**.
Se puede añadir `data-audio-src` o `data-audio-text` directamente al `<div>` del fragment:

```html
<div class="glass-panel fragment"
     data-audio-src="aepap-2026/audios/28b.webm"
     style="...">
```

**Opciones:**
1. **Grabar 28b.webm** con Paco leyendo el texto del fragment (lo más limpio)
2. **Añadir `data-audio-text` al fragment** con el texto en formato TTS (solución rápida)
3. **Silenciar el fragment**: `data-audio-src="aepap-2026/audios/silence.webm"` (si no quieres que se lea)

**Recomendación**: Opción 2 como solución rápida para el congreso, opción 1 para post-congreso.

---

## D. ESTRATEGIA POST-CONGRESO: SUBCARPETA DE AUDIOS ALTERNATIVOS

### Concepto:
Crear `aepap-2026/audios/postcongreso/` con versiones alternativas SOLO
de los slides que tienen contenido "en vivo". El HTML principal mantiene los
audios del congreso. Para la versión post-congreso, se copian los archivos
de la subcarpeta sobre los originales (o se cambia la ruta en el HTML).

### Slides que necesitan versión post-congreso (7 audios):

| # | Slide | Problema | Qué cambia |
|---|-------|----------|------------|
| 4 | Hoja de Ruta | "práctica guiada en grupos" | → "práctica con casos" |
| 6 | Encuesta Inicial | "Levantad la mano o responded en Mentimeter" | → eliminar interacción, reformular |
| 19 | Pausa: ¿Experiencias? | "¿alguno de vosotros ha tenido..." | → eliminar pregunta al público |
| 44 | Demo: NotebookLM | "Ernesto os cuenta cómo lo usa" | → "Podéis probarlo vosotros mismos" (o similar) |
| 45 | Demo: Pirámide 5.0 | "Ernesto os lo muestra" | → "Exploradlo en la versión interactiva" |
| 46 | Bloque 4: Práctica | "habla el auditorio" | → reformular para autoestudio |
| 48 | Generador RECORD | referencia a práctica en sala | → reformular para uso individual |

### Workflow propuesto:
```
1. Crear carpeta: aepap-2026/audios/postcongreso/
2. Escribir los 7 guiones alternativos (solo las frases que cambian)
3. Grabar los 7 .webm con la misma voz de Paco
4. Guardar como: postcongreso/4.webm, postcongreso/6.webm, etc.
5. Para activar versión post-congreso:
   cp aepap-2026/audios/postcongreso/*.webm aepap-2026/audios/
   (o crear un script que lo haga)
```

### Alternativa más limpia (sin copiar archivos):
Crear `ia-pediatria-aepap-2026-postcongreso.html` con un find-replace
de las 7 rutas de audio:
```
aepap-2026/audios/4.webm → aepap-2026/audios/postcongreso/4.webm
```
Y actualizar también los 7 `data-audio-text` correspondientes.
Así ambas versiones coexisten sin pisar archivos.

**Recomendación**: La alternativa del HTML duplicado con rutas cambiadas es más
segura. No hay riesgo de sobreescribir los audios originales del congreso.

---

## E. RESUMEN: CHECKLIST PARA MAÑANA (1 marzo)

### Crítico (sin esto la presentación tiene huecos):
- [ ] Grabar 52.webm, 53.webm, 54.webm
- [ ] Decidir sobre slide #28 (fragment + audio)
- [ ] Test end-to-end de la presentación completa

### Importante (mejora la robustez):
- [ ] Actualizar data-audio-text #1-#30 para que coincidan con libreto
      (necesito acceso al libreto para comparar)
- [ ] Verificar escuchando que los 6 audios legacy (#37-#40, #42, #45) suenan
      en la slide correcta

### Post-congreso (puede esperar al 4 de marzo):
- [ ] Crear subcarpeta `aepap-2026/audios/postcongreso/`
- [ ] Escribir 7 guiones alternativos para slides con handoffs
- [ ] Grabar 7 .webm post-congreso
- [ ] Crear HTML post-congreso con rutas actualizadas

---

## F. ERROR DETECTADO

### CLAUDE.md desactualizado (mapeo legacy):
El CLAUDE.md dice que ciertos slides usan nombres legacy de audio:
```
#37 GPTs → 36.webm    (HTML dice 37.webm)
#38 Tu Caja → 37.webm (HTML dice 38.webm)
#39 IA Agéntica → 49.webm (HTML dice 39.webm)
#40 RAG → 38.webm     (HTML dice 40.webm)
#42 Síntesis → 40.webm (HTML dice 42.webm)
#45 Demo Pirámide → 43.webm (HTML dice 45.webm)
```

**El HTML apunta a nombres secuenciales, no a los legacy.** Tú dices que
"los audios se corresponden", así que entiendo que renombraste los archivos
o que el mapeo legacy ya no aplica. En cualquier caso, el CLAUDE.md debería
actualizarse para evitar confusiones futuras (eliminar esa sección o marcarla
como obsoleta).

**Verificación recomendada**: Escuchar 30 segundos de los audios 37.webm,
38.webm, 39.webm, 40.webm, 42.webm y 45.webm para confirmar que corresponden
a sus slides.
