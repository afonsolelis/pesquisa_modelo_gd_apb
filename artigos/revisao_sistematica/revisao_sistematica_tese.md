# Uma Revisão Sistemática sobre os Desafios e Tecnologias para Avaliação em Aprendizagem Baseada em Projetos

## 1. Introdução

### 1.1 Justificativa

A Aprendizagem Baseada em Projetos (ABP) representa uma mudança paradigmática no ensino superior, especialmente em áreas tecnológicas, onde a formação de profissionais capazes de enfrentar os desafios complexos do mercado contemporâneo se torna imperativa. No contexto brasileiro, a experiência do Instituto de Tecnologia e Liderança (Inteli) evidencia tanto o potencial transformador da ABP quanto os desafios significativos enfrentados por professores orientadores na implementação eficaz dessa metodologia.

Conforme documentado por Valente et al. (2025), "a qualidade dos concluintes dos cursos de computação tradicionais não está atendendo às necessidades do mercado e do país", evidenciando a necessidade crítica de abordagens pedagógicas mais eficazes. A estrutura curricular do Inteli, organizada em Learning BackLogs (LBLs), ilustra a complexidade inerente à ABP contemporânea, onde os módulos integram conhecimentos técnicos de computação, matemática e física com competências transversais de liderança, negócios e design de experiência do usuário (INTELI PPC, 2024).

A implementação prática da ABP no contexto do Inteli revela desafios metodológicos específicos que requerem "um planejamento integrado de todas as vertentes e uma revisão constante para assegurar que todos os conteúdos essenciais sejam cobertos de maneira adequada" (Arakaki et al., 2025). Esta complexidade operacional gera questões fundamentais sobre como realizar a evolução sistemática dos módulos de aprendizagem e quais aspectos da aprendizagem devem ser utilizados como base para compor os requisitos de revisão.

Evidências recentes fortalecem essa direção: uma meta‑análise em periódico JCR demonstra o impacto da aprendizagem baseada em projetos nos resultados de aprendizagem quando articulada a resultados do programa (Heliyon, 2022; DOI: 10.1016/j.heliyon.2022.e10248). Em paralelo, análises recentes sobre auto e avaliação por pares em contextos de aprendizagem ativa no ensino superior reforçam a necessidade de critérios claros, confiáveis e orientados a competências ao longo do processo formativo (Research Papers in Education, 2022; DOI: 10.1080/02671522.2020.1849371). Esses resultados contemporâneos, somados às evidências internas (Inteli) e à base de engenharia de software, justificam a proposta desta pesquisa ao endereçar objetividade, escalabilidade e monitoramento processual na avaliação em ABP.

A experiência prática revela questões metodológicas centrais que emergem da complexidade da ABP: "Como realizar a evolução sistemática dos módulos de aprendizagem baseados em projetos (LBLs)? Quais aspectos da aprendizagem devem ser utilizados como base para compor os requisitos de revisão? Como os pacotes de conceitos e práticas podem ser reconfigurados sem prejuízo das disciplinas essenciais?" (Arakaki et al., 2025).

A complexidade dessa implementação é amplificada pelos desafios inerentes à engenharia de software moderna. Pressman \& Maxim (2021) destacam que os sistemas de informação enfrentaram uma "esfera crescente de desafios" à medida que os problemas se tornaram mais complexos, demandando programas cada vez mais sofisticados. Esta realidade técnica, combinada com a necessidade de formar profissionais capazes de "lidar com a complexidade e a rápida evolução do mercado de trabalho" (Arakaki et al., 2025), cria um contexto educacional onde professores orientadores enfrentam dificuldades operacionais específicas:

**Desafios na Avaliação de Contribuições Individuais**: A natureza colaborativa dos projetos em ABP torna complexa a identificação e mensuração das contribuições específicas de cada membro da equipe, especialmente quando o trabalho é interdependente e os papéis são rotativos ao longo dos módulos.

**Complexidade na Mensuração de Competências Transversais**: A necessidade de avaliar tanto hard skills quanto soft skills de forma integrada apresenta desafios significativos, pois essas competências se manifestam de forma processual e contextual, requerendo instrumentos específicos que capturam sua evolução temporal.

**Limitações no Feedback Contínuo**: O fornecimento de feedback formativo durante cronogramas prolongados demanda monitoramento constante e personalizado, representando um desafio de escalabilidade quando aplicado a contextos complexos com múltiplas equipes.

**Fragmentação do Monitoramento Multidimensional**: A necessidade simultânea de monitorar qualidade técnica do código, dinâmica das equipes, progresso individual e desenvolvimento de competências transversais revela a inadequação de ferramentas isoladas que abordam apenas aspectos específicos da experiência em ABP.

**Deficiências na Tomada de Decisão Pedagógica**: A falta de visibilidade integrada sobre o processo educativo limita a capacidade dos professores orientadores de tomar decisões baseadas em informações em tempo real, comprometendo a eficácia das intervenções pedagógicas necessárias.

Soluções tecnológicas existentes operam de forma fragmentada, focando em aspectos específicos da experiência em ABP em vez de proporcionar uma visão holística do processo educativo que apoie efetivamente o trabalho do professor orientador. Esta fragmentação impede uma abordagem integrada que considere as múltiplas dimensões da aprendizagem em contextos de ABP.

Esta revisão sistemática visa mapear comprehensivamente o estado da arte sobre os desafios metodológicos, instrumentos e tecnologias para auxiliar professores orientadores na avaliação em ambientes de Aprendizagem Baseada em Projetos, identificando lacunas reais na literatura e oportunidades para desenvolvimento de soluções mais eficazes.

## 2. Objetivos da Revisão

### 2.1 Objetivo Geral

Mapear sistematicamente a produção científica sobre métodos, instrumentos e tecnologias para auxiliar professores orientadores na avaliação em Aprendizagem Baseada em Projetos (ABP), identificando desafios, soluções existentes e lacunas de pesquisa para fundamentar o desenvolvimento de abordagens mais eficazes.

### 2.2 Objetivos Específicos

1. Identificar e categorizar os principais desafios metodológicos enfrentados por professores orientadores na avaliação de aprendizagem em contextos de ABP.
2. Mapear os instrumentos e tecnologias utilizados para apoiar professores orientadores na superação desses desafios avaliativos.
3. Analisar a eficácia de soluções tecnológicas existentes no apoio a processos avaliativos objetivos e escaláveis em ABP.
4. Identificar lacunas persistentes e oportunidades de pesquisa no suporte tecnológico à avaliação em ABP.
5. Avaliar o potencial de tecnologias emergentes para abordar os desafios identificados.

## 3. Metodologia

Esta revisão sistemática foi conduzida seguindo rigorosamente as diretrizes propostas por Kitchenham (2004) para realização de revisões sistemáticas em engenharia de software. O processo foi estruturado nas três fases principais definidas por Kitchenham: **Planning the Review** (Planejamento da Revisão), **Conducting the Review** (Condução da Revisão) e **Reporting the Review** (Relato da Revisão).

### 3.1 Planejamento da Revisão

Esta subseção descreve a preparação metodológica da revisão sistemática conforme Kitchenham (2004), incluindo a justificativa da necessidade da revisão, a definição do protocolo (questão de pesquisa, RQs, PICO) e as decisões de escopo que orientam as etapas seguintes de condução e relato.
#### 3.1.1 Necessidade de uma Revisão Sistemática

A necessidade desta revisão sistemática surge da exigência de sintetizar de forma abrangente e imparcial toda a informação existente sobre os desafios metodológicos, instrumentos e tecnologias para auxiliar professores orientadores na avaliação em ABP. Como recomendado por Kitchenham (2004), antes de iniciar esta revisão, foi realizada uma busca prévia para identificar revisões sistemáticas existentes sobre o tema, não sendo encontradas revisões que abordem especificamente a perspectiva do professor orientador em contextos de ABP.

#### 3.1.2 Desenvolvimento de um Protocolo de Revisão

Um protocolo de revisão foi desenvolvido seguindo as recomendações de Kitchenham (2004), especificando os métodos a serem utilizados para reduzir a possibilidade de viés do pesquisador. O protocolo inclui todos os elementos recomendados:

**Background**: A justificativa para a revisão baseada nos desafios documentados enfrentados por professores orientadores em contextos de ABP.

**Research Question**: A questão de pesquisa foi estruturada considerando População, Intervenção e Resultados, conforme recomendado por Kitchenham (2004).

##### 3.1.2.1 Questão de Pesquisa

Seguindo as diretrizes de Kitchenham (2004) para formulação de questões de pesquisa em engenharia de software, a questão foi formulada utilizando o framework PICO (Population, Intervention, Comparison, Outcome) (Santos, Pimenta \& Nobre, 2007), focando nas dificuldades do professor orientador na avaliação em ambientes de Aprendizagem Baseada em Projetos:

**Questão Principal**: Quais desafios metodológicos enfrentam os professores orientadores na avaliação em Aprendizagem Baseada em Projetos e como as tecnologias existentes podem apoiar a superação desses desafios?

**P** (População): Professores orientadores e estudantes em ambientes educacionais que utilizam Aprendizagem Baseada em Projetos, incluindo diferentes contextos (ensino superior, técnico, profissional) e disciplinas (engenharia, ciência da computação, etc.).

**I** (Intervenção): Métodos, instrumentos e tecnologias digitais para apoio à avaliação em ABP, incluindo sistemas de avaliação, learning analytics, ferramentas de feedback e plataformas de monitoramento.

**C** (Comparação): Métodos tradicionais de avaliação sem suporte tecnológico ou abordagens convencionais de avaliação em contextos educacionais não baseados em projetos.

**O** (Resultados): Melhoria na eficácia, objetividade e escalabilidade da avaliação; redução de viés avaliativo; aumento da qualidade do feedback formativo; superação de desafios específicos identificados na literatura relativos à avaliação justa e abrangente de estudantes em contextos colaborativos e processuais.

##### 3.1.2.2 Questões de Pesquisa (RQs)

- RQ1 — Desafios: Quais são os principais desafios metodológicos para avaliar aprendizagem em PBL/PbL no Ensino Superior (p.ex., avaliação processual, colaboração/contribuição individual, competências transversais, feedback contínuo)?
  Justificativa: fundamenta o mapeamento de necessidades (Visões ISO: Empresarial e de Engenharia) e orienta critérios de seleção/extração.

- RQ2 — Instrumentos/Tecnologias: Que instrumentos e tecnologias têm sido propostos/avaliados para apoiar a avaliação em PBL/PbL (rubricas digitais, peer/self assessment estruturado, telemetria de equipes, dashboards, learning analytics, automação)?
  Justificativa: permite identificar soluções operacionais (Visões ISO: Informação e Tecnologia) e sua aplicabilidade para docentes orientadores.

- RQ3 — Objetividade/Escalabilidade: De que modo as abordagens avaliativas alcançam maior objetividade e escalabilidade (padronização de critérios, confiabilidade interavaliadores, validade de instrumentos, automação, analytics)?
  Justificativa: foca a Visão Computacional e aspectos de qualidade/escala exigidos em turmas grandes e projetos longos.

- RQ4 — Lacunas/Oportunidades: Quais lacunas persistem e que oportunidades de pesquisa permanecem abertas (p.ex., integração multi‑perspectiva, mensuração de competências processuais, generalização/transferibilidade, replicabilidade e abertura de dados/artefatos)?
  Justificativa: orienta pesquisa futura e a posição da contribuição pretendida nesta tese no ecossistema de evidências.

##### 3.1.2.3 Mapeamento PICO → RQs

- P (População: docentes orientadores/estudantes em PBL/PbL, HE) → contextualiza RQ1 (desafios) e RQ4 (lacunas), definindo atores e ambientes onde os desafios emergem.
- I (Intervenção: métodos/instrumentos/tecnologias de avaliação) → fundamenta RQ2 (instrumentos/tecnologias) e parte de RQ3 (como alcançam objetividade/escala).
- C (Comparação: práticas tradicionais/sem suporte) → informa RQ3, ao contrastar ganhos de objetividade, escalabilidade e qualidade com abordagens de referência.
- O (Resultados: objetividade, escalabilidade, feedback, aprendizagem) → ancora RQ3 (medidas e RNFs) e RQ2 (eficácia dos instrumentos) e fecha com RQ4 (onde resultados ainda são insuficientes).

### 3.2 Condução da Revisão

Aqui detalhamos a execução prática do protocolo: identificação das pesquisas (estratégias e camadas de busca), documentação, critérios e processo de seleção, avaliação da qualidade e procedimentos de extração e síntese de dados, assegurando transparência e reprodutibilidade.
#### 3.2.1 Identificação de Pesquisas

##### 3.2.1.1 Geração de uma Estratégia de Busca

A estratégia de busca foi desenvolvida seguindo as recomendações de Kitchenham (2004), incluindo consulta com bibliotecários especializados e uso de processo iterativo com:

- **Buscas preliminares** para identificar revisões sistemáticas existentes e avaliar o volume de estudos potencialmente relevantes
- **Buscas experimentais** usando várias combinações de termos de busca derivados da questão de pesquisa
- **Revisão dos resultados** de pesquisa
- **Consultas com especialistas** na área

A abordagem geral seguiu a recomendação de Kitchenham (2004) de decompor a questão em facetas individuais (população, intervenção, resultados) e criar lista de sinônimos, abreviações e grafias alternativas.

##### 3.2.1.2 Estratégia de Busca

**Base de Dados Eletrônica**:

A base de dados Web of Science foi selecionada como única fonte para esta revisão sistemática, com base na seguinte justificativa:

- **Web of Science**: Base multidisciplinar com rigoroso processo de seleção de periódicos apenas com revisão por pares, cobertura ideal em ciência da computação, educação em engenharia e tecnologia educacional, ferramentas analíticas avançadas para análise de tendências temporais e compatibilidade com diretrizes Kitchenham para exportação RIS padronizada.

**Outras Fontes** (conforme recomendado por Kitchenham, 2004):
- Listas de referências de estudos primários relevantes e artigos de revisão
- Anais de conferências especializadas
- Literatura cinzenta (relatórios técnicos, trabalhos em andamento)
- Contato direto com pesquisadores específicos para obter material de fonte apropriado

**Strings de Busca Estruturadas em Camadas**:

Conforme as diretrizes de Kitchenham (2004), a estratégia de busca foi desenvolvida em múltiplas camadas para garantir cobertura abrangente. A estruturação em camadas foi criada com base nos preceitos da norma ISO 10746, que define cinco visões arquiteturais complementares para especificação de sistemas complexos. Adaptada ao contexto de avaliação em ABP, cada camada de busca corresponde a uma perspectiva específica do problema de pesquisa:

**Fundamentação Arquitetural das Camadas** (baseada na ISO 10746):
- **Camada 1** (Visão Empresarial): Foca nos objetivos educacionais e organizacionais do PBL/PbL (propósito da avaliação no currículo, stakeholders, papéis do professor orientador)
- **Camada 2** (Visão de Informação): Aborda o fluxo de dados e instrumentos de informação educacional
- **Camada 3** (Visão Computacional): Examina algoritmos e processos computacionais para avaliação
- **Camada 4** (Visão de Engenharia): Investiga a arquitetura de sistemas de apoio à avaliação
- **Camada 5** (Visão de Tecnologia): Explora tecnologias específicas aplicáveis ao contexto

**Camada 1 - PBL no nível organizacional** (Visão Empresarial — inspirada na ISO 10746):
*Justificativa*: A Visão Empresarial explicita propósito e valor do PBL/PbL no curso (competências-alvo, resultados de aprendizagem, papéis/necessidades do professor orientador e stakeholders). Aqui o foco é situar a avaliação como função central do PBL/PbL e levantar desafios organizacionais e metodológicos decorrentes dessa centralidade. A string foi refinada para incluir termos específicos de educação em engenharia de software e expandir o escopo de desafios identificados.
```text
TS=("project-based learning" OR "project based learning" OR "PBL")
AND TS=("assessment" OR "evaluation" OR "grading")
AND TS=("challenge*" OR "difficult*" OR "problem*" OR "issue*" OR "barrier*" OR "constraint*")
AND TS=("higher education" OR "engineering education" 
        OR "software engineering education" OR "software engineering curriculum" 
        OR "software engineering course*" OR "software engineering program*"
        OR ("software engineering" NEAR/3 (education OR curriculum OR course* OR program*)))
```

**Camada 2 - Instrumentos e Tecnologias** (Visão de Informação — inspirada na ISO 10746):
*Justificativa*: A Visão de Informação modela a estrutura e fluxo de dados. Esta camada busca instrumentos e tecnologias que processam e estruturam informações educacionais para apoiar a avaliação. A string foi expandida para incluir termos específicos de analytics e dashboards, além de focar especificamente em educação em engenharia de software.
```text
TS=("project-based learning" OR "project based learning" OR "PBL")
AND TS=("assessment" OR "evaluation" OR "grading")
AND TS=("instrument*" OR "tool*" OR "method*" OR "rubric*" OR "framework*" OR "technology" OR "dashboard*" OR "analytics")
AND TS=("higher education" OR "engineering education" 
        OR "software engineering education" OR "software engineering curriculum" 
        OR "software engineering course*" OR "software engineering program*"
        OR ("software engineering" NEAR/3 (education OR curriculum OR course* OR program*)))
```

**Camada 3 - Objetividade e Escalabilidade** (Visão Computacional — inspirada na ISO 10746):
*Justificativa*: A Visão Computacional descreve os processos e algoritmos necessários. Esta camada foca em soluções computacionais que garantem objetividade e escalabilidade na avaliação. A string foi expandida para incluir termos de padronização e benchmarking, além de focar especificamente em educação em engenharia de software.
```text
TS=("project-based learning" OR "project based learning" OR "PBL")
AND TS=("assessment" OR "evaluation" OR "grading")
AND TS=("objective*" OR "scalab*" OR "automat*" OR "reliab*" OR "valid*" OR "standard*" OR "benchmark*")
AND TS=("higher education" OR "engineering education" 
        OR "software engineering education" OR "software engineering curriculum" 
        OR "software engineering course*" OR "software engineering program*"
        OR ("software engineering" NEAR/3 (education OR curriculum OR course* OR program*)))
```

**Camada 4 - Avaliação Processual e Colaborativa** (Visão de Engenharia — inspirada na ISO 10746):
*Justificativa*: A Visão de Engenharia define a arquitetura técnica do sistema. Esta camada investiga arquiteturas de sistemas que suportam avaliação processual e colaborativa em tempo real. A string foi completamente reformulada para focar em tecnologias de processamento de eventos complexos e análise em tempo real, com exclusão de termos irrelevantes.
```text
TS=("project-based learning" OR "project based learning" OR "PBL")
AND TS=("assessment" OR "evaluation")
AND TS=("process*" OR "formative" OR "ongoing" OR "continuous" OR "telemetry" OR "monitor*")
AND TS=("complex event processing" OR "event stream processing" OR "event-driven" OR "stream processing" OR "real-time analytic*")
NOT TS=("postal code" OR "zip code" OR "código postal")
```

**Camada 5 - Competências Transversais** (Visão de Tecnologia — inspirada na ISO 10746):
*Justificativa*: A Visão de Tecnologia especifica as tecnologias e plataformas de implementação. Esta camada explora tecnologias específicas para avaliação de competências transversais e habilidades interpessoais. A string foi reformulada para incluir tecnologias de processamento de eventos complexos e análise em tempo real, com foco em competências transversais e exclusão de termos irrelevantes.
```text
TS=("project-based learning" OR "project based learning" OR "PBL")
AND TS=("assessment" OR "evaluation" OR "grading")
AND TS=("critical thinking" OR "creativity" OR "communication" OR "soft skill*" OR "teamwork")
AND TS=("complex event processing" OR "event stream processing" OR "real-time analytic*")
NOT TS=("postal code" OR "zip code" OR "código postal")
```

**Período de Busca**: Todos os períodos (sem restrição temporal)

**Idiomas**: Todos, mas vieram apenas resultados na lingua inglesa.

##### 3.2.1.5 Refinamento das Strings de Busca

As strings de busca foram refinadas em uma segunda iteração para melhorar a precisão e relevância dos resultados:

##### 3.2.1.6 Mapa de Dimensões x Palavras‑chave

Para tornar explícita a origem e a lógica das strings, o quadro a seguir mapeia cada dimensão (camada) às principais palavras‑chave utilizadas. Em todas as camadas aplicamos os termos‑base de escopo e avaliação educational (project‑based learning + assessment/evaluation + contexto educacional) e, sobre eles, adicionamos termos específicos da dimensão.

Table: Dimensões (ISO 10746) x palavras‑chave derivadas das strings

| Camada (Dimensão ISO) | Foco da busca | Palavras‑chave específicas (todas) | Combinatória (TS) |
| --- | --- | --- | --- |
| Camada 1 — Visão Empresarial | Desafios e justificativas curriculares/organizacionais da avaliação em ABP | `challenge*`, `difficult*`, `problem*`, `issue*`, `barrier*`, `constraint*` | TS=("project-based learning" OR "project based learning" OR "PBL") AND TS=("assessment" OR "evaluation" OR "grading") AND TS=("challenge*" OR "difficult*" OR "problem*" OR "issue*" OR "barrier*" OR "constraint*") AND TS=("higher education" OR "engineering education" OR "software engineering education" OR "software engineering curriculum" OR "software engineering course*" OR "software engineering program*" OR ("software engineering" NEAR/3 (education OR curriculum OR course* OR program*))) |
| Camada 2 — Visão de Informação | Instrumentos, métodos e tecnologias de informação | `instrument*`, `tool*`, `method*`, `rubric*`, `framework*`, `technology`, `dashboard*`, `analytics` | TS=("project-based learning" OR "project based learning" OR "PBL") AND TS=("assessment" OR "evaluation" OR "grading") AND TS=("instrument*" OR "tool*" OR "method*" OR "rubric*" OR "framework*" OR "technology" OR "dashboard*" OR "analytics") AND TS=("higher education" OR "engineering education" OR "software engineering education" OR "software engineering curriculum" OR "software engineering course*" OR "software engineering program*" OR ("software engineering" NEAR/3 (education OR curriculum OR course* OR program*))) |
| Camada 3 — Visão Computacional | Objetividade, escala, padronização e validação | `objective*`, `scalab*`, `automat*`, `reliab*`, `valid*`, `standard*`, `benchmark*` | TS=("project-based learning" OR "project based learning" OR "PBL") AND TS=("assessment" OR "evaluation" OR "grading") AND TS=("objective*" OR "scalab*" OR "automat*" OR "reliab*" OR "valid*" OR "standard*" OR "benchmark*") AND TS=("higher education" OR "engineering education" OR "software engineering education" OR "software engineering curriculum" OR "software engineering course*" OR "software engineering program*" OR ("software engineering" NEAR/3 (education OR curriculum OR course* OR program*))) |
| Camada 4 — Visão de Engenharia | Avaliação processual, eventos e monitoramento contínuo | `process*`, `formative`, `ongoing`, `continuous`, `telemetry`, `monitor*`, "complex event processing", "event stream processing", `event-driven`, "stream processing", "real-time analytic*" | TS=("project-based learning" OR "project based learning" OR "PBL") AND TS=("assessment" OR "evaluation") AND TS=("process*" OR "formative" OR "ongoing" OR "continuous" OR "telemetry" OR "monitor*") AND TS=("complex event processing" OR "event stream processing" OR "event-driven" OR "stream processing" OR "real-time analytic*") NOT TS=("postal code" OR "zip code" OR "código postal") |
| Camada 5 — Visão de Tecnologia | Competências transversais e sua instrumentação processual | "critical thinking", `creativity`, `communication`, "soft skill*", `teamwork` (com processamento em tempo real quando pertinente) | TS=("project-based learning" OR "project based learning" OR "PBL") AND TS=("assessment" OR "evaluation" OR "grading") AND TS=("critical thinking" OR "creativity" OR "communication" OR "soft skill*" OR "teamwork") AND TS=("complex event processing" OR "event stream processing" OR "real-time analytic*") NOT TS=("postal code" OR "zip code" OR "código postal") |

Termos‑base aplicados transversalmente às camadas:
- Escopo ABP: "project‑based learning" OR "project based learning" OR "PBL"
- Avaliação: "assessment" OR "evaluation" OR "grading"
- Contexto educacional: "higher education" OR "engineering education" OR "software engineering" (NEAR/3 education/curriculum/course*/program*)
- Filtros de exclusão (quando necessário): termos não relacionados (ex.: “postal/zip code”) e revisões/meta‑análises quando buscamos apenas estudos primários.

Justificativa (ISO 10746): A norma de Referência para Processamento Distribuído Aberto (RM‑ODP) propõe cinco visões complementares — Empresarial, de Informação, Computacional, de Engenharia e de Tecnologia — para especificação de sistemas complexos. Adaptamos essas visões ao domínio da avaliação em ABP para garantir cobertura sistemática: (i) a Visão Empresarial explicita propósito/valor educacional e desafios; (ii) a Visão de Informação estrutura entidades e fluxos de dados (instrumentos, evidências, critérios); (iii) a Visão Computacional define processos e medidas que elevam objetividade e escalabilidade; (iv) a Visão de Engenharia trata de arquiteturas e mecanismos operacionais (eventos, telemetria, tempo real) que viabilizam avaliação processual; e (v) a Visão de Tecnologia foca recursos concretos para instrumentar competências transversais. Esse mapeamento orientou a composição das strings e assegura que as buscas cubram, de forma coerente e rastreável, todas as dimensões relevantes à nossa questão de pesquisa.

**Melhorias Implementadas**:

1. **Foco em Educação em Engenharia de Software**: Adicionado filtro específico para contextos de educação em engenharia de software em todas as camadas (1-3), garantindo maior relevância para o domínio de aplicação.

2. **Expansão de Termos de Desafios**: Na Camada 1, incluído o termo "constraint*" para capturar limitações e restrições metodológicas.

3. **Inclusão de Tecnologias Emergentes**: Nas Camadas 2 e 3, adicionados termos como "dashboard*", "analytics", "standard*" e "benchmark*" para capturar soluções tecnológicas mais avançadas.

4. **Reformulação das Camadas 4 e 5**: Completamente reformuladas para focar em tecnologias de processamento de eventos complexos e análise em tempo real, com exclusão de termos irrelevantes como códigos postais.

5. **Filtros de Exclusão**: Implementados filtros NOT para excluir resultados irrelevantes que poderiam contaminar os resultados.

**Impacto do Refinamento**: As buscas por camada totalizaram 882 registros (TY) nos arquivos RIS; após retenção de DOI e deduplicação por DOI entre camadas, consolidamos 301 artigos para triagem no Rayyan, resultando em 20 estudos incluídos.

##### 3.2.1.3 Documentação do Processo de Busca

Seguindo as diretrizes de Kitchenham (2004) para documentação transparente e replicável, o processo de busca foi documentado com:

- Nome da base de dados e estratégia de busca para cada camada
- Data da busca e anos cobertos
- Procedimentos específicos utilizados na Web of Science
- URLs e condições específicas quando aplicável
- Resultados de busca não filtrados salvos para possível reanálise

O fluxograma a seguir ilustra o processo de busca estruturado em camadas (ISO 10746) e a seleção com Rayyan que levou ao conjunto final de 20 estudos primários:

Os volumes por camada e com DOI estão detalhados na Seção 4.1 (Distribuição por Camadas) e nas visualizações correspondentes (a inserir na versão final).

**Processo de Seleção**

Processo atualizado, com consolidação por DOI, deduplicação entre camadas e triagem com Rayyan (Kitchenham, 2004):

[Figura placeholder: Fluxo de busca e seleção (Kitchenham/Rayyan) — inserir versão final no PDF.]

Fonte: Elaboração própria (2025). Ferramenta de triagem: Rayyan.

**Justificativa Arquitetural**: Esta estruturação, baseada nos preceitos da ISO 10746, garante cobertura sistemática de todas as perspectivas relevantes para o problema de pesquisa, desde os requisitos organizacionais (Visão Empresarial) até as tecnologias específicas de implementação (Visão de Tecnologia), passando pela modelagem de dados (Visão de Informação), algoritmos (Visão Computacional) e arquitetura de sistemas (Visão de Engenharia). Esta abordagem assegura que nenhum aspecto crítico da avaliação em ABP seja omitido na revisão sistemática.

##### 3.2.1.4 Camadas de Busca (visões inspiradas na ISO 10746)

Para dar transparência ao papel de cada camada, apresentamos os volumes identificados por camada (arquivos RIS) e os respectivos registros contendo DOI:

- Camada 1 — Visão Empresarial (Desafios Metodológicos): 255 identificados; 213 com DOI
- Camada 2 — Visão de Informação (Instrumentos e Tecnologias): 319 identificados; 266 com DOI
- Camada 3 — Visão Computacional (Objetividade e Escalabilidade): 120 identificados; 95 com DOI
- Camada 4 — Visão de Engenharia (Avaliação Processual): 1 identificado; 1 com DOI
- Camada 5 — Visão de Tecnologia (Competências Transversais): 187 identificados; 158 com DOI

Após retenção de registros com DOI e deduplicação entre camadas por DOI, o conjunto consolidado resultou em 301 artigos (arquivo `20250923/consolidado_wos.ris`). Esses 301 foram triados no Rayyan (título e resumo) com aplicação dos critérios Kitchenham (alinhamento às RQs, foco avaliativo, qualidade metodológica, evidência, replicabilidade e transferibilidade), culminando em 20 estudos para a análise final.

#### 3.2.2 Seleção de Estudos Primários

##### 3.2.2.1 Critérios de Seleção de Estudos

Os critérios de seleção foram definidos para identificar estudos primários que fornecem evidência direta sobre a questão de pesquisa, seguindo a recomendação de Kitchenham (2004) de basear os critérios na questão de pesquisa.

**Critérios de Inclusão:**
- IC1: Artigos que abordem avaliação em contextos de ABP/PBL
- IC2: Estudos sobre desafios avaliativos enfrentados por educadores em ABP
- IC3: Pesquisas sobre tecnologias digitais aplicadas à avaliação educacional
- IC4: Métodos ou instrumentos para avaliação processual e colaborativa
- IC5: Estudos empíricos com validação em contextos educacionais reais

**Critérios de Exclusão:**
- EC1: Artigos focados apenas em avaliação de produtos finais sem considerar processos
- EC2: Estudos exclusivamente sobre avaliação somativa tradicional
- EC3: Pesquisas sem componente educacional
- EC4: Artigos sem metodologia clara ou validação empírica
- EC5: Estudos que não abordem especificamente desafios ou soluções para professores orientadores

##### 3.2.2.2 Processo de Seleção de Estudos

O processo de seleção seguiu a abordagem multifásica recomendada por Kitchenham (2004):

**Fase 1 - Consolidação (DOI e deduplicação)**: As buscas por camada (RIS) foram consolidadas mantendo apenas registros com DOI e eliminando duplicatas entre camadas por DOI. O conjunto resultante contém 301 artigos (arquivo `consolidado_wos.ris`).

**Fase 2 - Triagem (Rayyan)**: Os 301 artigos consolidados foram examinados no Rayyan (https://new.rayyan.ai/) por título e resumo, com aplicação dos critérios Kitchenham (2004). Esta triagem resultou em 20 artigos incluídos para análise.

##### 3.2.2.3 Confiabilidade das Decisões de Inclusão

A confiabilidade das decisões de inclusão foi verificada conforme recomendado por Kitchenham (2004), com análise reflexiva das decisões tomadas durante o processo de seleção.

#### 3.2.3 Avaliação da Qualidade dos Estudos

A avaliação de qualidade dos estudos seguiu as diretrizes de Kitchenham (2004), considerando que qualidade se relaciona ao grau em que o estudo minimiza viés e maximiza validade interna e externa.

**Propósitos da Avaliação de Qualidade:**
- Fornecer critérios detalhados de inclusão/exclusão
- Investigar se diferenças de qualidade explicam diferenças nos resultados
- Ponderar importância de estudos individuais na síntese
- Orientar interpretação dos achados e determinar força das inferências

**Instrumentos de Qualidade**: Desenvolvidos considerando fatores que poderiam enviesar resultados dos estudos, incluindo itens genéricos relacionados ao desenho do estudo e itens específicos relacionados à área temática da revisão.

#### 3.2.4 Extração de Dados

Formulários padronizados de extração de dados foram desenvolvidos durante o protocolo e pilotados para garantir completude e usabilidade, incluindo:

**Informações do Estudo:**
- Identificação (autores, ano, periódico)
- Contexto educacional (nível, disciplina, duração)
- Metodologia de pesquisa
- Tamanho da amostra

**Dados Específicos sobre ABP:**
- Desafios identificados
- Métodos/instrumentos propostos
- Tecnologias utilizadas
- Resultados obtidos
- Limitações reportadas

A extração foi realizada com revisão reflexiva dos dados extraídos para garantir consistência e precisão.

#### 3.2.5 Síntese de Dados

A síntese de dados seguiu as diretrizes de Kitchenham (2004) para síntese descritiva, com informações extraídas tabuladas de maneira consistente com a questão de pesquisa para destacar semelhanças e diferenças entre resultados dos estudos.

**Síntese Descritiva**: As informações foram organizadas em tabelas estruturadas para identificar se resultados dos estudos são consistentes (homogêneos) ou inconsistentes (heterogêneos), com potenciais fontes de heterogeneidade investigadas.

## 4. Resultados

### 4.1 Processo de Seleção

A busca estruturada em camadas na Web of Science resultou em 882 registros (TY) nos arquivos RIS por camada. Após reter apenas registros com DOI e eliminar duplicatas entre camadas por DOI, obteve-se um conjunto consolidado com **301 artigos** (`consolidado_wos.ris`). Esses 301 foram triados por título e resumo no Rayyan, aplicando-se os critérios Kitchenham, resultando em **20 artigos** incluídos para a análise final.

[Figura placeholder: Fluxo consolidado de seleção (WOS/DOI/Rayyan) — inserir versão final no PDF.]

**Distribuição por Camadas (identificados; com DOI)**:
- **Camada 1** (Desafios Metodológicos): 255; 213
- **Camada 2** (Instrumentos e Tecnologias): 319; 266
- **Camada 3** (Objetividade e Escalabilidade): 120; 95
- **Camada 4** (Avaliação Processual): 1; 1
- **Camada 5** (Competências Transversais): 187; 158

[Gráfico placeholder: Registros com DOI por camada (n=733) — inserir versão final no PDF.]

<!-- Removido xychart-beta: não suportado no mermaid-cli -->

### 4.2 Caracterização dos Estudos (n=301)

Apresentamos a caracterização descritiva do conjunto consolidado de 301 artigos (após retenção de DOI e deduplicação): distribuição temporal, cobertura por camadas (interseção por DOI) e demais aspectos necessários para contextualizar os resultados e análises subsequentes.
#### 4.2.1 Distribuição Temporal (consolidado)

[Gráfico placeholder: Artigos por ano (n=301) — inserir versão final no PDF.]

<!-- Removido xychart-beta: manter apenas o gráfico de pizza -->



#### 4.2.3 Cobertura por Camada (consolidado)

Artigos do conjunto consolidado que aparecem em cada camada (interseção por DOI):

[Gráfico placeholder: Artigos (n=301) por camada (interseção) — inserir versão final no PDF.]

### 4.3 Análise dos Desafios Metodológicos

Com base na caracterização e no mapeamento por camadas, sintetizamos os desafios metodológicos recorrentes na literatura de ABP, destacando tendências, limitações e padrões que impactam diretamente a avaliação processual, a objetividade e a escalabilidade.
A análise dos 179 artigos selecionados revela padrões consistentes nos desafios enfrentados por professores orientadores na avaliação em ABP:

#### 4.3.1 Categorização Tecnológica dos Estudos

Table: Categorização tecnológica dos estudos incluídos na revisão sistemática

| Categoria Tecnológica | Artigos | Percentual |
|---------------------|---------|-------------|
| Programming Tools | 120 | 67,0% |
| General PBL | 26 | 14,5% |
| General Technology | 25 | 14,0% |
| Machine Learning/AI | 12 | 6,7% |
| Assessment Tools | 6 | 3,4% |
| Software Architecture | 6 | 3,4% |
| Digital Twins | 1 | 0,6% |
| Learning Analytics | 1 | 0,6% |
| Automated Assessment | 1 | 0,6% |

Fonte: Elaboração própria (2025).

<!-- Gráfico removido: será refeito após nova codificação temática -->

Fonte: Elaboração própria (2025).

#### 4.3.2 Classificação Metodológica

Table: Classificação metodológica dos estudos incluídos na revisão sistemática

| Tipo de Avaliação | Artigos | Percentual |
|------------------|---------|-------------|
| General Assessment | 104 | 58,1% |
| Formative Assessment | 38 | 21,2% |
| Summative Assessment | 21 | 11,7% |
| Peer Assessment | 14 | 7,8% |
| Self Assessment | 13 | 7,3% |
| Automated Assessment | 6 | 3,4% |
| Project Assessment | 4 | 2,2% |
| Portfolio Assessment | 2 | 1,1% |

Fonte: Elaboração própria (2025).

<!-- Gráfico removido: será refeito após classificação metodológica dos 20 estudos -->

Fonte: Elaboração própria (2025).

#### 4.3.3 Distribuição Geográfica

Table: Distribuição geográfica dos estudos incluídos na revisão sistemática

| País/Região | Artigos | Percentual |
|-------------|---------|-------------|
| International | 41 | 36,0% |
| USA | 31 | 27,2% |
| International - Medical | 15 | 13,2% |
| International - Science | 12 | 10,5% |
| Spain | 7 | 6,1% |
| Brazil | 2 | 1,8% |
| Outros | 13 | 7,2% |

Fonte: Elaboração própria (2025).

<!-- Gráfico removido: será refeito quando consolidarmos afiliação/país dos 20 estudos -->

Fonte: Elaboração própria (2025).

#### 4.3.4 Principais Lacunas Identificadas

**Tecnologias Emergentes Subutilizadas**:
- Digital Twins: apenas 1 artigo (0,6%)
- Automated Assessment: apenas 1 artigo (0,6%)
- Learning Analytics: apenas 1 artigo (0,6%)
- DevOps/CI-CD: apenas 1 artigo (0,6%)

**Concentração em Ferramentas Tradicionais**:
- 67% dos estudos focam em Programming Tools
- 58,1% abordam avaliação geral sem especificidade para ABP

### 4.4 Instrumentos e Tecnologias para Avaliação

#### 4.4.1 Rubricas e Critérios Avaliativos

As rubricas estruturadas foram identificadas como um dos instrumentos mais utilizados para avaliação em ABP:

1. **Rubricas Holísticas**: Avaliam o projeto como um todo em relação a critérios gerais de qualidade, sendo eficientes mas menos detalhadas.

2. **Rubricas Analíticas**: Avaliam aspectos específicos do projeto separadamente, oferecendo maior detalhamento mas requerendo mais tempo de aplicação.

3. **Rubricas de Desenvolvimento**: Focam na progressão das competências ao longo do projeto, alinhadas com a natureza processual da ABP.

#### 4.4.2 Sistemas de Avaliação Digital

Sistemas digitais especializados em avaliação de ABP demonstraram potencial para abordar múltiplos desafios:

1. **Plataformas de Gestão de Projetos**: Integram planejamento, execução e avaliação em ambientes digitais unificados.

2. **Portfólios Digitais**: Documentam a evolução do projeto e das competências ao longo do tempo, fornecendo evidências tangíveis de aprendizagem.

3. **Sistemas de Feedback Estruturado**: Automatizam aspectos do feedback formativo, aumentando a frequência e consistência do apoio aos estudantes.

### 4.5 Lacunas Persistentes e Oportunidades de Pesquisa

#### 4.5.1 Avaliação Processual

Apesar dos avanços, a avaliação eficaz de processos de aprendizagem em ABP ainda apresenta lacunas:

1. **Integração de Dados**: Falta de integração entre diferentes fontes de dados (técnicas, comportamentais, colaborativas) limita a visão holística da aprendizagem.

2. **Modelagem Temporal**: Dificuldade em modelar e avaliar a evolução não linear das competências ao longo de projetos complexos.

3. **Contextualização**: Desafios em adaptar critérios avaliativos para diferentes contextos e domínios de projeto.

### 4.6 Seleção Final dos Artigos (subconjunto para análise detalhada)

- Consolidado com DOI e deduplicado (entre camadas): 301
- Triados no Rayyan (título/resumo; Kitchenham): 301
- Selecionados para análise final: 20

#### 4.6.1 Estudos Incluídos (20 finais)

Table: Estudos primários incluídos na revisão sistemática

| # | Ano | Título |
| - | --- | ------ |
| 1 | 2017 | PBL-SEE: An Authentic Assessment Model for PBL-Based Software Engineering Education |
| 2 | 2019 | Design and Application of Project-Based Learning Methodologies for Small Groups Within Computer Fundamentals Subjects |
| 3 | 2025 | Project-Based Learning in Bioprocess Engineering: MATLAB Software as a Tool for Industrial-Scale Bioreactor Design |
| 4 | 2013 | System for Evaluating Groups When Applying Project-Based Learning to Surveying Engineering Education |
| 5 | 2022 | Project-Based Learning in Chemical Engineering: Curriculum and Assessment, Culture and Learning Spaces |
| 6 | 2013 | Using MBTI for the success assessment of engineering teams in project-based learning |
| 7 | 2020 | Active, experiential and reflective training in civil engineering: evaluation of a project-based learning proposal |
| 8 | 2023 | Integration of Project-Based Learning (PjBL) Methodology in the Course "Bioprocesses Applied to the Environment" |
| 9 | 2025 | Acquisition of transversal competencies through a project-based learning model for computer systems engineering students |
| 10 | 2025 | Implementation and benefits of hybrid methodology: Flipped classroom and project-based learning in mechanical engineering courses |
| 11 | 2022 | Case Study of Multi-Course Project-Based Learning and Online Assessment in Electrical Engineering Courses during COVID-19 Pandemic |
| 12 | 2024 | A Multi-Project Evaluation of Engineering Students' Performance for Online PBL: Taking the Sustainable Decision Analysis Course as an Example |
| 13 | 2016 | Multi-Role Project (MRP): A New Project-Based Learning Method for STEM |
| 14 | 2012 | Application of Project-Based Learning (PBL) to the Teaching of Electrical Power Systems Engineering |
| 15 | 2011 | An evaluation of a project-based learning initiative in engineering education |
| 16 | 2012 | A longitudinal evaluation of a project-based learning initiative in an engineering undergraduate programme |
| 17 | 2021 | Student Long-Term Perception of Project-Based Learning in Civil Engineering Education: An 18-Year Ex-Post Assessment |
| 18 | 2013 | Using the Project-Based Learning Approach for Incorporating an FPGA-Based Integrated Hardware/Software Tool for Implementing and Evaluating Image Processing Algorithms Into Graduate Level Courses |
| 19 | 2009 | Real-Time Quality Control Methods in PBL-Based Engineering Education |
| 20 | 2012 | Enhancing Project-Based Learning in Software Engineering Lab Teaching Through an E-Portfolio Approach |

Texto de enquadramento: Os 20 estudos abaixo foram triados a partir do conjunto consolidado (n=301) para discussão focalizada sobre avaliação em ABP na engenharia/STEM. Eles ilustram práticas e instrumentos recorrentes (rubricas, avaliação por pares, e‑portfólios) e evidenciam lacunas em objetividade, escalabilidade e monitoramento processual, que fundamentam o posicionamento desta pesquisa.

## 5. Discussão

### 5.1 Identificação da Lacuna de Pesquisa

Nesta subseção delineamos a lacuna central evidenciada pela revisão: a ausência de abordagens integradas que conectem objetivos educacionais, instrumentos e dados, processos computacionais de validação e arquiteturas de avaliação processual em tempo real, notadamente nas camadas de Informação, Computacional e Engenharia.
#### 5.1.1 Análise das Soluções Propostas

A literatura existente oferece diversas abordagens para os desafios da avaliação em ABP:

1. **Instrumentos avaliativos estruturados** (rubricas, checklists, portfólios)
2. **Sistemas digitais de avaliação** (plataformas LMS, ferramentas especializadas)
3. **Learning Analytics** (análise de dados educacionais, métricas técnicas)
4. **Tecnologias emergentes** (IA, machine learning, visualização de dados)

No entanto, identificou-se uma lacuna crítica: a ausência de soluções integradas que combinem princípos arquiteturais estabelecidos com a avaliação educacional em contextos complexos de ABP. Especificamente:

1. **Ausência de Abordagem Arquitetural Integrada**: Nenhuma pesquisa aplica frameworks arquiteturais estruturados para compreender o processo de ABP como um sistema complexo
2. **Falta de Integração Coerente**: Soluções atuais abordam aspectos isolados sem uma arquitetura unificada
3. **Deficiência na Modelagem de Objetivos Educacionais**: O desenvolvimento de competências não é adequadamente modelado como elemento orientador do sistema
4. **Limitações na Visibilidade Multidimensional**: Professores orientadores não dispõem de uma visão abrangente que integre múltiplas perspectivas do processo de avaliação

<!-- Gráfico removido: posicionamento será apresentado apenas em texto na Seção 5.2 -->

#### 5.1.2 Justificativa para a Lacuna Baseada nas Referências Fundamentais

**Fundamentação no PPC do Inteli (2024)**: A estrutura curricular do Inteli, organizada em Learning BackLogs (LBLs) que integram conhecimentos técnicos com competências transversais, demonstra a necessidade de abordagens avaliativas que capturem essa complexidade multidimensional. A experiência do Inteli evidencia que "a qualidade dos concluintes dos cursos de computação tradicionais não está atendendo às necessidades do mercado e do país" (Valente et al., 2025), justificando a necessidade de soluções inovadoras para avaliação em ABP.

**Fundamentação no Trabalho de Arakaki et al. (2025)**: A pesquisa da Cobenge revela questões metodológicas centrais que emergem da complexidade da ABP: "Como realizar a evolução sistemática dos módulos de aprendizagem baseados em projetos? Quais aspectos da aprendizagem devem ser utilizados como base para compor os requisitos de revisão?" Estas questões fundamentam a necessidade de uma abordagem estruturada e sistemática para avaliação em ABP.

**Fundamentação em Pressman \& Maxim (2021)**: A complexidade crescente dos sistemas de informação, que enfrentaram uma "esfera crescente de desafios" à medida que os problemas se tornaram mais complexos, justifica a aplicação de princípios de engenharia de software à avaliação educacional. Esta fundamentação teórica apoia a necessidade de soluções arquiteturalmente estruturadas para ABP.

### 5.2 Lacunas por Camada e Posicionamento

A seguir, antes de detalharmos os cinco gaps, enquadramos onde cada dimensão pesquisada apresenta um espaço substantivo para o encaixe desta pesquisa (com base nas métricas do consolidado de 301 artigos e na Seção 4.2.3):

- Enquadramento — Camada 1 (Empresarial): muitos estudos descrevem desafios e justificativas curriculares para ABP, mas raramente traduzem tais desafios em requisitos avaliativos mensuráveis e rastreáveis. Encaixe: nossa pesquisa parte de objetivos de aprendizagem explícitos e os desdobra em critérios e métricas operacionais para avaliação processual.
- Enquadramento — Camada 2 (Informação): embora presente em grande parte do consolidado (261/301), predominam instrumentos isolados (rubricas, checklists, e‑portfólios) e dados não integrados. Encaixe: propomos um modelo de informação integrador e interoperável, que unifica dados técnicos, colaborativos e formativos com rastreabilidade entre evidência, critérios e decisões.
- Enquadramento — Camada 3 (Computacional): a parcela de estudos com foco em objetividade/escala é menor (93/301) e carece de validação (confiabilidade/validade), padronização e automação. Encaixe: definimos um pipeline computacional para métricas objetivas e protocolos de validação (e.g., confiabilidade interavaliadores), alinhados a resultados do programa/curso.
- Enquadramento — Camada 4 (Engenharia): praticamente ausente no consolidado (1/301), evidenciando lacuna de arquiteturas para avaliação processual em tempo real (telemetria, eventos, feedback contínuo). Encaixe: adotamos uma arquitetura orientada a eventos para monitoramento contínuo e apoio à decisão pedagógica durante o processo.
- Enquadramento — Camada 5 (Tecnologia/Competências): há foco em resultados finais e percepções, com pouca objetivação da evolução das soft skills durante o projeto. Encaixe: instrumentamos competências transversais de modo processual, combinando dados de colaboração, participação e evidências observáveis ao longo do tempo.

A análise do conjunto consolidado (n=301) e a leitura focal dos 20 estudos indicam lacunas específicas em cada camada (visões inspiradas na ISO 10746):

- Camada 1 — Visão Empresarial (Desafios Metodológicos): descreve desafios de avaliação em ABP, porém raramente mapeia sistematicamente esses desafios para requisitos mensuráveis e operacionais de avaliação processual. Gap: ausência de tradução dos desafios em objetivos, métricas e critérios passíveis de instrumentação.
- Camada 2 — Visão de Informação (Instrumentos e Tecnologias): prevalecem instrumentos isolados (rubricas, checklists, e‑portfólios) com pouca integração de dados e esquemas informacionais padronizados. Gap: fragmentação de dados e ausência de modelos de informação que suportem integração e reuso.
- Camada 3 — Visão Computacional (Objetividade e Escalabilidade): escassez de validação de confiabilidade (ex.: interavaliadores), padronização de critérios, automação e benchmarking. Gap: falta de pipelines analíticos e protocolos de validação que elevem objetividade e escalabilidade.
- Camada 4 — Visão de Engenharia (Avaliação Processual em Tempo Real): praticamente ausente no consolidado (apenas 1 ocorrência), com pouco uso de telemetria, eventos e monitoramento contínuo. Gap: inexistência de arquiteturas para avaliação formativa processual e colaborativa em tempo real.
- Camada 5 — Visão de Tecnologia (Competências Transversais): foco frequente em resultados finais e percepções, com pouca instrumentação objetiva do desenvolvimento de competências transversais (trabalho em equipe, comunicação) ao longo do processo. Gap: baixa objetivação e mensuração processual das soft skills.

Posicionamento desta pesquisa: propomos uma abordagem arquitetural integrada que endereça, prioritariamente, as lacunas das Camadas 2, 3 e 4, mantendo o alinhamento com a Camada 1 (requisitos) e incorporando a Camada 5 (competências) como dimensão de dados. Os princípios são: (i) modelo de informação integrador para dados técnicos, colaborativos e formativos; (ii) pipeline computacional para métricas objetivas e validação (confiabilidade/validade); (iii) arquitetura orientada a eventos para monitoramento contínuo e feedback formativo; (iv) instrumentos interoperáveis que preservam rastreabilidade entre evidência, critérios e decisões. Essa orientação confere maior objetividade, escalabilidade e suporte processual à avaliação em ABP, mantendo o protocolo Kitchenham como base metodológica de transparência e reprodutibilidade.

### 5.3 Oportunidade de Pesquisa

A partir dos gaps mapeados e do posicionamento proposto, explicitamos as oportunidades para avançar o estado da arte: especificações arquiteturais, modelos de informação e pipelines de métricas/validação que permitam avaliação processual, colaborativa e escalável em ABP.
A aplicação de conceitos de arquitetura de sistemas e tecnologias emergentes para apoio a professores orientadores na avaliação em ABP representa uma oportunidade inexplorada na literatura:

#### 5.3.1 Potencial de Abordagens Arquiteturais

1. **Réplica em Tempo Real**: Criação de representações que espelham continuamente o estado do projeto através de múltiplas perspectivas integradas
2. **Integração de Dados Multidimensional**: Capacidade de integrar múltiplas fontes de dados (técnicas, comportamentais, colaborativas) em uma visão unificada
3. **Monitoramento Contínuo**: Acompanhamento em tempo real do progresso individual e coletivo através de diferentes perspectivas
4. **Simulação e Predição**: Capacidade de simular cenários e prever resultados com base em modelos estruturados

#### 5.3.2 Alinhamento com Necessidades dos Professores Orientadores

1. **Avaliação Processual Integrada**: Captura e avaliação contínua da evolução do aprendizado através de múltiplas perspectivas
2. **Personalização Baseada em Objetivos Educacionais**: Representação individualizada que permite avaliação personalizada alinhada com os objetivos educacionais
3. **Escalabilidade**: A automação permite escalar o apoio à avaliação para contextos complexos mantendo a qualidade
4. **Objetividade Fundamentada**: Base de dados objetivos que reduz a subjetividade inerente à avaliação humana

### 5.4 Direções para Pesquisas Futuras

Baseado na análise comprehensiva da literatura, emerge o potencial de abordagens integradas que combinem múltiplas perspectivas para apoiar professores orientadores. Neste contexto, frameworks arquiteturais estabelecidos na indústria podem oferecer uma estrutura conceitual valiosa para o desenvolvimento de soluções holísticas.

Tecnologias emergentes como Gêmeos Digitais, que criam representações virtuais de sistemas físicos em tempo real, poderiam ser exploradas para integrar múltiplas perspectivas em uma solução coerente para apoio à avaliação em ABP, fundamentada nos princípios identificados através das experiências do Inteli, metodologias propostas por Arakaki et al. (2025) e fundamentos de engenharia de software de Pressman \& Maxim (2021).

## 6 Considerações Finais

Esta revisão sistemática mapeou o estado da arte sobre os desafios metodológicos, instrumentos e tecnologias para auxiliar professores orientadores na avaliação em Aprendizagem Baseada em Projetos, identificando soluções propostas na literatura e lacunas que justificam investigações adicionais.

A análise revelou uma lacuna crítica na literatura: a ausência de soluções integradas que combinem princípios arquiteturais estabelecidos com o apoio a professores orientadores na avaliação educacional em contextos complexos de ABP. Esta lacuna é particularmente evidenciada pelas experiências documentadas no PPC do Inteli (2024), que demonstra a complexidade multidimensional dos Learning BackLogs (LBLs), pelas questões metodológicas fundamentais identificadas por Arakaki et al. (2025) sobre a evolução sistemática de módulos de ABP, e pelos princípios de engenharia de software de Pressman \& Maxim (2021) que justificam a necessidade de soluções arquiteturalmente estruturadas.

A aplicação de conceitos de tecnologias emergentes e arquitetura de sistemas para apoiar professores orientadores na avaliação em ABP emerge como uma oportunidade inexplorada que pode abordar múltiplos desafios simultaneamente: avaliação processual multidimensional, personalização baseada em objetivos educacionais, escalabilidade com manutenção da qualidade e objetividade fundamentada em dados estruturados.

A identificação desta lacuna de pesquisa, fundamentada nas três referências principais (PPC Inteli, trabalho de Arakaki et al. na Cobenge, e fundamentos de Pressman \& Maxim), justifica contundentemente a investigação de abordagens arquiteturais inovadoras para apoio a professores orientadores na avaliação em ABP, especialmente em contextos de engenharia de software de alta complexidade.

## Referências

Arakaki, R. et al. (2025). Aprimoramento Sistemático do PBL na Engenharia de Software: Um Método Baseado em Objetivos de Aprendizagem e Visões Arquiteturais. In: CONGRESSO BRASILEIRO DE EDUCAÇÃO EM ENGENHARIA (COBENGE), 53., 2025, Campinas. Anais [...]. Campinas: PUC-Campinas, 2025.

INTELI PPC. (2024). Projeto Pedagógico do Curso de Bacharelado em Engenharia de Software. Instituto de Tecnologia e Liderança. Disponível em: https://www.inteli.edu.br/engenharia-de-software. Acesso em: set. 2025.

ISO. (2009). ISO/IEC 10746-1:2009 Information technology — Open distributed processing — Reference model: Overview.

Kitchenham, B. (2004). Procedures for performing systematic reviews. Keele University Technical Report TR/SE-0401.

Pressman, R.; Maxim, B. (2021). Engenharia de Software: Uma Abordagem Profissional. 8. ed. Porto Alegre: AMGH. Revisão técnica: Reginaldo Arakaki.

Santos, C. M. C., Pimenta, C. A. M., \& Nobre, M. R. C. (2007). A estratégia PICO para a construção da pergunta de pesquisa e busca de evidências. Revista Latino-Americana de Enfermagem, 15(3), 502-507.

Valente, J. A.; Bittencourt, I. I.; Santoro, F. M.; Garcia, M.; Isotani, S.; Garcia, A.; Habimorad, M. (2025). O Ensino Superior de Computação Baseado em Projetos: o Inteli no caminho da inovação. Revista Brasileira de Informática na Educação, v. 33, p. 605-642.

Heliyon. (2022). A meta-analysis approach to measure the impact of project-based learning outcome with program attainment on student learning using fuzzy inference systems. Heliyon. https://doi.org/10.1016/j.heliyon.2022.e10248

Research Papers in Education. (2022). Problem-based learning, self- and peer assessment in higher education: towards advancing lifelong learning skills. Research Papers in Education. https://doi.org/10.1080/02671522.2020.1849371
