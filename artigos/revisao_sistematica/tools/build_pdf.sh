#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "[1/4] Renderizando gráficos e MD..."
python3 "$ROOT_DIR/tools/render_mermaid.py"

echo "[2/4] Convertendo para PDF intermediário..."
npx -y md-to-pdf "$ROOT_DIR/build/revisao_sistematica_tese_rendered.md"

echo "[3/4] Gerando PDF final..."
cp -f "$ROOT_DIR/build/revisao_sistematica_tese_rendered.pdf" "$ROOT_DIR/build/revisao_sistematica_tese.pdf"

echo "[4/4] Limpando intermediários..."
rm -f "$ROOT_DIR/build/revisao_sistematica_tese_rendered.pdf"
rm -f "$ROOT_DIR/build/revisao_sistematica_tese_rendered.md"

echo "OK: PDF final em build/revisao_sistematica_tese.pdf"
