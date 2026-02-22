# Revisión de la Presentación IA-Pediatría AEPap 2026

## 📊 Resumen Ejecutivo

La presentación en reveal.js es **técnicamente sólida y visualmente atractiva**, con excelente uso de infografías NotebookLM y estructura clara en bloques. Sin embargo, existen **desajustes con el guion** que conviene revisar para mantener coherencia, y algunas **oportunidades de mejora** en contenido y navegabilidad.

---

## ✅ PUNTOS FUERTES

### 1. Estructura y Temporización
- Bloques bien definidos con tiempos claros (15 + 20 + 15 + 40 + 25 + 20 = 135 min)
- Uso coherente de section-intro para marcar transiciones
- Progreso visual con barras de navegación

### 2. Diseño Visual
- Paleta de colores consistente (azul pediátrico, verde secundario, ámbar para alertas)
- Glass panels con buen contraste sobre fondo oscuro
- Infografías de NotebookLM bien integradas (flujo clínico, human-in-the-loop, alucinaciones, etc.)
- Responsive design con media queries para diferentes resoluciones

### 3. Contenido Técnico
- Referencias DOI/enlaces funcionales en cada slide de evidencia
- Datos cuantitativos claros (métricas de precisión, concordancia, etc.)
- Diferenciación clara entre tareas de alta vs baja confianza

### 4. Interactividad
- Generador de prompts RECORD funcional
- Iframe del constructor de prompts
- Plugins de pizarra, menú y zoom

---

## 🔶 DESAJUSTES CON EL GUION

### 1. Contenido Ausente del Guion que NO Aparece en la Presentación

| Elemento del Guion | Status en HTML | Sugerencia |
|-------------------|----------------|------------|
| **Inteligencia Ambiental** (escucha activa + consentimiento) | ❌ Solo se menciona brevemente | Añadir slide dedicada o expandir en "Oxígeno para la consulta" |
| **Modelo Sándwich detallado** (3 capas explicadas) | ⚠️ Aparece muy resumido en cierre | Añadir slide explicativa en Bloque 3 |
| **Citación completa de 30 referencias** | ✅ Presente como DOIs inline | OK |
| **Gaps Críticos** (3 puntos específicos del guion) | ⚠️ Parcialmente cubierto | Añadir slide de "Limitaciones de la Evidencia" |
| **MedFound (176B)** | ✅ Presente | OK |
| **Inteligencia Ambiental con consentimiento** | ❌ Ausente | Añadir en Bloque 2C |

### 2. Contenido de la Presentación que NO Está en el Guion

| Elemento en HTML | Valoración |
|-----------------|------------|
| Bibliometría PubMed interactiva (iframe) | ✅ Excelente adición |
| Infografías NotebookLM (7 imágenes) | ✅ Enriquecen el contenido |
| NeonatalBERT, ROP, Coartación, Hipoxemia | ⚠️ Muy específicos - valorar si aportan al pediatra de AP |
| Patología confocal intraoperatoria | ⚠️ Fuera del scope de AP |
| AIS y consenso LLM | ⚠️ Muy especializado |

### 3. Énfasis Diferente

**En el guion se enfatiza más:**
- El enfoque pedagógico de "residente capaz pero propenso a fabulación"
- La cita de Alvin Toffler sobre preguntas correctas
- Los ejemplos concretos de personalización (GPT Revisor de Analíticas)

**En la presentación se enfatiza más:**
- Datos cuantitativos de evidencia reciente
- Casos específicos de deep learning en imagen médica
- Riesgos específicos (Dr. AI, RCP)

---

## 🔴 PROBLEMAS TÉCNICOS DETECTADOS

### 1. Rutas de Audio Incorrectas
```html
<!-- Línea 709: ruta local Windows que no funcionará en web -->
data-audio-src="C:\Users\ebarr\Documentos\GitHub\t\aepap-2026\audios\1.webm"
```
**Solución:** Convertir a rutas relativas o subir audios al servidor.

### 2. Rutas de Plugins Relativas al Padre
```html
<!-- Líneas 26-28: plugins con ruta "../reveal.js-plugins/" -->
<link rel="stylesheet" href="../reveal.js-plugins/menu/menu.css">
```
**Problema potencial:** Si la presentación no está en una subcarpeta, fallarán los plugins.

### 3. Imagen de Fondo
```html
<!-- Línea 236: ruta local -->
url('aepap-2026/assets/aepap-2026-bg.jpg')
```
Verificar que la imagen existe en esa ubicación relativa.

### 4. Slide Comentada (Sistema de Votación)
La slide del sistema de votación con folios verde/rojo está comentada (líneas ~867-913). ¿Se mantiene o se elimina?

---

## 📝 SUGERENCIAS DE MEJORA

### A. Contenido

#### A1. Añadir Slide de "Inteligencia Ambiental"
Crear una slide entre "Oxígeno para la Consulta" y "Prompt Engineering":

```html
<section class="wide-slide" data-menu-title="Inteligencia Ambiental">
    <div class="title-wrapper">
        <h2 class="assertion-title">La <span class="highlight">IA Ambiental</span> devuelve el contacto visual</h2>
        <p class="subtitle">Escucha activa → filtrado → nota estructurada automática</p>
    </div>
    <!-- Añadir diagrama o infografía del flujo -->
    <div class="glass-panel" style="max-width: 900px; margin: 14px auto; background: rgba(251,191,36,0.1);">
        <p style="font-size: 0.82em; text-align: center;">
            <i class="fa-solid fa-user-shield" style="color: var(--accent);"></i>
            <strong>Requisito ético:</strong> Consentimiento explícito del paciente/familia
        </p>
    </div>
</section>
```

#### A2. Expandir el Modelo Sándwich
Actualmente aparece solo en el cierre. Propongo añadir una slide explicativa en el Bloque 3:

```
Pan Superior (Humano): Define estrategia, elige herramienta
    ↓
Relleno (IA): Procesamiento masivo
    ↓
Pan Inferior (Humano): Verificación innegociable
```

#### A3. Reducir Slides Muy Especializadas
Las siguientes slides podrían condensarse en una sola de "Evidencia en Imagen Médica Pediátrica":
- Coartación prenatal (CoA-Net)
- Patología confocal intraoperatoria
- Hipoxemia pediátrica

**Razón:** Un pediatra de AP raramente usará estas herramientas directamente.

#### A4. Añadir Slide de "Gaps Críticos"
Del guion, crear slide específica:
1. Faltan ensayos prospectivos
2. No hay marcos estandarizados
3. Poblaciones pediátricas subrepresentadas

### B. Navegabilidad

#### B1. Índice Clicable
Añadir slide con índice interactivo después de la portada:

```html
<section data-menu-title="Índice">
    <h2>📋 Hoja de Ruta</h2>
    <div class="grid-2">
        <a href="#/1"><div class="glass-panel">1. Ruptura (15')</div></a>
        <a href="#/2"><div class="glass-panel">2. Fundamentos (20')</div></a>
        <!-- ... -->
    </div>
</section>
```

#### B2. Breadcrumbs
Añadir indicador visual del bloque actual en la esquina (actualmente no hay).

### C. Accesibilidad

#### C1. Alt Text en Imágenes
Revisar que todas las infografías NotebookLM tengan alt text descriptivo (la mayoría lo tienen ✅).

#### C2. Contraste
Algunos textos `var(--text-muted)` sobre fondo oscuro pueden ser difíciles de leer para personas con baja visión.

### D. Coherencia Temporal

| Bloque | Tiempo Guion | Tiempo Presentación | Diferencia |
|--------|--------------|---------------------|------------|
| Bloque 1: Ruptura | No especificado | 15 min | - |
| Bloque 2: Fundamentos | No especificado | 20 min | - |
| Bloque 2C: Puesta al día | No especificado | 15 min | - |
| Bloque 3: Demos | No especificado | 40 min | - |
| Bloque 4: Práctica | No especificado | 25 min | - |
| Bloque 5: Cierre | No especificado | 20 min | - |
| **TOTAL** | ~2 horas | **135 min** | **15 min extra** |

**Sugerencia:** Reducir Bloque 2C (Puesta al día) de 15 a 10 minutos eliminando slides muy especializadas.

---

## 🎯 PRIORIDADES DE ACCIÓN

### Alta Prioridad
1. **Corregir rutas de audio** (actualmente locales Windows)
2. **Añadir slide de Inteligencia Ambiental** (ausente del guion)
3. **Expandir Modelo Sándwich** en Bloque 3

### Media Prioridad
4. Consolidar slides de imagen médica especializada
5. Añadir slide de "Gaps Críticos"
6. Verificar todas las rutas de assets

### Baja Prioridad
7. Añadir índice clicable
8. Mejorar contraste de textos muted
9. Decidir sobre slide de votación (comentada)

---

## 📁 CHECKLIST DE IMÁGENES REFERENCIADAS

Las siguientes imágenes deben existir en `aepap-2026/assets/`:

- [ ] `aepap-2026-bg.jpg` (fondo)
- [ ] `slide_flujo_clinico_5etapas.jpg`
- [ ] `slide_human_in_the_loop.jpg`
- [ ] `slide_venn_colaboracion.jpg`
- [ ] `slide_alucinacion_bibliografica.jpg`
- [ ] `slide_brecha_examenes_clinica.jpg`
- [ ] `slide_fallos_rcp.jpg`
- [ ] `slide_oxigeno_consulta.jpg`
- [ ] `slide_prompt_engineering_checklist.jpg`
- [ ] `slide_matriz_madurez.jpg`
- [ ] `slide_rag_estandar.jpg`
- [ ] `slide_conclusiones_hibrido.jpg`
- [ ] `slide_semaforo_ap.jpg`
- [ ] `IA_en_Pediatría_Evidencia_y_Práctica_01.jpg`
- [ ] `IA_en_Pediatría_Evidencia_y_Práctica_02.jpg`
- [ ] `IA_en_Pediatría_Evidencia_y_Práctica_03.jpg`
- [ ] `IA_en_Pediatría_Evidencia_y_Práctica_04.jpg`

---

## 💡 CONCLUSIÓN

La presentación está **muy bien elaborada** y supera al guion en riqueza visual y datos cuantitativos. Los principales ajustes necesarios son:

1. **Técnicos**: Corregir rutas de audio locales
2. **Contenido**: Añadir Inteligencia Ambiental y expandir Modelo Sándwich
3. **Scope**: Valorar si las slides de imagen médica especializada aportan al pediatra de AP o distraen del mensaje central

El mensaje central del guion ("aumento, no reemplazo" + supervisión humana siempre) está bien transmitido en la presentación.
