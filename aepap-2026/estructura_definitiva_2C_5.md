# ESTRUCTURA DEFINITIVA: Bloques 2C–5

# Seminario AEPap 2026 — Versión post-sesión 2026-02-22

# Estado: EJECUTADO (slides HTML implementadas, audios parcialmente generados)

---

## RESUMEN EJECUTIVO

| Métrica                      | Valor                     |
| ---------------------------- | ------------------------- |
| Total slides visibles        | 54                        |
| Total slides hidden (legacy) | 19                        |
| Bloques                      | 0, 1, 2A, 2B, 2C, 3, 4, 5 |
| Timing estimado              | ~116 min (margen 4 min)   |

**Cambios sesión 2026-02-22:**

- Slide #36 Técnicas de Prompting: recuperada de hidden, insertada entre #35 y GPTs/Gems
- Slide #37 GPTs/Gems: reemplazada con nuevo contenido (era #36)
- Slide #38 Tu Caja de Herramientas: renumerada (era #37), audio-src actualizado
- Pirámide 5.0+Ecosistema sub-slide: eliminada de 2C (duplicada con Demo en Bloque 3)
- IA Agéntica: movida de Bloque 5 a Bloque 2C como #39 (entre Tu Caja y RAG)
- Barras navegación 2C: reordenadas (Cómo preguntar antes de Qué herramienta)
- 19 slides legacy ocultadas con `data-visibility="hidden"` (no borradas)
- Bloque 3 reestructurado: 2 demos (NotebookLM + Pirámide 5.0), Constructor hidden
- Corrección 2B.3: "PI: -31.65 a +41.42" → "Intervalo predicción: −31 a +41"
- Renumeración +1 desde #36 por inserción de Técnicas de Prompting
- Renumeración cascada: 2C #31-#42, B3 #43-#45, B4 #46-#48, B5 #49-#54

---

## ESTRUCTURA SLIDE POR SLIDE

### BLOQUE 0: "Encuadre" (4 slides, ~5 min) — ✅ Cerrado

| Deck# | Menu-title              |   Audio   | Estado |
| :---: | :---------------------- | :-------: | :----: |
|  #1   | Portada                 | ✅ 1.webm |   ✅   |
|  #2   | Conflicto de Intereses  | ✅ 2.webm |   ✅   |
|  #3   | Objetivos del Seminario | ✅ 3.webm |   ✅   |
|  #4   | 🗺️ Hoja de Ruta         | ✅ 4.webm |   ✅   |

### BLOQUE 1: "Ruptura" (4 slides, ~8 min) — ✅ Cerrado

| Deck# | Menu-title             |   Audio   | Estado |
| :---: | :--------------------- | :-------: | :----: |
|  #5   | Bloque 1: Ruptura      | ✅ 5.webm |   ✅   |
|  #6   | Encuesta Inicial       | ✅ 6.webm |   ✅   |
| #7–#8 | Pizarra + Bibliometría |    ✅     |   ✅   |
|  #9   | Historia de Impacto    | ✅ 9.webm |   ✅   |

### BLOQUE 2A: "Fundamentos" (4 slides, ~7 min) — ✅ Cerrado

| Deck# | Menu-title             |   Audio    | Estado |
| :---: | :--------------------- | :--------: | :----: |
|  #10  | Bloque 2A: Fundamentos | ✅ 10.webm |   ✅   |
|  #11  | Glosario IA            | ✅ 11.webm |   ✅   |
|  #12  | Flujo Clínico con IA   | ✅ 12.webm |   ✅   |
|  #13  | ¿Qué es un LLM?        | ✅ 13.webm |   ✅   |

### BLOQUE 2B: "Evidencia" (17 slides, ~25 min) — ✅ Cerrado

| Deck# | Menu-title                        |   Audio    | Estado |
| :---: | :-------------------------------- | :--------: | :----: |
|  #14  | Bloque 2B: Evidencia              | ✅ 14.webm |   ✅   |
|  #15  | Human-in-the-Loop                 | ✅ 15.webm |   ✅   |
|  #16  | Paradigma de Colaboración         | ✅ 16.webm |   ✅   |
|  #17  | Paradoja H+AI                     | ✅ 17.webm |   ✅   |
|  #18  | Psicopatología Humano-IA          | ✅ 18.webm |   ✅   |
|  #19  | Pausa: ¿Experiencias?             | ✅ 19.webm |   ✅   |
|  #20  | Evidencia Actual                  | ✅ 20.webm |   ✅   |
|  #21  | Alucinaciones                     | ✅ 21.webm |   ✅   |
|  #22  | Brecha Exámenes vs Clínica        | ✅ 22.webm |   ✅   |
|  #23  | Riesgo: Dr. AI                    | ✅ 23.webm |   ✅   |
|  #24  | Mapa del Rendimiento              | ✅ 24.webm |   ✅   |
|  #25  | RAG y sesgo                       | ✅ 25.webm |   ✅   |
|  #26  | Diagnóstico Pediátrico            | ✅ 26.webm |   ✅   |
|  #27  | Velocidad ≠ Fiabilidad ≠ Consenso | ✅ 27.webm |   ✅   |
|  #28  | Sesgos Algorítmicos               | ✅ 28.webm |   ✅   |
|  #29  | 🚦 Semáforo IA                    | ✅ 29.webm |   ✅   |
|  #30  | Marco Legal                       | ✅ 30.webm |   ✅   |

### BLOQUE 2C: "Aplicaciones" (12 slides, ~30 min)

Arco narrativo: Lo que funciona → En qué dominios → Cómo medir madurez → Cómo preguntar → Técnicas con datos → Automatiza con GPTs → Con qué herramientas → **IA agéntica: riesgos** → Cómo asegurar → Qué delegar → Resumen

Orden barra de navegación: Dónde empezar → Cómo preguntar → Qué herramienta → Cómo verificar → Qué delegar

|  Deck#  | Menu-title                            |   Audio    | Estado HTML | Notas                                                     |
| :-----: | :------------------------------------ | :--------: | :---------: | :-------------------------------------------------------- |
|   #31   | Bloque 2C: Aplicaciones               | ✅ 31.webm |     ✅      | Portada. Audio-text actualizado con nuevo orden barra     |
|   #32   | Documentación: evidencia sólida       | ✅ 32.webm |     ✅      | Fusión 2C.1+2C.2+2C.8. Zhao MA + pipeline ambiental       |
|   #33   | Aplicaciones por dominio              | ✅ 33.webm |     ✅      | Tabla 4 dominios. Fusión slides individuales              |
|   #34   | Matriz de Madurez                     | ✅ 34.webm |     ✅      | Tabla HTML nativa (sin imagen)                            |
|   #35   | Prompt Engineering clínico            | ⚠️ sin src |     ✅      | Callens + RECORD + determinista. Audio en data-audio-text |
|   #36   | Técnicas de Prompting                 | ⚠️ sin src |     ✅      | **RECUPERADA sesión 22/02.** CoT, RAG, Few-shot, Self-Consistency. 76pp |
|   #37   | GPTs, Gems y personalización          | ✅ 36.webm |     ✅      | **NUEVA sesión 22/02.** Puente #36→#38                    |
|   #38   | Tu Caja de Herramientas               | ✅ 37.webm |     ✅      | Tabla comparativa herramientas. Audio-text actualizado    |
|   #39   | IA Agéntica: Impacto y Control Clínico| ✅ 49.webm |     ✅      | **MOVIDA sesión 22/02** de Bloque 5 a 2C. Taxonomía 3 niveles |
|   #40   | RAG + Whitelisting                    | ✅ 38.webm |     ✅      | Fusión RAG + Whitelisting. Liu JAMIA (no Nat Med)         |
|   #41   | 🚦 Semáforo AP — Consulta             | ⚠️ sin src |     ✅      | Diferente de #29 (investigación vs consulta)              |
|   #42   | Síntesis: 5 mensajes                  | ✅ 40.webm |     ✅      | 5 mensajes accionables. Barra completada con ✅           |

**Nota audio-src:** Los archivos .webm mantienen su nombre original (ej: #37 GPTs usa `36.webm`, #39 IA Agéntica usa `49.webm`, #40 RAG usa `38.webm`). No se han renombrado.

---

### BLOQUE 3: "Demos en Vivo" (3 slides, ~12 min)

**Principio:** Solo lo que se ejecuta en directo ante el público. Sin teoría, sin catálogos.

| Deck# | Menu-title                     |   Audio    | Estado HTML | Notas                                         |
| :---: | :----------------------------- | :--------: | :---------: | :-------------------------------------------- |
|  #43  | Bloque 3: Demos en Vivo        | ⚠️ sin src |     ✅      | Portada. "2 demos: NotebookLM + Pirámide 5.0" |
|  #44  | Demo: NotebookLM Actualización | ⚠️ sin src |     ✅      | Demo en vivo. PubMed → abstracts → podcast    |
|  #45  | Demo: Pirámide 5.0             | ✅ 43.webm |     ✅      | **NUEVA sesión 22/02.** Iframe interactivo    |

Slides hidden en Bloque 3:

- Demo: Método RECORD (redundante con #35 y Bloque 4)
- Demo: Constructor (reemplazada por Demo Pirámide 5.0)
- Pirámide 5.0 (legacy, ya no en 2C)
- Herramientas IA (legacy, migrada a 2C)

---

### BLOQUE 4: "Práctica Guiada" (3 slides, ~20 min)

| Deck# | Menu-title                |   Audio    | Estado HTML |
| :---: | :------------------------ | :--------: | :---------: |
|  #46  | Bloque 4: Práctica RECORD | ⚠️ sin src |     ✅      |
|  #47  | Generador de Prompts      | ⚠️ sin src |     ✅      |
|  #48  | Ejercicio en Grupos       | ⚠️ sin src |     ✅      |

---

### BLOQUE 5: "Cierre" (6 slides, ~12 min)

**Cambio sesión 22/02:** IA Agéntica movida a Bloque 2C como #39 (ya no en Bloque 5).

| Deck# | Menu-title        |   Audio    | Estado HTML | Notas                        |
| :---: | :---------------- | :--------: | :---------: | :--------------------------- |
|  #49  | Bloque 5: Cierre  | ⚠️ sin src |     ✅      | Portada                      |
|  #50  | Modelo Sándwich   | ⚠️ sin src |     ✅      | Deliberación pre-algorítmica |
|  #51  | Lo que nos llevamos | ⚠️ sin src |   ✅      | 3 takeaways                  |
|  #52  | Pregunta Test 1   | ⚠️ sin src |     ✅      | GEA familias                 |
|  #53  | Pregunta Test 2   | ⚠️ sin src |     ✅      | Verificación crítica         |
|  #54  | Gracias           | ⚠️ sin src |     ✅      | Cierre                       |

---

## TIMING DEFINITIVO

| Bloque           |     Slides      |   Deck#    |   Min    |          Estado          |
| ---------------- | :-------------: | :--------: | :------: | :----------------------: |
| 0: Encuadre      |        4        |   #1–#4    |    ~5    |        ✅ Cerrado        |
| 1: Ruptura       |        4        |   #5–#9    |    ~8    |        ✅ Cerrado        |
| 2A: Fundamentos  |        4        |  #10–#13   |    ~7    |        ✅ Cerrado        |
| 2B: Evidencia    |       17        |  #14–#30   |   ~25    |        ✅ Cerrado        |
| 2C: Aplicaciones |       12        |  #31–#42   |   ~30    |  HTML ✅, audio parcial  |
| 3: Demo en vivo  |        3        |  #43–#45   |   ~12    |  HTML ✅, audio parcial  |
| 4: Práctica      |        3        |  #46–#48   |   ~20    | HTML ✅, audio pendiente |
| 5: Cierre        |        6        |  #49–#54   |   ~10    |  HTML ✅, audio parcial  |
| **TOTAL**        | **54 visibles** | **#1–#54** | **~117** |    **Margen: 3 min**     |

Nota: 54 slides visibles, sin sub-slides. IA Agéntica movida de B5 a 2C como #39.

---

## SLIDES HIDDEN (19 total, con data-visibility="hidden")

Estas slides permanecen en el HTML pero son invisibles en la presentación. Se pueden reactivar eliminando el atributo `data-visibility="hidden"`.

| Menu-title                |     Zona      | Motivo                                        |
| :------------------------ | :-----------: | :-------------------------------------------- |
| Context Engineering       | Post-Síntesis | Absorbida en #35 (prompting)                  |
| Mapa 2025-2026            | Post-Síntesis | Absorbida en #38 (herramientas)               |
| Ecosistema IA 2026        | Post-Síntesis | Absorbida en #38 (herramientas)               |
| Documentación y evidencia | Post-Síntesis | Redundante con #32                            |
| Diagnóstico precoz AP     | Post-Síntesis | Absorbida en #33 (dominios)                   |
| Pediatría                 | Post-Síntesis | Absorbida en #33 (dominios)                   |
| Riesgo suicida            | Post-Síntesis | Absorbida en #33 (dominios)                   |
| Educación médica          | Post-Síntesis | Absorbida en #33 (dominios)                   |
| Prompting determinista    | Post-Síntesis | Absorbida en #35 (prompting)                  |
| RAG como estándar         | Post-Síntesis | Absorbida en #40 (RAG+Whitelisting)           |
| Whitelisting Fuentes      | Post-Síntesis | Absorbida en #40 (RAG+Whitelisting)           |
| Futuro Híbrido            | Post-Síntesis | Redundante con #41/#42                        |
| 🚦 Semáforo AP            | Post-Síntesis | Reemplazada por #41 (versión Consulta)        |
| Síntesis                  | Post-Síntesis | Reemplazada por #42 (5 mensajes)              |
| Pirámide 5.0              |   Bloque 3    | Legacy; Demo Pirámide 5.0 (#45) la reemplaza  |
| Herramientas IA           |   Bloque 3    | Migrada a 2C como #38                         |
| Demo: Método RECORD       |   Bloque 3    | Redundante con #35 y Bloque 4                 |
| Demo: Constructor         |   Bloque 3    | Reemplazada por Demo Pirámide 5.0 (#45)       |
| IA Agéntica (original)    |       —       | Movida a Bloque 2C como #39 (ya no hidden)    |

**Nota:** "Técnicas de Prompting" ya no está hidden — recuperada como slide visible #36.

---

## PENDIENTES PARA PRÓXIMA SESIÓN

### Audio pendiente

- #35 Prompt Engineering: tiene data-audio-text pero sin data-audio-src
- #36 Técnicas de Prompting: tiene data-audio-text pero sin data-audio-src
- #41 Semáforo AP Consulta: tiene data-audio-text pero sin data-audio-src
- #43 Portada Bloque 3: sin data-audio-src
- #44 Demo NotebookLM: sin data-audio-src
- #46–#48 Bloque 4: sin data-audio-src
- #49–#50, #51–#54 Bloque 5: sin data-audio-src

### Correcciones pendientes

- Refs tabla Matriz (#34): Nguyen, Ilić & Sarajlija, Var — buscar DOIs
- Refs tabla dominios (#33): verificar DOIs de cada estudio
- 2B.14 (Consenso Clínico): decidir si eliminar por duplicación con #27
- Liu JAMIA: verificar que source-note en #40 dice "JAMIA" y no "Nat Med"

---

## INSTRUCCIONES PARA CLAUDE EN PRÓXIMA SESIÓN

```
Proyecto AEPap 2026 — Fase ejecución.

Audio completado: Bloques 0–2B (#1–#30) + parcial 2C (#31–#34, #37–#39, #42).
Estructura consolidada: ver estructura_definitiva_2C_5.md
19 slides legacy ocultas con data-visibility="hidden" (no borradas).
IA Agéntica movida a Bloque 2C como #39 (entre Tu Caja y RAG).
Sub-slide Pirámide 5.0 eliminada de 2C (duplicada con Demo #45).
Bloque 3 reestructurado: NotebookLM + Pirámide 5.0 interactiva.
Técnicas de Prompting recuperada como #36 (era hidden).

IMPORTANTE: Los archivos .webm NO fueron renombrados. La correspondencia es:
  #37 GPTs → 36.webm | #38 Tu Caja → 37.webm | #39 IA Agéntica → 49.webm
  #40 RAG → 38.webm | #42 Síntesis → 40.webm | #45 Demo Pirámide → 43.webm

Bloques pendientes de audio:
- 2C: #35, #36 y #41 (audio-text existe, falta generar .webm)
- 3: #43 y #44 (audio-text existe, falta generar .webm)
- 4: #46–#48 (audio-text existe, falta generar .webm)
- 5: #49–#50, #51–#54 (audio-text existe, falta generar .webm)

Prioridad: generar audios .webm para slides que ya tienen data-audio-text.
Numeración absoluta (#1–#54). Fonética TTS española.
Archivo HTML: ia-pediatria-aepap-2026.html (en raíz del repo t/).
```

---

*Documento actualizado: 2026-02-22. Vigente hasta próxima sesión.*
