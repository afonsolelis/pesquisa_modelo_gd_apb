# PASTA PLANTUML - MODELAGEM VISUAL

Esta pasta contém toda a modelagem visual da seção 6.5 "Modelagem: Entidades e Relacionamentos".

## 📁 Estrutura da Pasta

```
plantuml/
├── diagrama1_nucleo_central.puml           # Código PlantUML
├── diagrama1_nucleo_central.png            # Imagem gerada
├── diagrama2_entidades_execucao.puml       # Código PlantUML
├── diagrama2_entidades_execucao.png        # Imagem gerada
├── diagrama3_atividades_pedagogicas.puml  # Código PlantUML
├── diagrama3_atividades_pedagogicas.png   # Imagem gerada
├── diagrama4_artefatos_tecnicos.puml      # Código PlantUML
├── diagrama4_artefatos_tecnicos.png       # Imagem gerada
├── diagrama5_metricas_indicadores.puml    # Código PlantUML
├── diagrama5_metricas_indicadores.png     # Imagem gerada
├── diagrama6_modelo_integrado.puml        # Código PlantUML
├── diagrama6_modelo_integrado.png         # Imagem gerada
├── plantuml.jar                           # PlantUML executável
├── plantuml.sh                            # Script para gerar diagramas
├── plantuml.tex                           # Arquivo LaTeX com todos os diagramas
└── README.md                              # Este arquivo
```

## 🔧 Como Usar

### Gerar Diagramas
```bash
cd plantuml/
./plantuml.sh *.puml
```

### Gerar Diagrama Específico
```bash
cd plantuml/
./plantuml.sh diagrama1_nucleo_central.puml
```

### Incluir no LaTeX
No arquivo principal `tese.tex`, adicione antes de `\end{document}`:

```latex
\input{plantuml/plantuml}
```

## 📊 Diagramas Disponíveis

1. **Núcleo Central** - Curso, Módulo, TAPI, Parceiro
2. **Entidades de Execução** - Equipe, Sprint, Estudante, BacklogItem
3. **Atividades Pedagógicas** - Instruções, Autoestudos, Avaliação
4. **Artefatos Técnicos** - Commits, PRs, Reviews, Evidências
5. **Métricas e Indicadores** - CEP, Analytics, Dashboards
6. **Modelo Integrado** - Visão consolidada completa

## ✅ Integração Simples

1. Alterar título da seção 6.5 para: `\subsection{Modelagem: Entidades e Relacionamentos}`
2. Adicionar no final da tese: `\input{plantuml/plantuml}`
3. Compilar LaTeX normalmente

**Tudo organizado em uma pasta dedicada!**