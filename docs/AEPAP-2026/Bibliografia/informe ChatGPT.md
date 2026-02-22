# Informe integrador (últimos 365 días) + mapa temático + guion de 14 diapositivas (assertion-evidence)

Este informe se construye a partir de tu exportación de resultados (títulos/abstracts; ~1060 registros) y se apoya en fuentes “ancla” (guías, marcos de reporte, revisiones y estudios de despliegue real) para minimizar el riesgo de afirmaciones no sustentadas.

---

## Mini-glosario (para evitar ambigüedades)

- **Barandillas (guardrails):** controles técnicos y procedimentales que limitan qué puede hacer el sistema y cómo lo hace (p. ej., responder solo si hay evidencia recuperada; forzar citas; umbrales de abstención; plantillas; verificación; revisión humana; auditoría y monitorización).
- **“Viñetas limpias”:** casos clínicos “de examen” o escenarios idealizados sin ruido real (comorbilidad, contradicciones en notas, campos incompletos, cronología confusa). Sirven para comparar modelos, pero tienden a sobreestimar rendimiento y seguridad en práctica real.
- **Alucinación:** contenido plausible pero falso (dato inventado, omisión crítica, causalidad no justificada, cita inexistente o incorrecta). En clínica, el modo de fallo gemelo es la **omisión**: dejar fuera el dato peligroso.

---

## 1) Qué captura tu búsqueda (y qué sesgos introduce)

### 1.1 Arquitectura conceptual de la query

Tu estrategia combina 4 capas:

1. **Tareas clínicas**: diagnóstico/razonamiento, interpretación de pruebas, comunicación, educación sanitaria, flujo de trabajo/EHR, seguridad del paciente, ética, sesgos, implementación, cálculo de dosis, barreras lingüísticas.
2. **“Evidencia” y normativas**: guías, consensos, vías clínicas, reglas clínicas, y además evidencia secundaria (systematic review, meta-analysis, HTA, umbrella, etc.).
3. **Tecnología**: LLM/generative AI + nombres concretos (ChatGPT, Claude, Gemini, Copilot, etc.).
4. **Filtro de fuentes**: lista amplia de revistas + **“last 365 days”**.

### 1.2 Consecuencias para “estado del arte”

- **Fortaleza:** obliga a entrar a trabajos con estructura evaluable (revisiones, guías, consensos): lenguaje común para congreso.
- **Sesgo:** puede perder trabajos influyentes fuera de la lista de journals (conferencias, ingeniería, seguridad) y piezas técnicas que no se rotulan con términos de LLM.

---

## 2) Lectura descriptiva del corpus (tu exportación)

### 2.1 Macro-temas (asignación principal aproximada)

- evaluación y reporting ≈ 39%
- evidencia y guías ≈ 29%
- comunicación y educación ≈ 10%
- seguridad/ética/sesgo/privacidad ≈ 9%
- implementación y adopción ≈ 7%
- workflow y documentación ≈ 3%
- decisión clínica y diagnóstico ≈ 3%
- otros ≈ residual

**Lectura:** el último año está dominado por cómo evaluar, reportar y gobernar; la evidencia pragmática a gran escala crece pero sigue siendo minoritaria.

### 2.2 Señales de madurez

- muchos estudios “offline” y marcos de evaluación (bien)
- menos estudios prospectivos, menos monitorización post-despliegue (brecha)
- seguridad (alucinación/omisión) aparece, pero no siempre con métricas clínicas robustas

---

## 3) Mapa temático (clusters) para narrativa de congreso

### Isla 1 — Evaluación (la obsesión actual)

- benchmarks, exámenes, comparaciones humano vs LLM
- evaluación con datos reales vs “viñetas limpias”
- métricas: exactitud, utilidad, daño potencial, robustez, calibración, abstención
- evaluación por subgrupos (fairness)

**Ancla:** revisión sistemática que subraya foco excesivo en exámenes y limitaciones de despliegue.

- JAMA 2025: https://pubmed.ncbi.nlm.nih.gov/39405325/

### Isla 2 — Reporting & trazabilidad (antídoto contra hype)

- guías de reporte para estudios con chatbots/LLM
- declarar: datos, prompts, versiones, comparadores, métricas, fallos, gobernanza

**Ancla:** CHART statement (chatbots que dan consejo sanitario/educación).

- Artif Intell Med 2025: https://pubmed.ncbi.nlm.nih.gov/40753040/

### Isla 3 — Seguridad clínica (daño por invención u omisión)

- alucinación, omisiones, citas falsas
- riesgos de confianza injustificada
- “stop rules”: abstención + escalado + verificación

**Anclas:** evaluación de borradores de resúmenes/alta en urgencias.

- PLOS Digit Health 2025: https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000899

### Isla 4 — Integración en flujo real (donde se gana o se pierde)

- documentación (scribes, alta, resumen)
- carga cognitiva/administrativa
- riesgo: automatizar debilidades del registro

**Ancla:** ensayo/estudio en urgencias con reducción de tiempo al redactar alta.

- JAMA Netw Open 2025: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2840377

### Isla 5 — Gobernanza y regulación

- privacidad y seguridad (RGPD), responsabilidad, auditoría
- marco UE (AI Act) y guías OMS

**Anclas:**

- AI Act: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- OMS (gobernanza): https://pmc.ncbi.nlm.nih.gov/articles/PMC12406769/

### Isla 6 — Equidad (seguridad diferencial)

- sesgos por representación de datos
- degradación por idioma/dialecto/entorno
- auditoría por subgrupos y red teaming

**Ancla:** sesgos sociodemográficos en escenarios clínicos.

- npj Digit Med 2025: https://pubmed.ncbi.nlm.nih.gov/40195448/

---

## 4) Insights accionables (para el congreso)

1. La evidencia se desplaza de “¿acierta?” a “¿cómo se evalúa sin engañarnos?”  
   Fuente: https://pubmed.ncbi.nlm.nih.gov/39405325/

2. La amenaza principal no es el error grosero: es el error con buena prosa (y sin fuentes).  
   La respuesta segura es “proceso”: barandillas + auditoría + abstención.

3. Documentación es el motor de adopción más plausible por ROI medible, pero exige gobernanza del registro.  
   Fuente: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2840377

4. La unidad de análisis es el sistema socio-técnico: datos, tarea, supervisión, registro, monitorización.  
   Fuente: https://pmc.ncbi.nlm.nih.gov/articles/PMC12406769/

5. Reporting no es burocracia: es seguridad del paciente (si no se puede auditar, no se puede confiar).  
   Fuente: https://pubmed.ncbi.nlm.nih.gov/40753040/

6. Sesgo no es “tema moral”: es degradación diferencial de calidad clínica y comunicación.  
   Fuente: https://pubmed.ncbi.nlm.nih.gov/40195448/

---

# Diseño assertion-evidence (para Reveal.js)

**Regla:** 1 diapositiva = 1 afirmación verificable (assertion) + evidencia visible (evidence) + 1 referencia “ancla”.

**Formato por diapositiva:**

- **Título** (assertion) sobrio, técnico, sin eslóganes.
- **Evidence**: 3–6 bullets con definición + implicación práctica.
- **Visual sugerida**: diagrama simple (pipeline, matriz, checklist).
- **Nota del ponente**: 30–60 s de explicación.
- **Referencia clave**: 1–3 enlaces (artículo/guía).

---

# 14 diapositivas (Reveal.js friendly)

## 1. La adopción clínica de LLM requiere evaluar “utilidad + riesgo + control”, no solo exactitud

**Evidence**

- Evaluar: rendimiento (qué hace) + seguridad (cómo falla) + integración (cómo cambia el trabajo).
- Métricas clínicas además de “accuracy”: omisiones, confabulaciones, calibración de incertidumbre, daño potencial.
- La evidencia reciente muestra predominio de evaluaciones “tipo examen” y menos estudios de despliegue.

**Visual sugerida**: triángulo “Rendimiento–Seguridad–Flujo de trabajo” con ejemplos.

**Notas**

- “Funciona” no es binario; depende de tarea, contexto y barandillas.
- Mensaje: pasamos de demos a evaluación clínica formal.

**Referencia clave**

- JAMA 2025 (systematic review): https://pubmed.ncbi.nlm.nih.gov/39405325/  
  Cita (fragmento corto): “Existing evaluations… mostly focus on accuracy… for medical examinations.”

## 2. Qué es un LLM en clínica: motor probabilístico de lenguaje; la “verdad” es un proceso

**Evidence**

- Predice texto token a token: excelente completando patrones; no garantiza veracidad.
- Dos fallos críticos: invención (alucinación) y omisión (silenciosa).
- Convertirlo en herramienta clínica exige barandillas: anclaje a fuentes, abstención y supervisión.

**Visual sugerida**: pipeline “prompt + contexto → modelo → verificación → salida con citas”.

**Notas**

- Explicar de forma didáctica por qué suena convincente incluso cuando es incorrecto.
- En clínica, la prosa puede “enmascarar” incertidumbre.

**Referencia clave**

- OMS (gobernanza y riesgos): https://pmc.ncbi.nlm.nih.gov/articles/PMC12406769/  
  Cita (fragmento corto): “Governance… accountability… and risk management…”

## 3. Benchmarks vs práctica real: el campo produce métricas más rápido que evidencia pragmática

**Evidence**

- Benchmark: comparabilidad; práctica real: complejidad y consecuencias.
- Señal del último año: mucho “offline evaluation/reporting”, menos despliegue monitorizado.
- Implicación: prudencia al extrapolar “performance” a “seguridad”.

**Visual sugerida**: escalera de evidencia “benchmark → retrospectivo → prospectivo → despliegue monitorizado”.

**Notas**

- Conectar con medicina basada en evidencia: jerarquía y validez externa.
- “Lo que mide un benchmark” no siempre es lo que importa al paciente.

**Referencia clave**

- JAMA 2025: https://pubmed.ncbi.nlm.nih.gov/39405325/

## 4. “Viñetas limpias” inflan rendimiento: la clínica real introduce ruido y datos faltantes

**Evidence**

- Viñeta limpia: caso completo, sin contradicciones, sin longitudinalidad.
- Historia real: múltiples fuentes, cronología incierta, campos incompletos, comorbilidad, medicación.
- Esto cambia el modo de fallo: aumentan omisiones y confabulaciones plausibles.

**Visual sugerida**: comparación “viñeta” vs “historia real” (columnas).

**Notas**

- Aclarar el término: “limpio” = idealizado.
- Mensaje: la evaluación debe incluir “stress tests” con datos incompletos o contradictorios.

**Referencia clave**

- The evaluation illusion (preprint): https://www.researchgate.net/publication/396282525_The_evaluation_illusion_of_large_language_models_in_medicine  
  Cita (fragmento corto): “Benchmark success… can mask real-world failure.”

## 5. Reporting es una tecnología de seguridad: sin transparencia no hay reproducibilidad ni auditoría

**Evidence**

- Declarar: datos, prompts, versión de modelo, comparadores, métricas, manejo de incertidumbre.
- Sin reporting: resultados irrepetibles; imposible detectar sesgo o degradación.
- Buen reporting reduce alucinación “en el discurso científico” (afirmaciones sin soporte).

**Visual sugerida**: checklist mínimo (8–10 ítems) para estudios/implementaciones.

**Notas**

- Conectar con cultura clínica: como CONSORT/PRISMA para ensayos y revisiones.
- El reporting crea “defensas” contra hype.

**Referencia clave**

- CHART statement: https://pubmed.ncbi.nlm.nih.gov/40753040/  
  Cita (fragmento corto): “CHART… provide reporting recommendations…”

## 6. Alucinación clínica: modo de fallo esperable; debe detectarse, contenerse y registrarse

**Evidence**

- Modos: hechos inventados, omisiones críticas, cronología errónea, mezcla de paciente, citas falsas.
- Señales de riesgo: respuestas sin fuentes, tono de certeza, ausencia de “qué falta”.
- Contención: abstención (“no se puede concluir”), escalado y verificación sistemática.

**Visual sugerida**: árbol de fallos “origen → manifestación → mitigación”.

**Notas**

- Enfatizar que la omisión puede ser más peligrosa que el error evidente.
- Proponer lenguaje estándar de incertidumbre.

**Referencia clave**

- PLOS Digit Health 2025 (evaluación de borradores): https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000899  
  Cita (fragmento corto): “Omissions and confabulation…”

## 7. Barandillas técnicas: RAG + citas + límites de alcance reducen daño; el retrieval es el cuello de botella

**Evidence**

- RAG: recuperar texto fuente (guías/artículos) → responder anclado.
- Forzar citas y “evidencia mínima” para responder.
- Riesgo: si el retrieval falla (fuente irrelevante), el modelo “argumenta” con evidencia equivocada.

**Visual sugerida**: “RAG loop” (pregunta → retrieval → respuesta con citas → verificación).

**Notas**

- Explicar “cuello de botella”: la calidad de la respuesta depende de lo que recupera.
- Proponer métrica práctica: porcentaje de respuestas con cita pertinente.

**Referencia clave**

- RAG en medicina (revisión): https://pubmed.ncbi.nlm.nih.gov/39779929/

## 8. Documentación clínica es el caso de uso con ROI más medible, pero exige gobernanza del registro

**Evidence**

- Beneficios: tiempo, carga administrativa, estructura del texto.
- Riesgos: autoridad automática, copia sin revisión, alucinación documental.
- Requisito: revisión humana obligatoria + trazabilidad de edición.

**Visual sugerida**: flujo “borrador → revisión → firma” con puntos de control.

**Notas**

- Presentar documentación como “zona de aterrizaje” de IA porque el humano revisa naturalmente.
- Pero: lo escrito tiene consecuencias clínicas y legales.

**Referencia clave**

- JAMA Netw Open 2025: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2840377  
  Cita (fragmento corto): “Median writing time decreased from 69.5 to 32.0 seconds…”

## 9. Integración en EHR: cuando el LLM entra en el sistema, privacidad y auditoría son requisitos centrales

**Evidence**

- Evita “copiar/pegar” sin control; promueve despliegues seguros.
- Logs: qué se generó, qué se cambió, quién aprobó.
- Incidentes: deben reportarse como seguridad del paciente.

**Visual sugerida**: cadena del dato “entrada → generación → edición → registro → auditoría”.

**Notas**

- La integración formal permite gobernanza; el uso informal la impide.
- Introducir “safety case” para IA (argumento documentado de seguridad).

**Referencia clave**

- PLOS Digit Health 2025 (implementación en EHR): https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0001141  
  Cita (fragmento corto): “The system runs entirely within the hospital’s secure network…”

## 10. Soporte a decisión/diagnóstico: el patrón seguro es “hipótesis + plan de verificación + condiciones de abstención”

**Evidence**

- No “diagnóstico final”; sí: diferenciales, qué dato falta, qué prueba confirma, qué red flags cambian el plan.
- Validación: prospectiva, subgrupos, datos reales.
- Evitar cierre prematuro: diseñar fricción deliberada (checklists y límites).

**Visual sugerida**: plantilla 5 bloques (hallazgos → diferenciales → datos faltantes → pruebas → plan).

**Notas**

- Explicar “fricción deliberada”: añadir pasos para evitar confianza injustificada.
- Conectar con razonamiento clínico clásico.

**Referencia clave**

- JAMA 2025 (limitaciones de evaluación): https://pubmed.ncbi.nlm.nih.gov/39405325/

## 11. Comunicación y educación a pacientes: valor inmediato si se evalúa exactitud, comprensión y seguridad

**Evidence**

- Riesgo: consejo convincente pero incorrecto (y con “tono empático”).
- Evaluación: legibilidad + exactitud + “señales de alarma” + límites explícitos.
- Mejor uso: reescritura y estructuración; no “autorización clínica”.

**Visual sugerida**: plantilla “qué es / qué hacer / qué vigilar / cuándo volver”.

**Notas**

- Resaltar que comunicación es intervención clínica: reduce reconsultas y errores.
- Exigir revisión y fuentes cuando se dan recomendaciones.

**Referencia clave**

- CHART statement (health advice): https://pubmed.ncbi.nlm.nih.gov/40753040/

## 12. Educación médica: tutor útil, pero puede enseñar con seguridad injustificada si no se controla la fuente

**Evidence**

- Aporta: explicación, generación de casos, feedback, simulación.
- Riesgo: explicaciones plausibles falsas; “sobreconfianza pedagógica”.
- Barandillas: fuentes, ejercicios de verificación, evaluación de incertidumbre.

**Visual sugerida**: ciclo “caso → respuesta → fuente → verificación → reflexión”.

**Notas**

- Proponer práctica docente: el alumno debe poder rastrear el origen (guía/estudio).
- Usar como tutor socrático, no como oráculo.

**Referencia clave**

- Revisión sobre rendimiento en exámenes: https://www.jmir.org/2024/1/e60807/

## 13. Sesgo y equidad: rendimiento medio oculta degradación diferencial por subgrupos

**Evidence**

- Sesgo por datos: representación desigual.
- Sesgo por contexto: idioma, dialecto, nivel educativo, acceso digital.
- Mitigación: evaluación estratificada, red teaming, monitorización post-despliegue.

**Visual sugerida**: tabla de métricas por subgrupo + umbral de alerta.

**Notas**

- Enfatizar: equidad = seguridad. La degradación diferencial es daño.
- Recomendación: auditar antes y después del despliegue.

**Referencia clave**

- npj Digit Med 2025: https://pubmed.ncbi.nlm.nih.gov/40195448/

## 14. Gobernanza y regulación: convertir “prudencia” en sistema operativo (roles, procesos, auditoría)

**Evidence**

- Componentes mínimos: política de uso, revisión, trazabilidad, monitorización, respuesta a incidentes.
- Marco UE: enfoque por riesgo (AI Act).
- Gobernanza OMS: accountability y gestión de riesgos.

**Visual sugerida**: tablero de mando (métricas + incidentes + auditorías + actualizaciones).

**Notas**

- Cierre: IA en clínica = calidad asistencial aplicada a sistemas que generan texto.
- Propuesta: empezar por 1 caso de uso con evaluación y monitorización.

**Referencias clave**

- AI Act: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- OMS (gobernanza): https://pmc.ncbi.nlm.nih.gov/articles/PMC12406769/

---

## Bibliografía “ancla” (lista corta)

- JAMA 2025 systematic review: https://pubmed.ncbi.nlm.nih.gov/39405325/
- CHART statement (Artif Intell Med 2025): https://pubmed.ncbi.nlm.nih.gov/40753040/
- ED discharge documentation (JAMA Netw Open 2025): https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2840377
- EHR implementation (PLOS Digit Health 2025): https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0001141
- ED encounter summaries evaluation (PLOS Digit Health 2025): https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000899
- Sociodemographic bias (npj Digit Med 2025): https://pubmed.ncbi.nlm.nih.gov/40195448/
- OMS governance (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC12406769/
- AI Act (EU): https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- Evaluation illusion (preprint): https://www.researchgate.net/publication/396282525_The_evaluation_illusion_of_large_language_models_in_medicine
