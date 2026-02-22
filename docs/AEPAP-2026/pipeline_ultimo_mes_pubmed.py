#!/usr/bin/env python3
"""
Pipeline mensual PubMed -> curacion editorial -> paquete NotebookLM.

Implementa dos estrategias de consulta:
- Query A: revisiones/meta-analisis
- Query B: mixto alto impacto (revisiones + ensayos + guias)

Luego:
- deduplica por PMID
- clasifica tipo de estudio y tema clinico
- aplica scoring editorial 0-10
- selecciona top (8-12) con cobertura tematica minima y limite por tema
- exporta artefactos listos para NotebookLM
"""

from __future__ import annotations

import argparse
import calendar
import csv
import datetime as dt
import json
import random
import re
import sys
import textwrap
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Sequence, Tuple

EUTILS_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

TOPIC_BLOCK = textwrap.dedent(
    """
    (
      ( "Attention Deficit Disorder with Hyperactivity"[Mesh] OR ADHD[tiab] OR TDAH[tiab] OR "attention deficit hyperactivity"[tiab] OR "attention deficit disorder"[tiab] OR "hyperkinetic disorder*"[tiab] )
      OR ( "Autism Spectrum Disorder"[Mesh] OR autism[tiab] OR autistic[tiab] OR ASD[tiab] OR TEA[tiab] OR "trastorno* del espectro autista"[tiab] )
      OR ( "Bronchiolitis"[Mesh] OR bronchiolitis[tiab] OR bronquiolitis[tiab] OR RSV[tiab] OR "respiratory syncytial virus"[tiab] OR "virus sincitial respiratorio"[tiab] )
      OR ( "Asthma"[Mesh] OR asthma[tiab] OR wheez*[tiab] OR sibilanc*[tiab] OR "episodic viral wheez*"[tiab] OR "recurrent wheez*"[tiab] )
      OR ( "Upper Respiratory Tract Infections"[Mesh] OR "respiratory tract infection*"[tiab] OR "upper respiratory"[tiab] OR "common cold"[tiab] OR "upper respiratory infection*"[tiab] OR resfriado*[tiab] OR catarro*[tiab] )
      OR ( "Otitis Media"[Mesh] OR otitis[tiab] OR "otitis media"[tiab] OR "acute otitis"[tiab] OR "otitis media with effusion"[tiab] OR "otitis media aguda"[tiab] )
      OR ( "Gastroenteritis"[Mesh] OR gastroenteritis[tiab] OR diarrhea[tiab] OR diarrhoea[tiab] OR diarrea[tiab] OR vomiting[tiab] OR vomit*[tiab] )
      OR ( "Dermatitis, Atopic"[Mesh] OR "atopic dermatitis"[tiab] OR "dermatitis atopic*"[tiab] OR "dermatitis atopica"[tiab] OR eczema[tiab] OR eccema[tiab] )
      OR ( "Obesity"[Mesh] OR "Pediatric Obesity"[Mesh] OR obes*[tiab] OR overweight[tiab] OR sobrepeso[tiab] OR "body mass index"[tiab] OR BMI[tiab] )
      OR ( "Anxiety Disorders"[Mesh] OR anxiety[tiab] OR anxious[tiab] OR "trastorno* de ansiedad"[tiab] OR "social anxiety"[tiab] OR "generalized anxiety"[tiab] )
    )
    """
).strip()

PEDIATRIC_BASE = textwrap.dedent(
    """
    (hasabstract[text])
    AND ( "Child"[Mesh] OR "Infant"[Mesh] OR "Adolescent"[Mesh] OR pediatric*[tiab] OR paediatric*[tiab] )
    AND (humans[Filter])
    AND (allchild[Filter] OR newborn[Filter] OR allinfant[Filter] OR infant[Filter] OR preschoolchild[Filter] OR child[Filter])
    """
).strip()

REVIEW_BLOCK = textwrap.dedent(
    """
    (systematic[sb] OR "meta-analysis"[pt] OR "systematic review"[pt] OR meta-analy*[tiab] OR systematic review*[tiab])
    """
).strip()

MIXED_BLOCK = textwrap.dedent(
    """
    (
      (systematic[sb] OR "meta-analysis"[pt] OR "systematic review"[pt])
      OR ("Randomized Controlled Trial"[pt] OR "Clinical Trial"[pt])
      OR (guideline[pt] OR "practice guideline"[pt] OR guideline*[ti])
    )
    """
).strip()

# Mantiene la logica "excluir contextos no OCDE/desarrollados" evitando AND NOT.
GEO_EXCLUSION_BLOCK = textwrap.dedent(
    """
    NOT ("Developing Countries"[Mesh] NOT ("Developed Countries"[Mesh] OR "European Union"[Mesh] OR "Organisation for Economic Co-Operation and Development"[Mesh]))
    """
).strip()

NOISE_EXCLUSION_BLOCKS = [
    'NOT (protocol[ti] OR "study protocol"[ti])',
    'NOT (pregnan*[tiab] OR prenatal[tiab] OR maternal[tiab] OR postpartum[tiab] OR perinatal[tiab])',
    'NOT (parents[tiab] OR parental[tiab] OR caregiver*[tiab])',
]

TOPIC_RULES: List[Tuple[str, Tuple[str, ...]]] = [
    ("Bronquiolitis/RSV", ("bronchiolitis", "bronquiolitis", "rsv", "respiratory syncytial")),
    ("Asma/Sibilancias", ("asthma", "wheez", "sibilanc")),
    ("IVRS/Resfriado", ("upper respiratory", "common cold", "resfriado", "catarro", "respiratory tract infection")),
    ("Otitis media", ("otitis",)),
    ("Gastroenteritis", ("gastroenter", "diarr", "rotavirus", "norovirus")),
    ("Dermatitis atopica", ("atopic dermatitis", "dermatitis", "eczema", "eccema")),
    ("ADHD/TDAH", ("adhd", "tdah", "attention deficit", "hyperkinetic")),
    ("Autismo/TEA", ("autism", "autistic", "asd", "tea", "espectro autista")),
    ("Obesidad", ("obes", "overweight", "body mass index", "bmi", "sobrepeso")),
    ("Ansiedad", ("anxiety", "anxious", "social anxiety", "generalized anxiety")),
]

RESP_TOPICS = {"Bronquiolitis/RSV", "Asma/Sibilancias", "IVRS/Resfriado"}
NEURO_TOPICS = {"ADHD/TDAH", "Autismo/TEA", "Ansiedad"}
DIGESTIVE_DERM_TOPICS = {"Gastroenteritis", "Dermatitis atopica"}

ACTION_WORDS = (
    "guideline",
    "practice guideline",
    "randomized",
    "clinical trial",
    "meta-analysis",
    "systematic review",
    "efficacy",
    "effectiveness",
    "treatment",
    "management",
    "hospitalization",
)

LOW_APPLICABILITY_WORDS = (
    "gene expression",
    "genome",
    "microstructure",
    "post-hoc",
    "bioequivalence",
    "phase i",
    "phase 1",
    "pilot study",
    "feasibility",
)

EFFECT_WORDS = (
    "reduction",
    "improvement",
    "risk",
    "control",
    "hospitalization",
    "mortality",
    "odds ratio",
    "risk ratio",
    "confidence interval",
    "placebo",
    "double-blind",
)

HIGH_SIGNAL_JOURNALS = (
    "cochrane",
    "bmj",
    "jama",
    "lancet",
    "new england journal",
    "pediatrics",
)

STUDY_PROTOCOL_WORDS = ("protocol", "pilot", "feasibility")

MONTH_MAP = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}


@dataclass
class PaperRecord:
    pmid: str
    title: str
    journal: str
    pubdate_raw: str
    pubdate_iso: str
    doi: str
    pmc: str
    pubmed_url: str
    doi_url: str
    pmc_pdf_url: str
    in_query_a: int
    in_query_b: int
    study_type: str
    topic: str
    score_applicability: int
    score_effect: int
    score_robustness: int
    score_novelty: int
    score_total: int
    clinical_question: str
    key_finding: str
    main_limitation: str
    tomorrow_change: str


def chunks(items: Sequence[str], size: int) -> Iterator[List[str]]:
    for i in range(0, len(items), size):
        yield list(items[i : i + size])


def clamp(value: int, low: int, high: int) -> int:
    return max(low, min(value, high))


def date_range_block(days: int) -> str:
    start = (dt.date.today() - dt.timedelta(days=days)).strftime("%Y/%m/%d")
    return f'("{start}"[dp] : "3000"[dp])'


def build_query(evidence_block: str, days: int) -> str:
    query = (
        f"{PEDIATRIC_BASE} AND ({date_range_block(days)}) "
        f"AND {TOPIC_BLOCK} AND {evidence_block} "
        f"{GEO_EXCLUSION_BLOCK} "
        f"{NOISE_EXCLUSION_BLOCKS[0]} {NOISE_EXCLUSION_BLOCKS[1]} {NOISE_EXCLUSION_BLOCKS[2]}"
    )
    return " ".join(query.split())


def eutils_post_json(endpoint: str, params: Dict[str, str]) -> Dict:
    data = urllib.parse.urlencode(params).encode("utf-8")
    request = urllib.request.Request(
        f"{EUTILS_BASE}/{endpoint}.fcgi",
        data=data,
        headers={"User-Agent": "aepap-ultimo-mes-pipeline/1.0"},
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def eutils_post_text(endpoint: str, params: Dict[str, str]) -> str:
    data = urllib.parse.urlencode(params).encode("utf-8")
    request = urllib.request.Request(
        f"{EUTILS_BASE}/{endpoint}.fcgi",
        data=data,
        headers={"User-Agent": "aepap-ultimo-mes-pipeline/1.0"},
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read().decode("utf-8")


def esearch_all_pmids(term: str) -> Tuple[List[str], int]:
    retmax = 200
    retstart = 0
    all_ids: List[str] = []
    total_count = 0

    while True:
        payload = eutils_post_json(
            "esearch",
            {
                "db": "pubmed",
                "retmode": "json",
                "retmax": str(retmax),
                "retstart": str(retstart),
                "sort": "pub+date",
                "term": term,
            },
        )
        es = payload.get("esearchresult", {})
        count = int(es.get("count", "0"))
        if retstart == 0:
            total_count = count

        idlist = es.get("idlist", [])
        if not idlist:
            break

        all_ids.extend(idlist)
        retstart += retmax
        if retstart >= count:
            break

    return all_ids, total_count


def esummary_by_pmid(pmids: Sequence[str]) -> Dict[str, Dict]:
    result: Dict[str, Dict] = {}
    for batch in chunks(list(pmids), 200):
        payload = eutils_post_json(
            "esummary",
            {"db": "pubmed", "retmode": "json", "id": ",".join(batch)},
        )
        summary = payload.get("result", {})
        for pmid in batch:
            if pmid in summary:
                result[pmid] = summary[pmid]
    return result


def efetch_abstracts(pmids: Sequence[str]) -> Dict[str, str]:
    abstracts: Dict[str, str] = {}
    for batch in chunks(list(pmids), 100):
        xml_text = eutils_post_text(
            "efetch",
            {"db": "pubmed", "retmode": "xml", "id": ",".join(batch)},
        )
        root = ET.fromstring(xml_text)

        for article in root.findall(".//PubmedArticle"):
            pmid = (article.findtext(".//MedlineCitation/PMID") or "").strip()
            if not pmid:
                continue

            parts: List[str] = []
            for node in article.findall(".//Abstract/AbstractText"):
                text = " ".join("".join(node.itertext()).split())
                if not text:
                    continue
                label = (node.attrib.get("Label") or "").strip()
                if label:
                    parts.append(f"{label}: {text}")
                else:
                    parts.append(text)
            abstracts[pmid] = " ".join(parts)
    return abstracts


def extract_article_id(summary_item: Dict, idtype: str) -> str:
    for article_id in summary_item.get("articleids", []) or []:
        if (article_id.get("idtype") or "").lower() == idtype.lower():
            return (article_id.get("value") or "").strip()
    return ""


def parse_pubdate_to_iso(raw_date: str) -> str:
    text = (raw_date or "").strip()
    if not text:
        return ""

    # Primer patron: YYYY Mon DD
    match = re.search(r"(\d{4})\s+([A-Za-z]{3,9})\s+(\d{1,2})", text)
    if match:
        year = int(match.group(1))
        month = MONTH_MAP.get(match.group(2).lower()[:3], 1)
        day = int(match.group(3))
        day = min(day, calendar.monthrange(year, month)[1])
        return dt.date(year, month, day).isoformat()

    # Segundo patron: YYYY Mon
    match = re.search(r"(\d{4})\s+([A-Za-z]{3,9})", text)
    if match:
        year = int(match.group(1))
        month = MONTH_MAP.get(match.group(2).lower()[:3], 1)
        return dt.date(year, month, 15).isoformat()

    # Tercer patron: YYYY
    match = re.search(r"(\d{4})", text)
    if match:
        return dt.date(int(match.group(1)), 7, 1).isoformat()

    return ""


def classify_study_type(title: str, pubtypes: Sequence[str]) -> str:
    title_l = title.lower()
    pubtypes_l = " ".join((pubtypes or [])).lower()

    if "guideline" in pubtypes_l or "practice guideline" in pubtypes_l or "guideline" in title_l:
        return "Guideline"
    if "meta-analysis" in pubtypes_l or "systematic review" in pubtypes_l or "systematic review" in title_l or "meta-analysis" in title_l:
        return "SR/MA"
    if "randomized controlled trial" in pubtypes_l or "clinical trial" in pubtypes_l or "randomized" in title_l:
        return "RCT/CT"
    return "Other"


def classify_topic(title_text: str, abstract_text: str) -> str:
    title_l = title_text.lower()
    for topic, keywords in TOPIC_RULES:
        if any(keyword in title_l for keyword in keywords):
            return topic

    abstract_l = abstract_text.lower()
    for topic, keywords in TOPIC_RULES:
        if any(keyword in abstract_l for keyword in keywords):
            return topic
    return "Other"


def score_applicability(text: str, topic: str, study_type: str) -> int:
    score = 1
    if topic != "Other":
        score += 1
    if study_type in {"SR/MA", "RCT/CT", "Guideline"}:
        score += 1
    if any(word in text for word in ACTION_WORDS):
        score += 1
    if any(word in text for word in LOW_APPLICABILITY_WORDS):
        score -= 1
    return clamp(score, 0, 4)


def score_effect(text: str, study_type: str, journal: str) -> int:
    score = 0
    if study_type in {"SR/MA", "RCT/CT"}:
        score += 1
    if any(word in text for word in EFFECT_WORDS):
        score += 1
    if any(word in journal for word in HIGH_SIGNAL_JOURNALS):
        score += 1
    if any(word in text for word in STUDY_PROTOCOL_WORDS):
        score -= 1
    return clamp(score, 0, 3)


def score_robustness(study_type: str, text: str) -> int:
    if study_type in {"SR/MA", "Guideline"}:
        score = 2
    elif study_type == "RCT/CT":
        score = 1
    else:
        score = 0
    if any(word in text for word in STUDY_PROTOCOL_WORDS):
        score -= 1
    return clamp(score, 0, 2)


def score_novelty(pubdate_iso: str, today: dt.date) -> int:
    if not pubdate_iso:
        return 0
    try:
        pubdate = dt.date.fromisoformat(pubdate_iso)
    except ValueError:
        return 0
    days_delta = (today - pubdate).days
    return 1 if 0 <= days_delta <= 14 else 0


def clinical_question_for_topic(topic: str) -> str:
    mapping = {
        "Bronquiolitis/RSV": "Que cambia en soporte respiratorio y eventos clinicos en lactantes esta temporada?",
        "Asma/Sibilancias": "Hay intervenciones o biomarcadores que mejoren decisiones en asma pediatrica?",
        "IVRS/Resfriado": "Que medidas reducen sintomas, complicaciones o uso de recursos en IVRS?",
        "Otitis media": "Que evidencia reciente modifica manejo de OMA/OME en consulta?",
        "Gastroenteritis": "Que intervenciones previenen deshidratacion, ingreso o complicaciones?",
        "Dermatitis atopica": "Que terapias aportan mejor balance eficacia-seguridad en AP?",
        "ADHD/TDAH": "Que intervenciones mejoran sintomas nucleares y funcionalidad escolar/familiar?",
        "Autismo/TEA": "Que estrategias muestran beneficio funcional real en TEA?",
        "Obesidad": "Que programas o intervenciones consiguen cambios clinicamente relevantes?",
        "Ansiedad": "Que abordajes mejoran sintomas y funcionalidad en ninos/adolescentes?",
    }
    return mapping.get(topic, "Que aporta este estudio para la toma de decisiones en AP pediatrica?")


def tomorrow_change_for_topic(topic: str) -> str:
    mapping = {
        "Bronquiolitis/RSV": "Actualizar mensaje a familias y criterios de seguimiento respiratorio.",
        "Asma/Sibilancias": "Ajustar control y plan escrito segun nueva evidencia.",
        "IVRS/Resfriado": "Refinar consejo clinico y seguridad de manejo domiciliario.",
        "Otitis media": "Revisar decision antibiotica y ventanas de observacion.",
        "Gastroenteritis": "Reforzar plan de hidratacion y signos de alarma.",
        "Dermatitis atopica": "Optimizar escalado terapeutico y educacion familiar.",
        "ADHD/TDAH": "Priorizar intervenciones con mayor impacto funcional.",
        "Autismo/TEA": "Orientar objetivos realistas y derivacion temprana.",
        "Obesidad": "Afinar intervenciones de estilo de vida con metas medibles.",
        "Ansiedad": "Actualizar recomendaciones psicoterapeuticas de primera linea.",
    }
    return mapping.get(topic, "Aplicar el hallazgo en la decision compartida y revisar protocolos locales.")


def limitation_from_title(title: str) -> str:
    title_l = title.lower()
    if "post-hoc" in title_l:
        return "Analisis post-hoc: riesgo de inferencia exploratoria."
    if "pilot" in title_l or "feasibility" in title_l:
        return "Estudio piloto/viabilidad: validez externa limitada."
    if "single-center" in title_l:
        return "Unicentrico: generalizacion limitada."
    if "protocol" in title_l:
        return "Es protocolo, sin resultados clinicos definitivos."
    return "Revisar heterogeneidad, riesgo de sesgo y aplicabilidad local."


def pick_top_records(
    records: Sequence[PaperRecord],
    top_n: int,
    min_topics: int,
    max_per_topic: int,
) -> List[PaperRecord]:
    ranked = sorted(records, key=lambda r: (r.score_total, r.pubdate_iso, r.pmid), reverse=True)
    if not ranked:
        return []

    topic_best: Dict[str, PaperRecord] = {}
    for rec in ranked:
        if rec.topic not in topic_best:
            topic_best[rec.topic] = rec

    initial_topics = [t for t in topic_best if t != "Other"]
    initial_topics.sort(key=lambda t: (topic_best[t].score_total, topic_best[t].pubdate_iso), reverse=True)

    selected: List[PaperRecord] = []
    selected_pmids = set()
    topic_counts: Dict[str, int] = {}

    for topic in initial_topics[:min_topics]:
        rec = topic_best[topic]
        selected.append(rec)
        selected_pmids.add(rec.pmid)
        topic_counts[topic] = 1
        if len(selected) >= top_n:
            return selected

    for rec in ranked:
        if rec.pmid in selected_pmids:
            continue
        count = topic_counts.get(rec.topic, 0)
        if count >= max_per_topic:
            continue
        selected.append(rec)
        selected_pmids.add(rec.pmid)
        topic_counts[rec.topic] = count + 1
        if len(selected) >= top_n:
            break

    return selected


def summarize_acceptance(selected: Sequence[PaperRecord]) -> Dict[str, object]:
    n = len(selected)
    if n == 0:
        return {
            "selected_count": 0,
            "aplicabilidad_pct": 0.0,
            "protocol_count": 0,
            "has_respiratory": False,
            "has_neuro_mental": False,
            "has_digestive_or_derm": False,
            "distinct_topics": 0,
            "passes_aplicabilidad_70pct": False,
            "passes_protocol_zero": True,
        }

    applicable = [r for r in selected if r.score_applicability >= 3]
    protocol_count = sum(1 for r in selected if "protocol" in r.title.lower())
    topics = {r.topic for r in selected}
    has_resp = any(r.topic in RESP_TOPICS for r in selected)
    has_neuro = any(r.topic in NEURO_TOPICS for r in selected)
    has_digestive_derm = any(r.topic in DIGESTIVE_DERM_TOPICS for r in selected)
    aplicabilidad_pct = round((len(applicable) / n) * 100, 1)

    return {
        "selected_count": n,
        "aplicabilidad_pct": aplicabilidad_pct,
        "protocol_count": protocol_count,
        "has_respiratory": has_resp,
        "has_neuro_mental": has_neuro,
        "has_digestive_or_derm": has_digestive_derm,
        "distinct_topics": len(topics),
        "passes_aplicabilidad_70pct": aplicabilidad_pct >= 70.0,
        "passes_protocol_zero": protocol_count == 0,
    }


def write_csv(path: Path, rows: Sequence[Dict[str, object]], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def maybe_download_pmc_pdf(pmc_pdf_url: str, destination: Path) -> str:
    if not pmc_pdf_url:
        return ""
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(
        pmc_pdf_url,
        headers={"User-Agent": "aepap-ultimo-mes-pipeline/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            data = response.read()
        destination.write_bytes(data)
        return str(destination)
    except Exception:
        return ""


def build_records(
    pmids_a: Sequence[str],
    pmids_b: Sequence[str],
    summary_map: Dict[str, Dict],
    abstract_map: Dict[str, str],
) -> List[PaperRecord]:
    all_pmids = sorted(set(pmids_a) | set(pmids_b))
    pmids_a_set = set(pmids_a)
    pmids_b_set = set(pmids_b)
    today = dt.date.today()

    records: List[PaperRecord] = []
    for pmid in all_pmids:
        item = summary_map.get(pmid, {})
        title = (item.get("title") or "").replace("\n", " ").strip()
        journal = (item.get("fulljournalname") or item.get("source") or "").strip()
        pubdate_raw = (item.get("pubdate") or "").strip()
        pubdate_iso = parse_pubdate_to_iso(pubdate_raw)

        doi = extract_article_id(item, "doi")
        pmc = extract_article_id(item, "pmc")
        pubtypes = item.get("pubtype") or []
        abstract = abstract_map.get(pmid, "")
        text_blob = f"{title} {abstract}".lower()

        study_type = classify_study_type(title, pubtypes)
        topic = classify_topic(title, abstract)

        app_score = score_applicability(text_blob, topic, study_type)
        effect_score = score_effect(text_blob, study_type, journal.lower())
        robust_score = score_robustness(study_type, text_blob)
        novelty_score = score_novelty(pubdate_iso, today)
        total_score = app_score + effect_score + robust_score + novelty_score

        doi_url = f"https://doi.org/{doi}" if doi else ""
        pmc_pdf_url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/pdf/" if pmc else ""

        record = PaperRecord(
            pmid=pmid,
            title=title,
            journal=journal,
            pubdate_raw=pubdate_raw,
            pubdate_iso=pubdate_iso,
            doi=doi,
            pmc=pmc,
            pubmed_url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            doi_url=doi_url,
            pmc_pdf_url=pmc_pdf_url,
            in_query_a=1 if pmid in pmids_a_set else 0,
            in_query_b=1 if pmid in pmids_b_set else 0,
            study_type=study_type,
            topic=topic,
            score_applicability=app_score,
            score_effect=effect_score,
            score_robustness=robust_score,
            score_novelty=novelty_score,
            score_total=total_score,
            clinical_question=clinical_question_for_topic(topic),
            key_finding=title,
            main_limitation=limitation_from_title(title),
            tomorrow_change=tomorrow_change_for_topic(topic),
        )
        records.append(record)

    records.sort(key=lambda r: (r.score_total, r.pubdate_iso, r.pmid), reverse=True)
    return records


def write_queries_file(path: Path, query_a: str, query_b: str, days: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = (
        "# Pipeline mensual PubMed - Ultimo mes en Pediatria\n\n"
        f"Fecha de ejecucion: {dt.date.today().isoformat()}\n"
        f"Ventana temporal: ultimos {days} dias\n\n"
        "## Query A (solo revisiones/meta)\n\n"
        f"{query_a}\n\n"
        "## Query B (mixto alto impacto)\n\n"
        f"{query_b}\n"
    )
    path.write_text(content, encoding="utf-8")


def write_notebooklm_markdown(path: Path, selected: Sequence[PaperRecord], metadata: Dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# NotebookLM - Ultimo mes en Pediatria",
        "",
        f"- Fecha: {dt.date.today().isoformat()}",
        f"- Query A: {metadata['count_query_a']} resultados",
        f"- Query B: {metadata['count_query_b']} resultados",
        f"- Dedupe: {metadata['count_dedup']} PMIDs",
        f"- Seleccion final: {metadata['count_selected']} papers",
        "",
        "## Tabla de trabajo",
        "",
        "| PMID | Tema | Tipo | Score | Pregunta clinica | Hallazgo clave | Limitacion | Que cambia manana |",
        "|---|---|---|---:|---|---|---|---|",
    ]
    for rec in selected:
        title_short = rec.key_finding.replace("|", " ").strip()
        if len(title_short) > 130:
            title_short = title_short[:127] + "..."
        lines.append(
            "| {pmid} | {topic} | {stype} | {score} | {q} | {finding} | {lim} | {chg} |".format(
                pmid=rec.pmid,
                topic=rec.topic,
                stype=rec.study_type,
                score=rec.score_total,
                q=rec.clinical_question.replace("|", " "),
                finding=title_short,
                lim=rec.main_limitation.replace("|", " "),
                chg=rec.tomorrow_change.replace("|", " "),
            )
        )

    lines.extend(
        [
            "",
            "## Instruccion sugerida para NotebookLM",
            "",
            "Genera un resumen estilo podcast clinico para pediatria de AP en 6-8 minutos.",
            "Incluye 3 mensajes accionables, 3 limites metodologicos y 3 cambios inmediatos de practica.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Pipeline mensual PubMed para AEPap + NotebookLM.")
    parser.add_argument("--days", type=int, default=30, help="Ventana temporal en dias (default: 30).")
    parser.add_argument("--top-n", type=int, default=12, help="Numero maximo de articulos finales (default: 12).")
    parser.add_argument("--min-topics", type=int, default=5, help="Minimo de areas tematicas en la seleccion.")
    parser.add_argument("--max-per-topic", type=int, default=3, help="Maximo de articulos por tema.")
    parser.add_argument(
        "--output-dir",
        default="docs/AEPAP-2026/ultimo_mes_output",
        help="Directorio de salida para artefactos.",
    )
    parser.add_argument(
        "--download-pmc-pdf",
        action="store_true",
        help="Descarga PDFs cuando exista enlace PMC PDF.",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    query_a = build_query(REVIEW_BLOCK, args.days)
    query_b = build_query(MIXED_BLOCK, args.days)

    pmids_a, count_a = esearch_all_pmids(query_a)
    pmids_b, count_b = esearch_all_pmids(query_b)
    pmids_union = sorted(set(pmids_a) | set(pmids_b))

    summary_map = esummary_by_pmid(pmids_union)
    abstract_map = efetch_abstracts(pmids_union)

    records = build_records(pmids_a, pmids_b, summary_map, abstract_map)
    top_n = max(8, min(args.top_n, 12))
    selected = pick_top_records(records, top_n=top_n, min_topics=args.min_topics, max_per_topic=args.max_per_topic)

    # Export CSV completo.
    all_rows = [asdict(rec) for rec in records]
    all_fields = list(all_rows[0].keys()) if all_rows else list(PaperRecord.__annotations__.keys())
    write_csv(output_dir / "pubmed_all_records.csv", all_rows, all_fields)

    # Export top seleccionado.
    selected_rows = [asdict(rec) for rec in selected]
    selected_fields = list(selected_rows[0].keys()) if selected_rows else all_fields
    write_csv(output_dir / "top_selected.csv", selected_rows, selected_fields)

    # Manifest para NotebookLM (enlaces + opcional PDF).
    manifest_rows: List[Dict[str, object]] = []
    for rec in selected:
        pdf_path = ""
        if args.download_pmc_pdf and rec.pmc_pdf_url:
            pdf_path = maybe_download_pmc_pdf(rec.pmc_pdf_url, output_dir / "pdfs" / f"{rec.pmid}.pdf")
        manifest_rows.append(
            {
                "pmid": rec.pmid,
                "title": rec.title,
                "topic": rec.topic,
                "study_type": rec.study_type,
                "score_total": rec.score_total,
                "pubmed_url": rec.pubmed_url,
                "doi_url": rec.doi_url,
                "pmc_pdf_url": rec.pmc_pdf_url,
                "pdf_downloaded_path": pdf_path,
            }
        )

    write_csv(
        output_dir / "notebooklm_manifest.csv",
        manifest_rows,
        ["pmid", "title", "topic", "study_type", "score_total", "pubmed_url", "doi_url", "pmc_pdf_url", "pdf_downloaded_path"],
    )

    # PMIDs para chequeo manual aleatorio.
    rng = random.Random(42)
    sample_pmids = [r.pmid for r in rng.sample(records, k=min(10, len(records)))] if records else []
    (output_dir / "pmids_manual_check_10.txt").write_text("\n".join(sample_pmids) + ("\n" if sample_pmids else ""), encoding="utf-8")

    acceptance = summarize_acceptance(selected)
    metadata = {
        "run_date": dt.date.today().isoformat(),
        "days_window": args.days,
        "count_query_a": count_a,
        "count_query_b": count_b,
        "count_dedup": len(pmids_union),
        "count_selected": len(selected),
        "query_a": query_a,
        "query_b": query_b,
        "acceptance": acceptance,
    }
    (output_dir / "run_metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    write_queries_file(output_dir / "queries_pubmed.txt", query_a, query_b, args.days)
    write_notebooklm_markdown(output_dir / "notebooklm_briefing.md", selected, metadata)

    print(f"Query A count: {count_a}")
    print(f"Query B count: {count_b}")
    print(f"Union dedupe: {len(pmids_union)}")
    print(f"Selected top: {len(selected)}")
    print(f"Output dir: {output_dir}")
    print(
        "Acceptance snapshot: "
        f"aplicabilidad={acceptance['aplicabilidad_pct']}% "
        f"protocol={acceptance['protocol_count']} "
        f"resp={acceptance['has_respiratory']} "
        f"neuro={acceptance['has_neuro_mental']} "
        f"digestive_or_derm={acceptance['has_digestive_or_derm']}"
    )

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("Interrupted.", file=sys.stderr)
        raise SystemExit(130)
