# INSTRUÇÕES PARA INTEGRAÇÃO PLANTUML

## 1. Alteração no Título da Seção 6.5

**NO ARQUIVO `tese.tex`, LINHA ~1157:**

ALTERAR DE:
```latex
\subsection{Modelagem Escrita: Entidades e Relacionamentos}
```

PARA:
```latex
\subsection{Modelagem: Entidades e Relacionamentos}
```

## 2. Adicionar Referências aos Diagramas

**NO FINAL DA SEÇÃO 6.5, ANTES DA PRÓXIMA SUBSEÇÃO:**

Adicionar o seguinte parágrafo:

```latex
A representação visual completa desta modelagem, incluindo diagramas UML detalhados de todas as entidades e relacionamentos descritos, encontra-se no Apêndice de Modelagem Visual PlantUML (ver \hyperref[fig:plantuml_modelo_integrado]{Diagrama Integrado Completo} e diagramas específicos por dimensão).
```

## 3. Incluir o Arquivo PlantUML no Documento Principal

**NO ARQUIVO `tese.tex`, ANTES DE `\end{document}`:**

```latex
% Incluir modelagem visual PlantUML
\input{plantuml}
```

## 4. Garantir Pacotes LaTeX Necessários

**NO PREÂMBULO DO `tese.tex`, VERIFICAR SE EXISTE:**

```latex
\usepackage{graphicx}
\usepackage{float}
\usepackage{hyperref}
\usepackage{xcolor}
```

## 5. Estrutura Final Recomendada

```
tese.tex (documento principal)
├── Seção 6: MODELO PROPOSTO
│   └── 6.5 Modelagem: Entidades e Relacionamentos (texto)
│       └── [referência aos diagramas]
├── ...
└── APÊNDICE: Modelagem Visual PlantUML
    ├── 1. Núcleo Central
    ├── 2. Entidades de Execução
    ├── 3. Atividades Pedagógicas
    ├── 4. Artefatos Técnicos
    ├── 5. Métricas e Indicadores
    └── 6. Modelo Integrado Completo
```

## 6. Verificação da Compilação

Para testar se tudo está funcionando:

```bash
# 1. Gerar diagramas (se necessário)
./plantuml.sh *.puml

# 2. Compilar LaTeX
pdflatex tese.tex
pdflatex tese.tex  # Segunda passagem para referências

# 3. Verificar se todas as imagens foram incluídas
```

## 7. Benefícios da Organização

✅ **Separação clara** entre texto descritivo e modelagem visual
✅ **Navegação estruturada** com índice e hyperlinks
✅ **Referências cruzadas** conectam texto e diagramas
✅ **Manutenibilidade** - diagramas em arquivo separado
✅ **Flexibilidade** - pode ser movido para apêndice se necessário
✅ **Profissionalismo** - apresentação organizada e limpa