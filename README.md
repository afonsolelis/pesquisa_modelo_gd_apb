# Pesquisa Modelo GD APB — Instruções de Build

- Sempre compile o projeto dentro de `projeto/`.
- Para evitar artefatos gerados no diretório raiz, use o `Makefile` ou o script abaixo.

Comandos recomendados

- `make pdf`: compila o PDF chamando o `Makefile` dentro de `projeto/`.
- `make clean`: remove artefatos de compilação (apenas em `projeto/`).

Script alternativo

- `./build.sh`: compila sempre dentro de `projeto/` e recusa compilar na raiz.

Observações

- O arquivo principal é `projeto/modelo_gd_apb_completo.tex`.
- Imagens e assets devem ficar em `projeto/assets/`.
- Não execute `pdflatex` no diretório raiz.
