#!/usr/bin/env python3
"""
Second-stage strict filtering for SLR following Kitchenham guidelines.
Input: consolidated RIS with previously relevant PBL assessment articles.
Output: ranked RIS and CSV with rationale, targeting ~25-30 top studies.

Scoring dimensions (aligned to criterios_filtragem_aproximacao.md):
- PBL + assessment (precondition)
- Process-based evaluation
- Collaboration/individual contribution
- Transversal competencies
- Formative feedback/continuous monitoring
- Scalability/objectivity/standardization/automation
- Instrument/technology described
- Empirical validation (study, participants, metrics)
- Educational context clarity (HE/K-12/classroom)

Generates:
- strict_selection.csv: per-article flags, score, reasons
- strict_selection_top30.ris: top 30 articles
- strict_selection_full_ranked.ris: all ranked by score
"""

from __future__ import annotations

import re
import os
import csv
from dataclasses import dataclass, field
from typing import List, Dict, Any


RIS_END = "ER  -"


def parse_ris(path: str) -> List[Dict[str, Any]]:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    records_raw = [r.strip() for r in text.split(RIS_END) if r.strip()]
    records: List[Dict[str, Any]] = []
    for record in records_raw:
        art: Dict[str, Any] = {}
        for line in record.splitlines():
            line = line.strip()
            if not line:
                continue
            m = re.match(r'^([A-Z]{2})\s*-\s*(.*)$', line)
            if not m:
                continue
            k, v = m.group(1), m.group(2).strip()
            if k in art:
                if isinstance(art[k], list):
                    art[k].append(v)
                else:
                    art[k] = [art[k], v]
            else:
                art[k] = v
        if art:
            records.append(art)
    return records


def field_text(art: Dict[str, Any]) -> str:
    parts: List[str] = []
    for k in ('TI', 'AB', 'KW', 'T2', 'C3'):
        if k in art:
            v = art[k]
            parts.append(" ".join(v) if isinstance(v, list) else str(v))
    return " ".join(parts).lower()


def fmt_str(v: Any) -> str:
    if isinstance(v, list):
        return "; ".join(v)
    return str(v)


def ris_format(art: Dict[str, Any]) -> str:
    order = ['TY','AU','TI','T2','AB','KW','PY','DA','VL','IS','SP','EP','SN','DO','UR','AN','LA']
    lines: List[str] = []
    for k in order:
        if k in art:
            v = art[k]
            if isinstance(v, list):
                for vi in v:
                    lines.append(f"{k}  - {vi}")
            else:
                lines.append(f"{k}  - {v}")
    # include remaining
    for k, v in art.items():
        if k in order:
            continue
        if isinstance(v, list):
            for vi in v:
                lines.append(f"{k}  - {vi}")
        else:
            lines.append(f"{k}  - {v}")
    lines.append(RIS_END)
    lines.append("")
    return "\n".join(lines)


@dataclass
class Flags:
    has_pbl: bool = False
    has_assessment: bool = False
    process: bool = False
    collaboration: bool = False
    competencies: bool = False
    feedback: bool = False
    scalability_objectivity: bool = False
    instrument_tech: bool = False
    empirical_validation: bool = False
    edu_context: bool = False
    reasons: List[str] = field(default_factory=list)

    def score(self) -> int:
        if not (self.has_pbl and self.has_assessment):
            return 0
        s = 0
        # Core dimensions weigh 2
        for dim, name in [
            (self.process, 'process'),
            (self.collaboration, 'collaboration'),
            (self.competencies, 'competencies'),
            (self.feedback, 'feedback'),
            (self.scalability_objectivity, 'scalability_objectivity'),
            (self.empirical_validation, 'empirical_validation'),
        ]:
            if dim:
                s += 2
        # Supportive dimensions weigh 1
        if self.instrument_tech:
            s += 1
        if self.edu_context:
            s += 1
        # Small bonus if covers 4+ core dims
        core_count = sum([self.process, self.collaboration, self.competencies, self.feedback, self.scalability_objectivity, self.empirical_validation])
        if core_count >= 4:
            s += 1
        return s


STRICT_PROJECT_ONLY = True  # require explicit PjBL/PBL in title/keywords when True
INCLUDE_PROBLEM_BASED = True  # include Problem-Based Learning as eligible
YEAR_CUTOFF = 2018  # minimum publication year
EXCLUDE_REVIEWS = True  # exclude narrative/systematic reviews from selection


def analyze_flags(text: str) -> Flags:
    f = Flags()
    # Preconditions
    if STRICT_PROJECT_ONLY:
        pj_terms = ['project-based learning', 'project based learning', 'project-oriented learning', 'project oriented learning']
        pb_terms = ['problem-based learning', 'problem based learning'] if INCLUDE_PROBLEM_BASED else []
        if any(t in text for t in pj_terms + pb_terms):
            f.has_pbl = True
    else:
        if any(t in text for t in ['project-based learning', 'project based learning', 'project-oriented learning', 'project oriented learning', ' pbl ', '(pbl)', 'problem-based learning', 'problem based learning']):
            f.has_pbl = True
    if any(t in text for t in ['assessment', 'evaluation', 'grading', 'rubric', 'feedback', 'scoring', 'criterion', 'criteria']):
        f.has_assessment = True

    # Process
    if any(t in text for t in ['process', 'processual', 'ongoing', 'continuous', 'monitor', 'progress tracking', 'process-based', 'workflow']):
        f.process = True
        f.reasons.append('process')

    # Collaboration / individual contribution
    if any(t in text for t in ['team', 'group', 'collaborat', 'peer', 'contribution', 'free-rider', 'individual contribution', 'division of work']):
        f.collaboration = True
        f.reasons.append('collaboration')

    # Transversal competencies
    if any(t in text for t in ['competenc', 'skill', 'critical thinking', 'creativity', 'communication', 'self-regulation', 'soft skill', '21st-century']):
        f.competencies = True
        f.reasons.append('competencies')

    # Formative feedback / continuous
    if any(t in text for t in ['feedback', 'formative', 'real-time', 'dashboard', 'intervention', 'reflect', 'reflection']):
        f.feedback = True
        f.reasons.append('feedback')

    # Scalability / objectivity / standardization
    if any(t in text for t in ['scalab', 'objective', 'automated', 'automation', 'system', 'platform', 'software', 'standardized', 'rubric', 'reliab', 'validit', 'inter-rater', 'cronbach', 'kappa']):
        f.scalability_objectivity = True
        f.reasons.append('scalability/objectivity')

    # Instrument or technology
    if any(t in text for t in ['instrument', 'tool', 'framework', 'model', 'questionnaire', 'survey', 'protocol', 'application', 'app', 'ide plugin']):
        f.instrument_tech = True
        f.reasons.append('instrument/tech')

    # Empirical validation
    if any(t in text for t in ['experiment', 'case study', 'quasi-experiment', 'participants', 'students', 'sample', 'evaluation study', 'validation', 'pilot study', 'empirical', 'study with']):
        f.empirical_validation = True
        f.reasons.append('empirical')

    # Educational context
    if any(t in text for t in ['higher education', 'undergraduate', 'course', 'classroom', 'engineering education', 'computer science education', 'medical education', 'teacher education', 'secondary school', 'k-12', 'university']):
        f.edu_context = True
        f.reasons.append('edu context')

    return f


def main():
    base_dir = os.path.dirname(__file__)
    input_ris = os.path.join(base_dir, 'artigos_relevantes_pbl_avaliacao.ris')
    if not os.path.exists(input_ris):
        raise SystemExit(f"Input RIS not found: {input_ris}")

    records = parse_ris(input_ris)

    ranked: List[Dict[str, Any]] = []
    seen_keys = set()
    rows: List[List[str]] = []
    excluded_reviews: List[Dict[str, Any]] = []
    for art in records:
        text = field_text(art)
        ti_l = fmt_str(art.get('TI','')).lower()
        kw_l = fmt_str(art.get('KW','')).lower()

        # Year cutoff
        ysrc = art.get('PY') or art.get('DA') or ''
        m = re.search(r'\b(19|20)\d{2}\b', fmt_str(ysrc))
        year = int(m.group(0)) if m else 0
        if YEAR_CUTOFF and year < YEAR_CUTOFF:
            continue

        # Ensure PjBL or (if enabled) Problem-Based Learning in title/keywords
        if STRICT_PROJECT_ONLY:
            pj_toks = ['project-based learning', 'project based learning']
            pb_toks = ['problem-based learning', 'problem based learning'] if INCLUDE_PROBLEM_BASED else []
            if (not any(t in ti_l for t in pj_toks + pb_toks) and
                not any(t in kw_l for t in pj_toks + pb_toks)):
                continue

        # Restrict to higher education (heuristic) and avoid K-12
        he_terms = [
            'higher education','university','universities','college','undergraduate','postgraduate',
            'bachelor','master','graduate','tertiary','engineering education','medical education',
            'preservice teacher','pre-service teacher','pre-service teachers','preservice teachers',
            'teacher education','pre-service mathematics teachers','pre-service science teachers'
        ]
        k12_terms = [
            'k-12','k12','primary school','elementary','middle school','secondary school','high school',
            'secondary education','primary education','basic education'
        ]
        he_hit = any(t in text for t in he_terms) or any(t in ti_l for t in he_terms) or any(t in kw_l for t in he_terms)
        k12_hit = any(t in text for t in k12_terms) or any(t in ti_l for t in k12_terms) or any(t in kw_l for t in k12_terms)
        if not he_hit or k12_hit:
            continue

        # Exclude reviews if requested
        is_review = any(t in ti_l for t in [' review', 'systematic review', 'narrative review']) or \
                    any(t in kw_l for t in ['review', 'systematic review', 'narrative review'])
        if EXCLUDE_REVIEWS and is_review:
            excluded_reviews.append({'title': art.get('TI','N/A'), 'year': year, 'reason': 'revisão'})
            continue

        flags = analyze_flags(text)
        # Require preconditions
        if not (flags.has_pbl and flags.has_assessment):
            continue
        score = flags.score()
        title = art.get('TI', 'N/A')

        # Dedup key prefers AN; fallback to normalized title
        an = fmt_str(art.get('AN','')).strip()
        title_key = fmt_str(title).strip().lower()
        key = an or title_key
        if key in seen_keys:
            continue
        seen_keys.add(key)

        ranked.append({'score': score, 'flags': flags, 'art': art, 'year': year})
        rows.append([
            fmt_str(art.get('AN','')),
            year,
            fmt_str(title),
            score,
            int(flags.process),
            int(flags.collaboration),
            int(flags.competencies),
            int(flags.feedback),
            int(flags.scalability_objectivity),
            int(flags.instrument_tech),
            int(flags.empirical_validation),
            int(flags.edu_context),
            ", ".join(flags.reasons),
        ])

    # Sort by score desc, then by year desc (numeric)
    ranked.sort(key=lambda r: (r['score'], int(r['year'] or 0)), reverse=True)

    out_csv = os.path.join(base_dir, 'strict_selection.csv')
    with open(out_csv, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID','Year','Title','Score','Process','Collaboration','Competencies','Feedback','ScalabilityObjectivity','InstrumentTech','Empirical','EduContext','Reasons'])
        for row in rows:
            w.writerow(row)

    # Save full ranked RIS
    full_ris_path = os.path.join(base_dir, 'strict_selection_full_ranked.ris')
    with open(full_ris_path, 'w', encoding='utf-8') as f:
        for item in ranked:
            f.write(ris_format(item['art']))

    # Select top 25 with tie-handling: include up to 25; if >25 at same score, cap by 25
    top_n = 25
    top_items = ranked[:top_n]
    top_ris_path = os.path.join(base_dir, 'strict_selection_top25.ris')
    with open(top_ris_path, 'w', encoding='utf-8') as f:
        for item in top_items:
            f.write(ris_format(item['art']))

    # Also emit a simple summary list for quick inspection
    summary_path = os.path.join(base_dir, 'strict_selection_top25_summary.txt')
    with open(summary_path, 'w', encoding='utf-8') as f:
        for i, item in enumerate(top_items, 1):
            art = item['art']
            f.write(f"{i:02d}. [{item['year']}] {fmt_str(art.get('TI',''))}\n")
            f.write(f"    Venue: {fmt_str(art.get('T2',''))}\n")
            f.write(f"    Score: {item['score']} | Reasons: {', '.join(item['flags'].reasons)}\n")
            f.write(f"    ID: {fmt_str(art.get('AN',''))}\n\n")

    # Excluded list with reasons (Kitchenham doc): reviews + below top-25 cutoff
    excluded_report = os.path.join(base_dir, 'strict_selection_excluded_final.txt')
    with open(excluded_report, 'w', encoding='utf-8') as f:
        # reviews excluded
        for ex in excluded_reviews:
            f.write(f"- {ex['title']} ({ex['year']}) — Motivo: revisão\n")
        # below cutoff
        for item in ranked[top_n:]:
            t = fmt_str(item['art'].get('TI',''))
            y = item['year']
            f.write(f"- {t} ({y}) — Motivo: abaixo do corte Top-25 (score/ano)\n")

    print(f"Parsed records: {len(records)}")
    print(f"Ranked (with preconditions met): {len(ranked)}")
    print(f"Wrote: {out_csv}")
    print(f"Wrote: {full_ris_path}")
    print(f"Wrote: {top_ris_path}")
    print(f"Wrote: {summary_path}")
    print(f"Wrote: {excluded_report}")


if __name__ == '__main__':
    main()
