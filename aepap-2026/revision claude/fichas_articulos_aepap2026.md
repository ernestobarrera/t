# 📚 Fichas Técnicas de Artículos Seleccionados
## Seminario AEPAP 2026 - IA en Pediatría

---

## 🏆 ARTÍCULOS DE MÁXIMA PRIORIDAD

---

### 1. Colaboración Humano-LLM en Medicina Clínica

| Campo | Información |
|-------|-------------|
| **Título** | Human-large language model collaboration in clinical medicine: a systematic review and meta-analysis |
| **Autores** | Wang G, Zhang K, Jiang J, Wang C, Bi H, Liang H, Qi Z, Huang Y, Li Y, Yang X |
| **Revista** | NPJ Digital Medicine |
| **Fecha** | 28 enero 2026 (Online ahead of print) |
| **DOI** | [10.1038/s41746-026-02382-2](https://doi.org/10.1038/s41746-026-02382-2) |
| **PMID** | 41606089 |
| **Registro** | PROSPERO CRD420251068272 |

#### Diseño Metodológico
- **Tipo:** Revisión sistemática y meta-análisis
- **Guía:** PRISMA 2020
- **Bases de datos:** 4 bases hasta 28 junio 2025
- **Estudios incluidos:** 10 peer-reviewed + 3 preprints (análisis sensibilidad)

#### Hallazgos Clave

| Outcome | Resultado | IC 95% | Interpretación |
|---------|-----------|--------|----------------|
| Precisión diagnóstica (k=2) | RR 1.59 | 0.08-32.74 | Tendencia positiva pero NO significativa |
| Scores compuestos (k=2) | MD +4.88 pp | +0.65 a +9.12 | Significativo pero alta incertidumbre (PI: -31.65 a 41.42) |
| Eficiencia temporal (k=3) | MD +0.4 min | -4.18 a +4.97 | Sin diferencia (I²=70.1%) |
| Errores factuales | 26-36% | - | Persisten a pesar de colaboración |

#### Hallazgo Crítico para tu Presentación
> *"In three-arm settings, H + AI did not universally outperform AI-only"*

**Traducción para audiencia:** Los médicos usando IA no necesariamente superan a la IA sola → El valor está en la VERIFICACIÓN, no en delegar.

#### Recomendaciones de los Autores
1. Ensayos pragmáticos, multicéntricos, pre-registrados
2. Outcomes estandarizados que prioricen **métricas de seguridad/error**
3. Interfaces que muestren incertidumbre y faciliten verificación

#### Relevancia para Seminario AEPAP
- ✅ Refuerza el **Performance Paradox** que mencionas
- ✅ Justifica el **Human-in-the-Loop** como no negociable
- ✅ Evidencia de alta calidad metodológica (PRISMA + PROSPERO)
- ✅ Dato impactante: errores 26-36% incluso con supervisión humana

---

### 2. IA y Carga de Documentación Clínica

| Campo | Información |
|-------|-------------|
| **Título** | Application of artificial intelligence tools and clinical documentation burden: a systematic review and meta-analysis |
| **Autores** | Zhao J, Liu H, Chen Y, Song F |
| **Afiliación destacada** | Children's Hospital of Chongqing Medical University |
| **Revista** | BMC Medical Informatics and Decision Making |
| **Fecha** | 24 diciembre 2025 |
| **DOI** | [10.1186/s12911-025-03324-w](https://doi.org/10.1186/s12911-025-03324-w) |
| **PMID** | 41444884 |
| **Registro** | PROSPERO CRD420250653291 |

#### Diseño Metodológico
- **Tipo:** Revisión sistemática y meta-análisis
- **Guía:** PRISMA
- **Estudios incluidos:** 23 estudios (12 con control concurrente, 11 antes-después)
- **Población:** Médicos, cirujanos, **pediatras**, intensivistas (principalmente ambulatorio)

#### Hallazgos Clave

| Outcome | Resultado | IC 95% |
|---------|-----------|--------|
| **Carga documentación global** | SMD = **-0.71** | -0.93 a -0.49 |
| Tiempo documentación (con edición) | SMD = -0.72 | -0.99 a -0.45 |
| Calidad notas IA | ≥ comparable a manual | - |

#### Interpretación del SMD -0.71
- Efecto **moderado** según Cohen
- Equivale aproximadamente a **reducción de 30-40% en tiempo percibido**
- Consistente con tu slide "Oxígeno para la Consulta"

#### Limitaciones Reportadas
- Heterogeneidad considerable entre estudios
- Calidad metodológica generalmente **baja**
- Necesidad de control de calidad riguroso

#### Cita para Presentación
> *"AI technologies offer promising benefits for reducing clinical documentation burden. However, their implementation must be accompanied by rigorous quality control and ongoing evaluation"*

#### Relevancia para Seminario AEPAP
- ✅ **Contexto pediátrico directo** (Children's Hospital)
- ✅ Dato SMD -0.71 ya incluido en tu presentación - ahora con referencia completa
- ✅ Valida el concepto de IA como "oxígeno" para consulta sobrecargada
- ✅ Incluye advertencia sobre control de calidad

---

### 3. RAG en LLMs Biomédicos: Guías de Desarrollo Clínico

| Campo | Información |
|-------|-------------|
| **Título** | Large language models and retrieval-augmented generation: a systematic review, meta-analysis, and clinical development guidelines |
| **Autores** | Liu S, McCoy AB, Wright A |
| **Afiliación** | Vanderbilt University Medical Center |
| **Revista** | Journal of the American Medical Informatics Association (JAMIA) |
| **Fecha** | Enero 2025 |
| **DOI** | [10.1093/jamia/ocaf008](https://doi.org/10.1093/jamia/ocaf008) |
| **PMID** | 39812777 |
| **PMCID** | PMC12005634 |

#### Diseño Metodológico
- **Tipo:** Revisión sistemática + meta-análisis + desarrollo de guías
- **Guía:** PRISMA 2020
- **Bases:** PubMed, Embase, PsycINFO (2023-2024)
- **Estudios incluidos:** 20 de 335 cribados

#### Hallazgo Principal

| Comparación | OR | IC 95% | p-valor |
|-------------|-----|--------|---------|
| RAG vs LLM base | **1.35** | 1.19-1.53 | 0.001 |

**Interpretación:** RAG mejora rendimiento un 35% en odds ratio respecto a LLMs sin retrieval.

#### Framework GUIDE Propuesto
Los autores desarrollan **"Guidelines for Unified Implementation and Development of Enhanced LLM Applications with RAG in Clinical Settings"**

#### Direcciones Futuras Identificadas
1. **System-level:** Combinación RAG + agentes
2. **Knowledge-level:** Integración profunda de conocimiento en LLM
3. **Integration-level:** RAG dentro de historia clínica electrónica

#### Relevancia para Seminario AEPAP
- ✅ Complementa tu slide sobre RAG con dato cuantitativo
- ✅ Framework aplicable a AP pediátrica
- ✅ De Vanderbilt - alta credibilidad institucional
- ✅ Visión de integración con HCE (relevante para OMI-AP, etc.)

---

## 🔥 ARTÍCULOS DE ALTA PRIORIDAD

---

### 4. LLMs con Whitelisting para Neurología Basada en Evidencia

| Campo | Información |
|-------|-------------|
| **Título** | Evaluating Web Retrieval-Assisted Large Language Models With and Without Whitelisting for Evidence-Based Neurology: Comparative Study |
| **Autores** | Masanneck L, Epping PZ, Meuth SG, Pawlitzki M |
| **Afiliación** | Heinrich Heine University Düsseldorf |
| **Revista** | Journal of Medical Internet Research (JMIR) |
| **Fecha** | 29 octubre 2025 |
| **DOI** | [10.2196/79379](https://doi.org/10.2196/79379) |
| **PMID** | 41159599 |
| **PMCID** | PMC12612646 |

#### Diseño Metodológico
- **Tipo:** Estudio comparativo diagnóstico
- **Modelos evaluados:** Perplexity Sonar, Sonar-Pro, Sonar-Reasoning-Pro + OpenEvidence
- **Dataset:** 130 preguntas validadas de guías AAN (65 factuales + 65 casos clínicos)
- **Evaluadores:** 2 neurólogos cegados + 3º para desacuerdos
- **Respuestas evaluadas:** 3,640 (κ interobservador = 0.86)

#### Hallazgos Clave

| Modelo | Sin whitelisting | Con whitelisting | Δ Mejora |
|--------|------------------|------------------|----------|
| Sonar | 60% | 78% | **+18 pp** |
| Sonar-Pro | 80% | 88% | +8 pp |
| Sonar-Reasoning-Pro | 81% | 89% | +8 pp |
| OpenEvidence | 82% | - | (referencia) |

#### Hallazgo Crítico
- Incluir ≥1 fuente no profesional **reduce a la mitad** las odds de respuesta correcta (OR 0.50)
- Citar documento AAN/neurología **duplica** las odds de acierto (OR 2.18)

#### Cita Clave
> *"Lightweight source control is therefore a pragmatic safety lever for maintaining continuously updated, web-based RAG-augmented LLMs fit for evidence-based [medicine]"*

#### Aplicación Directa para Pediatría AP
- Configurar LLMs para usar SOLO:
  - Guías AEPAP
  - Protocolos AEPED
  - Pediamécum
  - Guías NICE/AAP pediátricas
- Evitar fuentes no profesionales (foros, blogs, contenido no revisado)

#### Relevancia para Seminario AEPAP
- ✅ **Mensaje práctico inmediato** para los asistentes
- ✅ Cuantifica el beneficio de restringir fuentes (+8-18 puntos)
- ✅ "Safety lever" - concepto fácil de comunicar
- ✅ Metodología robusta (κ = 0.86)

---

### 5. Benchmarking LLMs en Medicina Basada en Evidencia

| Campo | Información |
|-------|-------------|
| **Título** | Benchmarking Large Language Models in Evidence-Based Medicine |
| **Autores** | Li J, Deng Y, Sun Q, Zhu J, Tian Y, Li J, Zhu T |
| **Revista** | IEEE Journal of Biomedical and Health Informatics |
| **Fecha** | Septiembre 2025 |
| **DOI** | [10.1109/JBHI.2024.3483816](https://doi.org/10.1109/JBHI.2024.3483816) |
| **PMID** | 39437276 |

#### Diseño Metodológico
- **Tipo:** Estudio de benchmarking comparativo
- **Modelos:** 7 LLMs (propietarios + open-source + fine-tuned médicos)
- **Tareas evaluadas:**
  1. Evidence retrieval (PICO extraction, biomedical QA)
  2. Evidence synthesis (resumen de RCTs)
  3. Evidence dissemination (simplificación texto médico)

#### Hallazgos Clave

| Técnica de Prompting | Mejora en GPT-4 (PICO extraction) |
|---------------------|-----------------------------------|
| Zero-shot (baseline) | - |
| In-context learning | Moderada |
| Chain-of-thought | Moderada |
| **Knowledge-guided prompting** | **+13.10%** |

#### Limitaciones Identificadas
- LLMs **peor que PubMedBERT** en Named Entity Recognition
- Inconsistencias factuales persistentes
- Inexactitudes de dominio específico

#### Cita para Presentación
> *"Human evaluation revealed persisting challenges with factual inconsistencies and domain inaccuracies, underscoring the need for rigorous quality control before clinical application"*

#### Relevancia para Seminario AEPAP
- ✅ Valida tu **método RECORD** (prompting estructurado mejora rendimiento)
- ✅ Cuantifica mejora: +13% con prompts guiados por conocimiento
- ✅ Confirma necesidad de verificación humana
- ✅ Útil para explicar por qué el prompting importa

---

### 6. Acelerando Síntesis de Evidencia Clínica (TrialMind)

| Campo | Información |
|-------|-------------|
| **Título** | Accelerating clinical evidence synthesis with large language models |
| **Autores** | Wang Z, Cao L, Danek B, Jin Q, Lu Z, Sun J |
| **Afiliación** | University of Illinois + NIH/NLM |
| **Revista** | NPJ Digital Medicine |
| **Fecha** | 8 agosto 2025 |
| **DOI** | [10.1038/s41746-025-01840-7](https://doi.org/10.1038/s41746-025-01840-7) |
| **PMID** | 40775042 |
| **PMCID** | PMC12331930 |

#### Diseño Metodológico
- **Tipo:** Desarrollo de pipeline + estudio piloto de colaboración humano-IA
- **Dataset:** TrialReviewBench (100 revisiones sistemáticas, 2,220 estudios clínicos)
- **Herramienta:** TrialMind (pipeline de IA generativa)

#### Hallazgos del Estudio Piloto

| Tarea | Mejora con Human-AI |
|-------|---------------------|
| **Recall en búsqueda** | +71.4% |
| **Tiempo de screening** | -44.2% |
| **Precisión extracción datos** | +23.5% |
| **Tiempo extracción** | -63.4% |
| Preferencia expertos (TrialMind vs GPT-4) | 62.5-100% |

#### Relevancia para Seminario AEPAP
- ✅ Demuestra el **Modelo Sandwich** en acción (humano-IA-humano)
- ✅ Datos impactantes para mostrar beneficio de colaboración bien diseñada
- ✅ Contraste con Wang 2026: la colaboración SÍ funciona cuando está bien estructurada
- ✅ Aplicable a revisión de literatura/protocolos en AP

---

### 7. Panorámica de LLMs en Sanidad (Scoping Review)

| Campo | Información |
|-------|-------------|
| **Título** | Advancing healthcare with large language models: A scoping review of applications and future directions |
| **Autores** | Zhang Z, Momeni Nezhad MJ, Bagher Hosseini SM, et al. |
| **Afiliación** | Columbia University |
| **Revista** | International Journal of Medical Informatics |
| **Fecha** | Marzo 2026 |
| **DOI** | [10.1016/j.ijmedinf.2025.106231](https://doi.org/10.1016/j.ijmedinf.2025.106231) |
| **PMID** | 41443123 |

#### Diseño Metodológico
- **Tipo:** Scoping review
- **Estudios incluidos:** 415 (enero 2023 - julio 2024)
- **Base:** PubMed

#### Distribución de Aplicaciones

| Aplicación | Porcentaje |
|------------|------------|
| Decisión clínica | 26.7% |
| Información al paciente | 23.9% |
| Educación/formación | 18.1% |
| Investigación | 16.1% |
| Soporte workflow | 12.5% |

#### Hallazgo Crítico sobre Seguridad
> **Solo el 9.4% de estudios evaluaron errores y seguridad**

#### Modelos más Usados
1. GPT-4: 51.3%
2. GPT-3.5: 36.6%
3. ChatGPT: 22.4%

#### Relevancia para Seminario AEPAP
- ✅ Visión panorámica para contextualizar
- ✅ Dato impactante: <10% evalúan seguridad
- ✅ Justifica tu énfasis en gaps críticos
- ✅ De Columbia - alta credibilidad

---

## 📚 ARTÍCULOS COMPLEMENTARIOS

---

### 8. Tutorial: Terminología IA/ML en Medicina

| Campo | Información |
|-------|-------------|
| **Título** | AI and Machine Learning Terminology in Medicine, Psychology, and Social Sciences: Tutorial and Practical Recommendations |
| **Autores** | Cao B, Greiner R, Greenshaw A, Sui J |
| **Afiliación** | University of Alberta |
| **Revista** | JMIR |
| **Fecha** | 18 agosto 2025 |
| **DOI** | [10.2196/66100](https://doi.org/10.2196/66100) |
| **PMID** | 40825233 |
| **PMCID** | PMC12360722 |

#### Contenido Clave
- **Jerarquía conceptual:** AI → ML → DL → LLMs → GenAI
- Uso correcto de "predicción" vs "asociación"
- Diferencia entre features, predictores, factores de riesgo, factores causales
- Procedimientos de validación para generalización

#### Relevancia para Seminario AEPAP
- ✅ Perfecto para tu **Bloque 2: Fundamentos**
- ✅ Clarifica conceptos para audiencia no técnica
- ✅ Evita confusiones terminológicas comunes
- ✅ Formato tutorial - muy didáctico

---

### 9. IA y Salud Mental de Profesionales Sanitarios

| Campo | Información |
|-------|-------------|
| **Título** | Enhancing healthcare worker mental health via artificial intelligence-driven work process improvements: a scoping review |
| **Autores** | Dave B, Martin P, David SS, Kumar S, Chakraborty T |
| **Revista** | International Journal of Medical Informatics |
| **Fecha** | 26 septiembre 2025 |
| **DOI** | [10.1016/j.ijmedinf.2025.106122](https://doi.org/10.1016/j.ijmedinf.2025.106122) |
| **PMID** | 41037981 |

#### Hallazgos Clave
- **Burnout** = problema más frecuentemente abordado
- **Documentación clínica** = workflow más intervenido
- IA capaz de: streamlining workflows, reducir carga administrativa, mejorar satisfacción laboral

#### Barreras Identificadas
- Integración de datos
- Sesgo algorítmico
- **Aumento de demandas de supervisión** (oversight paradox)

#### Relevancia para Seminario AEPAP
- ✅ Conecta IA con bienestar del profesional
- ✅ Relevante para AP sobrecargada
- ✅ Advierte sobre posible aumento de carga por supervisión

---

### 10. Chatbots GenAI en Salud Mental: Meta-análisis

| Campo | Información |
|-------|-------------|
| **Título** | Generative AI Mental Health Chatbots as Therapeutic Tools: Systematic Review and Meta-Analysis |
| **Autores** | Zhang Q, Zhang R, Xiong Y, Sui Y, Tong C, Lin FH |
| **Afiliación** | Duke-NUS Medical School + Johns Hopkins |
| **Revista** | JMIR |
| **Fecha** | 16 diciembre 2025 |
| **DOI** | [10.2196/78238](https://doi.org/10.2196/78238) |
| **PMID** | 41401240 |
| **PMCID** | PMC12707440 |

#### Hallazgos del Meta-análisis (14 RCTs, N=6,314)

| Outcome | ES | IC 95% | p |
|---------|-----|--------|---|
| Reducción problemas salud mental | **0.30** | 0.004-0.59 | 0.047 |

#### Hallazgo sobre Tipo de Chatbot
- **Social-oriented** (interacción social) > **Task-oriented** (tareas específicas)

#### Limitaciones Identificadas
- Empatía limitada
- Transparencia de seguridad insuficiente
- Matiz emocional reducido

#### Relevancia para Seminario AEPAP
- ✅ Aplicable a comunicación con familias
- ✅ Efecto pequeño pero significativo
- ✅ Advierte sobre limitaciones en empatía
- ✅ Metodología robusta (RCTs + meta-análisis)

---

## 🔗 ENLACES RÁPIDOS PARA DESCARGA

| # | Artículo | Enlace DOI |
|---|----------|------------|
| 1 | Wang 2026 (H+AI) | https://doi.org/10.1038/s41746-026-02382-2 |
| 2 | Zhao 2025 (Documentación) | https://doi.org/10.1186/s12911-025-03324-w |
| 3 | Liu 2025 (RAG) | https://doi.org/10.1093/jamia/ocaf008 |
| 4 | Masanneck 2025 (Whitelisting) | https://doi.org/10.2196/79379 |
| 5 | Li 2025 (EBM Benchmark) | https://doi.org/10.1109/JBHI.2024.3483816 |
| 6 | Wang 2025 (TrialMind) | https://doi.org/10.1038/s41746-025-01840-7 |
| 7 | Zhang 2026 (Scoping) | https://doi.org/10.1016/j.ijmedinf.2025.106231 |
| 8 | Cao 2025 (Terminología) | https://doi.org/10.2196/66100 |
| 9 | Dave 2025 (Salud mental HCW) | https://doi.org/10.1016/j.ijmedinf.2025.106122 |
| 10 | Zhang 2025 (Chatbots MH) | https://doi.org/10.2196/78238 |

---

## 📋 ACCESO ALTERNATIVO

Para artículos con acceso restringido, opciones:

1. **PubMed Central (PMC):** Artículos 2, 3, 4, 6, 8, 10 tienen PMCID - acceso gratuito
2. **Sci-Hub:** Para acceso académico (uso bajo responsabilidad del usuario)
3. **Solicitud a autores:** Via ResearchGate o email institucional
4. **Biblioteca institucional:** Muchas universidades españolas tienen acceso a JMIR, JAMIA, NPJ Digital Medicine

---

*Documento generado para Seminario AEPAP 2026*
*Fecha: Febrero 2026*
