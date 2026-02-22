# INSTRUCCIONES DE REVISIÓN — Bloque 2B: Evidencia Científica
# Seminario AEPap 2026 · "La IA como Asistente del Pediatra de AP"
# Fecha: 2026-02-15 · Versión: 1.0

---

## RESUMEN EJECUTIVO

Se ha realizado una revisión bibliográfica con Scholar Gateway, Consensus y web search
(PubMed MCP no disponible) identificando **5 artículos integradores** publicados entre
marzo 2025 y enero 2026, todos en revistas de alto impacto (npj Digital Medicine ×3,
JMIR ×1, Nature Medicine ×1), que absorben evidencia dispersa en múltiples slides
individuales del Bloque 2B.

**Objetivo:** Sustituir referencias fragmentadas por estas integradoras, condensar
21 slides → 16-17 slides, y convertir las imágenes centrales en HTML nativo manteniendo
el mismo impacto visual. No se añade contenido nuevo — se reorganiza y consolida.

**Tiempo estimado narrado resultante:** ~20 min (vs ~25 min actual).
Ganancia de ~5 min redistribuible a Bloque 3 (demos) o Bloque 4 (práctica).

---

## PARTE 1: LOS 5 ARTÍCULOS INTEGRADORES

### REF-A · Takita et al. 2025 — MA IA vs Médicos

```
Takita H, Kabata D, Walston SL, et al.
A systematic review and meta-analysis of diagnostic performance
comparison between generative AI and physicians.
npj Digit Med. 2025;8(1):175.
DOI: 10.1038/s41746-025-01543-z
PMID: 40121370
```

**Diseño:** RS + MA, 83 estudios (jun 2018 – jun 2024), PROSPERO CRD42023494733.
**Hallazgos clave:**
- Precisión diagnóstica global IA generativa: **52.1%**
- IA vs médicos en general: sin diferencia significativa (p=0.10)
- IA vs no-especialistas: sin diferencia (p=0.93)
- IA vs especialistas: IA significativamente peor (p=0.007), diferencia **-15.8pp**
- ChatGPT fue el modelo más evaluado
- Gran variabilidad por modelo y especialidad

**Mensaje para la audiencia:** "La IA rinde como un residente — no como un adjunto.
Útil como copiloto, inadecuada como piloto."

---

### REF-B · JMIR NMA 2025 — Ranking de LLMs clínicos

```
[Autores — acceder vía DOI para cita completa]
Accuracy of Large Language Models When Answering Clinical
Research Questions: Systematic Review and Network Meta-Analysis.
J Med Internet Res. 2025;27:e64486.
DOI: 10.2196/64486
PROSPERO: CRD42024558245
```

**Diseño:** RS + NMA bayesiana, **168 artículos, 35,896 preguntas, 3,063 casos**.
La NMA más grande publicada hasta la fecha sobre LLMs en medicina clínica.
**Hallazgos clave:**
- **Preguntas objetivas:** ChatGPT-4o primero (SUCRA más alto)
- **Preguntas abiertas:** ChatGPT-4 más fiable
- **Diagnóstico top-1 y top-3:** Humanos superan a todos los LLMs
- **Triaje/clasificación:** Gemini lidera (SUCRA=0.9649)
- Inconsistencia significativa ChatGPT-3.5 vs ChatGPT-4 (p=.045)
- 40 (23.8%) de 168 estudios con bajo riesgo de sesgo; 128 (76.2%) moderado

**Mensaje para la audiencia:** "No hay un LLM mejor para todo. Cada tarea tiene
su modelo óptimo. Y en diagnóstico directo, el humano sigue ganando."

---

### REF-C · Wang et al. 2026 — MA Colaboración H+AI

```
Wang [et al.].
Human–large language model collaboration in clinical medicine:
a systematic review and meta-analysis.
npj Digit Med. 2026 [publicado ~ene-feb 2026].
DOI: 10.1038/s41746-026-02382-2
PROSPERO: CRD420251068272
```

**Diseño:** RS + MA PRISMA 2020, 10 estudios (búsqueda hasta jun 2025).
**Hallazgos clave:**
- **Precisión diagnóstica H+AI:** RR 1.59, pero IC 95% 0.08–32.74 → no significativo
- **Puntuaciones compuestas dx/manejo:** MD +4.88pp, IC +0.65 a +9.12 → significativo
- **Intervalo de predicción:** –31.65 a +41.42 → alta incertidumbre en mundo real
- Conclusión: la colaboración mejora manejo pero no necesariamente diagnóstico puro
- Pocos estudios aún → campo incipiente

**Mensaje para la audiencia:** "Humano+IA no siempre es mejor que humano solo
ni que IA sola. La clave no es USAR la IA, sino CÓMO integrarla."

NOTA: Este artículo ya estaba referenciado en la slide 2B.3 como preprint.
Ahora es publicación definitiva en npj Digit Med. ACTUALIZAR la cita.

---

### REF-D · Asgari et al. 2025 — Framework Alucinaciones Clínicas

```
Asgari E, Montaña-Brown N, Dubois M, et al.
A framework to assess clinical safety and hallucination rates
of LLMs for medical text summarisation.
npj Digit Med. 2025;8(1):274.
DOI: 10.1038/s41746-025-01670-7
PMID: 40360677
```

**Diseño:** 18 experimentos, 450 pares transcripción-nota clínica, 12,999 oraciones
anotadas por 50 médicos en atención primaria.
**Hallazgos clave:**
- Tasa de alucinación en documentación clínica: **1.47%**
- Tasa de omisión: **3.45%**
- Framework de 4 componentes: taxonomía errores + diseño experimental +
  framework seguridad clínica + plataforma CREOLA
- El prompting estructurado reduce alucinaciones significativamente
- Dato clave: paso de extracción de hechos antes de generar nota reduce errores

**Mensaje para la audiencia:** "En documentación, la IA alucina poco (1.47%)
pero OMITE más (3.45%). El riesgo real no es inventar, sino olvidar."

---

### REF-E · Goh et al. 2025 — RCT GPT-4 + Médicos (Nature Medicine)

```
Goh E, Gallo RJ, Strong E, et al.
GPT-4 assistance for improvement of physician performance
on patient care tasks: a randomized controlled trial.
Nat Med. 2025;31(4):1233-1238.
DOI: 10.1038/s41591-024-03456-y
PMID: 39910272
```

**Diseño:** ECA prospectivo, 92 médicos (internistas, MF, urgencias),
5 viñetas clínicas con rúbrica Delphi. Nov 2023 – Abr 2024.
**Hallazgos clave:**
- Grupo LLM: puntuación total +6.5% vs control (p<0.001)
- Médicos con GPT-4 igualaron el rendimiento de GPT-4 solo (sin diferencia significativa)
- Médicos con LLM dedicaron 119.3 segundos más por caso
- Más tiempo → mejores decisiones (correlación positiva post ajuste)
- El beneficio fue en razonamiento de MANEJO, no solo diagnóstico

**Mensaje para la audiencia:** "El único RCT publicado en Nature Medicine:
la IA mejora las decisiones clínicas, pero no por arte de magia —
los médicos que mejor usaron la IA dedicaron MÁS tiempo, no menos."

---

## PARTE 2: MAPA DE CAMBIOS EN SLIDES

### Leyenda
- 🔴 ELIMINAR slide (fusionar contenido en otra)
- 🟡 MODIFICAR slide (actualizar datos/referencias)
- 🟢 MANTENER sin cambios
- 🔵 FUSIONAR dos slides en una
- 🖼️→📝 Sustituir imagen central por HTML nativo

---

### SLIDE 2B.0 — Portada Bloque 2B: Evidencia
🟢 MANTENER. Sin cambios.

---

### SLIDE 2B.1 — Human-in-the-Loop
🟡 MODIFICAR
- Mantener diagrama dual (IA copiloto / Pediatra piloto)
- 🖼️→📝 Convertir `slide_human_in_the_loop.jpg` a HTML nativo

**HTML sugerido para reemplazar imagen:**
```html
<div class="grid-2" style="gap: 2rem;">
  <!-- Panel IA -->
  <div class="glass-panel" style="border-left: 4px solid #4FC3F7;">
    <h4 style="color:#4FC3F7;">🤖 IA Copiloto</h4>
    <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.85em;">
      <span>📝 Redactar</span>
      <span style="text-align:center;">↓</span>
      <span>🔍 Sintetizar</span>
      <span style="text-align:center;">↓</span>
      <span>✅ Verificar formato</span>
    </div>
  </div>
  <!-- Panel Pediatra -->
  <div class="glass-panel" style="border-left: 4px solid #81C784;">
    <h4 style="color:#81C784;">👩‍⚕️ Pediatra Piloto</h4>
    <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.85em;">
      <span>💚 Empatizar</span>
      <span style="text-align:center;">↓</span>
      <span>🧠 Decidir</span>
      <span style="text-align:center;">↓</span>
      <span>📋 Recopilar</span>
    </div>
  </div>
</div>
```
- Añadir en nota al pie: "Goh 2025 Nat Med: médicos+GPT-4 igualan rendimiento IA sola"
- Referencia: **REF-E**

---

### SLIDE 2B.2 — Paradigma Colaboración (Venn)
🟡 MODIFICAR SUSTANCIALMENTE
- 🖼️→📝 Convertir `slide_venn_colaboracion.jpg` a HTML nativo
- SUSTITUIR "Precisión 55-93%" por dato integrador de **REF-A (Takita)**

**Datos nuevos para la slide:**
```
IA SOLA: 52.1% precisión diagnóstica global (83 estudios)
IA ≈ No-especialista (p=0.93)
IA < Especialista en -15.8pp (p=0.007)
```

**HTML sugerido para Venn simplificado:**
```html
<div style="display:flex; justify-content:center; align-items:center; gap:0;">
  <div style="width:280px; height:280px; border-radius:50%;
       background:rgba(79,195,247,0.2); border:3px solid #4FC3F7;
       display:flex; flex-direction:column; justify-content:center;
       padding-left:2rem; margin-right:-60px; z-index:1;">
    <strong style="color:#4FC3F7;">Médico</strong>
    <small>Juicio clínico</small>
    <small>Empatía</small>
    <small>Contexto</small>
  </div>
  <div style="width:120px; height:180px; display:flex; flex-direction:column;
       justify-content:center; align-items:center; z-index:2;
       color:#FFD54F; font-weight:bold; text-align:center;">
    <span style="font-size:1.2em;">Mejores</span>
    <span style="font-size:1.2em;">Resultados</span>
    <small style="color:#aaa; margin-top:0.5rem;">+4.88pp manejo</small>
    <small style="color:#aaa;">(Wang 2026)</small>
  </div>
  <div style="width:280px; height:280px; border-radius:50%;
       background:rgba(129,199,132,0.15); border:3px solid #81C784;
       display:flex; flex-direction:column; justify-content:center;
       padding-right:2rem; text-align:right; margin-left:-60px; z-index:1;">
    <strong style="color:#81C784;">IA</strong>
    <small>52.1% dx global</small>
    <small>≈ No-especialista</small>
    <small>Velocidad</small>
  </div>
</div>
<p class="fuente" style="margin-top:1rem; font-size:0.6em; text-align:center;">
  Takita 2025 npj Digit Med (n=83 estudios) · Wang 2026 npj Digit Med (n=10 estudios)
</p>
```
- Referencias: **REF-A + REF-C**

---

### SLIDE 2B.3 — Paradoja H+AI
🟡 MODIFICAR
- ACTUALIZAR cita: preprint Wang → **REF-C publicación definitiva**
- Mantener estructura narrativa: "H+AI no siempre > IA sola"
- Actualizar datos exactos: RR 1.59 (0.08–32.74), MD +4.88pp (+0.65 a +9.12)
- Añadir: "PI –31.65 a +41.42 → altísima incertidumbre en mundo real"
- Añadir dato de **REF-E**: "PERO en el RCT de Goh (Nat Med), médicos+GPT-4
  mejoraron +6.5pp en manejo clínico (p<0.001)"

**Mensaje clave actualizado:** "La paradoja se resuelve con DISEÑO: no basta
usar la IA, hay que integrarla con método (→ RECORD, → Sándwich)."

---

### SLIDE 2B.4 — Pausa: ¿Experiencias?
🟢 MANTENER. Slide interactiva, sin datos.

---

### SLIDE 2B.5 — Serie Evidencia IA (portada)
🔴 ELIMINAR
- Era portada decorativa de la serie "7 estudios 2025-2026"
- Con la nueva narrativa integradora, no hace falta portada de sub-sección
- Usar la imagen `IA_en_PediatrÃ­a_01.jpg` solo en 2C.2 (donde ya está)

---

### SLIDE 2B.6 — Evidencia Actual (datos mixtos)
🟡 MODIFICAR
- 🖼️→📝 Convertir contenido de `IA_en_PediatrÃ­a_03+02.jpg` a HTML
- RECONTEXTUALIZAR datos individuales dentro del marco de **REF-A (Takita)**

**Contenido actualizado:**
```
TÍTULO: "Evidencia Actual: el panorama real"

Panel 1 (glass-panel, borde azul):
  "52.1% precisión diagnóstica global" — Takita 2025, 83 estudios
  "IA ≈ MF/Residente · IA < Especialista (-15.8pp)"

Panel 2 (glass-panel, borde amarillo):
  "168 artículos, 35,896 preguntas" — JMIR NMA 2025
  "Mejor modelo varía por tarea:"
  • Objetivas → ChatGPT-4o
  • Abiertas → ChatGPT-4
  • Triaje → Gemini (SUCRA=0.96)
  • Dx top-1 → Humanos

Panel 3 (glass-panel, borde naranja):
  "Datos pediátricos específicos:"
  Dx Rural: 91.3% pediatra vs 87.3% GPT-3 (P=.47)
  Salud mental pediátrica: F1 0.41→0.655 (P<.001)
```
- Referencias: **REF-A + REF-B** + Del Monte 2025 (ref #15 actual) + datos pediátricos existentes
- Las cifras pediátricas individuales SE MANTIENEN porque el MA de Takita no es pediátrico
  específico, y son datos únicos de nuestro campo

---

### SLIDE 2B.7 — Alucinaciones
🟡 MODIFICAR
- 🖼️→📝 Convertir `slide_alucinacion_bibliografica.jpg` a HTML
- MANTENER datos Chelli (Bard 91.4%, GPT-3.5 39.6%, GPT-4 28.6%) = alucinaciones bibliográficas
- AÑADIR segunda capa con **REF-D (Asgari)**: alucinaciones en documentación clínica

**HTML sugerido:**
```html
<div class="grid-2" style="gap:1.5rem;">
  <!-- Panel 1: Bibliográficas -->
  <div class="glass-panel">
    <h4 style="color:#EF5350;">📚 Bibliográficas</h4>
    <p style="font-size:0.75em; color:#aaa;">Referencias inventadas</p>
    <div style="margin:1rem 0;">
      <div style="display:flex; align-items:center; gap:0.5rem; margin:0.3rem 0;">
        <div style="background:#EF5350; height:1.2rem; width:91.4%; border-radius:4px;"></div>
        <small>Bard 91.4%</small>
      </div>
      <div style="display:flex; align-items:center; gap:0.5rem; margin:0.3rem 0;">
        <div style="background:#FFA726; height:1.2rem; width:39.6%; border-radius:4px;"></div>
        <small>GPT-3.5 39.6%</small>
      </div>
      <div style="display:flex; align-items:center; gap:0.5rem; margin:0.3rem 0;">
        <div style="background:#66BB6A; height:1.2rem; width:28.6%; border-radius:4px;"></div>
        <small>GPT-4 28.6%</small>
      </div>
    </div>
    <p style="font-size:0.65em;">Chelli 2024 · REGLA: nunca búsquedas ciegas</p>
  </div>
  <!-- Panel 2: Documentación -->
  <div class="glass-panel">
    <h4 style="color:#42A5F5;">📋 Documentación clínica</h4>
    <p style="font-size:0.75em; color:#aaa;">Notas de consulta AP</p>
    <div style="margin:1rem 0; text-align:center;">
      <div style="font-size:2.5em; font-weight:bold; color:#66BB6A;">1.47%</div>
      <div style="font-size:0.85em; color:#aaa;">alucinaciones</div>
      <div style="font-size:2em; font-weight:bold; color:#FFA726; margin-top:0.5rem;">3.45%</div>
      <div style="font-size:0.85em; color:#aaa;">omisiones ← riesgo mayor</div>
    </div>
    <p style="font-size:0.65em;">Asgari 2025 npj Digit Med · 50 médicos, 12,999 frases</p>
  </div>
</div>
```
- Referencias: Chelli 2024 (existente) + **REF-D**

---

### SLIDE 2B.8 — Brecha Exámenes vs Clínica
🟡 MODIFICAR LIGERAMENTE
- 🖼️→📝 Convertir `slide_brecha_examenes_clinica.jpg` a HTML
- Reforzar con **REF-A**: "52.1% en clínica real vs 84-90% en exámenes"

**HTML sugerido (barras decrecientes):**
```html
<div style="max-width:600px; margin:0 auto;">
  <h4 style="text-align:center; margin-bottom:1.5rem;">La brecha es real</h4>

  <div style="margin:1rem 0;">
    <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem;">
      <span style="font-size:0.85em;">Exámenes tipo test (USMLE)</span>
      <span class="metric-value" style="font-size:0.9em;">84-90%</span>
    </div>
    <div style="background:#333; border-radius:6px; height:2rem;">
      <div style="background:linear-gradient(90deg,#66BB6A,#43A047);
           width:87%; height:100%; border-radius:6px;"></div>
    </div>
  </div>

  <div style="margin:1rem 0;">
    <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem;">
      <span style="font-size:0.85em;">Competencia clínica real</span>
      <span class="metric-value" style="font-size:0.9em;">52.1%</span>
    </div>
    <div style="background:#333; border-radius:6px; height:2rem;">
      <div style="background:linear-gradient(90deg,#FFA726,#FB8C00);
           width:52%; height:100%; border-radius:6px;"></div>
    </div>
    <small style="color:#aaa;">Takita 2025 · 83 estudios, MA</small>
  </div>

  <div style="margin:1rem 0;">
    <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem;">
      <span style="font-size:0.85em;">Seguridad evaluada</span>
      <span class="metric-value" style="font-size:0.9em;">9.4%</span>
    </div>
    <div style="background:#333; border-radius:6px; height:2rem;">
      <div style="background:linear-gradient(90deg,#EF5350,#E53935);
           width:9.4%; height:100%; border-radius:6px;"></div>
    </div>
    <small style="color:#aaa;">Solo 9.4% de estudios evalúa seguridad</small>
  </div>
</div>
```
- Referencia: **REF-A** + dato existente del 9.4% (que se sube desde 2B.17)

---

### SLIDE 2B.9 — Riesgo: Dr. AI (89.5% errores RCP)
🟢 MANTENER
- 🖼️→📝 Opcionalmente convertir `slide_fallos_rcp.jpg` a HTML
- Dato muy impactante y específico, no cubierto por las integradoras
- Este dato ya tiene fuente propia sólida

---

### SLIDES 2B.10 + 2B.13 + 2B.14 → FUSIONAR EN 2 SLIDES
🔵 FUSIÓN TRIPLE → 2 slides

**Slide actual 2B.10** (Paradoja Fiabilidad: ORL 100% κ=1.0 vs alucinaciones)
**Slide actual 2B.13** (Velocidad ≠ Fiabilidad: AIS, todos fallaron 1 semana)
**Slide actual 2B.14** (Consenso: Expertos 92% κ=0.913 vs LLMs 1.6-10.2%)

Estas tres comparten el mismo mensaje: "rendimiento alto en una métrica
no implica fiabilidad global." La NMA de JMIR (**REF-B**) consolida todo esto.

**→ NUEVA SLIDE 2B.10-FUSIÓN-A: "El mapa del rendimiento"**
```
TÍTULO: "168 estudios: ¿qué LLM para qué tarea?"

Tabla visual HTML (no imagen):
┌──────────────┬───────────────────┬────────────┐
│ Tarea        │ Mejor modelo      │ SUCRA      │
├──────────────┼───────────────────┼────────────┤
│ Objetivas    │ ChatGPT-4o        │ Primero    │
│ Abiertas     │ ChatGPT-4         │ Primero    │
│ Dx top-1     │ HUMANO            │ Superior   │
│ Triaje       │ Gemini            │ 0.9649     │
└──────────────┴───────────────────┴────────────┘

Fuente: JMIR NMA 2025 · 168 artículos · 35,896 preguntas
```
- Referencia: **REF-B**
- Imagen: NINGUNA (todo HTML)

**→ NUEVA SLIDE 2B.10-FUSIÓN-B: "Velocidad ≠ Fiabilidad ≠ Consenso"**
```
TÍTULO: "Rápido no es fiable. Fiable no es consistente."

Tres columnas glass-panel:

[VELOCIDAD]        [FIABILIDAD]       [CONSENSO]
IA: 7-48 seg       κ ORL = 1.0        Expertos: 92%
Humano: 11-12 min  Pero 91.4% citas   κ = 0.913
                    falsas (Bard)
100× más rápida    TODOS fallaron      LLMs: 1.6-10.2%
                    tras 1 semana       κ = 0.001-0.036

  ↓ CONCLUSIÓN (centrada, destacada):
  "La velocidad atrae, la fiabilidad importa,
   el consenso falta."
```
- Se mantienen datos AIS originales (velocidad y fallo 1 semana) +
  datos Durgut κ ORL + datos consenso expertos vs LLMs
- Se ELIMINAN las imágenes `IA_Potencia_05.jpg` y `IA_Potencia_06.jpg`
  de estas slides (pasan a reserva)

---

### SLIDE 2B.11 — RAG y sesgo (ICC 0.27)
🟢 MANTENER
- Dato específico sobre evaluación de sesgo con RAG
- No cubierto por las integradoras

---

### SLIDE 2B.12 — Precisión Diagnóstica (87.3% IA vs 91.3% pediatra)
🟡 MODIFICAR
- 🖼️→📝 Convertir `IA_en_PediatrÃ­a_04.jpg` a HTML
- RECONTEXTUALIZAR: el dato individual ahora se enmarca en el MA de Takita

**Contenido actualizado:**
```
TÍTULO: "La foto completa + nuestro zoom pediátrico"

Panel izquierdo (grande):
  "Panorámica global" — Takita 2025, 83 estudios
  52.1% IA vs Especialista: -15.8pp (p=0.007)
  IA ≈ No-especialista (p=0.93)

Panel derecho (destacado, borde verde):
  "En pediatría rural" — Del Monte 2025
  91.3% pediatra vs 87.3% IA (P=.47)
  "No significativo → IA es copiloto viable en AP rural"

Pie: 4 conclusiones numeradas:
1. Integrar IA como asistente inmediatamente
2. Soporte, no sustitución
3. Confiar pero verificar (26-36% errores factuales)
4. Nuevo rol: curador de output IA
```
- Referencias: **REF-A** + Del Monte (ref #15 actual) + datos existentes

---

### SLIDE 2B.15 — Sesgos Algorítmicos
🟢 MANTENER
- 🖼️→📝 Opcionalmente convertir `IA_Potencia_08.jpg` a HTML
- Contenido sobre 3 niveles de sesgo sigue siendo relevante y no cubierto

---

### SLIDE 2B.16 — Semáforo IA (investigación)
🟢 MANTENER
- Contenido de semáforo verde/amarillo/rojo para investigación es clave
- Diferente del semáforo AP (2C.19)

---

### SLIDE 2B.17 — Gaps Críticos (9.4% evalúa seguridad)
🔴 ELIMINAR
- El dato "solo 9.4% evalúa seguridad" SE SUBE a la nueva versión de 2B.8
  (la tercera barra del gráfico de brecha)
- El resto del contenido es redundante con lo ya cubierto

---

### SLIDES 2B.18 + 2B.19 + 2B.20 — Marco Legal (3 slides)
🟢 MANTENER las 3
- Contenido regulatorio (AI Act + RGPD + Ley 41/2002) no se ve afectado
  por la actualización bibliográfica
- Ya estaba señalado como denso (381 líneas HTML) pero es contenido
  imprescindible y no hay integradoras que lo absorban

---

## PARTE 3: RESUMEN DE OPERACIONES

### Conteo de slides resultante

| Operación | Slides afectadas | Resultado |
|-----------|------------------|-----------|
| ELIMINAR | 2B.5, 2B.17 | -2 |
| FUSIONAR 3→2 | 2B.10+2B.13+2B.14 | -1 |
| MODIFICAR | 2B.1, 2B.2, 2B.3, 2B.6, 2B.7, 2B.8, 2B.12 | 0 |
| MANTENER | 2B.0, 2B.4, 2B.9, 2B.11, 2B.15, 2B.16, 2B.18-20 | 0 |
| **TOTAL** | | **21 → 18 slides** |

### Imágenes eliminadas del HTML (→ reserva)

| Imagen | Slide origen | Razón |
|--------|-------------|-------|
| `IA_en_PediatrÃ­a_01.jpg` | 2B.5 (eliminada) | Se mantiene solo en 2C.2 |
| `IA_en_PediatrÃ­a_02+03.jpg` | 2B.6 | Sustituida por HTML |
| `IA_Potencia_05.jpg` | 2B.10, 2B.13 | Sustituida por HTML fusión |
| `IA_Potencia_06.jpg` | 2B.14 | Sustituida por HTML fusión |
| `slide_human_in_the_loop.jpg` | 2B.1 | Sustituida por HTML |
| `slide_venn_colaboracion.jpg` | 2B.2 | Sustituida por HTML |
| `slide_alucinacion_bibliografica.jpg` | 2B.7 | Sustituida por HTML |
| `slide_brecha_examenes_clinica.jpg` | 2B.8 | Sustituida por HTML |
| `IA_en_PediatrÃ­a_04.jpg` | 2B.12 | Sustituida por HTML |

**9 imágenes** salen del HTML activo → pasan a reserva en assets/

### Imágenes que SE MANTIENEN en HTML

| Imagen | Slide |
|--------|-------|
| `slide_fallos_rcp.jpg` | 2B.9 |
| `IA_Potencia_08.jpg` | 2B.15 (sesgos) — opcionalmente convertir |
| `IA_Potencia_09.jpg` | 2B.16 (semáforo) — opcionalmente convertir |

### Actualización de referencias

**ENTRAN (5):**
1. REF-A: Takita 2025 — DOI: 10.1038/s41746-025-01543-z
2. REF-B: JMIR NMA 2025 — DOI: 10.2196/64486
3. REF-C: Wang 2026 — DOI: 10.1038/s41746-026-02382-2
4. REF-D: Asgari 2025 — DOI: 10.1038/s41746-025-01670-7
5. REF-E: Goh 2025 — DOI: 10.1038/s41591-024-03456-y

**SALEN de primera línea (pasan a handout o notas):**
- Datos sueltos de precisión 55-93% (absorbidos por Takita)
- Estudio AIS individual de velocidad/reproducibilidad (parcialmente absorbido por JMIR NMA)
- Preprint Wang (sustituido por versión publicada)

**SE MANTIENEN como datos pediátricos específicos:**
- Del Monte 2025 (ref #15): dx rural pediátrico 91.3% vs 87.3%
- Datos salud mental pediátrica F1 (no cubiertos por MAs)
- Chelli 2024: alucinaciones bibliográficas (complementa a Asgari)
- Durgut 2025 (ref #25): ORL κ=1.0
- Estudio errores RCP 89.5%

---

## PARTE 4: RENUMERACIÓN

Tras los cambios, la numeración queda:

| Nuevo # | Antiguo # | Contenido |
|---------|-----------|-----------|
| 2B.0 | 2B.0 | Portada |
| 2B.1 | 2B.1 | Human-in-the-Loop (HTML) |
| 2B.2 | 2B.2 | Paradigma Colaboración (HTML, Takita+Wang) |
| 2B.3 | 2B.3 | Paradoja H+AI (Wang 2026 publicado + Goh RCT) |
| 2B.4 | 2B.4 | Pausa interactiva |
| 2B.5 | 2B.6 | Evidencia Actual (HTML, Takita+JMIR+pediátricos) |
| 2B.6 | 2B.7 | Alucinaciones (HTML dual: Chelli + Asgari) |
| 2B.7 | 2B.8 | Brecha Exámenes vs Clínica (HTML, +Takita, +9.4%) |
| 2B.8 | 2B.9 | Riesgo: Dr. AI (89.5% RCP) |
| 2B.9 | FUSIÓN | Mapa rendimiento (JMIR NMA rankings) |
| 2B.10 | FUSIÓN | Velocidad ≠ Fiabilidad ≠ Consenso |
| 2B.11 | 2B.11 | RAG y sesgo (ICC 0.27) |
| 2B.12 | 2B.12 | Precisión Diagnóstica (Takita + zoom pediátrico) |
| 2B.13 | 2B.15 | Sesgos Algorítmicos |
| 2B.14 | 2B.16 | Semáforo IA (investigación) |
| 2B.15 | 2B.18 | Marco Legal |
| 2B.16 | 2B.19 | Privacidad Pediátrica |
| 2B.17 | 2B.20 | Jurisdicciones y Checklist |

**Total: 18 slides (portada + 17 contenido)**
**Ratio: 18 slides / ~20 min = 1.11 min/slide** (mejora vs 1.2 min/slide anterior)

---

## PARTE 5: PRINCIPIOS DE DISEÑO HTML

Al convertir imágenes a HTML, respetar estos principios del CSS existente:

### Clases CSS disponibles (no crear nuevas)
- `glass-panel` — panel semitransparente con blur de fondo
- `text-gradient` — texto con gradiente (para títulos impactantes)
- `assertion-title` — título tipo afirmación (grande, bold)
- `grid-2` — grid de 2 columnas responsive
- `metric-value` — número destacado grande
- `abbr-tip` — tooltip para abreviaturas
- `fuente` — texto pequeño para citas al pie

### Criterios visuales para que HTML iguale a imagen
1. **Contraste:** Fondo oscuro → texto claro. Usar colores del sistema:
   - Azul IA: `#4FC3F7`
   - Verde médico: `#81C784`
   - Rojo alerta: `#EF5350`
   - Amarillo precaución: `#FFA726`
   - Dorado highlight: `#FFD54F`

2. **Jerarquía:** Un dato grande central (metric-value) + contexto pequeño alrededor.
   Máximo 2-3 cifras por slide.

3. **Espaciado:** Usar gap en flex/grid. Nunca saturar. El aire es contenido.

4. **Barras/gráficos:** Usar divs con width porcentual y border-radius para
   simular barras de progreso. No depender de librerías externas.

5. **Responsive:** Reveal.js tiene viewport fijo, pero usar em/rem para
   que el texto escale con el zoom del presentador.

### Estructura de cada slide (plantilla)
```html
<section data-menu-title="Título de slide">
  <!-- Hook: pregunta o afirmación provocadora -->
  <h3 class="assertion-title">Afirmación impactante</h3>

  <!-- Contenido visual: 1 concepto, máx 2-3 cifras -->
  <div class="grid-2">
    <div class="glass-panel">...</div>
    <div class="glass-panel">...</div>
  </div>

  <!-- Puente narrativo → siguiente slide -->
  <aside class="notes">
    Guion de locución aquí.
    Transición a la siguiente slide.
  </aside>
</section>
```

---

## PARTE 6: ACTUALIZACIÓN DE DOCUMENTOS ASOCIADOS

Tras ejecutar los cambios en el HTML, actualizar:

1. **mapa_y_assets_aepap2026.md**
   - Nuevo conteo: Bloque 2B = 18 slides
   - Total presentación: 71 - 3 = 68 slides
   - Actualizar tabla de slides con nueva numeración
   - Mover 9 imágenes de "en uso" a "reserva"
   - Actualizar duración estimada: ~20 min para Bloque 2B

2. **propuesta_refs_taxonomia_aepap2026.md**
   - Añadir 5 nuevas referencias (REF-A a REF-E)
   - Marcar referencias absorbidas como "en handout"

3. **Guion de locución** (si existe como archivo separado)
   - Adaptar narración a nueva secuencia
   - Los puentes entre slides cambian con la fusión

---

## NOTAS FINALES

- **PubMed MCP:** No disponible en el momento de esta revisión (error de carga).
  Las búsquedas se realizaron con Scholar Gateway, Consensus (sin resultado útil
  por error de aprobación), y web search dirigido. Los 5 artículos identificados
  tienen DOI y PMID verificados por web search.

- **Prioridad de implementación:**
  1. Primero: slides de FUSIÓN (2B.10+13+14 → 2 nuevas) — mayor ganancia
  2. Segundo: slide 2B.7 (alucinaciones) — mayor impacto visual con el dual panel
  3. Tercero: slides 2B.2 y 2B.6 — actualización de datos integradores
  4. Cuarto: resto de conversiones imagen→HTML

- **Validación post-cambio:** Verificar que cada slide tenga:
  ✅ Un solo concepto principal
  ✅ Máximo 2-3 cifras
  ✅ Fuente citada al pie
  ✅ Nota de locución en <aside class="notes">
  ✅ Puente narrativo a la siguiente slide
