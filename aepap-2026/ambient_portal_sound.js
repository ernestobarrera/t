// ═══════════════════════════════════════════════════════════════════════
// AMBIENT PORTAL SOUND — Portada AEPap 2026
// Drone espacial procedural · Web Audio API · Sin archivos externos
// Diseño: serie armónica de A1 (55Hz) con LFOs lentos y reverb simulado
// ═══════════════════════════════════════════════════════════════════════

(function () {
  'use strict';

  // ── PARÁMETROS AJUSTABLES ─────────────────────────────────────────────
  var CFG = {
    masterVolume: 0.15,   // Volumen global. Aumentado para mayor presencia.
    fadeInTime: 3.0,     // Segundos de fade-in (sincroniza con lente SVG)
    fadeOutTime: 1.4,     // Segundos de fade-out al salir de portada
    reverbDelay: 0.42,    // Tiempo de delay del reverb (s). No tocar.
    reverbFeedback: 0.32,   // Feedback del reverb. No tocar.
    reverbWet: 0.26,    // Mezcla wet del reverb. No tocar.
    breathRate: 0.075,   // Hz del LFO master (ciclo ~13s). Efecto "respiración".
    breathDepth: 0.011,   // Profundidad de la respiración. Sutil.
  };

  // ── DEFINICIÓN DE CAPAS FRECUENCIALES ────────────────────────────────
  // Serie armónica natural de A1 (55Hz).
  // type: forma de onda | gain: volumen relativo | lfo: modulación individual
  var LAYERS = [
    { f: 55.0, gain: 0.58, type: 'sine', lfo: { rate: 0.037, depth: 0.25 } }, // Sub drone
    { f: 82.5, gain: 0.32, type: 'triangle', lfo: { rate: 0.028, depth: 0.18 } }, // Quinta baja
    { f: 110.0, gain: 1.00, type: 'sine', lfo: { rate: 0.063, depth: 0.45 } }, // Fundamental
    { f: 165.0, gain: 0.38, type: 'sine', lfo: { rate: 0.099, depth: 0.70 } }, // Quinta
    { f: 220.0, gain: 0.22, type: 'sine', lfo: { rate: 0.044, depth: 0.35 } }, // Octava
    { f: 440.0, gain: 0.07, type: 'sine', lfo: { rate: 0.172, depth: 1.80 } }, // Shimmer alto
  ];

  // ── ESTADO INTERNO ────────────────────────────────────────────────────
  var audioCtx = null;
  var masterGain = null;
  var allNodes = [];     // Todos los nodos para cleanup
  var isPlaying = false;
  var autoFadeTimer = null;   // Timer para apagar solo tras 30s

  // ── CREAR CONTEXTO (lazy, sólo cuando se necesita) ───────────────────
  function getContext() {
    if (audioCtx) return audioCtx;
    try {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      return audioCtx;
    } catch (e) {
      console.warn('[AmbientSound] Web Audio API no disponible:', e);
      return null;
    }
  }

  // ── CONSTRUIR RED DE REVERB (delay + feedback loop) ──────────────────
  function buildReverb(ctx, destination) {
    var delay = ctx.createDelay(2.0);
    var feedback = ctx.createGain();
    var wet = ctx.createGain();
    var dryPass = ctx.createGain();

    delay.delayTime.value = CFG.reverbDelay;
    feedback.gain.value = CFG.reverbFeedback;
    wet.gain.value = CFG.reverbWet;
    dryPass.gain.value = 1.0 - CFG.reverbWet;

    // Delay loop: delay → feedback → delay
    delay.connect(feedback);
    feedback.connect(delay);

    // Salida wet del reverb
    delay.connect(wet);
    wet.connect(destination);

    allNodes.push(delay, feedback, wet, dryPass);
    return delay; // devolvemos la entrada del reverb
  }

  // ── ARRANCAR SONIDO ───────────────────────────────────────────────────
  function startAmbient(isManual) {
    if (isPlaying) return;

    var ctx = getContext();
    if (!ctx) return;

    var doStart = function () {
      if (isPlaying) return;
      isPlaying = true; // Activar flag rápido

      var now = ctx.currentTime;

      // Nodo master con fade-in exponencial
      masterGain = ctx.createGain();
      masterGain.gain.setValueAtTime(0.0001, now);
      masterGain.gain.exponentialRampToValueAtTime(CFG.masterVolume, now + CFG.fadeInTime);
      masterGain.connect(ctx.destination);

      // Red de reverb (entrada = reverbIn)
      var reverbIn = buildReverb(ctx, masterGain);

      // ── Capas de osciladores ──────────────────────────────────────────
      LAYERS.forEach(function (def) {
        var osc = ctx.createOscillator();
        var gain = ctx.createGain();

        // Micro-detune aleatorio (±0.12Hz) → evita phase cancellation perfecta
        osc.type = def.type;
        osc.frequency.value = def.f + (Math.random() - 0.5) * 0.24;
        gain.gain.value = def.gain;

        // LFO individual en frecuencia (vibrato ultralento → "movimiento vivo")
        var lfo = ctx.createOscillator();
        var lfoGain = ctx.createGain();
        lfo.type = 'sine';
        lfo.frequency.value = def.lfo.rate;
        lfoGain.gain.value = def.lfo.depth;
        lfo.connect(lfoGain);
        lfoGain.connect(osc.frequency);

        // Conexiones de señal: osc → gain → master Y → reverb (en paralelo)
        osc.connect(gain);
        gain.connect(masterGain);
        gain.connect(reverbIn);

        osc.start(now);
        lfo.start(now);

        allNodes.push(osc, lfo, gain, lfoGain);
      });

      // ── LFO master: respiración global ───────────────────────────────
      var breathOsc = ctx.createOscillator();
      var breathGain = ctx.createGain();
      breathOsc.type = 'sine';
      breathOsc.frequency.value = CFG.breathRate;
      breathGain.gain.value = CFG.breathDepth;
      breathOsc.connect(breathGain);
      breathGain.connect(masterGain.gain); // modula el gain master directamente
      breathOsc.start(now);
      allNodes.push(breathOsc, breathGain);

      updateUIBtnState();

      // Auto-fade out suave tras 30 segundos, pero SOLO si arrancó automáticamente.
      // Si el usuario lo enciende manualmente, el dron sonará indefinidamente.
      clearTimeout(autoFadeTimer);
      if (!isManual) {
        autoFadeTimer = setTimeout(function () {
          if (isPlaying) {
            userMuted = true; // Actuamos como si el usuario lo muteara para que no vuelva a saltar
            stopAmbient();
          }
        }, 30000);
      }
    };

    // Reanudar si está suspendido por política de autoplay
    if (ctx.state === 'suspended') {
      ctx.resume().then(doStart).catch(function () {
        console.warn('[AmbientSound] Autoplay bloqueado. Esperando interacción del usuario.');
        isPlaying = false;
        updateUIBtnState();
      });
    } else {
      doStart();
    }
  }

  // ── DETENER SONIDO (con fade-out) ─────────────────────────────────────
  function stopAmbient() {
    clearTimeout(autoFadeTimer);
    if (!isPlaying || !audioCtx || !masterGain) return;

    var now = audioCtx.currentTime;

    // Fade-out exponencial
    masterGain.gain.cancelScheduledValues(now);
    masterGain.gain.setValueAtTime(masterGain.gain.value || CFG.masterVolume, now);
    masterGain.gain.exponentialRampToValueAtTime(0.0001, now + CFG.fadeOutTime);

    // Cleanup después del fade
    var nodesToKill = allNodes.slice();
    var gainRef = masterGain;

    setTimeout(function () {
      nodesToKill.forEach(function (n) {
        try { n.stop(); } catch (e) { }
        try { n.disconnect(); } catch (e) { }
      });
      try { gainRef.disconnect(); } catch (e) { }
      allNodes = [];
      masterGain = null;
      isPlaying = false;
      updateUIBtnState();
    }, (CFG.fadeOutTime + 0.15) * 1000);
  }

  // ── UI BOTÓN MUTE (Discreto) ──────────────────────────────────────────
  var uiBtn = null;
  var userMuted = false;

  function ensureUI() {
    if (uiBtn) return;
    uiBtn = document.createElement('button');
    uiBtn.innerHTML = '🔊';
    uiBtn.style.position = 'fixed';
    uiBtn.style.bottom = '15px';
    uiBtn.style.right = '15px';
    uiBtn.style.zIndex = '999999';
    uiBtn.style.background = 'rgba(15,23,42,0.6)';
    uiBtn.style.border = '1px solid rgba(255,255,255,0.2)';
    uiBtn.style.borderRadius = '50%';
    uiBtn.style.width = '44px';
    uiBtn.style.height = '44px';
    uiBtn.style.color = 'rgba(255,255,255,0.8)';
    uiBtn.style.cursor = 'pointer';
    uiBtn.style.fontSize = '20px';
    uiBtn.style.boxShadow = '0 0 10px rgba(96, 165, 250, 0.3)';
    uiBtn.style.display = 'flex';
    uiBtn.style.alignItems = 'center';
    uiBtn.style.justifyContent = 'center';
    uiBtn.style.opacity = '0';
    uiBtn.style.pointerEvents = 'none';
    uiBtn.style.transition = 'all 0.4s ease';
    uiBtn.style.backdropFilter = 'blur(6px)';
    uiBtn.title = 'Alternar drone espacial (Portada)';

    uiBtn.addEventListener('mouseenter', function () {
      uiBtn.style.opacity = '1';
      uiBtn.style.color = '#fff';
      uiBtn.style.boxShadow = '0 0 15px rgba(96, 165, 250, 0.6)';
    });
    uiBtn.addEventListener('mouseleave', function () {
      // If we are on portada, stay slightly visible
      if (typeof Reveal !== 'undefined' && Reveal.getCurrentSlide() && isPortada(Reveal.getCurrentSlide())) {
        uiBtn.style.opacity = '0.7';
        uiBtn.style.color = 'rgba(255,255,255,0.8)';
        uiBtn.style.boxShadow = '0 0 10px rgba(96, 165, 250, 0.3)';
      }
    });

    uiBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      if (isPlaying) {
        userMuted = true;
        stopAmbient();
      } else {
        userMuted = false;
        startAmbient(true);
      }
      updateUIBtnState();
    });
    document.body.appendChild(uiBtn);
  }

  function updateUIBtnState() {
    if (!uiBtn) return;
    if (isPlaying) {
      uiBtn.innerHTML = '🔊';
    } else {
      uiBtn.innerHTML = '🔇';
    }
  }

  function toggleUIVisibility(show) {
    if (!uiBtn) return;
    if (show) {
      uiBtn.style.opacity = '0.7';
      uiBtn.style.pointerEvents = 'auto';
    } else {
      uiBtn.style.opacity = '0';
      uiBtn.style.pointerEvents = 'none';
    }
  }

  // ── DETECCIÓN DE SLIDE PORTADA ────────────────────────────────────────
  // Identifica por data-menu-title="Portada" — robusto ante renumeraciones
  function isPortada(slideEl) {
    return slideEl &&
      (slideEl.dataset.menuTitle === 'Portada' ||
        slideEl.getAttribute('data-menu-title') === 'Portada');
  }

  // ── INTEGRACIÓN CON REVEAL.JS ─────────────────────────────────────────
  // Espera a que Reveal esté listo antes de suscribirse a eventos
  Reveal.on('ready', function (event) {
    ensureUI();
    if (isPortada(event.currentSlide)) {
      toggleUIVisibility(true);
      // Pequeño delay: deja que el SVG comience a animarse primero (100ms)
      setTimeout(function () {
        if (!userMuted) startAmbient(false);
      }, 100);
    }
  });

  Reveal.on('slidechanged', function (event) {
    ensureUI();
    var entrando = isPortada(event.currentSlide);
    var saliendo = isPortada(event.previousSlide);

    if (entrando) {
      toggleUIVisibility(true);
      if (!isPlaying && !userMuted) {
        setTimeout(function () { startAmbient(false); }, 80);
      }
    } else {
      toggleUIVisibility(false);
      if (saliendo && isPlaying) {
        stopAmbient();
      }
    }
  });

  // Seguridad: si por alguna razón el estado se desincroniza
  Reveal.on('slidetransitionend', function (event) {
    if (!isPortada(event.currentSlide)) {
      toggleUIVisibility(false);
      if (isPlaying) stopAmbient();
    }
  });

  // ── LIMPIEZA AL CERRAR LA VENTANA ────────────────────────────────────
  window.addEventListener('beforeunload', function () {
    if (isPlaying) stopAmbient();
    if (audioCtx) {
      try { audioCtx.close(); } catch (e) { }
    }
  });

})();
// ── FIN AMBIENT PORTAL SOUND ──────────────────────────────────────────
