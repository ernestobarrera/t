# Guía de Revisión — ia-pediatria-aepap-2026.html

## Instrucciones generales
- Abre el archivo HTML en tu IDE (VS Code, Sublime, etc.)
- Aplica los cambios **en el orden indicado** (de arriba a abajo en el archivo)
- Usa **Ctrl+F** para localizar cada cadena de búsqueda
- Usa **Ctrl+H** para reemplazar cuando se indique
- Tras cada cambio, guarda y previsualiza en navegador para verificar
- Los cambios están ordenados por posición en el archivo (de principio a fin)

---

## CAMBIO 1 — Eliminar `</section>` huérfano tras votación comentada

**Aspecto:** Hay un `</section>` suelto después del bloque de votación que está comentado (cerca del Bloque 0/Glosario). Este tag rompe la jerarquía de secciones de Reveal.js.

**Motivo:** Un `</section>` huérfano puede causar que Reveal.js interprete mal qué slides son horizontales y cuáles verticales. Es un error estructural que puede provocar comportamiento impredecible en la navegación.

**Qué verás:** Después del comentario HTML que cierra la sección de votación (`-->`), encontrarás un `</section>` que no tiene su `<section>` de apertura correspondiente. Está justo antes del inicio de la primera sección horizontal real (Bloque 1: Ruptura).

**Cómo localizarlo:**
Busca con Ctrl+F:
```
-->
</section>
```
justo después del bloque de votación comentado (busca "voto" o "votación" o "encuesta" dentro de un comentario HTML `<!-- ... -->`). El `</section>` inmediatamente posterior al cierre `-->` es el huérfano.

**Acción:** ELIMINAR esa línea `</section>` completa. No reemplazarla por nada.

**Verificación:** Tras eliminarlo, la estructura debe pasar del cierre del comentario `-->` directamente a la siguiente `<section>` de apertura del bloque horizontal.

---

## CAMBIO 2 — Eliminar slide del Diagrama de Venn (redundante con Human-in-the-Loop)

**Aspecto:** Hay dos slides consecutivas que comunican la misma idea (colaboración humano-IA): el Diagrama de Venn y la infografía Human-in-the-Loop. Son redundantes.

**Motivo:** Tener dos metáforas distintas para el mismo concepto (colaboración H+IA) en slides seguidas viola el principio de distintividad y consume tiempo sin aportar información nueva. Human-in-the-Loop es más visual y accionable.

**Qué verás:** Una slide `<section>` que contiene un diagrama de Venn con dos o tres círculos superpuestos que representan las capacidades del humano y de la IA. Estará dentro del Bloque 2 (Fundamentos).

**Cómo localizarlo:**
Busca con Ctrl+F:
```
Venn
```
o bien:
```
venn
```
Encontrarás la `<section>` que contiene este diagrama.

**Acción:** COMENTAR toda la slide (desde su `<section` de apertura hasta su `</section>` de cierre):
```html
<!-- SLIDE ELIMINADA: Venn redundante con Human-in-the-Loop
<section data-audio-text="...">
  ... todo el contenido de la slide Venn ...
</section>
FIN SLIDE ELIMINADA -->
```

**Verificación:** La navegación vertical del Bloque 2 debe saltar directamente de la slide anterior a la siguiente, sin pasar por el Venn.

---

## CAMBIO 3 — Insertar microactividad después de la Paradoja H+AI

**Aspecto:** Tras la slide que dice que "H+IA no siempre supera a IA sola" (la paradoja), insertar una slide de pausa activa para romper la exposición pasiva.

**Motivo:** En el análisis se detectó que entre el Bloque 1 y el ejercicio del Bloque 4 no hay ninguna interacción programada. Son ~28 slides de monólogo. Tu propio marco de presentaciones basadas en evidencia exige pausas activas cada 10-15 minutos.

**Qué verás:** La slide de la paradoja tiene un título tipo assertion que menciona "H+IA no siempre supera" o similar. Inmediatamente después de su `</section>` de cierre, insertarás la nueva slide.

**Cómo localizarlo:**
Busca con Ctrl+F:
```
H+IA no siempre supera
```
Avanza hasta el `</section>` que cierra esa slide.

**Acción:** INSERTAR inmediatamente después de ese `</section>` la siguiente slide nueva:
```html
            <!-- MICROACTIVIDAD: Pausa activa post-paradoja -->
            <section data-audio-text="Vamos a hacer una pausa. Quiero que penséis en vuestra experiencia. ¿Alguno ha tenido una experiencia donde la IA le dio una respuesta que parecía correcta pero no lo era?">
              <h2 class="assertion-title">⏸️ Pausa activa</h2>
              <div class="glass-panel" style="text-align:center; padding:2em;">
                <p style="font-size:1.3em;">🤔 Pensad un momento...</p>
                <p style="font-size:1.1em; margin-top:1em;">¿Alguno ha tenido la experiencia de que la IA le dio una respuesta que <strong>parecía correcta</strong> pero <strong>no lo era</strong>?</p>
                <p style="font-size:1.4em; margin-top:1.5em;">🙋 Levantad la mano</p>
                <p class="source-note" style="margin-top:2em; font-size:0.7em;">💡 Esto conecta directamente con lo que acabamos de ver: la paradoja de la automatización</p>
              </div>
            </section>
```

**Verificación:** Al navegar verticalmente, tras la paradoja H+AI aparece esta slide de interacción antes de continuar con el siguiente contenido.

---

## CAMBIO 4 — Comentar slides de Bloque 2B para material complementario

**Aspecto:** Cuatro slides del Bloque 2B (Riesgos) son demasiado técnicas o específicas para el ritmo del seminario: "RAG y sesgo", "Precisión Diagnóstica" (Velocidad vs Fiabilidad), y "Consenso Clínico". Pasan a material complementario.

**Motivo:** Hay 10 slides de riesgos, lo cual es excesivo. El público saldrá pensando "la IA es peligrosa" en vez de "sé cómo usarla bien". Las 5 imprescindibles son: alucinaciones, paradoja H+AI, brecha exámenes/clínica, sesgos algorítmicos y semáforo de seguridad. Las demás son material complementario.

**Qué verás:** Slides individuales dentro de la sección vertical del Bloque 2B (Riesgos), cada una con su `<section>` y `</section>`.

**Cómo localizarlo y actuar (hacer para CADA una de las siguientes):**

### 4a. Slide "RAG y sesgo" (ICC 0.27)
Busca con Ctrl+F:
```
RAG y sesgo
```
o bien:
```
ICC 0.27
```
Comenta toda la `<section>`:
```html
<!-- MATERIAL COMPLEMENTARIO: RAG y sesgo
<section data-audio-text="...">
  ...
</section>
FIN MATERIAL COMPLEMENTARIO -->
```

### 4b. Slide "Velocidad vs Fiabilidad" / "Precisión Diagnóstica"
Busca con Ctrl+F:
```
Velocidad vs Fiabilidad
```
o bien:
```
Precisión Diagnóstica
```
Misma operación: comentar toda la `<section>`.

### 4c. Slide "Consenso Clínico"
Busca con Ctrl+F:
```
Consenso Clínico
```
Misma operación: comentar toda la `<section>`.

**Verificación:** Al navegar el Bloque 2B, estas slides ya no aparecen. El bloque se siente más ágil.

---

## CAMBIO 5 — Eliminar Semáforo 09 (mantener solo Semáforo AP)

**Aspecto:** El semáforo de seguridad aparece dos veces: como infografía 09 (dentro de Riesgos) y como "Semáforo AP" o "Hoja de Ruta AP" (en Puesta al día). Son prácticamente la misma idea.

**Motivo:** Redundancia directa. La versión "Semáforo AP" es más práctica y accionable para el público de pediatras de AP, así que se mantiene esa y se comenta la infografía 09.

**Qué verás:** Una slide que contiene una imagen de infografía (probablemente `slide_semaforo` o referencia a infografía "09") con un semáforo de colores.

**Cómo localizarlo:**
Busca con Ctrl+F:
```
semaforo_09
```
o bien:
```
infografia_09
```
o bien:
```
slide_09
```
Si no encuentras ninguna de esas, busca la palabra "semáforo" y localiza la que está dentro del Bloque 2B (Riesgos), NO la que está en el Bloque 2C (Puesta al día).

**Acción:** Comentar toda la `<section>` de esta slide:
```html
<!-- MATERIAL COMPLEMENTARIO: Semáforo 09 (se mantiene Semáforo AP)
<section data-audio-text="...">
  ...
</section>
FIN MATERIAL COMPLEMENTARIO -->
```

**Verificación:** Solo queda un semáforo en toda la presentación: el de "Semáforo AP" en el Bloque 2C.

---

## CAMBIO 6 — Comentar slides de Bloque 2C para material complementario

**Aspecto:** Cuatro slides del Bloque 2C (Puesta al día) que no se vinculan directamente con los 3 objetivos de aprendizaje. Pasan a material complementario.

**Motivo:** El Bloque 2C tiene 14 slides en ~15 minutos, lo cual es una ráfaga de datos que viola el principio de "bloques cortos con pausas". Bajamos de 14 a ~8 slides, ganando tiempo para interacción.

**Cómo localizarlo y actuar (para CADA una):**

### 6a. Slide "Caries escolar"
Busca con Ctrl+F:
```
Caries
```
o bien:
```
caries escolar
```
Comenta toda la `<section>`.

### 6b. Slide "Riesgo suicida"
Busca con Ctrl+F:
```
Riesgo suicida
```
o bien:
```
suicida
```
Comenta toda la `<section>`.

### 6c. Slide "Diagnóstico precoz AP" (multi-agente)
Busca con Ctrl+F:
```
Diagnóstico precoz AP
```
o bien:
```
multi-agente
```
Comenta toda la `<section>`.

### 6d. Slide "Matriz de Madurez Tecnológica"
Busca con Ctrl+F:
```
Matriz de Madurez
```
Comenta toda la `<section>`.

**Formato de comentario (igual para todas):**
```html
<!-- MATERIAL COMPLEMENTARIO: [nombre de la slide]
<section data-audio-text="...">
  ...
</section>
FIN MATERIAL COMPLEMENTARIO -->
```

**Verificación:** El Bloque 2C ahora tiene ~8 slides en vez de 14. El ritmo mejora notablemente.

---

## CAMBIO 7 — Fusionar slides de modelos open-source + modelos especializados

**Aspecto:** Hay dos slides separadas: una sobre "modelos open-source" y otra sobre "modelos especializados". Se fusionan en una sola.

**Motivo:** Ambas slides comparten la misma narrativa (el ecosistema de modelos se diversifica) y juntas comunican un mensaje más potente que separadas. Además, reducen una slide del Bloque 2C.

**Qué verás:** Dos slides consecutivas en el Bloque 2C. La primera habla de open-source (con assertion tipo "Los modelos open-source ya igualan a los propietarios") y la segunda de modelos especializados para diagnóstico.

**Cómo localizarlo:**
Busca con Ctrl+F:
```
open-source ya igualan
```
Esta es la PRIMERA de las dos slides.

**Acción en dos pasos:**

**Paso 1:** Comenta la SEGUNDA slide (modelos especializados):
Busca:
```
Modelos especializados
```
o bien:
```
modelos especializados
```
Comenta toda esa `<section>`.

**Paso 2:** Modifica el título de la primera slide para que integre ambos conceptos. Busca el `<h2>` de la slide open-source y reemplázalo:

Busca:
```
Los modelos open-source ya igualan a los propietarios
```
Reemplaza por:
```
El ecosistema de modelos se diversifica: open-source compite, especializados destacan en diagnóstico
```

Opcionalmente, dentro del contenido de esa slide, añade una mención breve a los modelos especializados (una línea de glass-panel adicional).

**Verificación:** Ahora hay una sola slide que cubre ambos temas de forma integrada.

---

## CAMBIO 8 — Añadir Pregunta Test 2

**Aspecto:** La Pregunta Test 2 no está en la presentación. Solo existe la Pregunta 1. El Objetivo 2 (valoración crítica) no tiene evaluación formativa.

**Motivo:** El DOCX de objetivos define dos preguntas test. Solo la primera está implementada. La segunda es necesaria para evaluar el Objetivo 2 (reconocer limitaciones y riesgos).

**Qué verás:** La Pregunta 1 ya existe como slide con título "Pregunta de Evaluación 1" o similar.

**Cómo localizarlo:**
Busca con Ctrl+F:
```
Pregunta de Evaluación
```
o bien:
```
Pregunta Test
```
Localiza la slide existente (Pregunta 1). La Pregunta 2 se insertará DESPUÉS de ella o bien justo antes del cierre/takeaways.

**Acción:** Inserta esta nueva slide. El mejor lugar es **después del Bloque 2C** (tras "El futuro es híbrido") o **antes de los takeaways finales**:

Busca el punto de inserción:
```
El futuro es híbrido
```
Avanza hasta el `</section>` que cierra esa slide. Inserta inmediatamente después:

```html
            <!-- PREGUNTA TEST 2: Evaluación Objetivo 2 -->
            <section data-audio-text="Segunda pregunta de evaluación. Ante un informe generado por IA para un paciente pediátrico, ¿cuál de las siguientes acciones es la más adecuada?">
              <h2 class="assertion-title">📝 Pregunta de Evaluación 2</h2>
              <p style="font-size:0.85em; margin-bottom:0.8em;">Ante un informe generado por IA sobre el manejo de una bronquiolitis en lactante de 3 meses, ¿cuál es la acción <strong>más adecuada</strong> antes de aplicar sus recomendaciones?</p>
              <div class="glass-panel" style="padding:0.8em;">
                <p><strong>a)</strong> Aplicar directamente si proviene de un modelo validado como GPT-4</p>
                <p><strong>b)</strong> Contrastar con guías clínicas vigentes y adaptar al contexto del paciente</p>
                <p><strong>c)</strong> Consultar con un colega para confirmar la respuesta de la IA</p>
                <p><strong>d)</strong> Solicitar al modelo que cite sus fuentes y aceptar si las muestra</p>
              </div>
              <div class="action-box" style="margin-top:1em;">
                <p>✅ <strong>Respuesta correcta: b)</strong> — La IA es asistente, no decisora. El juicio clínico y las guías vigentes son el estándar. Las citas de la IA pueden ser alucinadas (cambio 4b de la paradoja que vimos).</p>
              </div>
            </section>
```

**Nota:** Ajusta el texto de la pregunta al contenido exacto de tu DOCX de objetivos si difiere.

**Verificación:** Ahora la presentación tiene dos preguntas test, cubriendo ambos objetivos evaluables.

---

## CAMBIO 9 — Mover slide "Modelo Sándwich" dentro del Bloque 5

**Aspecto:** La slide del Modelo Sándwich está "flotando" entre el cierre del Bloque 4 y la apertura del Bloque 5, fuera de cualquier `<section>` contenedora vertical.

**Motivo:** En Reveal.js, una slide fuera de una sección horizontal contenedora se convierte en un bloque horizontal independiente, rompiendo la navegación vertical esperada. El Sándwich debe ir dentro del Bloque 5 (Cierre), justo antes de los takeaways, donde funciona como transición.

**Qué verás:** Busca la slide que menciona "Modelo Sándwich" o "Sándwich". Estará entre dos `</section>` de bloques horizontales (uno cerrando el Bloque 4, otro abriendo el Bloque 5).

**Cómo localizarlo:**
Busca con Ctrl+F:
```
Modelo Sándwich
```
o bien:
```
Sándwich
```

**Acción:**
1. **CORTA** toda la `<section>...</section>` del Modelo Sándwich (incluyendo apertura y cierre)
2. **LOCALIZA** el inicio del Bloque 5 (busca el `<section>` horizontal que contiene el cierre/takeaways)
3. **PEGA** la slide del Sándwich como PRIMERA slide vertical dentro de ese bloque, justo después del `<section>` de apertura del Bloque 5

La estructura debe quedar:
```html
<!-- BLOQUE 5: CIERRE -->
<section>
  <!-- Modelo Sándwich (movido aquí desde entre bloques) -->
  <section data-audio-text="...">
    ... contenido del Sándwich ...
  </section>
  
  <!-- Takeaways, pregunta test, etc. -->
  <section ...>
    ...
```

**Verificación:** Al navegar, el Bloque 5 empieza con el Modelo Sándwich y luego baja verticalmente a los takeaways.

---

## CAMBIO 10 — Eliminar definición CSS duplicada de .demo-overlay

**Aspecto:** La clase `.demo-overlay` está definida dos veces en el `<style>` del documento, con propiedades diferentes.

**Motivo:** La segunda definición sobrescribe la primera (por cascada CSS). La primera es código muerto que genera confusión al mantener el archivo.

**Qué verás:** Dentro del bloque `<style>` del `<head>`, dos reglas separadas para `.demo-overlay`.

**Cómo localizarlo:**
Busca con Ctrl+F:
```
.demo-overlay
```
Encontrarás **dos** resultados dentro del CSS. La primera aparición es la que hay que eliminar.

**Acción:** Elimina la PRIMERA definición completa de `.demo-overlay { ... }`. Mantén la SEGUNDA (que es la que realmente se usa).

Para identificar los límites: la definición empieza en `.demo-overlay {` y termina en el `}` correspondiente (cuidado con llaves anidadas).

**Verificación:** Busca `.demo-overlay` de nuevo. Solo debe aparecer UNA vez en el CSS (más las veces que se use como clase en el HTML).

---

## CAMBIO 11 — Mejorar títulos-etiqueta → títulos-aserción

**Aspecto:** Varias slides tienen títulos temáticos ("de qué va la slide") en vez de aserciones ("qué afirma la slide"). Según tu marco de presentaciones basadas en evidencia, el titular debe ser una proposición completa y verificable.

**Motivo:** Los titulares-enunciado son más memorables, facilitan el procesamiento cognitivo, y permiten al público saber qué recordar incluso si pierde atención durante la explicación.

**Cambios específicos (buscar → reemplazar):**

### 11a. Glosario
Busca:
```
📚 Hablando el mismo idioma
```
Reemplaza por:
```
📚 Seis conceptos que cambiarán tu forma de entender la IA
```
*(Alternativa: dejarlo como está si consideras que funciona como slide-herramienta, no como argumento.)*

### 11b. Evidencia 2025-2026 (título de transición)
Busca:
```
Evidencia 2025-2026
```
Si es un título de slide/sección, reemplaza por:
```
La evidencia 2025-2026 confirma: alta precisión en tareas acotadas, baja fiabilidad en diagnóstico autónomo
```

### 11c. Matriz de Madurez (si decidiste NO comentarla en el cambio 6d)
Busca:
```
Matriz de Madurez Tecnológica por dominio
```
Reemplaza por:
```
Solo 3 dominios pediátricos tienen evidencia para automatización parcial
```

### 11d. RAG (si decidiste NO comentarla en el cambio 4a)
Busca:
```
RAG: estándar de oro para implementación segura
```
Reemplaza por:
```
RAG reduce alucinaciones al anclar la respuesta en fuentes verificadas
```

**Verificación:** Lee los títulos de tus slides como si fueran los "titulares de portada" de tu presentación. Cada uno debe comunicar una idea completa, no un tema.

---

## RESUMEN VISUAL DE CAMBIOS

| # | Tipo | Dónde | Impacto |
|---|------|-------|---------|
| 1 | 🔧 Bug fix | Bloque 0 (tras votación) | Estructura Reveal.js |
| 2 | ❌ Eliminar | Bloque 2 (Venn) | -1 slide redundante |
| 3 | ➕ Insertar | Tras Paradoja H+AI | Ritmo: pausa activa |
| 4 | 💬 Comentar | Bloque 2B (3 slides) | -3 slides técnicas |
| 5 | 💬 Comentar | Bloque 2B (Semáforo 09) | -1 slide redundante |
| 6 | 💬 Comentar | Bloque 2C (4 slides) | -4 slides tangenciales |
| 7 | 🔀 Fusionar | Bloque 2C (2→1) | -1 slide |
| 8 | ➕ Insertar | Tras "Futuro híbrido" | +1 pregunta evaluación |
| 9 | 📦 Mover | Sándwich → Bloque 5 | Estructura narrativa |
| 10 | 🔧 Bug fix | CSS `<style>` | Código limpio |
| 11 | ✏️ Editar | Varios títulos | Claridad assertion |

**Balance neto:** ~-9 slides del flujo principal (pasan a comentario/material complementario) + 2 slides nuevas (microactividad + pregunta test 2) = **~7 slides menos** en el flujo activo.

---

## NOTA IMPORTANTE

Las cadenas de búsqueda están basadas en el análisis detallado del HTML original. Si alguna cadena no da resultado exacto con Ctrl+F, prueba una variación cercana (por ejemplo, sin tildes, con/sin emojis, o usando solo las primeras palabras del título). El contenido semántico es el indicado; la cadena literal puede tener ligeras variaciones tipográficas.
