# Guion de Locuciones — AEPap 2026
## "La IA como Asistente del Pediatra de AP"
### Ernesto Barrera Linares

---

> **Notas para el orador:**
> - Velocidad recomendada: ~140 palabras/minuto (español, tono didáctico).
> - Cada locución es autónoma: puede funcionar sin las diapositivas anterior o posterior.
> - Estructura interna de cada locución: **gancho → contenido → cierre-puente**. Facilita la memorización y la modularidad.
> - Principio de carga cognitiva: un mensaje central por diapositiva, máximo tres ideas de apoyo.
> - Archivos de audio: `aepap_1.webm` → `aepap_73.webm` (73 archivos).

---

## BLOQUE 0 · PORTADA Y ENCUADRE

---

### SLIDE 1 · Portada

Bienvenidos al seminario "La Inteligencia Artificial como Asistente del Pediatra de Atención Primaria".

Me llamo Ernesto Barrera, soy médico de familia en la Comunidad de Madrid, y llevo más de quince años trabajando en la intersección entre tecnología, formación y práctica clínica.

Durante las próximas dos horas vamos a explorar juntos tres cuestiones que considero esenciales. Primera: dónde puede ayudarnos la IA hoy, con evidencias reales. Segunda: dónde puede hacernos daño si la usamos mal. Y tercera, y quizá la más práctica: cómo interactuar con ella para obtener resultados útiles y seguros en nuestra consulta.

Será un seminario con elementos prácticos. Vais a ver demos en vivo, vais a practicar vosotros mismos, y os vais a llevar herramientas que podéis usar el lunes en vuestra consulta.

Empecemos.

---

### SLIDE 2 · Conflicto de intereses

Antes de entrar en materia, la declaración obligada: no tengo conflictos de interés relacionados con este contenido. Las herramientas que mencionaré son de uso personal. No tengo vinculación comercial con ningún proveedor de inteligencia artificial.

Dicho esto, sí tengo un sesgo que quiero hacer explícito: creo que estas herramientas tienen un potencial enorme para mejorar nuestra práctica, pero solo si las usamos con el mismo rigor con el que evaluamos cualquier otra intervención clínica.

---

### SLIDE 3 · Objetivos del Seminario

Al finalizar estas dos horas, seréis capaces de hacer tres cosas concretas.

Uno: identificar escenarios clínicos donde la IA puede ser útil en vuestra consulta de pediatría. No todos los escenarios son iguales; veremos dónde el semáforo está en verde y dónde está en rojo.

Dos: reconocer las limitaciones y los riesgos más importantes. Porque la IA puede generar información falsa con una convicción que impresiona. Aprenderéis a detectar esas trampas.

Y tres: aplicar un método básico de interacción, lo que llamamos "prompt", para obtener respuestas clínicas útiles. Distinguiréis una instrucción eficaz de una que no lo es.

Tres objetivos, dos horas. Vamos a ello.

---

### SLIDE 4 · Hoja de Ruta: 120 minutos

Esta es nuestra hoja de ruta. Cinco bloques, ciento veinte minutos.

Empezamos con un bloque de ruptura, quince minutos, para situar el impacto de lo que está ocurriendo. Después, cuarenta y cinco minutos de fundamentos: qué es la IA, qué dice la evidencia, y qué aplicaciones concretas existen para pediatría. A continuación, cuarenta minutos de demos en vivo: veréis las herramientas funcionando en tiempo real. Habrá una pausa para café. Después, veinticinco minutos de práctica guiada donde vosotros seréis los protagonistas. Y cerraremos con veinte minutos de mensajes clave y evaluación.

Podéis hacer clic en cualquier bloque de la pantalla para saltar directamente si necesitáis volver a algún punto durante la sesión.

Ahora sí, entramos en materia.

---

## BLOQUE 1 · RUPTURA (15 min)

---

### SLIDE 5 · Portada Bloque 1

Bloque uno: Ruptura.

Vamos a empezar rompiendo el hielo. Y también, si me lo permitís, rompiendo alguna idea preconcebida.

---

### SLIDE 6 · Encuesta Inicial

Primera pregunta, y quiero que seáis sinceros.

¿Cuántos de vosotros habéis usado alguna herramienta de inteligencia artificial esta semana para algo relacionado con vuestra práctica clínica?

No solo ChatGPT. Cualquier cosa: buscar información, redactar un informe, preparar una sesión, traducir un artículo...

Levantad la mano si es "sí, regularmente". ¿Alguna vez? ¿Nunca?

Perfecto. Guardad vuestra respuesta en la cabeza. Al final del seminario volveremos a esta pregunta y veremos si algo ha cambiado.

---

### SLIDE 7 · Tweet de lanzamiento de ChatGPT

El treinta de noviembre de dos mil veintidós, OpenAI publicó un tuit. Decía, simplemente: "Introducing ChatGPT."

Nada más. Un tuit, un enlace.

En cinco días, un millón de usuarios. En dos meses, cien millones. Ningún producto tecnológico en la historia había crecido así.

Ese tuit cambió las reglas del juego. No porque la tecnología fuese nueva, los modelos de lenguaje llevaban años desarrollándose, sino porque por primera vez cualquier persona podía hablar con una inteligencia artificial. Y eso incluye a nuestros pacientes, a sus familias... y a nosotros.

---

### SLIDE 8 · Bibliometría PubMed

Mirad este gráfico. Son las publicaciones en PubMed sobre inteligencia artificial y modelos de lenguaje.

En dos mil veintitrés, era una de cada doscientas quince publicaciones. Hoy, una de cada noventa. El crecimiento ha superado incluso al de los artículos sobre tratamiento de COVID.

Esto no es una moda pasajera. Es una transformación estructural de la literatura biomédica. Y como clínicos, necesitamos saber cómo navegar este tsunami de información.

La buena noticia: no tenéis que leerlo todo. Lo que sí necesitáis son herramientas y criterios para separar el grano de la paja. Y eso es exactamente lo que vamos a hacer hoy.

---

### SLIDE 9 · Dos historias reales

Voy a contaros dos historias. Las dos son reales.

Historia uno, en verde. Un pediatra necesita dar información a unos padres sobre gastroenteritis aguda. Usa un modelo de IA para generar un borrador. Lo revisa, lo adapta al caso concreto, y lo entrega. Quince minutos ahorrados. Bajo riesgo, alto impacto.

Historia dos, en rojo. Un modelo de IA sugiere una dosis de medicación. El clínico no la verifica. La referencia bibliográfica que cita el modelo no existe. Es inventada. Una alucinación.

La diferencia entre estas dos historias no es la herramienta. Es exactamente la misma herramienta. La diferencia está en cómo, cuándo y para qué la usamos. Y sobre todo, en si verificamos antes de actuar.

Este contraste va a ser el hilo conductor de todo el seminario. Vamos a los fundamentos.

---

## BLOQUE 2A · FUNDAMENTOS TEÓRICOS (10 min)

---

### SLIDE 10 · Portada Bloque 2A

Bloque dos A: Fundamentos.

Antes de hablar de lo que la IA puede o no puede hacer, necesitamos hablar el mismo idioma. Así que empezamos con un glosario rápido.

---

### SLIDE 11 · Glosario IA

Seis conceptos que vamos a usar constantemente.

LLM, o modelo de lenguaje grande: es el motor que hay detrás de ChatGPT, Claude o Gemini. Predice la siguiente palabra basándose en patrones estadísticos. Importante: predice, no comprende.

Prompt: la instrucción que le das al modelo. La calidad de lo que obtienes depende directamente de la calidad de lo que preguntas.

IA generativa: genera contenido nuevo. No busca en una base de datos; crea texto, imágenes o código de la nada.

Alucinación: cuando la IA inventa información falsa con total convicción. Es el riesgo crítico que veremos en detalle.

RAG, o generación aumentada por recuperación: la IA se conecta a fuentes externas y busca antes de responder. Herramientas como Perplexity u Open Evidence funcionan así. Es mucho más seguro.

Y finalmente, IA agéntica: la IA que no solo responde, sino que planifica y ejecuta tareas autónomamente. Es el siguiente nivel, y ya empieza a verse en medicina.

Con este vocabulario compartido, pasemos a ver cómo encaja la IA en nuestro flujo de trabajo clínico.

---

### SLIDE 12 · Flujo Clínico con IA

La IA puede integrarse en las cinco etapas del flujo clínico: admisión, diagnóstico, tratamiento, documentación y seguimiento.

Una revisión sistemática publicada en dos mil veinticinco por Li y colaboradores en Applied Clinical Informatics analizó hasta qué punto GPT-4 podía asistir en tareas clínicas. El resultado: es aplicable al setenta y uno por ciento de las subtareas.

Pero, y esto es clave, "aplicable" no significa "autónomo." Significa que puede aportar valor si un clínico supervisa. Veremos exactamente dónde sí y dónde no a lo largo de la sesión.

---

### SLIDE 13 · ¿Qué es un LLM?

Esto es lo que necesitáis entender de verdad sobre cómo funciona un modelo de lenguaje.

Un LLM es un sistema que predice la siguiente palabra basándose en patrones estadísticos de billones de textos. Genera texto coherente: sí. Comprende lo que dice: no. Razona lógicamente: no.

¿Por qué es importante? Porque de aquí se deriva el riesgo más importante: puede generar información completamente falsa con una confianza absoluta. Eso es lo que llamamos alucinaciones. Y lo veremos en detalle en el bloque de evidencia, que empieza ahora.

---

## EVIDENCIA CIENTÍFICA

---

### SLIDE 14 · Portada Evidencia

Dejemos las opiniones a un lado. Vamos a ver qué dice la literatura reciente. Porque en este campo, lo que era cierto hace seis meses puede haber cambiado.

La síntesis que vais a ver se basa en una revisión de más de quinientas referencias publicadas entre dos mil veinticinco y dos mil veintiséis.

---

### SLIDE 15 · Human-in-the-Loop

El modelo Human-in-the-Loop define cómo debe funcionar la colaboración. La IA propone, redacta, sintetiza. El pediatra verifica, decide, empatiza.

En el único ensayo clínico aleatorizado publicado hasta la fecha, Goh y colaboradores probaron esto con 1213 consultas reales. Los médicos con GPT-4 mejoraron un 6.5% en manejo clínico. Pero tardaron 2 minutos más por caso.

La IA aumenta el razonamiento clínico. No lo sustituye. Y tiene un coste en tiempo que hay que valorar.

---

### SLIDE 16 · Paradigma de Colaboración (Venn)

El paradigma de colaboración se resume así: por separado, médico e inteligencia artificial tienen capacidades complementarias.

El médico aporta juicio clínico, empatía y contexto. La IA aporta velocidad y procesamiento masivo, pero con una precisión global del 52.1% según el meta-análisis de Takita, equivalente a un médico no especialista.

En la intersección, Wang muestra una mejora de casi 5 puntos en manejo clínico. Juntos, mejor. Pero no de cualquier manera.

---

### SLIDE 17 · Paradoja H+IA

Atención a la paradoja del rendimiento. Wang y colaboradores, en su meta-análisis publicado en npj Digital Medicine, muestran que Humano más IA no siempre supera a la IA sola.

El riesgo relativo es de 1.59 pero no significativo. Los errores persisten entre el 26 y el 36 por ciento incluso con supervisión. Y el intervalo de predicción va de menos 31 a más 41 puntos, una incertidumbre enorme.

Pero hay una excepción importante: en el ensayo clínico de Goh, médicos con GPT-4 mejoraron el manejo clínico un 6.5 por ciento. La clave está en el diseño. No basta usar la IA, hay que integrarla con método.

Y hay un riesgo añadido: el deskilling, la pérdida de competencias. Si delegamos sistemáticamente, perdemos la habilidad de detectar cuándo el modelo se equivoca.

---

### SLIDE 18 · Pausa para reflexión

Antes de seguir con más datos, una reflexión importante. La paradoja del rendimiento que acabamos de ver invita a preguntarnos algo incómodo: ¿alguna vez hemos confiado demasiado en una herramienta sin verificar? No solo con IA: con calculadoras de dosis, con guías clínicas desactualizadas, con el "siempre se ha hecho así."

La respuesta honesta es que sí, nos pasa a todos. Y con la IA el riesgo es mayor porque la respuesta suena convincente. Esa autorreflexión es el mejor escudo.

Sigamos con la evidencia, que nos queda mucho por ver.

---



### SLIDE 20 · Evidencia Actual (rendimiento mixto)

La evidencia de 2025 confirma un rendimiento mixto. Un meta-análisis de 83 estudios de Takita y colaboradores muestra que la IA tiene una precisión diagnóstica global del 52.1%. Es comparable a un médico no especialista, pero significativamente inferior al experto: 15.8 puntos menos.

En tareas acotadas como cribado de artículos o extracción de datos, funciona bien. Pero en diagnóstico autónomo, la supervisión sigue siendo imprescindible.

La acción: tareas acotadas con confianza; en diagnóstico, solo como segunda opinión supervisada.

---

### SLIDE 21 · Alucinaciones

Las alucinaciones son el riesgo más crítico. Y se manifiestan en dos contextos distintos.

Primero, las bibliográficas: hasta el 91.4% de las citas de Bard eran fabricadas. GPT-3.5, el 39.6%. GPT-4, el 28.6%. Nunca hagáis búsquedas bibliográficas ciegas con estos modelos.

Segundo, en documentación clínica: un framework de Asgari y colaboradores con 50 médicos y casi 13 mil frases anotadas mostró que las alucinaciones se pueden reducir al 1.47%, por debajo del nivel humano. Pero las omisiones, lo que el modelo olvida incluir, alcanzan el 3.45% y son el riesgo mayor.

La regla de oro sigue siendo la misma: verificar siempre antes de usar. Nunca copiar y pegar sin comprobar el DOI o el PMID en la fuente primaria.

---

### SLIDE 22 · Brecha Exámenes vs Clínica

La brecha entre aprobar exámenes y saber curar es enorme. Los modelos de lenguaje obtienen entre 84 y 90 por ciento en exámenes teóricos tipo USMLE. Impresionante, ¿verdad?

Pero el meta-análisis de Takita con 83 estudios muestra que en clínica real, la precisión global es del 52.1%. Y el dato más preocupante: solo el 9.4 por ciento de los estudios publicados evalúan errores y seguridad.

Aprobar el examen no es saber curar. Lo sabemos con los residentes; con la IA aplica exactamente igual.

---

### SLIDE 23 · Riesgo: Dr. AI en emergencias

Esto me preocupa especialmente como clínico. Cuando los padres consultan a la IA sobre emergencias.

Un estudio publicado en The Lancet Digital Health encontró que el ochenta y nueve con cinco por ciento de las respuestas de modelos de IA sobre primeros auxilios y reanimación cardiopulmonar en niños contenían errores significativos o alucinaciones.

Pensadlo: una familia en pánico, un niño que se atraganta, y la primera reacción es preguntar a ChatGPT. La respuesta puede parecer impecable y estar completamente equivocada.

La acción para nosotros es doble: educar activamente a las familias sobre las limitaciones de la IA en emergencias, y seguir insistiendo en un mensaje que no cambia: ante una emergencia, llama al ciento doce.

---

### SLIDE 24 · Mapa del Rendimiento

168 estudios, casi treinta y seis mil preguntas clínicas analizadas en un meta-análisis en red publicado en JMIR: ¿qué modelo de IA es mejor para qué tarea?

La respuesta: ninguno gana en todo. ChatGPT-4o lidera en preguntas objetivas. ChatGPT-4 en preguntas abiertas. Gemini en triaje y clasificación.

Pero en diagnóstico top-1, donde hay que acertar a la primera, los humanos expertos siguen siendo superiores. Con un SUCRA de cero con noventa frente a cero con ochenta y uno de GPT-4.

El mensaje clave: no hay un modelo universal. La elección depende de la tarea clínica. Y para lo más crítico, el diagnóstico de primera línea, el experto humano sigue siendo insustituible.

---

### SLIDE 25 · RAG y sesgo

¿Y si usamos RAG para evaluar sesgo? ¿Mejora la cosa?

Los datos no son alentadores. Cuando se probó NotebookLM para evaluar riesgo de sesgo en estudios clínicos, la concordancia con revisores humanos fue muy baja: un coeficiente de correlación intraclase de cero con veintisiete y un acuerdo porcentual del catorce con ocho al veintinueve con seis por ciento.

Mensaje claro: la evaluación de riesgo de sesgo es una tarea que requiere juicio experto. No la deleguéis a la máquina, ni siquiera con RAG.

---

### SLIDE 26 · Precisión Diagnóstica

Zoom al diagnóstico pediátrico. En entornos rurales, la IA iguala prácticamente al pediatra: 87.3% frente a 91.3%, una diferencia no significativa.

Pero a nivel global, según el meta-análisis de Takita con 83 estudios, la IA es equivalente solo al médico no especialista. El especialista sigue siendo superior en 15.8 puntos.

En salud mental, la transición de GPT-3.5 a GPT-4 mejoró significativamente: F1 de 0.41 a 0.655. La progresión es real, pero aún no estamos en autonomía para diagnóstico.

---

### SLIDE 27 · Velocidad ≠ Fiabilidad ≠ Consenso

Tres lecciones del mismo campo, la escoliosis del adolescente, que ilustran por qué no debemos confundir velocidad con fiabilidad, ni fiabilidad con consistencia.

Velocidad: la IA clasificó radiografías cien veces más rápido, siete a cuarenta y ocho segundos frente a once o doce minutos. Impresionante. Pero cuando se repitió la prueba una semana después, todos los modelos fallaron en reproducir sus propios resultados.

Fiabilidad: en guías protocolizadas de otorrinolaringología, kappa igual a uno, cien por cien de adherencia. Perfecto. Pero el mismo tipo de modelo fabrica hasta el noventa y uno con cuatro por ciento de sus citas bibliográficas.

Consenso: los cirujanos expertos coinciden el noventa y dos por ciento de las veces, con kappa de cero con novecientos trece. Los modelos de lenguaje multimodales: entre uno con seis y diez con dos por ciento, prácticamente aleatorio.

La conclusión: rápido no es fiable. Fiable no es consistente. Tres dimensiones que no van juntas.

---

### SLIDE 29 · Sesgos Algorítmicos

Los sesgos algorítmicos son otro riesgo que debemos conocer.

Aparecen en tres niveles. Primero, en la entrada: los datos de entrenamiento pueden no representar a nuestra población pediátrica. Segundo, en el proceso: la selección automatizada amplifica patrones preexistentes. Y tercero, en la salida: las alucinaciones se presentan con alta confianza, sin señales de alerta.

La acción: validar siempre en poblaciones infrarrepresentadas, y recordar que lo que funciona en un contexto anglosajón puede no aplicarse directamente a nuestra práctica.

---

### SLIDE 30 · Semáforo de Seguridad

Os presento un semáforo de seguridad basado en la evidencia que hemos revisado.

Luz verde: automatizar con supervisión tareas como revisiones sistemáticas, extracción de datos tabulares y generación de resúmenes estructurados.

Luz amarilla: monitorizar estrechamente borradores de informes, síntesis de historiales y apoyo al diagnóstico diferencial. Siempre con un clínico validando.

Luz roja: nunca automatizar diagnóstico primario de imagen, planificación quirúrgica, ni dosificación sin verificación humana.

Guardad esta imagen. La vais a necesitar.

---



## BLOQUE 2B · MARCO LEGAL (10 min)

---

### SLIDE 32 · Portada Bloque 2B

Bloque dos B: Marco Legal.

Antes de poner en práctica lo que sabemos, necesitamos conocer las reglas del juego. Porque usar inteligencia artificial con datos de pacientes no es solo una cuestión técnica. Es una cuestión legal y ética que nos afecta directamente.

---

### SLIDE 33 · Marco Legal: reglas del juego

El marco legal que regula el uso de IA en consulta se apoya en tres pilares.

Primero, el Reglamento Europeo de Inteligencia Artificial, que clasifica las herramientas de IA por nivel de riesgo. Las herramientas diagnósticas certificadas se consideran de alto riesgo.

Segundo, el Reglamento General de Protección de Datos, el RGPD, que regula el tratamiento de datos personales con especial protección para datos de salud.

Y tercero, la Ley 41/2002 de Autonomía del Paciente, que establece las bases del consentimiento informado.

Es importante distinguir: ChatGPT, Claude o Gemini no son productos sanitarios certificados. Para ellos, la norma vinculante hoy es el RGPD. Y en datos de salud pediátrica, las exigencias son máximas.

---

### SLIDE 34 · Médico responsable

Hay un punto que debe quedar absolutamente claro: la responsabilidad clínica siempre es del médico.

Da igual que la IA haya generado el borrador, sugerido el diagnóstico o propuesto la dosis. La decisión final, la firma, la responsabilidad legal y ética, es del profesional que actúa.

Esto es lo que llamamos el principio del "médico en el bucle". La IA puede asistir, pero el acto médico sigue siendo humano. Usar IA es legal y puede llegar a ser exigible por competencia profesional. Pero la responsabilidad clínica nunca se delega a un algoritmo.

---

### SLIDE 35 · Semáforo de datos paciente

¿Qué datos puedes introducir en un modelo de IA? Depende del nivel de sensibilidad.

Nivel bajo, en verde: preguntas genéricas sobre guías o protocolos. Sin datos de paciente. Cualquier herramienta vale.

Nivel medio, en azul: consultas con datos anonimizados. Aquí necesitas activar el modo efímero o temporal, para que la herramienta no almacene ni entrene con tu consulta.

Nivel alto, en naranja: imágenes o analíticas. Solo herramientas institucionales integradas en la historia clínica electrónica. Y es obligatoria una Evaluación de Impacto en Protección de Datos.

Y nivel muy alto, en rojo: enfermedades raras. Aquí se produce una situación especial: el setenta y cinco por ciento de pacientes con enfermedades raras tienen alto riesgo de reidentificación. En prevalencias menores de uno entre cincuenta mil, el nombre de la enfermedad más el país puede bastar para identificar al paciente. Solo IA local o certificada, y reformular la consulta a nivel fisiopatológico, sin nombrar la enfermedad.

Recordad el protocolo de treinta segundos: sustituir nombres por "paciente", edad exacta por rango, fechas por "hace tres días", sin geografía, y nunca incluir número de historia clínica ni DNI.

---

### SLIDE 36 · Jurisdicciones y Checklist

No todas las IAs son iguales en protección de datos. Os presento un semáforo de jurisdicciones.

Verde: despliegue local con modelos open-source como Llama o Mistral vía Ollama. Cero transferencia de datos, máximo control.

Azul: proveedores europeos como Mistral Le Chat o Azure EU. Jurisdicción de la Unión Europea, sin transferencia a terceros países.

Amarillo: proveedores americanos como OpenAI, Anthropic o Google, con Data Privacy Framework. Este acuerdo de adecuación entre la UE y Estados Unidos es válido pero frágil, porque está recurrido ante el Tribunal de Justicia de la Unión Europea.

Y rojo: proveedores chinos como DeepSeek. Esencialmente incompatibles con el RGPD para datos de salud. Italia los prohibió de emergencia en enero de dos mil veinticinco y la OCU ha denunciado ante la Agencia Española de Protección de Datos.

El mensaje clave: usar IA es legal y puede ser exigible, pero la responsabilidad clínica siempre es tuya. Anonimiza, documenta, y mantén el juicio crítico.

---

## BLOQUE 2C · APLICACIONES PRÁCTICAS (15 min)

---

### SLIDE 37 · Portada Bloque 2C

Bloque dos C: Aplicaciones Prácticas.

Hemos visto los fundamentos, la evidencia y el marco legal. Ahora vamos a lo concreto: ¿cómo puedes usar la IA en tu consulta de forma segura y efectiva?

---

### SLIDE 38 · Oxígeno para la Consulta

Empiezo con la aplicación que tiene la evidencia más sólida: la reducción de carga documental.

Un meta-análisis de catorce estudios confirma que la IA reduce moderada a altamente la carga de documentación clínica, con una diferencia de medias estandarizada de menos cero con setenta y uno, manteniendo la calidad comparable a la documentación manual.

Traducido: menos tiempo rellenando formularios, más tiempo mirando al niño y hablando con la familia. La IA puede ser literalmente oxígeno para la consulta asfixiada por el papeleo.

---

### SLIDE 39 · Inteligencia Ambiental

La inteligencia ambiental va un paso más allá. Imagina una herramienta que escucha la conversación en consulta, filtra lo clínicamente relevante y genera una nota estructurada automáticamente.

Esto ya existe. El flujo es: escucha activa, filtrado inteligente de síntomas y signos, y generación de documentación en formato SOAP o similar.

Pero hay un requisito ético que es innegociable: el consentimiento explícito del paciente o la familia antes de activar cualquier sistema de grabación. Sin consentimiento, no hay inteligencia ambiental que valga.

---

### SLIDE 40 · Prompt Engineering como Habilidad Clínica

Llegamos a una idea que quiero que os llevéis grabada: el prompt engineering ya es una habilidad clínica.

Callens y colaboradores proponen un checklist de cuatro pasos para interactuar con un modelo de IA de forma efectiva. Primero, definir el rol y el contexto. Segundo, especificar el output deseado. Tercero, incluir restricciones y limitaciones. Y cuarto, definir el formato de respuesta.

¿Os suena? Es la base del método RECORD que os enseñaré en el bloque de demos. Saber preguntar a la IA es tan importante como saber preguntar a un paciente.

---

### SLIDE 41 · Técnicas de Prompting

Las cuatro técnicas de prompting con mayor impacto según la evidencia son las siguientes.

Chain-of-Thought, o cadena de pensamiento: pedir al modelo que "piense paso a paso" mejora el rendimiento del diecisiete al cincuenta y ocho por ciento en tareas de razonamiento.

Few-shot: dar dos o tres ejemplos antes de la consulta. El formato importa más que las etiquetas.

RAG, o generación aumentada por recuperación: conectar el modelo a fuentes verificadas para reducir alucinaciones, con reducciones del dieciocho al cuarenta por ciento.

Y Self-Consistency: generar varias respuestas y elegir la más frecuente, con una mejora de casi dieciocho puntos porcentuales.

Pero atención: un estudio de Sclar y colaboradores demostró que cambios triviales en el formato del prompt, como espaciado o puntuación, pueden causar variaciones de hasta setenta y seis puntos porcentuales en la precisión. El cómo preguntas importa enormemente.

---

### SLIDE 42 · Context Engineering

Dos mil veinticinco marca un cambio de paradigma. Los modelos de razonamiento como o1 o DeepSeek R1 internalizan el Chain-of-Thought. Así que pedirles "piensa paso a paso" es redundante o incluso perjudicial.

El nuevo enfoque se llama Context Engineering: ya no se trata de encontrar las palabras perfectas, sino de dar la información correcta en el momento adecuado. Herramientas más memoria más fuentes verificadas.

Para el pediatra de Atención Primaria, la clave es sencilla: con modelos clásicos, usad el método RECORD con cadena de pensamiento. Con modelos de razonamiento, sed directos y dad contexto rico. Y siempre, siempre: fuentes verificadas más verificación del output.

---

### SLIDE 43 · Mapa de Evidencia 2025-2026

¿Dónde se concentra la evidencia actual? Fundamentalmente, en evaluaciones de modelos generalistas. El noventa y tres con cincuenta y cinco por ciento de los estudios evalúan modelos como GPT-4, Claude o Gemini.

Solo el seis con cuarenta y cinco por ciento evalúa modelos médicos especializados. Y la métrica más usada es la precisión simple, en más del veintiuno por ciento de los estudios.

Esto nos dice dos cosas. Primera: la evidencia está dominada por herramientas que vosotros ya podéis usar. Segunda: queda mucho por hacer en evaluación de modelos específicos para nuestra especialidad.

---

### SLIDE 44 · Ecosistema IA 2026

El ecosistema de IA médica se diversifica en tres direcciones interesantes.

Por un lado, los modelos open-source como DeepSeek ya igualan en rendimiento a los modelos propietarios, y permiten despliegue local. Esto es fundamental para la privacidad de datos clínicos.

Por otro, los modelos médicos especializados, como MedFound con ciento setenta y seis mil millones de parámetros, superan a los generalistas en diagnóstico complejo en hasta ocho especialidades.

Y la tercera dirección es la IA agéntica: modelos que no solo responden preguntas, sino que planifican y ejecutan tareas autónomamente. Un agente puede recibir una instrucción como "busca los últimos metaanálisis sobre bronquiolitis, selecciona los tres más relevantes y genera un resumen para mi sesión clínica", y ejecutar todo el flujo sin intervención. Ya hay sistemas multi-agente, varios modelos coordinados, que muestran resultados prometedores en diagnóstico precoz.

Para vuestra práctica: modelos open-source cuando necesitéis privacidad; modelos especializados cuando busquéis precisión; y agentes cuando necesitéis automatizar flujos completos, siempre con supervisión del resultado final.

---

### SLIDE 45 · Documentación y Evidencia

La IA ambiental para documentación tiene el respaldo de un meta-análisis de veintitrés estudios que confirma una reducción significativa de la fatiga administrativa.

Mirad esta infografía: el antes y el después. La montaña de papeleo se reduce a un resumen estructurado que el clínico solo necesita revisar y validar. El modelo hace el trabajo pesado; el clínico aporta el juicio.

---

### SLIDE 46 · Diagnóstico Precoz en AP

Sistemas multi-agente, es decir, varios modelos de IA trabajando coordinados, ya muestran resultados prometedores en diagnóstico precoz en atención primaria. Sensibilidad de cero con noventa y cuatro y exactitud de cero con ochenta y seis en cohortes de validación.

La acción para nosotros: considerar estos sistemas como apoyo a la derivación temprana, no como sustituto del juicio clínico.

---

### SLIDE 47 · Pediatría: tres áreas con evidencia

En pediatría concretamente, hay tres áreas donde la evidencia cuantitativa es más sólida.

Neonatal: predicción de morbilidad con modelos especializados. Retina: detección de retinopatía del prematuro con F1 del ochenta y nueve por ciento. Y perioperatorio: predicción de hipoxemia con un área bajo la curva de cero con ochenta y cinco.

La acción: priorizar el uso de IA para cribado y predicción; el diagnóstico complejo sigue requiriendo supervisión.

---

### SLIDE 48 · Caries Escolar

Un ejemplo muy concreto para pediatría de primaria: detección de caries en escolares mediante fotografías intraorales analizadas por IA.

Sensibilidad entre ochenta y dos y noventa y seis por ciento. Especificidad entre setenta y siete y noventa y nueve por ciento. Útil como herramienta de cribado escolar para priorizar qué niños necesitan revisión odontológica urgente.

---

### SLIDE 49 · Riesgo Suicida

Un tema delicado pero crucial: la detección de riesgo suicida en adolescentes.

La IA alcanza un noventa y nueve por ciento de detección en mensajes individuales. Pero cuando se evalúa riesgo genuino, no solo la presencia de palabras clave, el rendimiento cae al ochenta y nueve por ciento. Se recupera al noventa y uno cuando se añade contexto conversacional.

El mensaje: el contexto importa. Un mensaje aislado no basta; el modelo necesita la conversación completa para reducir falsos positivos.

---

### SLIDE 50 · Educación Médica

En formación, los modelos de lenguaje rinden espectacularmente bien en exámenes de elección múltiple: hasta el noventa y cuatro con cinco por ciento de precisión.

Pero en casos clínicos reales la variabilidad es enorme según el modelo utilizado. La acción: evaluar el razonamiento con casos clínicos, no solo con preguntas tipo test. Esto aplica tanto a residentes como a la IA.

---

### SLIDE 51 · Prompting Determinista

Un hallazgo práctico muy relevante: el prompting determinista.

Con prompts estándar, preguntas abiertas, la adherencia a protocolos clínicos fue del treinta y dos por ciento. Noventa y seis de trescientos casos. Inaceptable.

Con prompts deterministas, instrucciones cerradas, paso a paso, tipo checklist, la adherencia subió al cien por cien. Trescientos de trescientos.

Esto confirma algo que veremos en la práctica: cómo preguntas a la IA determina la calidad de lo que obtienes. Los prompts estructurados salvan la consulta.

---

### SLIDE 52 · Matriz de Madurez Tecnológica

Esta matriz resume el estado del arte de la IA en pediatría por dominio clínico. Cada celda está coloreada según su nivel de evidencia y seguridad: verde, amarillo o rojo.

Guardadla como referencia. Os dice exactamente qué funciona hoy, qué es prometedor pero inmaduro, y qué debéis evitar.

---

### SLIDE 53 · RAG como Estándar de Oro

La generación aumentada por recuperación, RAG, se consolida como el estándar de oro para implementaciones seguras de IA en salud.

¿Por qué? Porque combina la potencia generativa de un modelo de lenguaje con datos reales y verificados. El modelo no inventa: busca primero en fuentes fiables y luego responde con citas.

Herramientas como Open Evidence o Perplexity Pro funcionan con esta arquitectura. Son las que os recomiendo para consultas clínicas point-of-care.

---

### SLIDE 54 · Whitelisting de Fuentes

Un estudio de Masanneck y colaboradores demuestra algo con implicaciones prácticas inmediatas.

Restringir las fuentes del modelo a fuentes profesionales mejora la precisión del sesenta al setenta y ocho por ciento. Dieciocho puntos porcentuales de mejora.

Y al revés: usar aunque sea una fuente no profesional reduce las odds de respuesta correcta a la mitad.

La acción es directa: configurad vuestros modelos para trabajar con guías AEPAP, protocolos de AEPED, Pediamécum y guías internacionales pediátricas. Limitad las fuentes y multiplicaréis la fiabilidad.

---

### SLIDE 55 · Conclusiones: Futuro Híbrido

Cuatro conclusiones de la evidencia que acabamos de revisar.

Primera: la IA aumenta al médico, no lo sustituye. Segunda: en documentación y burocracia, la reducción es real y significativa, pero en diagnóstico la supervisión es obligatoria. Tercera: los modelos especializados superan a los generalistas. Y cuarta: toda la evidencia apunta en la misma dirección: verificación antes de uso clínico.

El futuro no es la IA sola, ni el médico solo. El futuro es híbrido.

---

### SLIDE 56 · Semáforo AP

Para terminar este bloque, una hoja de ruta en formato semáforo que podéis llevar a vuestra consulta.

Verde: adoptad la IA para documentación, educación a familias y síntesis de evidencia. Amarillo: usadla con supervisión para apoyo diagnóstico diferencial, preparación de sesiones clínicas y codificación. Rojo: evitad el diagnóstico autónomo, la dosificación sin verificación y cualquier uso sin revisión humana posterior.

Esta imagen estará disponible en los materiales del seminario.

---

### SLIDE 57 · Cinco mensajes clave (Síntesis)

Cinco mensajes clave antes de pasar a las demos.

Uno: la evidencia sólida está en documentación y síntesis; semiautomatizad con revisión humana. Dos: en diagnóstico pediátrico real, usad la IA como segunda opinión, nunca como sustituto. Tres: los modelos open-source on-premise ya son competitivos y ofrecen privacidad. Cuatro: modelos médicos especializados rinden mejor, pero siguen siendo minoría. Y cinco: los prompts deterministas con checklists reducen errores en protocolos críticos.

Estos cinco puntos son la base. Ahora vamos a ver cómo se aplican en la práctica.

---

## BLOQUE 3 · DEMOS EN VIVO (40 min)

---

### SLIDE 58 · Portada Bloque 3

Bloque tres: Demos en vivo.

Hasta ahora hemos hablado de evidencia y de conceptos. Ahora viene la parte que más me gusta: ver las herramientas funcionando en tiempo real.

Vamos a navegar el ecosistema de IA disponible, y vais a ver exactamente cómo se usa cada herramienta.

---

### SLIDE 59 · Pirámide de Evidencia 5.0

Para navegar este ecosistema necesitamos un mapa. Os presento la Pirámide de Evidencia 5.0, adaptada del modelo clásico de Alper y Haynes.

En la cima están las herramientas point-of-care con RAG clínico: Open Evidence, Perplexity Pro, NotebookLM. Dan respuestas verificables con citas a fuentes de alta calidad. Son las más seguras.

En el nivel medio: herramientas de búsqueda y síntesis como Undermind, Scite.ai, Elicit o Consensus. Agentes de investigación que sintetizan literatura.

Y en la base: los modelos fundacionales como ChatGPT, Claude o Gemini. Razonan bien, pero su conocimiento está "congelado" y tienen riesgo de alucinación.

La regla es sencilla: para decisiones clínicas, subid lo más alto posible en la pirámide. Para tareas de redacción o formato, la base puede ser suficiente.

---

### SLIDE 60 · Herramientas por Nivel

Aquí tenéis el catálogo completo, organizado por tipo, uso principal y nivel de confianza.

Open Evidence y Perplexity Pro: RAG clínico, confianza alta. NotebookLM: RAG personal sobre tus propios documentos, confianza alta. Scite.ai: análisis de citas, confianza moderada. Y ChatGPT o Claude: modelos fundacionales, confianza alta para redacción y formato, pero baja para datos clínicos sin verificación externa.

Fijaos en el asterisco: la confianza de los modelos fundacionales cambia radicalmente según la tarea. Redactar un email a una familia: alto. Calcular una dosis: bajo.

---

### SLIDE 61 · Demo NotebookLM: Actualización Periódica

Vamos a ver un caso de uso real que podéis replicar mañana en vuestro centro de salud.

El flujo es este: empezamos con una búsqueda avanzada en PubMed que filtra revisiones sistemáticas y metaanálisis del último mes, centrada en las diez patologías más frecuentes de nuestra consulta pediátrica: TDAH, TEA, bronquiolitis, asma, infecciones respiratorias de vías altas, otitis, gastroenteritis, dermatitis atópica, obesidad y ansiedad.

Cargamos los abstracts en NotebookLM. Y a partir de ahí, la herramienta genera tres productos: un podcast tipo journal club de más de veinte minutos que puedes escuchar en el coche camino al trabajo, una presentación de diapositivas para tu sesión clínica, y un vídeo resumen.

Todo a partir de la misma fuente de evidencia verificable. La IA no inventa nada porque trabaja exclusivamente sobre los artículos que tú le has dado. Eso es RAG en acción.

Veámoslo en directo.

---

### SLIDE 62 · Método RECORD

Ahora vamos a ver el método RECORD, que es el framework que os propongo para escribir prompts efectivos.

RECORD es un acrónimo de seis letras.

R de Rol: dile al modelo quién es. "Actúa como pediatra de Atención Primaria."

E de Escenario: sitúa la acción. "En consulta de seguimiento."

C de Contexto: da los datos clínicos relevantes. "Lactante de tres meses con bronquiolitis."

O de Objetivo: di exactamente qué quieres obtener. "Genera una hoja informativa para padres."

R de Restricciones: marca los límites. "Sin términos médicos, sin causar alarma."

Y D de Diseño: define el formato. "Cinco secciones con signos de alarma destacados."

Cuanto más completo sea tu prompt, más útil será la respuesta. Vamos a construir uno en vivo.

---

### SLIDE 63 · GPTs y Gems: Personalización

Una de las funcionalidades más potentes de estos modelos es la personalización.

Podéis crear mini-asistentes preconfigurados, los llaman GPTs en ChatGPT, Gems en Gemini, sin saber programar. Le das las instrucciones una vez, y a partir de ahí el modelo las aplica automáticamente cada vez que lo usas.

Un ejemplo concreto: un GPT que reciba resultados analíticos anonimizados y genere una versión explicativa para padres, más pistas de interpretación clínica y sugerencias para ampliar estudio.

Otros usos: generador de informes, traductor de jerga médica, asistente de codificación CIE-10, preparador de sesiones clínicas.

La clave: una vez configurado, el asistente recuerda las instrucciones y aplica el mismo formato cada vez. Es como tener un residente digital que no se cansa y no se equivoca, siempre que le hayas dado bien las instrucciones.

---

### SLIDE 64 · Demo Constructor de Prompts

Aquí tenéis el constructor de prompts interactivo, una herramienta de código abierto que he desarrollado para este seminario.

Podéis interactuar directamente con ella. Seleccionad un escenario, rellenad los campos del método RECORD, y el constructor genera el prompt completo listo para copiar y pegar en cualquier modelo de IA.

Probadla. Está disponible en mi web y os la lleváis para usar en vuestra consulta.

---

## BLOQUE 4 · PRÁCTICA GUIADA (25 min)

---

### SLIDE 65 · Portada Bloque 4

Bloque cuatro: Práctica Guiada.

Ahora os toca a vosotros. Habéis visto la evidencia, habéis visto las herramientas, habéis visto el método. Es hora de ponerlo en práctica.

---

### SLIDE 66 · Generador de Prompts

Aquí tenéis tres plantillas listas para usar, basadas en escenarios reales de pediatría de primaria.

Información para padres: genera una hoja explicativa sobre cualquier patología. Sesión clínica: resume un artículo para presentar en cinco minutos. Email a familia: responde una consulta de forma empática y profesional.

Haced clic en cualquiera de ellas y obtendréis un prompt RECORD completo que podéis copiar, adaptar y usar inmediatamente. Escanead también el QR del kit de supervivencia para acceder a más plantillas.

---

### SLIDE 67 · Ejercicio en Grupos

Bien, ahora la práctica.

Formad parejas o tríos. Elegid uno de estos tres casos.

Caso uno: generar información para padres sobre varicela, con cuidados en casa y signos de alarma. Caso dos: resumir un artículo sobre bronquiolitis para una sesión clínica de cinco minutos. Caso tres: responder por email a una madre que pregunta sobre introducción de alimentación complementaria.

Usad el método RECORD. Tenéis quince minutos. Podéis usar la plantilla impresa o la herramienta online con el QR.

Al terminar, compartiremos algunos ejemplos y veremos qué funciona y qué se puede mejorar.

Adelante.

---

## BLOQUE 5 · CIERRE (20 min)

---

### SLIDE 68 · Portada Bloque 5

Bloque cinco: Cierre.

Llegamos al final. Vamos a recapitular lo esencial y asegurarnos de que os lleváis las herramientas y los conceptos bien consolidados.

---

### SLIDE 69 · Modelo Sándwich

Si tuviera que resumir todo el seminario en una sola imagen, sería esta: el Modelo Sándwich.

Tres capas.

Pan superior: el humano. Tú defines la estrategia, eliges la herramienta, formulas la pregunta correcta. Sin una buena pregunta, no hay buena respuesta.

Relleno: la IA. Procesa datos masivamente, genera borradores, sintetiza evidencia, busca patrones. Hace el trabajo pesado que antes nos robaba horas.

Pan inferior: el humano de nuevo. Verificas los hechos, validas el contexto clínico, y tomas la decisión final asumiendo la responsabilidad.

El relleno puede cambiar, hoy es GPT-4, mañana será otro modelo, pero el pan siempre es humano. La verificación al final no es opcional. Es innegociable.

---

### SLIDE 70 · Lo que nos llevamos para casa

Tres cosas que os lleváis para casa. Solo tres, porque si son más, no os acordaréis de ninguna.

Primero: el Modelo Sándwich. Humano define, IA procesa, humano verifica. La responsabilidad siempre es tuya.

Segundo: el Método RECORD. Rol, Escenario, Contexto, Objetivo, Restricciones, Diseño. La calidad del output depende de la calidad del prompt.

Y tercero: el Detector de Alucinaciones. Verifica siempre las referencias y los datos específicos. Usa herramientas con RAG como Open Evidence o Perplexity Pro.

Tres herramientas mentales. Tres escudos. Lleváoslos al centro de salud.

---

### SLIDE 71 · Pregunta de Evaluación 1

Primera pregunta de evaluación.

De las siguientes opciones, ¿cuál representa la aplicación más segura de IA generativa en la consulta de pediatría de Atención Primaria?

Uno: sustituir la consulta con dermatología. Dos: prescribir autónomamente. Tres: diagnosticar TDAH. Cuatro: interpretar una espirometría sin validación. O cinco: generar un borrador de información para padres sobre gastroenteritis.

La respuesta es la cinco. Bajo riesgo clínico, alto valor comunicativo, y siempre, siempre, con revisión del pediatra antes de entregar.

---

### SLIDE 72 · Pregunta de Evaluación 2

Segunda pregunta.

Según la paradoja humano más IA que vimos, ¿cuál es el riesgo principal de añadir supervisión humana a las respuestas de IA?

Uno: aumentar el coste. Dos: generar falsa confianza sin reducir errores. Tres: ralentizar el flujo. Cuatro: reducir la autonomía profesional. O cinco: crear dependencia tecnológica.

La respuesta es la dos. Recordad: el meta-análisis de Wang mostró que los errores persisten en un veintiséis a treinta y seis por ciento incluso con supervisión humana, porque la supervisión puede generar una falsa sensación de seguridad.

---

### SLIDE 73 · Gracias

Y con esto llegamos al final.

"Homines, dum docent, discunt." Los hombres, mientras enseñan, aprenden.

Os aseguro que preparar este seminario me ha enseñado tanto como espero que os haya enseñado a vosotros. La inteligencia artificial es una herramienta extraordinaria, pero solo si la usamos con rigor, con humildad y con el paciente siempre en el centro.

Recordad el sándwich. Recordad RECORD. Y recordad verificar.

Muchas gracias por vuestra atención, vuestra participación y vuestra generosidad compartiendo experiencias. Los materiales y todas las herramientas están en mi web. Y como siempre, mi buzón está abierto para preguntas, sugerencias o para seguir aprendiendo juntos.

Gracias.

---

## APÉNDICE · NOTAS PARA EL ORADOR

### Principios de oratoria aplicados

1. **Regla del tres:** cada bloque cierra con tres ideas clave. El cierre final tiene tres herramientas. Las evaluaciones tienen cinco opciones con una correcta destacada.

2. **Carga cognitiva:** máximo un concepto nuevo por diapositiva. Los datos numéricos se limitan a dos o tres cifras por slide. Las transiciones sirven como "descanso cognitivo."

3. **Anclajes de memoria:** cada concepto clave tiene un anclaje visual o metafórico (sándwich, semáforo, pirámide, oxígeno). Los acrónimos (RECORD) facilitan la recuperación.

4. **Estructura interna de cada locución:**
   - **Gancho** (primera frase): captura atención con dato, pregunta o afirmación provocadora.
   - **Desarrollo** (cuerpo): máximo tres puntos de apoyo.
   - **Cierre-puente** (última frase): resume y conecta con la siguiente diapositiva.

5. **Modularidad narrativa:** cada locución empieza con una frase autónoma que no depende de la anterior. Los puentes son opcionales: si se elimina una diapositiva, la siguiente sigue teniendo sentido.

6. **Calibración de tono:**
   - Bloques 0-1: cercano, accesible, rompehielos.
   - Bloque 2: riguroso, basado en datos, con alertas claras.
   - Bloque 3: entusiasta, práctico, demostrativo.
   - Bloque 4: motivador, participativo.
   - Bloque 5: recapitulativo, emocional, memorable.

### Tiempos estimados por locución

| Bloque | Slides con audio | Tiempo estimado |
|--------|-----------------|-----------------|
| 0 - Portada | 4 | ~5 min |
| 1 - Ruptura | 5 | ~8 min |
| 2A - Fundamentos | 4 | ~7 min |
| Evidencia | 18 | ~20 min |
| 2B - Marco Legal | 5 | ~8 min |
| 2C - Aplicaciones | 21 | ~24 min |
| 3 - Demos | 7 | ~10 min* |
| 4 - Práctica | 3 | ~5 min* |
| 5 - Cierre | 6 | ~10 min |
| **TOTAL** | **73** | **~97 min narrados** |

*El resto del tiempo de los bloques 3 y 4 se dedica a demos en vivo y práctica grupal.

