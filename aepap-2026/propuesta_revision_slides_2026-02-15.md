# Propuesta de Revisión — Slides 10-57 (Bloques 2A, 2B, 2C)

**Fecha**: 2026-02-15
**Autor**: Claude Opus (revisión asistida)
**Principio rector**: Cada slide debe funcionar como ancla visual del discurso: headline assertivo → dato clave → implicación clínica → puente narrativo.

---

## ÍNDICE

- [A. Resumen ejecutivo](#a-resumen-ejecutivo)
- [B. Referencias mal construidas (todas las slides)](#b-referencias-mal-construidas)
- [C. Propuestas por batch de slides](#c-propuestas-por-batch)
  - [Batch 1: Slides 10-13 (Bloque 2A — Fundamentos)](#batch-1-slides-10-13)
  - [Batch 2: Slides 14-18 (Bloque 2B — Evidencia inicial)](#batch-2-slides-14-18)
  - [Batch 3: Slides 20-27 (Bloque 2B — Evidencia central)](#batch-3-slides-20-27)
  - [Batch 4: Slides 29-36 (Semáforo + Regulatorio)](#batch-4-slides-29-36)
  - [Batch 5: Slides 37-44 (Bloque 2C — Aplicaciones I)](#batch-5-slides-37-44)
  - [Batch 6: Slides 45-57 (Bloque 2C — Aplicaciones II + Síntesis)](#batch-6-slides-45-57)
- [D. Tabla resumen de cambios](#d-tabla-resumen)

---

## A. Resumen ejecutivo

### Diagnóstico general

Las slides de los bloques 2A-2C están **bien estructuradas en contenido y jerarquía visual**. La mayoría ya usa el patrón `assertion-title` + `subtitle` + contenido + `source-note`. Los principales problemas detectados son:

1. **Referencias mal construidas** (10+ slides): DOI desnudos como anchor text, referencias tipo `1021:#2` incomprensibles para el público, y ausencia de DOI en citas que deberían tenerlo.
2. **Slides telegráficas sin implicación visible** (especialmente 45-54): Muchas tienen un `<strong>Acción:</strong>` genérico que no traduce el dato a la práctica del pediatra de AP.
3. **Títulos descriptivos residuales** (pocas, pero las hay): Algunas slides usan títulos que nombran un tema en lugar de afirmar una conclusión.
4. **Sobrecarga de datos en algunas slides** (20, 26): Más de 3 cifras compitiendo visualmente sin jerarquía clara.
5. **Puentes narrativos ausentes**: La mayoría de slides no anticipan visualmente la siguiente.

### Lo que funciona bien (NO TOCAR)

- Estructura `has-title-wrapper` + `assertion-title` + `subtitle` es excelente
- Jerarquía visual con `metric-value`, `glass-panel`, `grid-2/3` está bien aplicada
- Slides de infografía (28, 30, 52, 53, 56) son visualmente potentes
- Slides regulatorias (33-36) están muy bien construidas
- Las slides de Human-in-the-Loop (15-17) ya tienen headlines assertivos

---

## B. Referencias mal construidas

### Problema crítico: DOI como anchor text

Varias slides usan el DOI como texto del enlace en lugar del nombre del estudio. Esto es ilegible para el público.

| Línea HTML aprox. | Slide | Texto actual del enlace | Debería decir |
|---|---|---|---|
| 2316 | RAG y sesgo (~25) | `<a href="...">DOI</a>` | `Orthopaedic J 2025` |
| 3460 | Diagnóstico precoz (~46) | `<a href="...">DOI</a>` | `npj Digit Med 2026` |
| 3519 | Pediatría (~47) | `<a href="...">DOI</a>; <a href="...">DOI</a>; <a href="...">DOI</a>` | `Lancet Digit Health 2025 \| BMJ Ophth 2025 \| PLoS ONE 2025` |
| 3567 | Caries escolar (~48) | `<a href="...">DOI</a>` | `BMC Oral Health 2025` |
| 3607 | Riesgo suicida (~49) | `<a href="...">DOI</a>` | `JMIR 2025` |
| 3656 | Educación médica (~50) | `<a href="...">DOI</a>` | `BMC Med Educ 2025` |
| 3699 | Prompting determinista (~51) | `<a href="...">DOI</a>` | `Front AI 2025` |

### Problema: Referencias tipo `1021:#N` sin contexto

Varias slides usan identificadores internos de la revisión bibliográfica que son incomprensibles para el público.

| Línea HTML aprox. | Slide | Texto actual | Debería decir |
|---|---|---|---|
| 3324 | Mapa 2025-2026 (~43) | `1021:#2` | `Shool et al. BMC Med Inform 2025` |
| 3377-3378 | Ecosistema IA (~44) | `1021:#3` y `1021:#5` | `Sandmann et al. Nat Med 2025` y `Liu et al. Nat Med 2025` |
| 3901-3906 | Síntesis (~57) | `1021:#2`, `1021:#3`, `1021:#5` + 3× `DOI` | Nombres completos de cada referencia |

### Problema: Refs sin DOI que deberían tenerlo

| Slide | Texto actual | DOI correcto (de la bibliografía) |
|---|---|---|
| Oxígeno consulta (~38) | `Zhao J, et al. BMC Med Inform Decis Mak. 2025` (sin enlace) | `10.1186/s12911-025-03324-w` |
| IA Ambiental (~39) | `Zhao J, et al. 2025 · Dave B, et al. 2025` (sin enlaces) | Zhao: `10.1186/s12911-025-03324-w` · Dave: `10.1016/j.ijmedinf.2025.106122` |
| Prompt Engineering (~40) | `Callens S, et al. 2026` (sin enlace) | Verificar DOI — no está en la bibliografía canónica |
| Documentación/evidencia (~45) | `BMC Med Inform` (enlace OK) | OK |
| Matriz madurez (~52) | `Elaboración propia` (sin refs) | Aceptable como elaboración propia |

---

## C. Propuestas por batch

### Batch 1: Slides 10-13 (Bloque 2A — Fundamentos)

#### Slide 10 — Intro Bloque 2A (línea ~1493)
**Estado**: ✅ OK. Section-intro estándar, no requiere cambios.

#### Slide 11 — Glosario IA (línea ~1512)
**Estado**: ⚠️ Título descriptivo
**Headline actual**: `📚 Hablando el mismo idioma`
**Guion correspondiente (slide 11)**: "Seis conceptos que usaremos constantemente..."

**Cambio propuesto**:
- **Título** → `Seis conceptos que definen tu relación con la IA` (assertivo: promete un número concreto y una utilidad)
- Subtítulo → `Domínalos y entenderás cada headline del resto del seminario`
- **Footer/implicación** (añadir): `Estos 6 términos aparecerán en cada slide de evidencia. Guardar como referencia.`

> **Justificación**: El guion enfatiza que estos conceptos se usarán "constantemente". El título actual no transmite urgencia ni utilidad.

#### Slide 12 — Flujo Clínico con IA (línea ~1625)
**Estado**: ✅ OK. Ya tiene assertion-title assertivo (`La IA puede asistir en las 5 etapas del flujo clínico`), subtitle con dato (71%), infografía, y source-note.

#### Slide 13 — ¿Qué es un LLM? (línea ~1652)
**Estado**: ✅ OK. Headline assertivo (`Los LLM predicen palabras, no comprenden significados`). Source-note funciona como implicación clínica.

---

### Batch 2: Slides 14-18 (Bloque 2B — Evidencia inicial)

#### Slide 14 — Intro Bloque 2B (línea ~1704)
**Estado**: ✅ OK. Section-intro estándar.

#### Slide 15 — Human-in-the-Loop (línea ~1724)
**Estado**: ✅ Muy bien. Headline assertivo, datos claros (6.5%, +119s), visualización copiloto/piloto, referencia con DOI.

#### Slide 16 — Paradigma Colaboración (línea ~1775)
**Estado**: ✅ OK. Headline assertivo. Datos de Takita y Wang bien presentados.

#### Slide 17 — Paradoja H+AI (línea ~1839)
**Estado**: ⚠️ Problema técnico de HTML
- **Línea ~1878**: `<p<0.001< /p>` — HTML roto (el `<` del valor p se interpreta como apertura de tag).
- **Cambio propuesto**: Escapar el `<` → `&lt;` en `p&lt;0.001`

#### Slide 18 — Pausa reflexión (línea ~1898)
**Estado**: ⚠️ Título descriptivo
**Headline actual**: `🤔 Pausa para reflexión`
**Guion (slide 18)**: "¿Hemos confiado alguna vez en una herramienta sin verificar?"

**Cambio propuesto**:
- **Título** → `¿Has confiado en una herramienta sin verificar?` (retórico, assertivo)
- El subtítulo actual está bien
- **Puente visual** (añadir al final): `→ Siguiente: la evidencia específica para calibrar dónde confiar`

> **Justificación**: El guion usa exactamente esta pregunta retórica. Transferirla al headline aprovecha la redundancia controlada.

---

### Batch 3: Slides 20-27 (Bloque 2B — Evidencia central)

#### Slide 20 — Evidencia Actual (línea ~1933)
**Estado**: ⚠️ Título mejorable + sobrecarga
**Headline actual**: `La evidencia muestra un rendimiento mixto de la IA`
**Guion (slide 20)**: "52.1%: acierta uno de cada dos. Un no-especialista."

**Cambios propuestos**:
- **Título** → `La IA acierta uno de cada dos diagnósticos` (assertivo, escala humana, impactante)
- **Subtítulo** → `52.1% en 83 estudios: ≈ médico no-especialista, 15.8 pp inferior al experto (Takita 2025)`
- El contenido de 3 paneles (Precisión global, Rankings NMA, Pediatría) tiene demasiados datos compitiendo. **Propuesta**: Convertir el panel de "Precisión global" en un `metric-value` dominante (52.1%) y hacer los otros dos `fragment` para aparición progresiva.

> **Justificación**: "Rendimiento mixto" es descriptivo y olvidable. "Acierta uno de cada dos" es escala humana y memorable. Coincide con el guion.

#### Slide 21 — Alucinaciones (línea ~2015)
**Estado**: ✅ Bueno. Headline assertivo. Gráfico de barras + panel dual es eficaz.

**Mejora menor**: El footer "Regla de Oro" podría ser más específico para pediatría:
- **Actual**: `Nunca copiar y pegar referencias o datos clínicos sin verificación primaria (DOI/PMID).`
- **Propuesto**: `Regla de Oro pediátrica: verifica cada DOI en PubMed antes de incluir en informe o sesión clínica.`

#### Slide 22 — Brecha Exámenes vs Clínica (línea ~2083)
**Estado**: ✅ Excelente. Headline assertivo (`Aprobar el examen no es saber curar`), barras visuales claras, dato de 9.4% impactante.

**Mejora menor** (puente visual):
- **Añadir footer**: `→ Si no medimos el daño, no podemos prevenirlo. Siguiente: qué pasa cuando los padres preguntan a la IA.`

#### Slide 23 — Riesgo Dr. AI (línea ~2151)
**Estado**: ✅ Bueno. Headline assertivo, infografía, action box.

#### Slide 24 — Mapa del Rendimiento (línea ~2190)
**Estado**: ⚠️ Headline mejorable
**Headline actual**: `168 estudios: ¿qué LLM para qué tarea?`
**Guion (slide 24)**: "Ningún modelo gana en todo."

**Cambio propuesto**:
- **Título** → `Ningún modelo de IA gana en todo` (assertivo, conclusión directa)
- **Subtítulo** → `168 estudios, 35.896 preguntas: el mejor modelo cambia según la tarea clínica`
- La tabla está bien pero es densa. **Propuesta**: Resaltar la fila de "Diagnóstico top-1 → HUMANO" con un background ligeramente más intenso (ya tiene `rgba(255,255,255,0.03)`, subir a `rgba(251,191,36,0.08)`) para que el mensaje clave salte a la vista.

#### Slide 25 — RAG y sesgo (línea ~2279)
**Estado**: ⚠️ Referencia mal construida
- **source-note actual**: `Refs: <a href="...">DOI</a>`
- **Cambio propuesto**: `<a href="https://doi.org/10.1016/j.jposna.2025.100294">J Ped Ortho Surg North Am 2025</a>`

#### Slide 26 — Precisión Diagnóstica pediátrica (línea ~2321)
**Estado**: ⚠️ Título mejorable + sobrecarga
**Headline actual**: `Zoom: IA y diagnóstico pediátrico`
**Guion (slide 26)**: "En zona rural, sin acceso a especialista, la IA iguala al pediatra."

**Cambios propuestos**:
- **Título** → `En zona rural, la IA iguala al pediatra` (assertivo, provoca reacción)
- **Subtítulo** → `87.3% IA vs 91.3% pediatra (NS); pero en global: 15.8 pp inferior al especialista`
- 3 paneles con datos redundantes respecto a slide 20. **Propuesta**: Mantener solo los paneles de "Diagnóstico rural" y "Salud mental" (los que aportan datos nuevos), y sustituir el panel central "Meta-análisis global" por un texto tipo `Para datos globales → ver slide anterior`.
- **Problema de HTML** (línea ~2380): `P<0.001< /p>` — mismo bug que en slide 17. Escapar el `<`.

#### Slide 27 — Velocidad ≠ Fiabilidad ≠ Consenso (línea ~2393)
**Estado**: ✅ Excelente. Headline assertivo, 3 paneles bien diferenciados, implicación visible.

---

### Batch 4: Slides 29-36 (Semáforo + Regulatorio)

#### Slide ~28 — Sesgos Algorítmicos (línea ~2492)
**Estado**: ✅ OK. Headline assertivo (`Lo que la IA hereda de sus datos`), infografía.

**Mejora menor**: El guion (slide 29) da ejemplos concretos pediátricos (dermatitis en piel oscura, TDAH infradiagnosticado en niñas) que NO aparecen en la slide.
- **Propuesta**: Añadir un `glass-panel` debajo de la infografía con 2 ejemplos pediátricos concretos como fragment:

```html
<div class="glass-panel fragment" style="max-width: 900px; margin: 10px auto;">
    <p style="font-size: 0.82em; text-align: center; margin: 0;">
        <strong>Ejemplos pediátricos:</strong>
        Dermatitis en piel oscura infradiagnosticada ·
        TDAH en niñas invisibilizado por datos históricos sesgados
    </p>
</div>
```

#### Slide ~29 — Semáforo de Seguridad (línea ~2528)
**Estado**: ⚠️ Título mejorable
**Headline actual**: `Protocolo de seguridad 2025`
**Guion (slide 30)**: "El criterio no es si la IA lo hace bien o mal. El criterio es: si se equivoca, ¿puedo detectarlo antes de que cause daño?"

**Cambio propuesto**:
- **Título** → `Si la IA se equivoca, ¿puedes detectarlo a tiempo?` (retórico, assertivo)
- **Subtítulo** → `El criterio de seguridad: detectabilidad del error, no precisión del modelo`
- Mantener la infografía sin cambios

> **Justificación**: El guion tiene una formulación retórica brillante que la slide no aprovecha. "Protocolo de seguridad 2025" es descriptivo y no transmite el concepto clave.

#### Slides 33-36 — Marco Regulatorio y Privacidad
**Estado**: ✅ Excelentes. Los headlines son assertivos, la jerarquía visual es clara, los 4 niveles de riesgo están bien presentados, el semáforo de jurisdicciones es muy claro. No requieren cambios de contenido.

**Mejora menor en slide 33** (línea ~2567):
- **source-note**: Tiene muchas referencias en una línea. Propuesta: Mover `WMA Porto 2025` y `Lazcoz & Miguel, Bioethics 2025` a una segunda línea con `<br>` para legibilidad.

---

### Batch 5: Slides 37-44 (Bloque 2C — Aplicaciones I)

#### Slide 37 — Intro Bloque 2C (línea ~2955)
**Estado**: ✅ OK. Section-intro estándar.

#### Slide 38 — Oxígeno para la Consulta (línea ~2977)
**Estado**: ⚠️ Referencia sin DOI
- **source-note actual**: `Zhao J, et al. BMC Med Inform Decis Mak. 2025` (sin enlace)
- **Cambio propuesto**: `<a href="https://doi.org/10.1186/s12911-025-03324-w" target="_blank" rel="noopener">Zhao et al. BMC Med Inform 2025</a>`

**Mejora de implicación**: El footer dice "Reducción directa del burnout asociado al papeleo. Calidad comparable a documentación manual." — OK pero genérico.
- **Propuesta**: `Impacto para tu consulta: 35 pacientes/día × menos tiempo escribiendo = más tiempo mirando al niño.`

> **Justificación**: El guion (slide 38) usa exactamente esta traducción a escala humana.

#### Slide 39 — Inteligencia Ambiental (línea ~3015)
**Estado**: ⚠️ Referencia sin DOI
- **source-note actual**: `Referencias: Zhao J, et al. 2025 · Dave B, et al. 2025` (sin enlaces)
- **Cambio propuesto**: Añadir DOIs: Zhao `10.1186/s12911-025-03324-w`, Dave `10.1016/j.ijmedinf.2025.106122`

#### Slide 40 — Prompt Engineering Clínico (línea ~3076)
**Estado**: ⚠️ Referencia sin DOI
- **source-note actual**: `Callens S, et al. 2026` (sin enlace ni DOI)
- **Cambio propuesto**: Verificar DOI de Callens 2026 y añadirlo. Si no está disponible, dejar como está pero añadir al menos el nombre de la revista.

**Mejora de implicación**: El footer actual dice "Preview: En el Bloque 3 aprenderemos el método RECORD, basado en estos principios." — funciona como puente. ✅ OK.

#### Slide 41 — Técnicas de Prompting (línea ~3111)
**Estado**: ✅ Bueno. Headline assertivo, 4 técnicas con datos cuantificados, alerta de variabilidad.

**Mejora menor**: El dato de 76pp de variabilidad por cambios triviales es tan impactante que merece más prominencia visual.
- **Propuesta**: Mover el box de alerta (actualmente al final) ANTES de los paneles de técnicas, como `fragment` que aparece primero para crear tensión narrativa.

#### Slide 42 — Context Engineering (línea ~3195)
**Estado**: ✅ OK. Headline assertivo, comparativa paradigmas, takeaway para pediatra.

#### Slide 43 — Mapa 2025-2026 (línea ~3267)
**Estado**: ⚠️ Título mejorable + referencia interna
**Headline actual**: `La evidencia 2025-2026 se concentra en benchmarking técnico`
**Guion (slide 43)**: "93.55% de los estudios evalúan modelos generalistas. Solo 6.45% evalúan modelos médicos específicos."

**Cambios propuestos**:
- **Título** → `Solo el 6% de los estudios evalúa modelos médicos específicos` (assertivo, el dato minoritario es más impactante)
- **Subtítulo** → `El 93.55% evalúa modelos generalistas: sabemos mucho de GPT-4, poco de modelos pediátricos`
- **Referencia**: Cambiar `1021:#2` → `<a href="https://doi.org/10.1186/s12911-025-02954-4">Shool et al. BMC Med Inform 2025</a>`
- **Footer** (mejorar): Actual: `"Accuracy es la métrica más usada (21.78%)" en evaluaciones clínicas`. Propuesta: `Accuracy mide acierto/fallo, pero no mide daño ni seguridad. Solo 9.4% evalúa errores.`

#### Slide 44 — Ecosistema IA 2026 (línea ~3329)
**Estado**: ⚠️ Título mejorable + referencias internas
**Headline actual**: `El ecosistema IA se diversifica`
**Guion (slide 44)**: "Tres direcciones: open-source para privacidad, especializados para precisión, agentes para automatizar."

**Cambios propuestos**:
- **Título** → `Privacidad, precisión o automatización: tres caminos` (assertivo, orientado a decisión)
- **Subtítulo** → `Open-source iguala en rendimiento · Especializados superan en diagnóstico · Agentes automatizan flujos`
- **Referencias**: Cambiar `1021:#3` → `<a href="https://doi.org/10.1038/s41591-025-03727-2">Sandmann et al. Nat Med 2025</a>` y `1021:#5` → `<a href="https://doi.org/10.1038/s41591-024-03416-6">Liu et al. Nat Med 2025</a>`

---

### Batch 6: Slides 45-57 (Bloque 2C — Aplicaciones II + Síntesis)

#### Slide 45 — Documentación y evidencia (línea ~3383)
**Estado**: ⚠️ Título redundante con slide 38
**Headline actual**: `La IA Ambiental reduce la fatiga administrativa`
Slide 38 ya cubre "IA como oxígeno para la consulta" con el mismo meta-análisis.

**Cambios propuestos**:
- **Título** → `23 estudios confirman: menos papeleo, misma calidad` (assertivo, distingue de slide 38 por ser meta-analítico)
- **Subtítulo** → `Meta-análisis: reducción significativa de carga documental con IA de voz a texto`

#### Slide 46 — Diagnóstico precoz AP (línea ~3418)
**Estado**: ⚠️ Telegráfica + referencia DOI
- **Referencia**: Cambiar `DOI` → `<a href="https://doi.org/10.1038/s41746-026-02372-4">npj Digit Med 2026</a>`
- **Footer actual**: `Acción: usar como apoyo a derivación temprana en AP.` — muy genérico.
- **Footer propuesto**: `En tu consulta: cuando dudas si derivar, un sistema multi-agente puede cruzar síntomas, analítica y guías en segundos. No decide por ti, pero te da un segundo par de ojos.`

#### Slide 47 — Pediatría: tres áreas sólidas (línea ~3465)
**Estado**: ⚠️ Telegráfica + referencias DOI
- **Referencias**: Cambiar los 3× `DOI` por: `Lancet Digit Health 2025 | BMJ Ophth 2025 | PLoS ONE 2025`
- **Footer actual**: `Acción: priorizar cribado/predicción; diagnóstico complejo con supervisión.` — OK pero genérico.
- **Footer propuesto**: `Patrón común: la IA alerta, el pediatra confirma. En cribado neonatal y ROP, la evidencia ya justifica la integración.`

#### Slide 48 — Caries escolar (línea ~3525)
**Estado**: ⚠️ Telegráfica + referencia DOI
- **Referencia**: Cambiar `DOI` → `BMC Oral Health 2025`
- **Footer actual**: `Acción: útil para cribado escolar y priorización de revisión.` — genérico.
- **Footer propuesto**: `Programa de salud bucodental: la enfermera escolar fotografía, la IA prioriza, el odontólogo revisa los urgentes. Reduce meses de espera.`

> **Justificación**: El guion (slide 48) describe exactamente este escenario. La slide debería reflejarlo.

#### Slide 49 — Riesgo suicida (línea ~3572)
**Estado**: ⚠️ Telegráfica + referencia DOI
- **Referencia**: Cambiar `DOI` → `JMIR 2025`
- **Footer actual**: `Acción: usar contexto conversacional para reducir falsos positivos.` — técnico, no traduce a práctica.
- **Footer propuesto**: `"No quiero vivir" puede ser frustración adolescente o grito de auxilio. Esa distinción requiere empatía y contexto clínico: exactamente lo que la IA no tiene.`

> **Justificación**: El guion (slide 49) tiene esta frase exacta, mucho más potente que el footer actual.

#### Slide 50 — Educación médica (línea ~3612)
**Estado**: ⚠️ Referencia DOI
- **Referencia**: Cambiar `DOI` → `BMC Med Educ 2025`
- **Footer actual**: `Acción: evaluar razonamiento con casos clínicos y no solo con MCQ.` — OK, mantener.

#### Slide 51 — Prompting determinista (línea ~3661)
**Estado**: ⚠️ Título mejorable + referencia DOI
**Headline actual**: `El prompting determinista fuerza adherencia a protocolos`
**Guion (slide 51)**: "De 32% a 100%: la diferencia entre preguntar abiertamente y dar un checklist."

**Cambios propuestos**:
- **Título** → `De 32% a 100%: la estructura lo cambia todo` (assertivo, usa el dato en el headline)
- **Subtítulo** → `Prompts abiertos: 32% adherencia · Prompts tipo checklist: 100% adherencia a protocolo`
- **Referencia**: Cambiar `DOI` → `<a href="https://doi.org/10.3389/frai.2025.1728320">Arriola-Montenegro et al. Front AI 2025</a>`
- **Footer actual**: OK. Pero añadir puente: `→ Esta es la base científica del método RECORD que aprenderemos en el Bloque 3.`

#### Slide 52 — Matriz de Madurez (línea ~3704)
**Estado**: ✅ OK. Infografía + título assertivo. La source-note como "elaboración propia" es aceptable.

#### Slide 53 — RAG estándar de oro (línea ~3729)
**Estado**: ✅ OK. Headline assertivo, infografía, referencia con DOI.

#### Slide 54 — Whitelisting (línea ~3755)
**Estado**: ✅ Bueno. Headline assertivo, métricas claras, implicación visible con fuentes recomendadas.

#### Slide 55 — Futuro Híbrido (línea ~3806)
**Estado**: ✅ OK. Infografía, título assertivo.

#### Slide 56 — Semáforo AP (línea ~3829)
**Estado**: ✅ Excelente. Infografía con semáforo, download prompt. Sin cambios.

#### Slide 57 — Síntesis: 5 mensajes clave (línea ~3867)
**Estado**: ⚠️ Título descriptivo + referencias internas
**Headline actual**: `📌 Cinco mensajes clave para el pediatra de AP` (descriptivo, usa h2 estándar en vez de assertion-title)

**Cambios propuestos**:
- Convertir a estructura `has-title-wrapper` + `assertion-title`:
  - **Título** → `Cinco ideas que puedes aplicar el lunes` (assertivo, orientado a acción)
  - **Subtítulo** → `Síntesis de la evidencia 2025-2026 para tu consulta`
- **Referencias**: Cambiar `1021:#2` → `Shool BMC 2025`, `1021:#3` → `Sandmann Nat Med 2025`, `1021:#5` → `Liu Nat Med 2025`, y los 3× `DOI` por nombres legibles.

---

## D. Tabla resumen de cambios

### Cambios de headline (título)

| Slide | Línea aprox. | Headline actual | Headline propuesto | Tipo |
|---|---|---|---|---|
| ~11 | 1514 | `📚 Hablando el mismo idioma` | `Seis conceptos que definen tu relación con la IA` | Descriptivo → Assertivo |
| ~18 | 1900 | `🤔 Pausa para reflexión` | `¿Has confiado en una herramienta sin verificar?` | Descriptivo → Retórico |
| ~20 | 1937 | `La evidencia muestra un rendimiento mixto de la IA` | `La IA acierta uno de cada dos diagnósticos` | Vago → Escala humana |
| ~24 | 2194 | `168 estudios: ¿qué LLM para qué tarea?` | `Ningún modelo de IA gana en todo` | Pregunta → Afirmación |
| ~26 | 2325 | `Zoom: IA y diagnóstico pediátrico` | `En zona rural, la IA iguala al pediatra` | Descriptivo → Assertivo |
| ~29 | 2532 | `Protocolo de seguridad 2025` | `Si la IA se equivoca, ¿puedes detectarlo a tiempo?` | Descriptivo → Retórico |
| ~43 | 3271 | `La evidencia 2025-2026 se concentra en benchmarking técnico` | `Solo el 6% de los estudios evalúa modelos médicos específicos` | Descriptivo → Dato impactante |
| ~44 | 3333 | `El ecosistema IA se diversifica` | `Privacidad, precisión o automatización: tres caminos` | Vago → Orientado a decisión |
| ~45 | 3387 | `La IA Ambiental reduce la fatiga administrativa` | `23 estudios confirman: menos papeleo, misma calidad` | Repetitivo → Diferenciado |
| ~51 | 3665 | `El prompting determinista fuerza adherencia a protocolos` | `De 32% a 100%: la estructura lo cambia todo` | Técnico → Dato en headline |
| ~57 | 3869 | `📌 Cinco mensajes clave para el pediatra de AP` | `Cinco ideas que puedes aplicar el lunes` | Descriptivo → Accionable |

### Correcciones de referencias (resumen)

| Tipo de problema | Nº de slides afectadas | Slides |
|---|---|---|
| DOI como anchor text | 7 | 25, 46, 47, 48, 49, 50, 51 |
| `1021:#N` sin contexto | 3 | 43, 44, 57 |
| Sin enlace DOI | 3 | 38, 39, 40 |
| HTML roto (`<` no escapado) | 2 | 17, 26 |

### Footers/implicaciones mejorados

| Slide | Footer actual (resumen) | Footer propuesto (resumen) |
|---|---|---|
| ~38 | Reducción burnout genérico | 35 pacientes/día × menos tiempo escribiendo |
| ~46 | "Apoyo a derivación temprana" | Segundo par de ojos cuando dudas si derivar |
| ~47 | "Priorizar cribado" | La IA alerta, el pediatra confirma |
| ~48 | "Cribado escolar" | Escenario completo: enfermera fotografía → IA prioriza → odontólogo revisa |
| ~49 | "Contexto conversacional para falsos positivos" | Frase del guion sobre empatía vs. IA |

### Puentes narrativos añadidos

| Slide | Puente propuesto |
|---|---|
| ~18 | `→ Siguiente: la evidencia específica para calibrar dónde confiar` |
| ~22 | `→ Si no medimos el daño, no podemos prevenirlo` |
| ~51 | `→ Esta es la base científica del método RECORD` |

---

## Notas finales

1. **Prioridad alta**: Corregir las 12 referencias mal construidas. Son visibles para cualquier asistente que lea las slides.
2. **Prioridad media**: Los 11 cambios de headline. Mejoran la retórica pero las slides ya funcionan.
3. **Prioridad baja**: Footers e implicaciones mejoradas. Son refinamientos que alinean slide ↔ guion.
4. **No olvidar**: Los 2 bugs de HTML con `<` no escapado en slides 17 y 26.
