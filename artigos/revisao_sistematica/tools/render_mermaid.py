#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path
import os
import sys
import math

ROOT = Path(__file__).resolve().parents[1]
SRC_MD = ROOT / 'revisao_sistematica_tese.md'
BUILD_DIR = ROOT / 'build'
MM_DIR = BUILD_DIR / 'mermaid'
ASSETS_DIR = ROOT / 'assets'
OUT_MD = BUILD_DIR / 'revisao_sistematica_tese_rendered.md'


def extract_mermaid_blocks(text: str, img_prefix: str):
    blocks = []
    out_lines = []
    i = 0
    n = 0
    lines = text.splitlines()
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('```mermaid'):
            n += 1
            i += 1
            content = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                content.append(lines[i])
                i += 1
            # skip closing ```
            if i < len(lines) and lines[i].strip().startswith('```'):
                i += 1
            blocks.append((n, '\n'.join(content)))
            # placeholder for image (path relative to OUT_MD location)
            out_lines.append(f'![Gráfico Mermaid {n}]({img_prefix}/mermaid_{n}.svg)')
            # caption/source under each graphic
            out_lines.append('Fonte: Autor (2025).')
        else:
            out_lines.append(line)
            i += 1
    return blocks, '\n'.join(out_lines)


def ensure_dirs():
    BUILD_DIR.mkdir(exist_ok=True)
    MM_DIR.mkdir(exist_ok=True)
    ASSETS_DIR.mkdir(exist_ok=True)


def render_with_mmdc(blocks):
    rendered = {}
    for idx, content in blocks:
        mm_file = MM_DIR / f'{idx}.mmd'
        svg_file = ASSETS_DIR / f'mermaid_{idx}.svg'
        # If it's a pie chart, render as bar SVG instead of calling mmdc
        if content.lstrip().startswith('pie'):
            labels, values, title = parse_pie_to_series(content)
            svg = make_bar_svg(labels, values, title)
            svg_file.write_text(svg, encoding='utf-8')
        else:
            mm_file.write_text(content, encoding='utf-8')
            # Render via mermaid-cli (mmdc)
            cmd = [
                'npx', '-y', '@mermaid-js/mermaid-cli',
                '-i', str(mm_file),
                '-o', str(svg_file),
                '-b', 'transparent',
                '-t', 'neutral',
                '-V', '{"fontSize":"16px","fontFamily":"Arial","padding":12}'
            ]
            try:
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as e:
                print(f'Erro ao renderizar Mermaid {mm_file}: {e}', file=sys.stderr)
                raise
        rendered[idx] = svg_file
    return rendered


def parse_pie_to_series(content: str):
    title = ''
    labels = []
    values = []
    for line in content.splitlines():
        s = line.strip()
        if s.startswith('pie'):
            # try to capture title "..."
            m = re.search(r'title\s+"([^"]+)"', s)
            if m:
                title = m.group(1)
        else:
            m = re.match(r'"(.+?)"\s*:\s*([0-9]+)', s)
            if m:
                labels.append(m.group(1))
                values.append(int(m.group(2)))
    return labels, values, title


def make_bar_svg(labels, values, title=''):
    # Simple vertical bar chart SVG with larger fonts and margins to avoid overlap
    n = len(values)
    if n == 0:
        return '<svg xmlns="http://www.w3.org/2000/svg" width="600" height="80"></svg>'
    max_v = max(values)
    # layout parameters
    w_bar = 40
    gap = 24
    margin_left = 80
    margin_right = 40
    margin_top = 68
    margin_bottom = 90
    axis = 30
    w = margin_left + margin_right + n*w_bar + (n-1)*gap
    h = max(360, margin_top + 200 + margin_bottom)
    # plotting frame
    x0 = margin_left
    y0 = h - margin_bottom
    h_plot = y0 - margin_top
    # Build bars
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">']
    parts.append('<style>text{font-family:Arial, sans-serif; font-size:14px;} .lbl{font-size:13px;} .title{font-size:16px; font-weight:bold;}</style>')
    if title:
        parts.append(f'<text class="title" x="{w/2}" y="{max(24, margin_top-36)}" text-anchor="middle">{escape_xml(title)}</text>')
    # axes
    parts.append(f'<line x1="{x0}" y1="{y0}" x2="{w-margin_right}" y2="{y0}" stroke="#333"/>')
    parts.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{margin_top}" stroke="#333"/>')
    # ticks
    ticks = max(3, min(6, max_v))
    step = max_v / ticks if max_v else 1
    for i in range(ticks+1):
        v = step * i
        y = y0 - (0 if max_v == 0 else (v / max_v) * h_plot)
        parts.append(f'<line x1="{x0-5}" y1="{y}" x2="{x0}" y2="{y}" stroke="#333"/>')
        parts.append(f'<text x="{x0-10}" y="{y+5}" text-anchor="end">{int(round(v))}</text>')
    # bars
    for i, (lab, val) in enumerate(zip(labels, values)):
        x = x0 + i*(w_bar+gap)
        bh = 0 if max_v == 0 else (val/max_v)*h_plot
        y = y0 - bh
        parts.append(f'<rect x="{x}" y="{y}" width="{w_bar}" height="{bh}" fill="#4e79a7"/>')
        parts.append(f'<text x="{x + w_bar/2}" y="{y - 8}" text-anchor="middle">{val}</text>')
        # labels
        lbl = escape_xml(lab)
        parts.append(f'<text class="lbl" x="{x + w_bar/2}" y="{y0 + 24}" text-anchor="middle">{lbl}</text>')
    parts.append('</svg>')
    return '\n'.join(parts)


def escape_xml(s: str) -> str:
    return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')


def main():
    ensure_dirs()
    text = SRC_MD.read_text(encoding='utf-8')
    # compute relative prefix from OUT_MD dir to ASSETS_DIR (e.g., ../assets)
    img_prefix = os.path.relpath(ASSETS_DIR, OUT_MD.parent)
    blocks, replaced = extract_mermaid_blocks(text, img_prefix)
    svg_map = {}
    if blocks:
        svg_map = render_with_mmdc(blocks)
    style = """
<style>
  body { font-family: "Liberation Serif", "Times New Roman", serif; line-height: 1.35; }
  p, li { text-align: justify; hyphens: auto; }
  img { max-width: 100%; display: block; margin: 0.5rem auto; }
  table { width: 100%; border-collapse: collapse; }
  th, td { border: 1px solid #ccc; padding: 0.25rem 0.4rem; }
</style>
"""
    # Embed SVGs inline as data URIs to ensure visibility in PDF
    import base64
    embedded = replaced
    for idx, svg_path in svg_map.items():
        if not svg_path.exists():
            continue
        b64 = base64.b64encode(svg_path.read_bytes()).decode('ascii')
        placeholder = f'![Gráfico Mermaid {idx}]'
        img_tag = f'<img alt="Gráfico Mermaid {idx}" src="data:image/svg+xml;base64,{b64}" />'
        embedded = embedded.replace(placeholder, img_tag)

    OUT_MD.write_text(style + "\n" + embedded, encoding='utf-8')
    print(f'Escrito markdown renderizado em: {OUT_MD}')
    print(f'Gráficos Mermaid: {len(blocks)} gerados em {ASSETS_DIR}')


if __name__ == '__main__':
    main()
