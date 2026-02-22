# ESTRUCTURA DEFINITIVA: Bloques 2C–5
# Seminario AEPap 2026 — Versión post-consolidación
# Fecha: 2026-02-20
# Estado: APROBADO PARA EJECUCIÓN (abierto a ajustes incrementales)

---

## RESUMEN DE CAMBIOS

| Métrica | Antes | Después | Δ |
|---------|-------|---------|---|
| Slides 2C | 21 | 10 | −11 |
| Slides Bloque 3 | 7 | 3 | −4 |
| Slides Bloque 4 | 3 | 3 | 0 |
| Slides Bloque 5 | 6 | 6 | 0 |
| **Total pendientes** | **37** | **22** | **−15** |
| **Total presentación** | **67** | **52** | **−15** |
| Tiempo estimado | ~120+ | ~114 | Margen 6 min |

**Principio rector:** Pirámide 5.0, catálogo de herramientas, RECORD y GPTs/Gems NO son demos — son contenido teórico-práctico que pertenece al bloque de Aplicaciones. "Demo" = solo lo que funciona en directo ante el público.

---

## ESTRUCTURA SLIDE POR SLIDE

### BLOQUE 2C: "De la Evidencia a la Práctica" (10 slides, ~25 min)

Arco narrativo: Lo que funciona → En qué dominios → Cómo medir madurez → Cómo preguntar → Con qué herramientas → Cómo asegurar → Qué delegar → Resumen

---

#### #31 — 2C.0 Portada bloque
- **Assertion:** "De la evidencia a tu consulta: 5 decisiones prácticas"
- **Subtítulo:** "~25 minutos"
- **Contenido:** Transición desde 2B. Icono + título + tiempo
- **Origen:** 2C.0 original (actualizar subtítulo de 15→25 min)
- **Audio:** ~15s. "Hemos visto la evidencia. Ahora toca lo concreto."
- **Imagen:** Ninguna
- **HTML:** Mínimo, solo actualizar tiempo y assertion

---

#### #32 — Documentación: la evidencia más sólida
- **Assertion:** "La IA recupera tiempo clínico al reducir burocracia"
- **Subtítulo:** "Meta-análisis: reducción moderada-alta (SMD = −0.71)"
- **Contenido principal:**
  - Panel izq: Zhao MA (23 incluidos, 14 en pool, SMD=-0.71). CONSERVAR imagen slide_oxigeno_consulta.jpg (metáfora antes/después)
  - Panel der: IA ambiental pipeline (23 estudios speech-to-text). CONSERVAR infografía de #40 original
  - Barra inferior: Goodson caveat ("percepción ≠ métrica") + Impacto consulta
- **Origen:** Fusión #32 (2C.1 Oxígeno) + #40 (2C.2 IA Ambiental) + #39 (2C.8 Documentación, ELIMINADA)
- **Refs verificadas:**
  - Zhao et al. BMC Med Inform Decis Mak. 2025;26:29. DOI: 10.1186/s12911-025-03324-w
  - Goodson et al. Learning Health Systems. 2025 (paradoja productividad burnout)
- **Audio:** ~90s. Tesis: la documentación es donde la evidencia es más sólida. Goodson matiza: percepción de ahorro ≠ ahorro medido. Triple impuesto de revisión. Pero el balance neto es positivo.
- **Imágenes:** 2 (slide_oxigeno_consulta.jpg + infografía pipeline ambiental de #40)
- **⚠️ Complejidad HTML:** ALTA. Dos paneles con imágenes distintas + barra caveat. Requiere diseño cuidado

---

#### #33 — Aplicaciones clínicas por dominio
- **Assertion:** "Más allá de la documentación: dónde la IA ya aporta valor"
- **Subtítulo:** "5 dominios pediátricos con evidencia 2024-2026"
- **Contenido:** Tabla HTML 5 filas × 4 columnas:

| Dominio | Aplicación | Métrica clave | Nivel evidencia |
|---------|-----------|---------------|-----------------|
| Neonatal | ROP screening, hipoxemia periop | F1 0.89, AUC 0.85 | Medio (validación) |
| Salud bucodental | Caries escolar (screening) | Sens 82-96%, Esp 77-99% | Medio (screening) |
| Salud mental | Detección riesgo suicida | 99% detección, 89% genuino | Bajo (solo investigación) |
| Dx precoz AP | Apoyo diagnóstico precoz | Variable según contexto | Medio (soporte) |
| Educación médica | MCQs, simulación, simplificación | Calidad comparable | Alto (listo) |

- **Origen:** Fusión #41 (Dx precoz) + #42 (Pediatría neonatal) + #43 (Caries) + #44 (Riesgo suicida) + #45 (Educación médica)
- **Audio:** ~75s. No listar: narrar con hilo. "La IA no solo documenta. En neonatología detecta ROP con F1 de 0.89. En salud mental, identifica mensajes de riesgo suicida con 99% de detección. Pero fijaos en la columna de la derecha: cuanto más cerca del juicio clínico, más lejos del uso seguro."
- **Imagen:** Ninguna (tabla HTML nativa)
- **Refs:** Verificar DOIs de cada dominio (pendiente sesión futura)

---

#### #34 — Matriz de madurez tecnológica
- **Assertion:** "Estado del arte 2026: qué funciona, qué promete, qué evitar"
- **Contenido:** Tabla HTML nativa 5×4 (reemplaza imagen slide_matriz_madurez.jpg)
  - Administrativo: Alto (Listo) — Zhao 2025
  - Educación: Alto (Listo) — Nguyen 2025
  - Diagnóstico: Medio (Soporte) — Ilić & Sarajlija 2025
  - Investigación: Medio (Verificar) — Var 2025
  - Salud Mental: Bajo (Solo Investigación) — Mansoor 2025
- **Origen:** #46 (2C.15 Matriz Madurez), rediseñada sin imagen
- **Audio:** ~60s. "Esta tabla resume lo que hemos visto. Verde: listo para usar, con supervisión. Amarillo: promete pero hay que verificar cada output. Rojo: solo investigación, nada clínico todavía."
- **Imagen:** ELIMINAR slide_matriz_madurez.jpg → tabla HTML
- **Refs pendientes:** Verificar DOIs de Nguyen, Ilić & Sarajlija, Var, Mansoor

---

#### #35 — Prompt Engineering clínico: la estructura lo cambia todo
- **Assertion:** "Un prompt pobre genera medicina inestable"
- **Subtítulo:** "De 32% a 100% de adherencia con estructura"
- **Contenido:**
  - Panel izq: Callens 4 pasos (Rol, Contexto, Tarea, Salida) — HTML nativo, NO imagen con erratas
  - Panel central: Método RECORD (R+E+C+O+R+D con ejemplos pediátricos)
  - Panel der o inferior: Dato determinista (32%→100% adherencia con checklist)
  - Técnicas mencionadas en texto/audio: CoT, Few-shot, Role prompting
- **Origen:** Fusión #34 (2C.3 Callens) + #35 (2C.4 Técnicas) + #36 (2C.5 Context Eng) + #45 (2C.14 Determinista) + **3.4 (RECORD como método)**
- **Refs verificadas:**
  - Callens S. Acta Clin Belg. 2026;1-12. DOI: 10.1080/17843286.2026.2613903
  - Barrera-Linares E. Método RECORD. Zenodo. 2024
- **Audio:** ~90s. Slide densa pero crucial. "La diferencia entre una respuesta útil y una peligrosa no está en el modelo. Está en cómo le preguntas. Callens propone 4 pasos. Nosotros lo ampliamos con RECORD, que añade restricciones y diseño de salida. El dato clave: con estructura, la adherencia a estándares pasa del treinta y dos al cien por ciento."
- **Imagen:** ELIMINAR slide_prompt_eng_checklist.jpg (erratas irrecuperables) → HTML limpio
- **⚠️ Complejidad HTML:** ALTA. 3 paneles con mucho contenido. Considerar dividir en 2 slides si la carga cognitiva es excesiva: #35a (Callens + RECORD) y #35b (Técnicas avanzadas + dato determinista). Decisión final en ejecución.

---

#### #36 — Tu caja de herramientas: Pirámide 5.0
- **Assertion:** "No todas las herramientas IA son iguales: elige por nivel de confianza"
- **Contenido:**
  - Pirámide 5.0 adaptada: 3 niveles de herramientas IA + evidencia
    - Base: Búsqueda y síntesis (Undermind, Scite, Elicit, Consensus)
    - Medio: Modelos fundacionales (ChatGPT, Claude, Gemini, DeepSeek)
    - Cima: RAG clínico (Open Evidence, Perplexity Pro, NotebookLM)
  - Catálogo por nivel de confianza (absorbe contenido de 3.2 Herramientas)
  - Mención ecosistema 2026: 93.55% estudios evalúan generalistas, open-source emerge
- **Origen:** Fusión 3.1 (Pirámide 5.0) + 3.2 (Herramientas IA) + parte de 2C.6 (Mapa) + 2C.7 (Ecosistema)
- **Refs:**
  - Alper BS, Haynes RB. EBHC pyramid 5.0. Evid Based Med. 2016;21(4):123-5
  - Barrera E. Pirámide de Evidencia 5.0 y Herramientas IA. 2025
- **Audio:** ~75s. "No es lo mismo preguntarle a ChatGPT que buscar en Consensus. La Pirámide 5.0, que conocéis de medicina basada en la evidencia, se adapta perfectamente a la IA. En la base, herramientas de búsqueda semántica. En el medio, los modelos generalistas. Y en la cima, herramientas que solo responden desde fuentes verificadas. Vuestro nivel de confianza debe subir con la pirámide."
- **Imagen:** Ninguna nueva (diseño HTML con CSS pirámide/escalones)
- **⚠️ Considerar:** Si la Pirámide 5.0 tiene complejidad visual alta, puede justificar slide propia (#36) y separar Ecosistema/Agéntica en #37. Evaluar en ejecución.

---

#### #37 — GPTs, Gems y personalización: tu asistente a medida
- **Assertion:** "Un asistente preconfigurado elimina el prompting repetitivo"
- **Contenido:**
  - Qué son: mini-asistentes preconfigurados sin programar
  - Ejemplos pediátricos: "GPT Revisor de Analíticas", "Gem Simplificador para Padres"
  - Cómo crearlos (3 pasos)
  - Limitaciones: herencia de alucinaciones del modelo base
- **Origen:** 3.5 (GPTs y Gems), migrada íntegramente a 2C
- **Audio:** ~60s. "Si os habéis preguntado cómo evitar escribir el mismo prompt cada vez, esta es la respuesta. Un GPT personalizado o un Gem de Google es un asistente que ya tiene vuestras instrucciones memorizadas."
- **Imagen:** Ninguna específica

---

#### #38 — RAG + Whitelisting: la solución técnica
- **Assertion:** "En point-of-care, sin RAG no hay seguridad suficiente"
- **Subtítulo:** "Regla binaria: si no cita fuente primaria verificable, no se usa clínicamente"
- **Contenido:**
  - Panel izq: Diagrama RAG (Pregunta → Búsqueda Fuentes → Generación SOLO de lo leído). HTML nativo, reemplaza imagen
  - Panel der: Whitelisting (precisión 60%→78%, +18pp)
  - Métrica central: OR=1.35 (Liu JAMIA 2025)
  - Regla binaria en barra inferior
- **Origen:** Fusión #47 (2C.16 RAG) + #48 (2C.17 Whitelisting)
- **Refs verificadas:**
  - Liu S et al. JAMIA. 2025;32(4):605-615. DOI: 10.1093/jamia/ocaf008
  - ⚠️ Source-note actual dice "Nat Med" → CORREGIR a "JAMIA"
- **Audio:** ~70s. "RAG es la diferencia entre una IA que inventa y una que busca antes de responder. El metaanálisis de Liu, veinte estudios, muestra una mejora significativa: OR de uno con treinta y cinco. Y si además restringes las fuentes, el whitelisting, la precisión sube dieciocho puntos. La regla es simple: si no cita fuente verificable, no lo uses en clínica."
- **Imagen:** ELIMINAR slide_rag_estandar.jpg → diagrama HTML

---

#### #39 — Semáforo AP: qué delegar hoy y qué prohibir
- **Assertion:** "Tu consulta del lunes: qué adoptar, qué supervisar, qué evitar"
- **Diferenciación con #29 (2B.16):**
  - #29 = semáforo de INVESTIGACIÓN (criterio: detectabilidad del error)
  - #39 = semáforo de CONSULTA AP (criterio: nivel de supervisión requerido)
- **Contenido:** 3 cajas (verde/amarillo/rojo) con tareas de consulta AP
  - Verde (Usar ahora): Admin, documentación, borradores para familias
  - Amarillo (Con supervisión): Dx diferencial con RAG, enfermedades raras
  - Rojo (Evitar): Confianza ciega, sustitución del juicio clínico
- **Origen:** #50 (2C.19 Semáforo AP)
- **Audio:** ~65s. Anclar: "En el bloque de evidencia vimos el semáforo para investigación. Este es el de vuestra consulta del lunes." Ref Moulaei 2024
- **Imagen:** CONSERVAR slide_semaforo_ap.jpg (infografía clara y accionable) O sustituir por HTML
- **Nota:** Si se conserva imagen, verificar que no duplique visualmente #29

---

#### #40 — Síntesis: 5 mensajes para el lunes
- **Assertion:** "Lo que te llevas de este bloque"
- **Contenido:** 5 mensajes accionables alineados con las "5 decisiones":
  1. **Empieza por documentación** — evidencia sólida, riesgo bajo
  2. **Elige herramienta por nivel de confianza** — Pirámide 5.0
  3. **Estructura tus prompts** — RECORD o Callens, siempre
  4. **Exige fuentes verificables** — sin RAG, no hay seguridad clínica
  5. **Delega lo verde, supervisa lo amarillo, prohíbe lo rojo**
- **Origen:** #51 (2C.20 Síntesis), reescrita para alinear con 5 decisiones
- **Audio:** ~45s. Breve, impactante, sin datos nuevos. Cierre de bloque.
- **Imagen:** Ninguna (texto limpio)

---

### BLOQUE 3: "Demostración en Vivo" (3 slides, ~12 min)

**Principio:** Solo lo que se ejecuta en directo ante el público. Sin teoría, sin catálogos.

---

#### #41 — 3.0 Portada demos
- **Assertion:** "Veámoslo funcionar"
- **Subtítulo:** "~12 minutos"
- **Audio:** ~10s. "Basta de teoría. Vamos a ver estas herramientas funcionar en directo."

---

#### #42 — Demo: NotebookLM
- **Contenido:** Demo en vivo. PubMed → abstracts → podcast/slides generados
- **Origen:** 3.3 (sin cambios sustanciales)
- **Audio:** Breve intro (~20s) + demo en directo (sin audio narrado durante la demo)
- **Iframe/recurso embebido:** Sí

---

#### #43 — Demo: Constructor de Prompts
- **Contenido:** Demo en vivo. Prompt builder interactivo embebido en Reveal.js
- **Origen:** 3.6 (sin cambios sustanciales)
- **Audio:** Breve intro (~20s) + demo interactiva
- **Iframe/recurso embebido:** Sí

---

### BLOQUE 4: "Práctica Guiada" (3 slides, ~20 min)

Sin cambios estructurales. RECORD se practica aquí (el método se aprendió en #35).

---

#### #44 — 4.0 Portada práctica
- **Origen:** 4.0 original
- **Audio:** ~15s. "Ahora os toca a vosotros. Vamos a practicar con el método RECORD."
- **Subtítulo:** Actualizar tiempo si procede

#### #45 — 4.1 Generador de prompts (3 templates)
- **Origen:** 4.1 original
- **Contenido:** 3 templates: info familias, sesión clínica, email
- **Audio:** ~60s explicando cada template

#### #46 — 4.2 Ejercicio en grupos
- **Origen:** 4.2 original
- **Contenido:** 3 casos clínicos, 15 min práctica
- **Audio:** ~30s intro + 15 min ejercicio (sin audio narrado)

---

### BLOQUE 5: "Cierre" (6 slides, ~12 min)

Sin cambios estructurales. Enriquecimiento del audio pendiente.

---

#### #47 — 5.0 Portada cierre
- **Origen:** 5.0 original

#### #48 — 5.1 Modelo Sándwich
- **Origen:** 5.1 original
- **Audio pendiente:** Enriquecer con deliberación pre-algorítmica + analogía aviación/CRM (del arsenal conceptual)

#### #49 — 5.2 Lo que nos llevamos
- **Origen:** 5.2 original
- **Contenido:** 3 takeaways: Sándwich + RECORD + Detector alucinaciones

#### #50 — 5.3 Test 1 (GEA familias)
- **Origen:** 5.3 original. Respuesta correcta: 5 (borrador info familias)

#### #51 — 5.4 Test 2 (verificación crítica)
- **Origen:** 5.4 original. Respuesta correcta: 4 (evaluar críticamente)

#### #52 — 5.5 Gracias
- **Origen:** 5.5 original

---

## TABLA DE CORRESPONDENCIA: NUMERACIÓN ANTIGUA → NUEVA

| Deck# ANTIGUO | Código slide | Deck# NUEVO | Acción |
|:---:|:---:|:---:|:---:|
| #31 | 2C.0 | **#31** | Mantener (actualizar subtítulo) |
| #32 | 2C.1 Oxígeno | **#32** | Fusionar con #39 y #40 |
| #33 | 2C.2 Ambiental | — | ELIMINAR (absorbida en #32 nuevo) |
| #34 | 2C.3 Prompt Eng | **#35** | Fusionar con #35, #36, #45, 3.4 |
| #35 | 2C.4 Técnicas | — | ELIMINAR (absorbida en #35 nuevo) |
| #36 | 2C.5 Context Eng | — | ELIMINAR (absorbida en #35 nuevo) |
| #37 | 2C.6 Mapa | — | ELIMINAR (absorbida en #36 nuevo) |
| #38 | 2C.7 Ecosistema | **#36** (parcial) | Fusionar con 3.1 y 3.2 |
| #39 | 2C.8 Documentación | — | ELIMINAR (redundante con #32) |
| #40 | 2C.9/Ambiental 23 estudios | **#32** (parcial) | Fusionar en #32 nuevo |
| #41 | 2C.10 Dx precoz | **#33** | Fusionar en tabla dominios |
| #42 | 2C.11 Pediatría | **#33** | Fusionar en tabla dominios |
| #43 | 2C.12 Caries | **#33** | Fusionar en tabla dominios |
| #44 | 2C.13 Riesgo suicida | **#33** | Fusionar en tabla dominios |
| #45 | 2C.14 Educación/Determinista | **#33** + **#35** | Dividir entre tabla y prompting |
| #46 | 2C.15 Matriz | **#34** | Rediseñar (imagen → HTML) |
| #47 | 2C.16 RAG | **#38** | Fusionar con #48 + corregir Nat Med→JAMIA |
| #48 | 2C.17 Whitelisting | **#38** | Fusionar con #47 |
| #49 | 2C.18 Híbrido | — | ELIMINAR (redundante con #39/#40/#49 nuevos) |
| #50 | 2C.19 Semáforo AP | **#39** | Mantener (diferenciar de #29) |
| #51 | 2C.20 Síntesis | **#40** | Reescribir: alinear con 5 decisiones |
| #52 | 3.0 Portada demos | **#41** | Simplificar (solo demos reales) |
| #53 | 3.1 Pirámide 5.0 | **#36** | Migrar a 2C (es teoría, no demo) |
| #54 | 3.2 Herramientas IA | **#36** | Migrar a 2C (es catálogo, no demo) |
| #55 | 3.3 Demo NotebookLM | **#42** | Mantener en Bloque 3 |
| #56 | 3.4 Demo RECORD | **#35** | Migrar a 2C como método (no demo rota) |
| #57 | 3.5 GPTs y Gems | **#37** | Migrar a 2C (es descripción, no demo) |
| #58 | 3.6 Demo Constructor | **#43** | Mantener en Bloque 3 |
| #59 | 4.0 | **#44** | Mantener |
| #60 | 4.1 | **#45** | Mantener |
| #61 | 4.2 | **#46** | Mantener |
| #62 | 5.0 | **#47** | Mantener |
| #63 | 5.1 | **#48** | Mantener (enriquecer audio) |
| #64 | 5.2 | **#49** | Mantener |
| #65 | 5.3 | **#50** | Mantener |
| #66 | 5.4 | **#51** | Mantener |
| #67 | 5.5 | **#52** | Mantener |

---

## TIMING DEFINITIVO

| Bloque | Slides | Deck# | Min | Rol narrativo |
|--------|:---:|:---:|:---:|:---:|
| 0: Encuadre | 4 | #1–#4 | ~5 | ✅ Cerrado |
| 1: Ruptura | 5 | #5–#9 | ~8 | ✅ Cerrado |
| 2A: Fundamentos | 4 | #10–#13 | ~7 | ✅ Cerrado |
| 2B: Evidencia | 17 | #14–#30 | ~25 | ✅ Cerrado |
| **2C: Aplicaciones** | **10** | **#31–#40** | **~25** | Qué, cómo, con qué |
| **3: Demo en vivo** | **3** | **#41–#43** | **~12** | Ver funcionar |
| 4: Práctica | 3 | #44–#46 | ~20 | Hacer (5+15) |
| 5: Cierre | 6 | #47–#52 | ~12 | Cerrar + evaluar |
| **TOTAL** | **52** | **#1–#52** | **~114** | **Margen: 6 min** |

---

## SLIDES ELIMINADAS (15 total)

| Deck# antiguo | Motivo |
|:---:|:---:|
| #33 (2C.2 Ambiental) | Absorbida en #32 fusionada |
| #35 (2C.4 Técnicas) | Absorbida en #35 nuevo (prompting) |
| #36 (2C.5 Context Eng) | Absorbida en #35 nuevo (prompting) |
| #37 (2C.6 Mapa) | Absorbida en #36 nuevo (ecosistema) |
| #39 (2C.8 Documentación) | Redundante con #32 (misma ref Zhao) |
| #41-#44 (dominios individuales) | Fusionadas en #33 nuevo (tabla) |
| #45 (2C.14 Determinista) | Dato absorbido en #35 nuevo (prompting) |
| #48 (2C.17 Whitelisting) | Fusionada con #47 → #38 nuevo |
| #49 (2C.18 Híbrido) | Redundante con #39/#40/#49 nuevos |
| #53 (3.1 Pirámide) | Migrada a 2C como #36 |
| #54 (3.2 Herramientas) | Migrada a 2C como #36 |
| #56 (3.4 RECORD demo) | Migrada a 2C como método en #35 |
| #57 (3.5 GPTs/Gems) | Migrada a 2C como #37 |

---

## IMÁGENES: DECISIONES FINALES

| Imagen | Slide nueva | Acción | Motivo |
|--------|:---:|:---:|:---:|
| slide_oxigeno_consulta.jpg | #32 | ✅ CONSERVAR | Metáfora visual antes/después |
| Infografía pipeline ambiental (#40) | #32 | ✅ CONSERVAR | Diagrama complejo bien hecho |
| slide_prompt_eng_checklist.jpg | — | ❌ ELIMINAR | Erratas IA irrecuperables |
| slide_matriz_madurez.jpg | — | ❌ ELIMINAR | Sustituir por tabla HTML |
| slide_rag_estandar.jpg | — | ❌ ELIMINAR | Sustituir por HTML + corregir fuente |
| slide_conclusiones_hibrido.jpg | — | ❌ ELIMINAR | Slide eliminada |
| slide_semaforo_ap.jpg | #39 | ⚠️ EVALUAR | Conservar si no confunde con #29 |
| IA_en_Pediatría_01.jpg | — | Libre | Ya no usada en 2C (era #33 Ambiental) |

---

## ERRORES CORREGIDOS / PENDIENTES

### ✅ Resueltos en esta sesión
1. Callens DOI: 10.1080/17843286.2026.2613903 (Acta Clin Belg 2026)
2. Liu JAMIA: 10.1093/jamia/ocaf008 (JAMIA 2025;32(4):605-615, NO Nat Med)
3. Zhao año: publicado dic 2025, vol.26. Citar como 2025;26:29
4. Zhao números: 23 incluidos / 14 en MA pooled (ambos correctos)

### 🔧 Pendientes para ejecución
5. Refs tabla Matriz (#34): Nguyen, Ilić & Sarajlija, Var — buscar DOIs
6. Refs tabla dominios (#33): verificar DOIs de cada estudio por dominio
7. Slide #39 (Semáforo AP): decidir imagen vs HTML
8. Slide #35 (Prompting): decidir si 1 o 2 slides según carga cognitiva
9. 2C.4 dato CoT 17.9%→58.1%: es GSM8K (matemáticas), no clínico — buscar dato clínico o eliminar
10. Bloque 2B pendientes: #17 PI→composite, #18 pie→JAMA Netw Open, eliminar 2B.14

### 📌 Notas para ajustes futuros (14 días hasta congreso)
- Nuevas slides con recursos prácticos: bienvenidas si refuerzan didáctica
- Cualquier adición debe tener tesis única y no duplicar contenido existente
- Nuevos recursos deben encajar en la Pirámide 5.0 (nivel de confianza)
- Si se añaden slides a 2C, ajustar timing (#40 Síntesis se desplaza al final)

---

## INSTRUCCIONES PARA CLAUDE EN PRÓXIMA SESIÓN

```
Proyecto AEPap 2026 — Fase ejecución.

Audio completado: Bloques 0–2B (#1–#30).
Estructura consolidada: ver estructura_definitiva_2C_5.md

Bloques pendientes de audio:
- 2C (#31–#40): 10 slides, ~25 min
- 3 (#41–#43): 3 slides, ~12 min
- 4 (#44–#46): 3 slides, ~20 min
- 5 (#47–#52): 6 slides, ~12 min

Prioridad: ejecutar HTML + audio de 2C slide por slide.
Slides de mayor complejidad HTML: #32 (2 paneles con imagen), 
#35 (prompting consolidado), #36 (Pirámide + ecosistema).

Principios: numeración absoluta (#31...), fonética TTS española, 
estilo Feynman, una tesis por slide, verificar DOIs.
Abierto a ajustes incrementales si refuerzan didáctica.
```

---

*Documento generado: 2026-02-20. Vigente hasta ejecución completa.*
