#!/usr/bin/env bash
set -euo pipefail

# Recusa compilar fora de projeto/
if [[ "$PWD" != *"/projeto"* ]]; then
  echo "[build] Compilando em 'projeto/' para evitar artefatos na raiz..."
  exec make pdf
fi

echo "[build] Diretório atual já é 'projeto/'. Use 'make pdf'."
