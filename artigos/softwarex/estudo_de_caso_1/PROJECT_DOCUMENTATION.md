# Afonsystem - Documentação Completa

## Índice
1. [Visão Geral](#visão-geral)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Classes e Arquitetura](#classes-e-arquitetura)
4. [Lógica de Código](#lógica-de-código)
5. [Diagramas UML](#diagramas-uml)
6. [Táticas Arquiteturais](#táticas-arquiteturais)

## Visão Geral

O Afonsystem é uma aplicação web Streamlit desenvolvida para análise de repositórios GitHub. A aplicação coleta dados de commits e pull requests de repositórios configurados, armazena-os em snapshots Parquet no Supabase Storage e fornece uma interface web para análise e visualização desses dados.

### Tecnologias Utilizadas
- **Streamlit**: Framework web para interface
- **PyGithub**: Integração com a API do GitHub
- **Supabase**: Banco de dados e armazenamento
- **Pandas**: Manipulação de dados
- **Plotly**: Visualização de dados
- **Pydantic**: Modelagem de dados com validação
- **Parquet**: Formato de armazenamento de dados

## Estrutura do Projeto

```
afonsystem/
├── app.py                     # Arquivo principal da aplicação Streamlit
├── requirements.txt           # Dependências do projeto
├── models/                    # Modelos de dados (Pydantic)
│   ├── commit.py             # Modelo de commit
│   ├── pull_request.py       # Modelo de pull request
│   └── snapshot.py           # Modelo de snapshot
├── helpers/                   # Módulos auxiliares
│   ├── __init__.py           # Exportação de módulos
│   ├── analytics_service.py  # Serviço de análise de dados
│   ├── app_config.py         # Configuração da aplicação
│   ├── data_analysis.py      # Funções de análise de dados
│   ├── data_collector.py     # Coletor de dados do GitHub
│   ├── data_formatter.py     # Formatação de dados
│   ├── database_helper.py    # Helper para banco de dados
│   ├── snapshot_manager.py   # Gerenciador de snapshots
│   ├── supabase_helper.py    # Helper para Supabase
│   └── ui_components.py      # Componentes de interface
├── repositories/              # Repositórios de dados
│   ├── commit_repository.py  # Repositório de commits
│   └── pull_request_repository.py # Repositório de pull requests
├── docs/                     # Documentação
└── ...
```

## Classes e Arquitetura

### Modelos de Dados (Pydantic)

#### Commit
- **sha**: Hash SHA do commit
- **message**: Mensagem do commit
- **author**: Autor do commit
- **date**: Data do commit
- **url**: URL do commit no GitHub

#### PullRequest
- **number**: Número do pull request
- **title**: Título do pull request
- **author**: Autor do pull request
- **state**: Estado do pull request (open/closed)
- **created_at**: Data de criação
- **url**: URL do pull request

#### SnapshotMetadata
- **timestamp**: Timestamp do snapshot
- **repository_name**: Nome do repositório
- **commits_count**: Contagem de commits
- **pull_requests_count**: Contagem de pull requests
- **snapshot_id**: ID único do snapshot
- **created_at**: Timestamp de criação

### Classes de Serviço

#### GitHubDataCollector
Classe responsável por coletar dados do GitHub:
- Conecta-se à API do GitHub usando token
- Coleta commits e pull requests de repositórios configurados
- Cria snapshots de dados usando SnapshotManager

#### SupabaseHelper
Classe para operações de armazenamento Supabase:
- Cria e gerencia snapshots Parquet
- Carrega dados de snapshots
- Lista e deleta snapshots
- Fornece resumos de snapshots

#### SnapshotManager
Classe para gerenciamento de snapshots:
- Cria snapshots Parquet de dados
- Faz upload para Supabase Storage
- Lista e obtém metadados de snapshots
- Carrega dados de snapshots

#### AnalyticsService
Serviço para análise de dados:
- Calcula KPIs de commits
- Fornece dados para visualização
- Filtra dados por intervalo de datas

#### CommitRepository e PullRequestRepository
Repositórios para persistência de dados:
- Operações CRUD para commits e pull requests
- Filtros por data, autor, tipo
- Agrupamentos e contagens

## Lógica de Código

### Fluxo Principal
1. A aplicação Streamlit inicia e configura o ambiente virtual
2. O usuário seleciona um trimestre e repositório
3. Um snapshot pode ser criado coletando dados do GitHub
4. Dados são armazenados em formato Parquet no Supabase Storage
5. O usuário seleciona um snapshot existente para análise
6. Dados são carregados e visualizações são renderizadas

### Coleta de Dados
- A aplicação usa PyGithub para acessar a API do GitHub
- Coleta commits e pull requests de repositórios configurados
- Dados são convertidos para DataFrames pandas
- DataFrames são salvos em formato Parquet em snapshots

### Armazenamento de Dados
- Dados são salvos em formato Parquet para eficiência
- Cada snapshot contém commits.parquet, pull_requests.parquet e metadata.json
- Snapshots são organizados por trimestre e repositório
- Armazenados no Supabase Storage

### Análise de Dados
- Commits são categorizados por tipo (feat, fix, docs, etc.)
- KPIs são calculados baseados em tipos de commits
- Visualizações são geradas com Plotly (gráficos de pizza, linha e barra)
- Dados podem ser filtrados por intervalo de datas e autor

## Diagramas UML

### Diagrama de Classes

```plantuml
@startuml
package "models" {
  class Commit {
    +sha: str
    +message: str
    +author: str
    +date: datetime
    +url: str
  }

  class PullRequest {
    +number: int
    +title: str
    +author: str
    +state: str
    +created_at: datetime
    +url: str
  }

  class SnapshotMetadata {
    +timestamp: str
    +repository_name: str
    +commits_count: int
    +pull_requests_count: int
    +snapshot_id: str
    +created_at: str
  }
}

package "helpers" {
  class GitHubDataCollector {
    -github_token: str
    -repo_names: List[str]
    -snapshot_manager: SnapshotManager
    +collect_and_create_snapshot(repo_name, progress_callback, quarter): str
    +get_available_repos(): List[str]
  }

  class SupabaseHelper {
    -url: str
    -key: str
    -client: Client
    -snapshot_manager: SnapshotManager
    +create_parquet_snapshot(): str
    +list_parquet_snapshots(): List[Dict]
    +load_snapshot_data(): pd.DataFrame
    +delete_parquet_snapshot(): bool
  }

  class SnapshotManager {
    -url: str
    -key: str
    -client: Client
    +create_repository_snapshot(): str
    +list_repository_snapshots(): List[Dict]
    +load_snapshot_data(): pd.DataFrame
    +get_snapshot_metadata(): Dict
    +delete_snapshot(): bool
  }

  class AnalyticsService {
    -commit_repo: CommitRepository
    -pr_repo: PullRequestRepository
    +get_commit_kpis(): Dict[str, int]
    +get_commits_data(): List[Dict]
    +get_pull_requests_data(): List[Dict]
  }
}

package "repositories" {
  abstract class Repository {
    +dataset_path: str
    +close()
  }

  class CommitRepository {
    -commits_file: str
    +_read_commits(): pd.DataFrame
    +get_commits_by_date_range(): List[dict]
    +count_commits_by_type(): int
    +get_commits_by_type_count(): List[dict]
  }

  class PullRequestRepository {
    -prs_file: str
    +_read_prs(): pd.DataFrame
    +get_pull_requests_by_date_range(): List[dict]
    +count_pull_requests_by_state(): int
    +get_pull_requests_by_state_count(): List[dict]
  }
}

Commit ||--|| CommitRepository : uses
PullRequest ||--|| PullRequestRepository : uses

GitHubDataCollector --> SnapshotManager : uses
SupabaseHelper --> SnapshotManager : uses
AnalyticsService --> CommitRepository : uses
AnalyticsService --> PullRequestRepository : uses
CommitRepository --|> Repository : extends
PullRequestRepository --|> Repository : extends
@enduml
```

### Diagrama de Sequência - Criação de Snapshot

```plantuml
@startuml
title Criação de Snapshot

actor User
participant "Streamlit UI" as UI
participant "GitHubDataCollector" as Collector
participant "Supabase Storage" as Storage
participant "SnapshotManager" as SM
participant "GitHub API" as GitHub

User -> UI: Clicar em "Criar Snapshot"
UI -> Collector: collect_and_create_snapshot()
Collector -> GitHub: get_repo(repo_name)
GitHub -> Collector: Repository object
Collector -> GitHub: get_commits()
GitHub -> Collector: Commits data
Collector -> GitHub: get_pulls(state='all')
GitHub -> Collector: Pull requests data
Collector -> SM: create_repository_snapshot()
SM -> Storage: upload commits.parquet
Storage -> SM: confirmation
SM -> Storage: upload pull_requests.parquet
Storage -> SM: confirmation
SM -> Storage: upload metadata.json
Storage -> SM: confirmation
SM -> Collector: snapshot_id
Collector -> UI: snapshot_id
UI -> User: Exibir resultado
@enduml
```

### Diagrama de Componentes

```plantuml
@startuml
package "Afonsystem Application" {
  [Streamlit UI] as UI
  [Data Collection] as DC
  [Data Storage] as DS
  [Data Analysis] as DA
  [Visualization] as VIZ
}

package "External Dependencies" {
  [GitHub API]
  [Supabase Storage]
  [Pandas]
  [Plotly]
}

UI --> DC : user input
UI --> DA : request data
UI --> VIZ : render charts
DC --> [GitHub API] : fetch data
DC --> DS : create snapshots
DS --> [Supabase Storage] : store data
DA --> DS : load data
DA --> [Pandas] : data processing
VIZ --> [Plotly] : create charts
VIZ --> UI : display results

note bottom of [Supabase Storage]
  Armazena snapshots Parquet
  Organizados por trimestre e repositório
end note

note bottom of [GitHub API]
  Coleta commits e pull requests
  Autenticação via token
end note
@enduml
```

## Táticas Arquiteturais

### 1. Persistência de Dados
- **Tática**: Armazenamento Parquet em nuvem
- **Implementação**: Dados são salvos em formato Parquet (colunar, eficiente) no Supabase Storage
- **Benefícios**: Compactação eficiente, leitura rápida de colunas específicas, armazenamento escalável

### 2. Isolamento de Dados
- **Tática**: Snapshots independentes
- **Implementação**: Cada coleta de dados gera um snapshot separado com metadados
- **Benefícios**: Histórico de estados, recuperação fácil, dados imutáveis para análise

### 3. Cache de Dados
- **Tática**: Cache de Streamlit
- **Implementação**: @st.cache_resource e @st.cache_data para objetos e dados
- **Benefícios**: Redução de chamadas à API e Supabase, melhor performance

### 4. Separação de Responsabilidades
- **Tática**: Padrão de repositórios e serviços
- **Implementação**: Repositórios para persistência, serviços para lógica de negócio
- **Benefícios**: Testabilidade, manutenibilidade, escalabilidade

### 5. Interface de Dados Tipada
- **Tática**: Pydantic para modelagem de dados
- **Implementação**: Modelos Pydantic com validação automática
- **Benefícios**: Validação de dados, documentação automática, segurança de tipo

### 6. Escalabilidade Horizontal
- **Tática**: Arquitetura stateless
- **Implementação**: Streamlit app sem estado de sessão crítico
- **Benefícios**: Fácil horizontal scaling, menor acoplamento

### 7. Integração com APIs Externas
- **Tática**: Abstração de clientes de API
- **Implementação**: GitHubDataCollector abstrai a API do GitHub
- **Benefícios**: Fácil substituição, testabilidade, centralização de lógica

### 8. Visualização de Dados
- **Tática**: Camada de visualização separada
- **Implementação**: Componentes UI separados da lógica de dados
- **Benefícios**: Facilidade de atualização de visualizações, reutilização de componentes