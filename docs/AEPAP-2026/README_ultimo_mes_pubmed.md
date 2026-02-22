# Pipeline "Ultimo mes en Pediatria" (PubMed -> NotebookLM)

Script principal: `docs/AEPAP-2026/pipeline_ultimo_mes_pubmed.py`

## Que hace
1. Ejecuta dos consultas fijas:
   - Query A: revisiones/meta-analisis.
   - Query B: mixto alto impacto (revisiones + ECA/ensayos + guias).
2. Deduplica por PMID.
3. Aplica cribado editorial (protocolos, embarazo/materno/perinatal, parental/cuidadores).
4. Clasifica tipo de estudio y tema clinico.
5. Calcula score editorial 0-10:
   - 0-4 aplicabilidad inmediata en AP.
   - 0-3 claridad/magnitud del efecto.
   - 0-2 robustez metodologica.
   - 0-1 novedad.
6. Selecciona top 8-12 con:
   - minimo 5 temas,
   - maximo 3 articulos por tema.
7. Exporta artefactos listos para NotebookLM.

## Uso rapido
```bash
python docs/AEPAP-2026/pipeline_ultimo_mes_pubmed.py
```

## Opciones utiles
```bash
python docs/AEPAP-2026/pipeline_ultimo_mes_pubmed.py --days 30 --top-n 12 --min-topics 5 --max-per-topic 3 --output-dir docs/AEPAP-2026/ultimo_mes_output
```

Descargar PDFs de PMC (si existen enlaces abiertos):
```bash
python docs/AEPAP-2026/pipeline_ultimo_mes_pubmed.py --download-pmc-pdf
```

## Archivos de salida
En `docs/AEPAP-2026/ultimo_mes_output/`:
- `queries_pubmed.txt`: query A y query B completas.
- `pubmed_all_records.csv`: todo el set deduplicado y puntuado.
- `top_selected.csv`: seleccion final editorial.
- `notebooklm_manifest.csv`: enlaces PubMed/DOI/PMC para cargar en NotebookLM.
- `notebooklm_briefing.md`: tabla resumen (PMID, pregunta clinica, hallazgo, limitacion, accion).
- `pmids_manual_check_10.txt`: 10 PMIDs para verificacion manual.
- `run_metadata.json`: conteos, queries y checks de aceptacion.

## Check de aceptacion esperado
- Volumen mensual: ideal 80-220 registros en query mixta curada.
- Seleccion: 8-12 articulos.
- Cobertura: respiratorio + neuro/salud mental + digestivo/dermatologia.
- Protocolos en top final: 0.
- Aplicabilidad AP (score aplicabilidad >= 3): objetivo >= 70%.

## Nota de implementacion
La exclusión geografica se mantiene como bloque `NOT (...)` separado (evitando `AND NOT`) para conservar la traduccion de PubMed estable.
