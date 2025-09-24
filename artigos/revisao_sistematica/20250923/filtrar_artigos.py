#!/usr/bin/env python3
import re
from pathlib import Path

RIS_TAG_RE = re.compile(r"^([A-Z0-9]{2})  - (.*)$")


def parse_ris(path: Path):
    records = []
    current = None
    current_tag = None
    with path.open('r', encoding='utf-8', errors='ignore') as f:
        for raw in f:
            line = raw.rstrip('\n')
            m = RIS_TAG_RE.match(line)
            if m:
                tag, val = m.group(1), m.group(2).strip()
                if tag == 'TY':
                    # start new record
                    if current:
                        records.append(current)
                    current = {}
                if current is None:
                    # ignore headers before first TY
                    continue
                current.setdefault(tag, [])
                current[tag].append(val)
                current_tag = tag
            else:
                if current is None:
                    continue
                if line.strip() == '':
                    continue
                # continuation of previous tag value
                if current_tag is not None:
                    current[current_tag][-1] += ' ' + line.strip()
        # flush last
        if current:
            records.append(current)
    return records


def get_text(rec, tags):
    vals = []
    for t in tags:
        for v in rec.get(t, []):
            if v:
                vals.append(v)
    return ' '.join(vals)


def contains_any(text, terms):
    t = text.lower()
    return any(term in t for term in terms)


def filter_records(records):
    pbl_terms = [
        'project-based learning', 'project based learning', 'pbl', 'capstone', 'project course'
    ]
    assessment_terms = [
        'assessment', 'evaluation', 'grading', 'assess', 'evaluate', 'rubric', 'feedback'
    ]
    challenge_terms = [
        'challenge', 'difficulty', 'problem', 'issue', 'barrier', 'constraint', 'limitation'
    ]
    instrument_terms = [
        'instrument', 'tool', 'method', 'rubric', 'framework', 'technology', 'dashboard', 'analytics', 'system', 'platform',
        'criterion', 'criteria', 'score', 'scoring', 'grade', 'grading', 'portfolio', 'checklist', 'benchmark'
    ]
    process_terms = [
        'process', 'formative', 'ongoing', 'continuous', 'telemetry', 'monitor', 'collaborative', 'collaboration', 'teamwork', 'peer assessment', 'self-assessment', 'peer-assessment'
    ]
    education_terms = [
        'higher education', 'engineering education', 'software engineering', 'curriculum', 'course', 'program', 'undergraduate', 'university', 'students', 'classroom', 'teaching', 'education'
    ]
    domain_terms = [
        'engineering', 'software engineering', 'computer', 'computing', 'electrical', 'mechanical', 'civil', 'chemical',
        'bioprocess', 'surveying', 'stem', 'industrial', 'manufactur', 'automation', 'fpga', 'robot', 'mechatronic'
    ]
    empirical_terms = [
        'case study', 'experiment', 'evaluation', 'survey', 'interview', 'mixed methods', 'participants', 'sample', 'dataset', 'pilot', 'study', 'observ'
    ]
    exclusion_terms = [
        'final exam', 'final product', 'summative assessment', 'end-of-course exam', 'standardized test',
        'systematic review', 'literature review', 'meta-analysis'
    ]

    included = []
    for rec in records:
        text = ' '.join([
            get_text(rec, ['TI']),
            get_text(rec, ['AB']),
            get_text(rec, ['KW', 'DE', 'ID'])
        ]).strip()
        if not text:
            continue

        has_pbl = contains_any(text, pbl_terms)
        has_assess = contains_any(text, assessment_terms)
        has_focus = contains_any(text, challenge_terms) or contains_any(text, instrument_terms) or contains_any(text, process_terms)
        in_edu = contains_any(text, education_terms)
        is_empirical = contains_any(text, empirical_terms)
        excluded_hint = contains_any(text, exclusion_terms)
        domain_match = contains_any(text, domain_terms)

        # Exclude Problem-Based Learning (PBL) when not about Project-Based Learning
        txt_lower = text.lower()
        if ('problem-based learning' in txt_lower or 'problem based learning' in txt_lower) and ('project-based learning' not in txt_lower and 'project based learning' not in txt_lower):
            continue

        # Expanded inclusion: PBL context + at least one of (assessment, focus)
        # Keep exclusion hints to avoid purely summative-only focus on final products.
        if has_pbl and (has_assess or has_focus) and domain_match and not excluded_hint:
            included.append(rec)

    return included


def main():
    ris_path = Path('20250923/consolidado_wos.ris')
    out_path = Path('20250923/titulos_filtrados.txt')
    if not ris_path.exists():
        raise SystemExit('Arquivo RIS não encontrado: %s' % ris_path)
    records = parse_ris(ris_path)
    included = filter_records(records)
    titles = [get_text(r, ['TI']).strip() for r in included if get_text(r, ['TI']).strip()]
    # Deduplicate while preserving order
    seen = set()
    titles_unique = []
    for t in titles:
        k = t.lower()
        if k in seen:
            continue
        seen.add(k)
        titles_unique.append(t)

    out_path.write_text('\n'.join(titles_unique) + ('\n' if titles_unique else ''), encoding='utf-8')
    print(f'Incluídos: {len(titles_unique)}')
    for t in titles_unique:
        print('- ' + t)


if __name__ == '__main__':
    main()
