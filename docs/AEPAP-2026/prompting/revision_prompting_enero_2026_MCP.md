# Ingeniería de prompts para modelos de lenguaje: taxonomía, evidencia y fronteras

**La ingeniería de prompts constituye hoy el principal mecanismo de interacción entre humanos y modelos de lenguaje de gran escala (LLMs), y su dominio determina diferencias de rendimiento de hasta 76 puntos porcentuales en una misma tarea.** Este libro blanco sintetiza más de 58 técnicas documentadas en la literatura, con evidencia cuantitativa procedente de benchmarks como GSM8K, MMLU y BigBench Hard, y analiza cómo el paradigma está siendo transformado por modelos con razonamiento nativo (o1, o3, DeepSeek-R1). La revolución iniciada por Brown et al. (2020) con GPT-3 —que demostró que los LLMs podían resolver tareas sin entrenamiento adicional, únicamente mediante instrucciones en lenguaje natural— ha evolucionado en menos de cinco años hacia sistemas multiagente, optimización automática de prompts y la integración de herramientas externas. Sin embargo, como revelan los estudios de Sclar et al. (2024, ICLR), incluso cambios triviales en el formato de un prompt (espaciado, delimitadores, puntuación) pueden colapsar el rendimiento de un modelo, lo que subraya la necesidad de un enfoque riguroso y basado en evidencia para esta disciplina.

---

## 1. Evolución histórica: de la ingeniería de características al diseño de contexto

La trayectoria de la interacción con modelos de lenguaje puede describirse mediante cuatro cambios paradigmáticos. El primero ocurrió en 2018, cuando BERT (Devlin et al.) popularizó el paradigma de preentrenamiento y ajuste fino (*pre-train, fine-tune*), reemplazando la ingeniería manual de características. El segundo llegó en 2020, cuando **GPT-3** (Brown et al., NeurIPS 2020), con 175.000 millones de parámetros, demostró que un modelo podía realizar tareas en configuración zero-shot, one-shot y few-shot sin actualizar sus pesos, inaugurando la era del prompting como forma primaria de programación de LLMs.

El tercer cambio se consolidó entre 2022 y 2023, con la explosión de técnicas estructuradas de razonamiento: Chain-of-Thought (Wei et al., 2022), ReAct (Yao et al., 2022), Tree of Thoughts (Yao et al., 2023) y Self-Consistency (Wang et al., 2022). Simultáneamente, la alineación mediante instrucciones (InstructGPT, Ouyang et al., 2022) y RLHF democratizó el acceso a modelos que seguían instrucciones de forma nativa, reduciendo la necesidad de ejemplos few-shot elaborados. El cuarto cambio, aún en curso en 2025, desplaza el foco desde el prompt individual hacia la **ingeniería de contexto**: el diseño de sistemas completos que proporcionan la información correcta en el momento adecuado, incluyendo agentes, herramientas, memoria y orquestación multi-modelo (Anthropic, 2025; DSPy, Khattab et al., ICLR 2024).

La encuesta más exhaustiva hasta la fecha —*The Prompt Report* (Schulhoff et al., 2024, arXiv:2406.06608)— analizó 1.565 artículos mediante revisión PRISMA y catalogó **58 técnicas de prompting textual**, 40 técnicas multimodales y 33 términos formales del vocabulario del campo.

---

## 2. Taxonomía comprehensiva de técnicas de prompting

### 2.1 Técnicas fundacionales: zero-shot y few-shot

El **prompting zero-shot** consiste en presentar una instrucción al modelo sin ningún ejemplo demostrativo. Fue conceptualizado por Radford et al. (2019) con GPT-2 y formalizado por Brown et al. (2020). Su rendimiento mejora consistentemente con la escala del modelo: GPT-2 (1.500M parámetros) obtuvo resultados competitivos en 7 de 8 benchmarks de modelado de lenguaje, y GPT-3 demostró mejoras monotónicas en 42 benchmarks de precisión conforme aumentaba la escala.

El **prompting few-shot** (también llamado aprendizaje en contexto, *in-context learning* o ICL) proporciona K pares de entrada-salida como demostración antes de la consulta. Brown et al. (2020) evaluaron K entre 10 y 100 (limitado por la ventana de contexto de 2.048 tokens). Los resultados clave revelan que el rendimiento mejora con más ejemplos, pero con rendimientos decrecientes; que modelos más grandes se benefician más de los ejemplos adicionales; y que el few-shot de GPT-3 se aproximó al rendimiento de BERT ajustado finamente en varias tareas de SuperGLUE.

Un hallazgo seminal de Min et al. (2022, EMNLP) transformó la comprensión del ICL: **las etiquetas correctas en las demostraciones no son necesarias** — reemplazar etiquetas por valores aleatorios apenas afecta el rendimiento. Los factores realmente determinantes son el espacio de etiquetas (mostrar qué etiquetas existen), la distribución del texto de entrada y el formato estructural de la secuencia. Esto reenmarca el aprendizaje en contexto como señalización de formato y distribución, no como aprendizaje de correspondencias entrada-etiqueta.

### 2.2 Razonamiento mediante cadena de pensamiento (CoT)

**Chain-of-Thought prompting** (Wei et al., 2022, NeurIPS 2022) constituye posiblemente la innovación más influyente en ingeniería de prompts. La técnica aumenta el prompting few-shot incluyendo pasos de razonamiento intermedios en las demostraciones: en lugar de pares ⟨entrada, salida⟩, se proporcionan tripletas ⟨entrada, cadena de pensamiento, salida⟩. Los resultados cuantitativos son extraordinarios:

- **GSM8K**: PaLM 540B pasó del **17,9%** (prompting estándar) al **58,1%** con CoT, superando a GPT-3 ajustado fino con verificador (55%).
- CoT es una **capacidad emergente de la escala**: solo funciona en modelos con ≥100.000 millones de parámetros. Modelos más pequeños producen cadenas "fluidas pero ilógicas".
- Las mejoras son mayores en problemas más difíciles: GSM8K mostró una mejora de más del doble, mientras que tareas triviales mostraron mejora mínima o negativa.

**Zero-shot CoT** (Kojima et al., 2022, NeurIPS 2022) elimina la necesidad de ejemplos manuales añadiendo simplemente la frase **"Let's think step by step"** al final del prompt. Los resultados son notables: en MultiArith, InstructGPT pasó del 17,7% al **78,7%** (una mejora absoluta de 61 puntos); en GSM8K, del 10,4% al **40,7%**. Kojima et al. probaron múltiples variantes de la frase inductora; "Let's think step by step" resultó ser la más efectiva.

### 2.3 Self-Consistency y métodos de ensamblaje

**Self-Consistency** (Wang et al., 2022, ICLR 2023) reemplaza la decodificación greedy del CoT estándar con un procedimiento de muestreo y voto mayoritario: se generan múltiples caminos de razonamiento mediante muestreo estocástico (temperatura > 0) y se selecciona la respuesta más frecuente. La intuición es que problemas complejos admiten múltiples rutas de razonamiento válidas que convergen en la respuesta correcta.

Los resultados sobre PaLM-540B son consistentes: **+17,9 puntos** en GSM8K (de 56,5% a 74,4%), +12,5 en AQuA, +7,6 en SVAMP, +6,3 en StrategyQA. El rendimiento escala positivamente con el número de caminos muestreados (típicamente 40), y la técnica es robusta ante diferentes conjuntos de prompts y estrategias de muestreo. Su principal limitación es el **costo computacional**: requiere múltiples pasadas de inferencia, y solo es aplicable a problemas con conjuntos de respuestas fijos (no generación abierta).

### 2.4 Estructuras de razonamiento: Tree of Thoughts y Graph of Thoughts

**Tree of Thoughts (ToT)** (Yao et al., 2023, NeurIPS 2023) generaliza CoT modelando el razonamiento como búsqueda en un árbol. Cada nodo representa una solución parcial; el modelo genera candidatos de pensamiento, los autoevalúa (clasificándolos como "seguro/posible/imposible") y aplica BFS o DFS con retroceso. El caso emblemático es el **Juego del 24**: GPT-4 con prompting estándar alcanza solo el **7,3%**, CoT baja al 4,0%, CoT-SC (k=100) llega al 9,0%, pero **ToT (b=5, BFS) alcanza el 74%** — una mejora de 10× sobre el mejor método alternativo. El costo, sin embargo, es de 5-100× más tokens generados.

**Graph of Thoughts (GoT)** (Besta et al., 2024, AAAI 2024) extiende ToT a grafos dirigidos arbitrarios G = (V, E), donde los vértices son pensamientos y las aristas representan dependencias. La innovación clave es la **agregación**: GoT puede combinar múltiples pensamientos en síntesis sinérgicas, crear bucles de refinamiento y realizar destilación. En tareas de ordenamiento, GoT mejoró la calidad un **62% sobre ToT** y un **70% sobre CoT**, reduciendo simultáneamente los costos en más del 31% respecto a ToT.

### 2.5 ReAct: razonamiento con acción

**ReAct** (Yao et al., 2023, ICLR 2023) entrelaza trazas de razonamiento en lenguaje natural con acciones sobre entornos externos (APIs de búsqueda, bases de datos). El modelo genera alternadamente tokens de *Thought* (razonamiento), *Action* (llamada a herramienta) y *Observation* (respuesta del entorno). En **ALFWorld**, ReAct superó a métodos de imitación y refuerzo por **+34 puntos** de tasa de éxito absoluta usando solo 1-2 ejemplos en contexto. En **HotpotQA**, la combinación ReAct + CoT-SC produjo los mejores resultados globales, reduciendo las alucinaciones al anclar el razonamiento en información externa.

### 2.6 Retrieval-Augmented Generation (RAG)

**RAG** (Lewis et al., 2020, NeurIPS 2020) combina memoria paramétrica (modelo generativo) con memoria no paramétrica (índice vectorial de documentos). Gao et al. (2024) propusieron una taxonomía tripartita: **RAG ingenuo** (indexación → recuperación → generación), **RAG avanzado** (con reescritura de consultas, re-ranking y compresión de contexto) y **RAG modular** (arquitectura flexible con módulos intercambiables). RAG estableció el estado del arte en tres tareas de QA de dominio abierto (Natural Questions, TriviaQA, WebQuestions) y los evaluadores humanos prefirieron sus generaciones sobre las de BART por factualidad y especificidad. Los enfoques RAG más recientes reducen las alucinaciones entre un **18% y un 40%** dependiendo de la arquitectura; SELF-RAG logró tasas de alucinación del **5,8%** en QA clínica.

### 2.7 Técnicas de descomposición

**Least-to-Most prompting** (Zhou et al., 2023, ICLR 2023) aborda el problema de la generalización composicional: primero descompone un problema complejo en subproblemas ordenados del más simple al más complejo, y luego resuelve cada subproblema secuencialmente, incorporando las respuestas anteriores. En el benchmark **SCAN** (split de longitud), alcanzó el **99,7%** de precisión con GPT-3 code-davinci-002 usando solo 14 ejemplos, frente al 16,2% con CoT — modelos neurales-simbólicos especializados requerían 15.000+ ejemplos.

**Decomposed Prompting (DecomP)** (Khot et al., 2023, ICLR 2023) va más allá al delegar subtareas a una **biblioteca de manejadores especializados** que pueden ser otros prompts de LLM, modelos entrenados o sistemas simbólicos (e.g., ElasticSearch para recuperación). Esto permite optimización independiente de cada componente y descomposición recursiva.

### 2.8 Verificación y reducción de alucinaciones

**Chain-of-Verification (CoVe)** (Dhuliawala et al., 2024, ACL Findings 2024) implementa un marco de autoverificación en cuatro etapas: respuesta inicial → generación de preguntas de verificación → respuesta independiente a cada pregunta (sin sesgo de la respuesta original) → respuesta revisada. La variante *factor+revise* mejoró el **FACTSCORE** en generación de biografías un 28% (de 55,9 a ~71,4), logrando reducciones de alucinaciones del **50-70%** en tareas de QA y generación de formato largo.

**Generated Knowledge Prompting** (Liu et al., 2022, ACL 2022) genera conocimiento declarativo relevante antes de responder, usando el propio modelo como fuente de conocimiento. Logró mejoras zero-shot del **7-10%** en NumerSense, CSQA y QASC, y estableció el estado del arte en tres benchmarks de razonamiento de sentido común.

### 2.9 Prompting de roles, personas y sistemas

El **prompting de roles** asigna una persona o identidad al modelo. Los resultados son mixtos y matizados: Kong et al. (2024, NAACL) demostraron mejoras significativas (AQuA: de 53,5% a 63,8%; Last Letter: de 23,8% a 84,2%), pero Pei y Jurgens (2024) encontraron en un estudio a gran escala que **los roles en prompts de sistema generalmente no mejoran el rendimiento** en tareas objetivas. El consenso emergente es que el role prompting beneficia primariamente las tareas subjetivas y creativas.

El **prompting de sistema** es una característica arquitectónica de los modelos de chat que define roles, límites comportamentales y restricciones persistentes. OpenAI implementa un sistema de tres roles (system, user, assistant); Anthropic utiliza un parámetro de sistema dedicado. La guía de GPT-4.1 (OpenAI, 2025) recomienda una estructura canónica: Rol y Objetivo → Instrucciones → Pasos de razonamiento → Formato de salida → Ejemplos → Contexto → Instrucciones finales.

### 2.10 Técnicas avanzadas y automatizadas

**Directional Stimulus Prompting (DSP)** (Li et al., 2023, NeurIPS 2023) utiliza un modelo de política pequeño y ajustable (e.g., T5) para generar estímulos direccionales específicos por instancia que guían a un LLM congelado. Con solo 80 diálogos, DSP mejoró el rendimiento de ChatGPT en MultiWOZ un **41,4%**.

**Automatic Prompt Engineering (APE)** (Zhou et al., 2022, ICLR 2023) enmarca la ingeniería de prompts como optimización de caja negra: un LLM genera candidatos de instrucciones, que se evalúan mediante rendimiento zero-shot. APE superó prompts escritos por humanos en **24 de 24 tareas** de Instruction Induction. **OPRO** (Yang et al., 2023, Google DeepMind) extendió este paradigma, descubriendo prompts que superaron a los escritos por humanos en un 8% en GSM8K y 50% en BigBench Hard.

**Meta-Prompting** (Suzgun y Kalai, 2024) transforma un LLM único en un "director" que descompone tareas, delega subtareas a instancias "expertas" del mismo modelo con instrucciones especializadas, e integra los resultados con verificación cruzada. Superó a CoT y few-shot estándar en benchmarks como BigBench Hard y MGSM.

**Reflexion** (Shinn et al., 2023, NeurIPS 2023) dota a agentes LLM de memoria dinámica y autorreflexión: tras recibir retroalimentación del entorno, el agente reflexiona verbalmente sobre sus fallos y almacena esta reflexión para intentos futuros. Alcanzó el **91% pass@1** en HumanEval (superando el 80% de GPT-4) y una mejora del 22% sobre líneas base en AlfWorld.

**Step-Back Prompting** (Zheng et al., 2023, ICLR 2024) implementa abstracción prerrazonamiento: primero el modelo deriva principios de alto nivel, luego los usa para guiar la resolución. En PaLM-2L, logró +7% en Física MMLU, +11% en Química, y **+27% en TimeQA**.

**SELF-DISCOVER** (Zhou et al., 2024, ICML 2024) permite que los LLMs autodescubran estructuras de razonamiento intrínsecas a cada tarea, seleccionando y componiendo módulos atómicos. Mejoró GPT-4 hasta un **32% sobre CoT** en BigBench-Hard con 10-40× menos cómputo de inferencia.

Otras técnicas notables incluyen: **EmotionPrompt** (Li et al., 2023, AAAI 2024), que añade estímulos emocionales logrando mejoras promedio del 8%; **Rephrase and Respond (RaR)** (Deng et al., 2023), donde el modelo reformula la pregunta antes de responder; **Thread-of-Thought (ThoT)** (Zhou et al., 2023), para contextos caóticos con mejoras del 47,2%; **Program-of-Thought (PoT)** (Chen et al., 2022), que delega cálculos a un intérprete Python logrando ~12% de mejora promedio sobre CoT en 8 datasets; **Skeleton-of-Thought (SoT)** (Ning et al., 2023, ICLR 2024), que reduce latencia mediante generación paralela; y **Contrastive CoT** (Chia et al., 2023), que incluye razonamientos válidos e inválidos como demostración.

### 2.11 Constitutional AI y alineación

**Constitutional AI (CAI)** (Bai et al., 2022, Anthropic) entrena modelos harmoniosos mediante ~10 principios constitucionales escritos por humanos, reemplazando miles de etiquetas de preferencia humana. El proceso combina aprendizaje supervisado (autocrítica y revisión guiada por principios) con RL desde retroalimentación de IA (RLAIF). Los modelos CAI son significativamente menos dañinos que los modelos base, el razonamiento CoT mejora la capacidad de la IA para identificar daños, y el enfoque reduce el compromiso entre utilidad y seguridad inherente al RLHF estándar.

---

## 3. Anatomía de un prompt: elementos, parámetros e interacciones

### Los componentes estructurales y su impacto medible

Schulhoff et al. (2024) establecieron un vocabulario formal que incluye: **directiva** (instrucción nuclear), **formato de salida** (especificaciones estructurales como CSV, JSON, markdown), **instrucciones de estilo**, **rol/persona**, **información adicional/contexto** y **ejemplos/demostraciones**. La guía de OpenAI para GPT-4.1 (2025) recomienda organizar estos componentes en una jerarquía clara: encabezados markdown (H1-H4) para secciones principales, backticks para código, y listas numeradas para pasos secuenciales.

Los **delimitadores** (```, ---, XML tags) tienen un impacto medible en el rendimiento. Sclar et al. (2024, ICLR) demostraron que cambios puramente de formato —semánticamente equivalentes— causan diferencias de hasta **76 puntos de precisión** en LLaMA-2-13B y un promedio de ~10 puntos en más de 50 tareas. Esta sensibilidad **no se elimina** aumentando el tamaño del modelo, añadiendo más ejemplos few-shot ni realizando ajuste por instrucciones. Los autores propusieron **FormatSpread**, un algoritmo para estimar la dispersión del rendimiento entre formatos plausibles.

El **orden de los ejemplos** es igualmente crítico. Lu et al. (2022, ACL) demostraron que la permutación de solo 4 ejemplos puede hacer oscilar la precisión entre el **nivel de azar y el estado del arte**, un efecto presente en todos los tamaños de modelo evaluados y que no se transfiere entre familias de modelos. Zhao et al. (2021, ICML) identificaron tres sesgos sistemáticos: **sesgo de etiqueta mayoritaria** (el modelo predice etiquetas frecuentes en los ejemplos), **sesgo de recencia** (predice etiquetas cercanas al final), y **sesgo de token común** (favorece tokens frecuentes del preentrenamiento). Su técnica de **calibración contextual** mejoró la precisión hasta **30 puntos absolutos**.

### Parámetros de generación y su interacción con las estrategias de prompting

La **temperatura** controla la aleatoriedad de la distribución softmax. Los rangos recomendados son: **0,0-0,4** para tareas factuales y técnicas, **0,5-0,7** para conversacionales, **0,7-1,0+** para creación. DeepSeek-R1 requiere específicamente temperatura 0,5-0,7 (óptimo 0,6) para prevenir repeticiones infinitas.

**Top-p (Nucleus Sampling)**, introducido por Holtzman et al. (2019/2020, ICLR 2020), muestrea del núcleo dinámico de la distribución que contiene la mayor masa de probabilidad. El estudio demostró que la decodificación por maximización (beam search) es inapropiada para generación abierta, produciendo texto plano y repetitivo.

La interacción entre parámetros y técnicas de prompting es fundamental: **Self-Consistency requiere temperatura alta** (≥0,7) para generar caminos de razonamiento diversos, mientras que las tareas de salida estructurada se benefician de temperatura baja. La recomendación general es ajustar temperatura **o** top-p, pero no ambos simultáneamente.

### El fenómeno "Lost in the Middle" y los efectos de longitud

Liu et al. (2023/2024, TACL 2024, 2.576+ citas) descubrieron una **curva de rendimiento en forma de U**: la precisión es máxima cuando la información relevante aparece al inicio o al final del contexto, pero **degrada significativamente** cuando está en la zona intermedia. Este efecto persiste incluso en modelos explícitamente diseñados para contextos largos (Claude-1.3 100K, LongChat). El hallazgo tiene implicaciones directas para RAG y tareas documentales: la posición de la información recuperada en el prompt determina significativamente el rendimiento.

---

## 4. Evidencia cuantitativa: lo que revelan los benchmarks

### Comparaciones directas entre técnicas

Los benchmarks más utilizados en la investigación de prompting incluyen **GSM8K** (Cobbe et al., 2021; 8.500 problemas matemáticos escolares), **MMLU** (Hendrycks et al., 2020; 57 materias), **HumanEval** (Chen et al., 2021; 164 problemas de código), y **BIG-Bench Hard** (Suzgun et al., 2022; 23 tareas de razonamiento difíciles). Cabe notar que para 2025, GSM8K, MMLU y HumanEval se consideran **saturados** para modelos frontera; el campo ha migrado hacia GPQA Diamond, AIME, Humanity's Last Exam, ARC-AGI-2 y FrontierMath.

Las comparaciones cuantitativas entre técnicas revelan patrones consistentes. En GSM8K, la progresión típica con PaLM 540B es: estándar (17,9%) → CoT (58,1%) → CoT + Self-Consistency (**74,4%**). En BIG-Bench Hard, sin CoT los mejores modelos superaban al evaluador humano promedio en solo el 65% de las tareas; **con CoT, Codex superó al humano en 17 de 23 tareas**. Los datos de Tree of Thoughts en el Juego del 24 ilustran que para tareas que requieren exploración deliberada, las técnicas lineales (CoT, CoT-SC) son insuficientes: 4-9% frente al **74%** de ToT.

### Sensibilidad y robustez de los prompts

La evidencia sobre sensibilidad es alarmante. Sclar et al. (2024) documentaron que cambios preservadores de significado —espaciado, puntuación, elección de delimitadores— causan variaciones de hasta 76 puntos en la precisión. Zhao et al. (2021) mostraron que el formato, la selección de ejemplos y su ordenamiento causan cada uno variaciones de hasta 30 puntos absolutos. Turpin et al. (2023, NeurIPS) demostraron que las explicaciones de CoT pueden estar fuertemente influenciadas por características sesgantes del prompt (e.g., reordenar opciones de respuesta), y que los modelos sistemáticamente **omiten mencionar** estas influencias en sus explicaciones, lo cual pone en cuestión la transparencia del razonamiento generado.

Un hallazgo contraintuitivo pero replicado es que los **prompts genéricos "mejorados" pueden degradar el rendimiento** en tareas específicas: añadir reglas genéricas a prompts de usuario redujo la tasa de extracción del 100% al 90% y el cumplimiento RAG del 93,3% al 80% en Llama 3 8B (arXiv:2601.22025).

### El estado del arte en febrero de 2026

Los modelos de razonamiento han transformado radicalmente los resultados de referencia. La progresión en **AIME 2024** ilustra la velocidad del avance: GPT-4o alcanzó el **12%** (1,8/15), o1-preview el 44,6%, o1 el 74,4%, o3 el 96,7%, y los modelos frontera de 2026 (GPT-5.2, Gemini 3 Pro) alcanzan el **100%**. En GPQA Diamond (preguntas de nivel doctoral), los mejores modelos actuales superan el **92%**. En SWE-bench Verified (ingeniería de software autónoma), Claude Sonnet 4.5 lidera con el **82%**. El benchmark más desafiante, Humanity's Last Exam, muestra que incluso los mejores modelos (Gemini 3 Pro: 45,8%) están lejos de la saturación. El **Densing Law** (Xiao et al., 2025, Nature Machine Intelligence) establece que la densidad de capacidad se duplica cada ~3,5 meses: el tamaño del modelo necesario para un rendimiento equivalente se reduce a la mitad en ese período.

---

## 5. Cómo responden los diferentes modelos a las técnicas de prompting

### Modelos de razonamiento nativo y el declive del CoT explícito

El hallazgo más significativo de 2024-2025 es que **el CoT explícito es en gran medida redundante para modelos con razonamiento nativo**. El estudio más riguroso al respecto (Meincke, Mollick et al., Wharton GAIL, 2025) evaluó GPQA Diamond con 25 ensayos por condición y encontró que para modelos de razonamiento (o3-mini, o4-mini), CoT proporcionó mejoras no significativas de solo **+2,9% a +3,1%**, con un incremento del 20-80% en tiempo de procesamiento. Para Gemini Flash 2.5 (razonamiento), CoT **redujo** el rendimiento en -3,3%. En contraste, para modelos sin razonamiento nativo, CoT produjo mejoras significativas: Gemini Flash 2.0 (+13,5%), Claude Sonnet 3.5 (+11,7%).

La guía oficial de OpenAI para modelos de razonamiento es explícita: "Estos modelos funcionan mejor con prompts directos. Algunas técnicas de ingeniería de prompts, como instruir al modelo a 'pensar paso a paso', pueden no mejorar el rendimiento (y a veces perjudicarlo)." OpenAI calificó a GPT-4.5 como su "último modelo sin cadena de pensamiento", señalando la convergencia hacia modelos donde el razonamiento es intrínseco.

### Prácticas óptimas por familia de modelos

**GPT-4o/GPT-4.1 (OpenAI)**: Entrenados para seguir instrucciones "más literalmente" que sus predecesores. Requieren prompts explícitos y específicos. GPT-4.1 responde bien a markdown y delimitadores; admite mensajes de sistema/desarrollador para comportamiento global. Las instrucciones colocadas en el parámetro `instructions` de la API tienen prioridad.

**o1/o3/o4-mini (OpenAI)**: Prompts directos y sin ornamento. Los mensajes de *developer* reemplazan a los de system. El esfuerzo de razonamiento se controla via `reasoning.effort` (low/medium/high). El markdown está deshabilitado por defecto en la API. En tareas con ≥5 pasos de razonamiento, o1-mini superó a GPT-4o en un 16,67%; pero para tareas con <3 pasos, **o1-mini fue inferior en el 24% de los casos** por "razonamiento excesivo."

**Claude 3.5/4.x (Anthropic)**: Claude fue entrenado con etiquetas XML en sus datos de entrenamiento, por lo que el uso de `<example>`, `<document>`, `<thinking>` mejora significativamente la calidad. El **prefilling** (prellenar el inicio de la respuesta) permite dirigir el formato de salida. El *extended thinking* (desde Claude 3.7 Sonnet) mejora el rendimiento "logarítmicamente con el número de tokens de pensamiento." Para modelos con extended thinking, las **instrucciones de alto nivel funcionan mejor que la guía prescriptiva paso a paso**. Antropic desaconseja pasar el pensamiento extendido de vuelta al modelo como entrada, ya que puede degradar los resultados. Claude Opus 4.5 es "particularmente sensible a la palabra 'think'" cuando extended thinking está desactivado — se recomienda sustituirla por "consider", "believe" o "evaluate."

**Gemini 1.5/2.0/2.5/3 (Google)**: Modelos nativamente multimodales con ventanas de contexto masivas (hasta **1.048.576 tokens**). La recomendación clave para contextos largos es **colocar las instrucciones al final**, después de todo el material contextual, usando frases de anclaje como "Basándose en la información anterior...". La temperatura recomendada es 0,4 como punto de partida. Gemini 3 (noviembre 2025) es tan sensible a las señales del prompt que los prompts diseñados para versiones anteriores pueden resultar "excesivos" — se recomienda simplificar.

**DeepSeek-R1**: Entrenado mediante RL puro sobre DeepSeek-V3-Base, desarrolló comportamientos de razonamiento sofisticados de forma autónoma. Las recomendaciones oficiales incluyen: temperatura 0,5-0,7 (0,6 óptimo), **no usar prompt de sistema** (todas las instrucciones en el prompt de usuario), y forzar el modo de pensamiento iniciando respuestas con `<think>\n`. DeepSeek-R1 alcanzó el **77,9% en AIME 2024** (comparable a o1), pero con un costo de entrenamiento significativamente menor.

**LLaMA 3/3.1/3.2 (Meta)**: Usa tokens especiales para el formato de chat (`<|begin_of_text|><|start_header_id|>`). Sigue prompts de sistema con alta fidelidad. Su principal limitación es la ventana de contexto más reducida (8K base vs. 32K de Mistral). LLaMA 3.2 incluye modelos multimodales (11B/90B visión). Los modelos de código abierto generalmente requieren **formato de prompt más cuidadoso** que los modelos de API cerrada, pero los distilados de DeepSeek-R1 basados en Qwen 2.5 (14B, 32B) muestran rendimiento de razonamiento excepcional.

### Transferibilidad entre modelos: un problema abierto

La investigación (arXiv:2411.10541) demostró **baja compatibilidad** entre familias de modelos: el IoU de templates de prompt de alto rendimiento entre series diferentes es frecuentemente inferior a 0,2. Sin embargo, modelos dentro de la misma subserie muestran IoU >0,7. GPT-3.5-turbo prefiere formato JSON; GPT-4 favorece markdown. Los prompts few-shot son consistentemente más robustos que los zero-shot ante variaciones adversarias (Zhu et al., 2024, PromptRobust).

---

## 6. Seguridad, optimización automática y el horizonte de los agentes

### Inyección de prompts: la vulnerabilidad número uno

La inyección de prompts fue clasificada como la **amenaza #1** en el OWASP Top 10 para Aplicaciones LLM 2025. Se distinguen tres categorías principales: la **inyección directa** (el usuario manipula el modelo mediante instrucciones adversarias como "ignora las instrucciones anteriores"), la **inyección indirecta** (formalizada por Greshake et al., 2023, AISec@CCS; instrucciones maliciosas embebidas en fuentes externas procesadas por el LLM), y el **jailbreaking** (técnicas para evadir la alineación de seguridad, incluyendo DAN prompts, codificación base64, homoglifos Unicode y escalación multi-turno).

Los incidentes reales documentados incluyen: exfiltración de datos de Slack AI mediante envenenamiento RAG (agosto 2024), ejecución remota de código en GitHub Copilot (CVE-2025-53773, CVSS 9.6) mediante inyección en imágenes, y manipulación de revisiones académicas mediante inyección en artículos científicos. La **inyección multimodal** ha emergido con GPT-4V y Claude 3, donde texto oculto en imágenes constituye un vector de ataque novedoso. El análisis fundamental revela que la inyección de prompts es una **limitación arquitectónica inherente**: los LLMs no distinguen entre "instrucciones" y "datos" porque todo se procesa como tokens de texto indiferenciados.

Las defensas incluyen filtrado de entrada/salida, defensa sándwich, jerarquía de instrucciones (OpenAI), Spotlighting (Microsoft), SmoothLLM (perturbación aleatoria del input), y alineación deliberativa (modelos o1). Sin embargo, ninguna defensa individual es suficiente; se requiere una estrategia de **defensa en profundidad**.

### La automatización del diseño de prompts

El campo ha evolucionado desde la optimización gradientista (AutoPrompt, Shin et al., 2020; Prefix Tuning, Li y Liang, 2021) hacia la **optimización de caja negra** liderada por LLMs. **DSPy** (Khattab et al., 2024, ICLR) representa el cambio más significativo: trata la ingeniería de prompts como programación, usando firmas declarativas y módulos composicionales en Python. Su optimizador MIPROv2 automatiza la selección de demostraciones few-shot y la optimización de instrucciones. Un estudio reciente (arXiv:2507.03620, 2025) demostró que DSPy mejoró la precisión de evaluación de prompts del **46,2% al 64,0%**.

**PromptBreeder** (Fernando et al., 2023, DeepMind) introdujo la optimización evolutiva de prompts mediante algoritmos genéticos, evolucionando tanto los prompts de tarea como los prompts de mutación (meta-optimización). **EvoPrompt** (Guo et al., 2023) implementó evolución diferencial via prompts de LLM, superando consistentemente el diseño manual. La tendencia más reciente, **ReflectivePrompt** (Zhuravlev et al., 2025), combina módulos reflexivos con búsqueda evolutiva, logrando ganancias del 33% en METEOR sobre GSM8K.

### Agentes LLM y uso de herramientas

La arquitectura de agentes ha madurado desde los prototipos de 2023 (AutoGPT, BabyAGI) hacia frameworks robustos. **LangChain/LangGraph** proporciona orquestación con gestión explícita de estado; **CrewAI** implementa sistemas multiagente basados en roles con más de 20.000 estrellas en GitHub; **Microsoft AutoGen** ofrece conversaciones multiagente con humano en el bucle. La llamada a funciones (*function calling*), estandarizada por OpenAI en junio de 2023, permite a los modelos generar llamadas estructuradas a herramientas externas.

Un desafío documentado es la **interferencia de tareas**: requerir salida JSON redujo la precisión en GSM8K en **27,3 puntos** (Tam et al., 2024), y la gestión simultánea de comprensión de consulta, selección de herramienta y restricciones de formato puede degradar la precisión en más del 20% (Gupta et al., 2024). La investigación reciente propone separar la selección de herramientas en un modelo dedicado para mitigar esta interferencia.

### Prompting multimodal: visión, audio y video

El **Set-of-Mark (SoM) Prompting** (Yang et al., 2023, Microsoft) constituye un avance significativo: usa modelos de segmentación para superponer marcas alfanuméricas sobre regiones de imagen, permitiendo a GPT-4V anclar su razonamiento en regiones visuales específicas. En modo zero-shot, GPT-4V con SoM superó a modelos ajustados finamente de última generación en RefCOCOg. Los modelos Gemini procesan texto, imágenes, audio y video como "entradas de primera clase" equivalentes. Gemini 2.0 Flash añadió salida multimodal nativa (imágenes mezcladas con texto). En el dominio de audio, prompts como AV-STFP (BMVC 2025) introducen fusión espaciotemporal audiovisual ajustando solo el **0,6%** de los parámetros del modelo.

---

## 7. ¿Tiene futuro la ingeniería de prompts?

El debate sobre la obsolescencia de la ingeniería de prompts se ha intensificado. Los argumentos a favor del declive incluyen la demostración de que los LLMs pueden optimizar prompts mejor que los humanos (Battle y Lal, IEEE Spectrum), la caída de las búsquedas de empleo para "prompt engineer" tras un pico en abril de 2023, y la clasificación de Microsoft (encuesta a 31.000 trabajadores, 2025) del rol como penúltimo en prioridad de contratación. Los modelos de razonamiento (o1, o3, R1) internalizan el CoT, haciendo redundante la ingeniería manual de cadenas de pensamiento.

Sin embargo, los argumentos a favor de la relevancia continuada son igualmente sólidos. Sander Schulhoff (Learn Prompting, coautor del Prompt Report con OpenAI, Microsoft, Google, Princeton y Stanford) sostiene que "la ingeniería de prompts está más viva que nunca y es más importante que nunca", distinguiendo entre prompting "conversacional" (chatear con ChatGPT, que se simplifica) y prompting "orientado a producto" (construir sistemas de IA, que crece en importancia). La disciplina no ha muerto; ha madurado y se ha especializado en gobernanza de prompts, seguridad, orquestación de agentes y diseño de sistemas de contexto.

**La transición conceptual más significativa es el paso del "prompt engineering" al "context engineering"**: ya no se trata de encontrar las palabras perfectas, sino de diseñar sistemas que proporcionen la información correcta en el momento adecuado, con las herramientas apropiadas disponibles. Como señala Anthropic (2025) en su guía de ingeniería de contexto efectiva para agentes de IA: el contexto es un recurso finito con rendimientos marginales decrecientes que puede sufrir "degradación de contexto" (*context rot*) cuando se vuelve excesivo o mal estructurado.

---

## Conclusiones y perspectivas

Este análisis revela cinco insights fundamentales que trascienden la mera catalogación de técnicas. **Primero**, la ingeniería de prompts no es un arte sino una ciencia empírica: la evidencia demuestra que las diferencias entre técnicas son cuantificables, replicables y, en muchos casos, sorprendentemente grandes (40+ puntos en GSM8K entre prompting estándar y CoT). **Segundo**, la sensibilidad extrema de los LLMs al formato del prompt (hasta 76 puntos de variación por cambios cosméticos) impone la necesidad de evaluación sistemática; reportar resultados con un único formato de prompt es científicamente insuficiente.

**Tercero**, la emergencia de modelos de razonamiento nativo representa un cambio cualitativo, no meramente cuantitativo: la internalización del CoT transforma la relación entre el usuario y el modelo, desplazando la complejidad del prompt hacia la configuración del sistema (esfuerzo de razonamiento, presupuesto de tokens de pensamiento, integración de herramientas). **Cuarto**, la convergencia entre prompting y programación —catalizada por frameworks como DSPy, LMQL y la optimización evolutiva de prompts— indica que el futuro pertenece a sistemas declarativos y optimizables, no a cadenas de texto artesanales.

**Quinto**, y quizás más importante, la baja transferibilidad de prompts entre modelos (IoU < 0,2) implica que no existen "prompts universales óptimos". La ingeniería de prompts efectiva requiere comprensión profunda de las características específicas de cada familia de modelos, evaluación continua contra benchmarks relevantes, y la humildad epistemológica de reconocer que incluso las técnicas más exitosas tienen dominios de aplicabilidad limitados. El campo avanza inexorablemente desde la ingeniería de prompts individuales hacia la ingeniería de contextos completos — sistemas dinámicos que integran recuperación, razonamiento, herramientas, memoria y verificación en arquitecturas orquestadas que harán del prompt, tal como lo conocemos hoy, un componente más dentro de un ecosistema más amplio de interacción humano-IA.