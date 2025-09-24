# Registro de alterações – Visões ISO, RQs, PICO e Classificação

Este arquivo documenta, de forma rastreável, as mudanças realizadas nesta seção do trabalho.

## Alterações realizadas

- Integração de base.md ao artigo principal (`revisao_sistematica_tese.md`), expandindo a narrativa e referências.
- Inserção das Questões de Pesquisa (RQs) explícitas:
  - Seção 3.1.2.2 “Questões de Pesquisa (RQs)” com RQ1–RQ4 e respectivas justificativas.
  - Seção 3.1.2.3 “Mapeamento PICO → RQs”, mostrando como P, I, C, O dão origem/ancoram cada RQ.
- Ajustes nas Visões (ISO 10746):
  - Visão Empresarial (Camada 1): foco explícito no PBL/PbL como propósito educacional, objetivos de aprendizagem e papel do professor orientador.
  - Visão de Informação (Camada 2): mantida (fluxo de dados e instrumentos de informação educacional).
  - Visão Computacional (Camada 3): texto reformulado para enfatizar suporte sistemático ao professor e requisitos não funcionais (RNFs) – sem alterar as strings de busca.
  - Visões de Engenharia (Camada 4) e de Tecnologia (Camada 5): mantidas conforme base.md.
- Fluxograma atualizado para refletir o processo completo:
  - 811 registros totais → triagem por camadas → conjunto temático (n=179) → classificação multicritério → Top‑25.
- Substituição de “filtro estrito” por “classificação multicritério (Kitchenham)”.
- Inclusão da seção 4.5.3 com os critérios de classificação (alinhamento às RQs, qualidade metodológica, evidência empírica, operacionalidade, replicabilidade, transferibilidade, atualidade).

## Organização das seções (ordenação corrigida)

- A antiga “4.5 Seleção Final Atualizada” que aparecia após a Conclusão foi removida daquele local e reinserida dentro do capítulo 4 (Resultados) como:
  - 4.6 Seleção Final Atualizada (Classificação multicritério)
  - 4.6.1 Estudos Incluídos (Top‑25)
  - 4.6.2 Artefatos e Reprodutibilidade
  - 4.6.3 Critérios de classificação adotados
- Ordem atual do capítulo 4:
  - 4.1 Processo de Seleção
  - 4.2 Caracterização dos Estudos Incluídos
  - 4.3 Análise dos Desafios Metodológicos
  - 4.4 Instrumentos e Tecnologias para Avaliação
  - 4.5 Lacunas Persistentes e Oportunidades de Pesquisa
  - 4.6 Seleção Final Atualizada (Classificação multicritério)
- As seções 5 (Discussão), 6 (Conclusão) e Referências permanecem após o capítulo 4.

## Strings de busca

- As strings de busca foram mantidas exatamente como no `base.md`.
- Em especial, a Camada 3 (Visão Computacional) foi revertida ao original:
  - TS=("project-based learning" OR "project based learning" OR "PBL")
  - AND TS=("assessment" OR "evaluation" OR "grading")
  - AND TS=("objective*" OR "scalab*" OR "automat*" OR "reliab*" OR "valid*")

Observação: O texto explicativo da Visão Computacional foi atualizado para mencionar RNFs (confiabilidade, escalabilidade, usabilidade, desempenho, segurança/privacidade, interoperabilidade, manutenibilidade), mas as STRINGS NÃO FORAM ALTERADAS.

## Artefatos gerados/atualizados

- Artigo extenso: `revisao_sistematica_tese.md`
- PDF do artigo: `revisao_sistematica_tese.pdf` (compilado com pandoc + xelatex; fontes DejaVu para suportar o fluxograma)
- Seleção final (25 estudos) e auxiliares:
  - `busca/consolidado/strict_selection_top25.ris`
  - `busca/consolidado/strict_selection_top25_summary.txt`
  - `busca/consolidado/strict_selection_excluded_final.txt`
  - `busca/consolidado/strict_selection.csv`

## Observações

- Qualquer alteração futura nas strings deve referenciar explicitamente o `base.md`. Este registro confirma que as strings permanecem idênticas ao original.
- A narrativa das visões foi ajustada conforme solicitado, sem tocar nas strings.
