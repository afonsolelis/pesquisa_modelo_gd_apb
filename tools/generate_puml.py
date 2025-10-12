#!/usr/bin/env python3
import re
from pathlib import Path

BASE = Path('modelagens ascii')
OUT_DIR = BASE / 'puml'
PNG_DIR = BASE / 'png'
OUT_DIR.mkdir(parents=True, exist_ok=True)
PNG_DIR.mkdir(parents=True, exist_ok=True)

def sanitize(name: str) -> str:
    # Create a PlantUML alias-friendly token
    token = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_")
    if not token:
        token = "P"
    # Avoid starting with number
    if token[0].isdigit():
        token = "P_" + token
    return token

def extract_participants(lines):
    # Find header line with columns of names followed by a line of '|'s
    for i in range(len(lines)-1):
        if '|' in lines[i+1] and set(lines[i+1].strip()) == {'|'}:
            # rare case, ignore
            continue
        if '|' in lines[i+1] and lines[i+1].count('|') >= 2 and re.search(r"\S\s+\S", lines[i]):
            header = lines[i].rstrip('\n')
            # Split by 2+ spaces
            parts = [p.strip() for p in re.split(r"\s{2,}", header) if p.strip()]
            if len(parts) >= 2:
                return parts
    # Fallback: try bullet list under "Participantes:" if present
    parts = []
    found = False
    for ln in lines:
        if ln.strip().lower().startswith('participantes'):
            found = True
            continue
        if found:
            if ln.strip().startswith('-'):
                parts.append(ln.split('-',1)[1].strip())
            else:
                break
    return parts or ["Ator1","Ator2"]

def extract_steps(lines):
    steps = []
    it = iter(range(len(lines)))
    start = None
    for i in it:
        if lines[i].lower().startswith('legenda dos passos') or lines[i].lower().startswith('legendas de passos'):
            start = i+1
            break
    if start is not None:
        for j in range(start, len(lines)):
            m = re.match(r"\[([A-Z])\]\s*(.*)", lines[j].strip())
            if m:
                steps.append((m.group(1), m.group(2)))
            elif lines[j].strip()=='' and steps:
                break
    return steps

def guess_subject_target(step_text, participants):
    # subject is first word, map to participant containing that word
    subject = None
    for p in participants:
        if re.search(r"\b"+re.escape(p.split()[0])+r"\b", step_text, re.IGNORECASE):
            subject = p
            break
    # pick a target mentioned in text different from subject
    target = None
    for p in participants:
        if subject and p == subject:
            continue
        if re.search(re.escape(p.split()[0]), step_text, re.IGNORECASE):
            target = p
            break
    # heuristic defaults
    if subject is None:
        subject = participants[0]
    if target is None and len(participants) > 1:
        target = participants[1]
    return subject, target

def build_puml(title, participants, steps):
    lines = []
    lines.append("@startuml")
    lines.append("autonumber")
    lines.append("skinparam ArrowColor #222")
    lines.append("skinparam NoteBackgroundColor #FFFDE7")
    # participants
    aliases = {}
    for p in participants:
        alias = sanitize(p)
        aliases[p] = alias
        lines.append(f'participant "{p}" as {alias}')
    lines.append(f'title {title}')
    # steps -> arrows or notes
    flows = MANUAL_FLOWS.get(title, [])
    if flows:
        for key, src, dst, label in flows:
            a_subj = aliases.get(src, sanitize(src))
            a_tgt = aliases.get(dst, sanitize(dst))
            lines.append(f'{a_subj} -> {a_tgt} : [{key}] {label}')
    else:
        for key, text in steps:
            subj, tgt = guess_subject_target(text, participants)
            a_subj = aliases.get(subj, sanitize(subj))
            a_tgt = aliases.get(tgt, sanitize(tgt))
            # arrow
            lines.append(f'{a_subj} -> {a_tgt} : [{key}] {text}')
    lines.append("@enduml")
    return "\n".join(lines)+"\n"

# Manual flows for PBL sequences: (step_key, source, target, label)
MANUAL_FLOWS = {
    'seq-pbl-01-aluno-inicia-atividade': [
        ('A', 'Aluno', 'LMS/Adalove', 'Inicia tarefa (card → fazendo)'),
        ('B', 'Aluno', 'Repositório', 'Commit/push da entrega'),
        ('C', 'Aluno', 'LMS/Adalove', 'Finaliza (card → feito e trava)'),
        ('D', 'LMS/Adalove', 'Professor', 'Notifica: aguardando correção'),
    ],
    'seq-pbl-02-professor-corrige-lanca-nota': [
        ('A', 'Professor', 'Repositório', 'Abre artefato para revisão'),
        ('B', 'Professor', 'LMS/Adalove', 'Registra feedback'),
        ('C', 'Professor', 'LMS/Adalove', 'Lança nota'),
        ('D', 'LMS/Adalove', 'Aluno', 'Notifica publicação de nota'),
    ],
    'seq-pbl-03-solicita-revisao-de-nota': [
        ('A', 'Aluno', 'LMS/Adalove', 'Abre pedido de revisão'),
        ('B', 'LMS/Adalove', 'Professor', 'Encaminha pedido ao professor'),
        ('C', 'Professor', 'LMS/Adalove', 'Atualiza/justifica nota'),
        ('D', 'LMS/Adalove', 'Aluno', 'Notifica resultado da revisão'),
        ('E', 'Aluno', 'Repositório', 'Ajusta artefato (se solicitado)'),
    ],
    'seq-pbl-04-onboarding-parceiro-e-tapi': [
        ('A', 'Parceiro', 'Escritório Projetos', 'Submete proposta'),
        ('B', 'Escritório Projetos', 'Coordenação', 'Triagem e agendamento'),
        ('C', 'Coordenação', 'Professores(Ori/Eixo)', 'Reunião de alinhamento'),
        ('D', 'Coordenação', 'Escritório Projetos', 'Aprova diretrizes / consolidar TAPI'),
        ('E', 'Escritório Projetos', 'LMS/Adalove', 'Publica TAPI e habilita módulo'),
        ('F', 'LMS/Adalove', 'Parceiro', 'Notifica publicação'),
    ],
    'seq-pbl-05-formacao-de-grupos': [
        ('A', 'Orientador', 'Secretaria', 'Define composição de grupos'),
        ('B', 'Secretaria', 'LMS/Adalove', 'Cadastra grupos'),
        ('C', 'LMS/Adalove', 'Aluno', 'Publica composição para a turma'),
        ('D', 'Aluno', 'LMS/Adalove', 'Confirma ciência'),
        ('E', 'LMS/Adalove', 'Orientador', 'Encerra fase e notifica'),
    ],
    'seq-pbl-06-alocacao-de-repositorio-ao-grupo': [
        ('A', 'Automação GitHub', 'Repositório', 'Cria repositório por grupo'),
        ('B', 'Automação GitHub', 'Aluno', 'Envia convites de acesso'),
        ('C', 'Aluno', 'Repositório', 'Aceita convite e testa acesso'),
        ('D', 'Automação GitHub', 'LMS/Adalove', 'Informa URL e status para registro'),
    ],
    'seq-pbl-07-planning-definicao-de-metas': [
        ('A', 'Grupo', 'Orientador', 'Inicia Planning (1ª aula)'),
        ('B', 'Orientador', 'Grupo', 'Conduz e valida escopo'),
        ('C', 'Grupo', 'Kanban (software de apoio)', 'Cria/estima cards'),
        ('D', 'Orientador', 'Kanban (software de apoio)', 'Aprova backlog'),
    ],
    'seq-pbl-08-criacao-de-branch': [
        ('A', 'Aluno', 'Repositório', 'Cria branch e push inicial'),
        ('B', 'Repositório', 'CI/CD', 'Dispara pipeline inicial'),
    ],
    'seq-pbl-09-abertura-de-item-parceiro': [
        ('A', 'Parceiro', 'Sistema Ágil', 'Registra novo item/requisito'),
        ('B', 'Grupo', 'Sistema Ágil', 'Prioriza/posiciona item com orientação'),
    ],
    'seq-pbl-10-daily-com-impedimento': [
        ('A', 'Aluno', 'Grupo', 'Reporta impedimento'),
        ('B', 'Grupo', 'Orientador', 'Aciona orientador'),
        ('C', 'Orientador', 'LMS/Adalove', 'Registra orientação/escalação'),
        ('D', 'Orientador', 'Grupo', 'Retorno e plano de ação'),
    ],
    'seq-pbl-11-pull-request-e-revisao': [
        ('A', 'Autor PR', 'Repositório', 'Abre PR'),
        ('B', 'Repositório', 'Revisor', 'Notifica revisão / checks'),
        ('C', 'Revisor', 'Autor PR', 'Comenta ou solicita mudanças'),
        ('D', 'Autor PR', 'Repositório', 'Envia ajustes até aprovação'),
    ],
    'seq-pbl-12-merge-e-integracao': [
        ('A', 'Revisor', 'Repositório', 'Executa merge'),
        ('B', 'Repositório', 'CI/CD', 'Pipeline de integração'),
        ('C', 'CI/CD', 'Grupo', 'Status de build (verde/vermelho)'),
    ],
    'seq-pbl-13-falha-de-build-e-correcao': [
        ('A', 'CI/CD', 'Grupo', 'Notifica falha de build'),
        ('B', 'Grupo', 'Autor', 'Designa responsável'),
        ('C', 'Autor', 'Repositório', 'Commit/push da correção'),
        ('D', 'Repositório', 'CI/CD', 'Reexecuta pipeline'),
    ],
    'seq-pbl-14-registro-de-presenca': [
        ('A', 'Aluno', 'LMS/Adalove', 'Check-in de presença'),
        ('B', 'LMS/Adalove', 'Professor', 'Envio de lista para conferência'),
        ('C', 'LMS/Adalove', 'Aluno', 'Confirmação de presença'),
    ],
    'seq-pbl-15-entrega-de-autoestudo': [
        ('A', 'Aluno', 'LMS/Adalove', 'Entrega autoestudo'),
        ('B', 'LMS/Adalove', 'Professor', 'Notifica para correção'),
        ('C', 'LMS/Adalove', 'Aluno', 'Confirmação de envio'),
    ],
    'seq-pbl-16-feedback-de-autoestudo': [
        ('A', 'Professor', 'LMS/Adalove', 'Registra rubrica e comentários'),
        ('B', 'LMS/Adalove', 'Aluno', 'Notifica feedback'),
        ('C', 'Professor', 'LMS/Adalove', 'Ajusta nota se necessário'),
    ],
    'seq-pbl-17-solicitacao-de-extensao-de-prazo': [
        ('A', 'Aluno', 'Professor', 'Solicita prorrogação'),
        ('B', 'Professor', 'LMS/Adalove', 'Aprova/nega e registra'),
        ('C', 'LMS/Adalove', 'Aluno', 'Notifica decisão'),
    ],
    'seq-pbl-18-pitch-com-parceiro': [
        ('A', 'Grupo', 'Parceiro', 'Apresenta pitch'),
        ('B', 'Parceiro', 'Professores', 'Fornece feedback'),
        ('C', 'Professores', 'LMS/Adalove', 'Registra notas/observações'),
        ('D', 'LMS/Adalove', 'Grupo', 'Consolida feedbacks'),
    ],
    'seq-pbl-19-retrospectiva-pos-pitch': [
        ('A', 'Grupo', 'Orientador', 'Apresenta aprendizados'),
        ('B', 'Orientador', 'Grupo', 'Consolida ações de melhoria'),
        ('C', 'Grupo', 'Sistema Ágil', 'Registra ações e ajustes de backlog'),
        ('D', 'Sistema Ágil', 'Parceiro', 'Confirmações quando impactar escopo'),
    ],
    'seq-pbl-20-mudanca-no-tapi': [
        ('A', 'Parceiro', 'Coordenação', 'Propõe alteração de escopo'),
        ('B', 'Coordenação', 'LMS/Adalove', 'Aprova/nega no LMS'),
        ('C', 'LMS/Adalove', 'Turma', 'Publica nova versão do TAPI'),
    ],
    'seq-pbl-21-escalonamento-de-bloqueio': [
        ('A', 'Aluno', 'Orientador', 'Relata bloqueio sem solução'),
        ('B', 'Orientador', 'Coordenação', 'Escala para coordenação'),
        ('C', 'Coordenação', 'LMS/Adalove', 'Registra decisão'),
    ],
    'seq-pbl-22-mentoria-da-sprint': [
        ('A', 'Orientador', 'LMS/Adalove', 'Agenda mentoria da sprint'),
        ('B', 'LMS/Adalove', 'Grupo', 'Notifica pautas e horário'),
        ('C', 'Orientador', 'Grupo', 'Devolutiva: notas individuais e de artefatos'),
        ('D', 'Orientador', 'LMS/Adalove', 'Lança notas e feedbacks'),
        ('E', 'LMS/Adalove', 'Aluno', 'Notifica publicação'),
    ],
    'seq-pbl-23-encerramento-de-sprint': [
        ('A', 'Sistema Ágil', 'Grupo', 'Sinaliza fechamento'),
        ('B', 'Automação GitHub', 'Repositório', 'Gera tag/release'),
    ],
    'seq-pbl-24-preparacao-de-demonstracao-final': [
        ('A', 'Grupo', 'Professores', 'Envia roteiro e agenda ensaio'),
        ('B', 'Professores', 'Parceiro', 'Revisão e confirmação'),
        ('C', 'Parceiro', 'LMS/Adalove', 'Confirma disponibilidade'),
        ('D', 'Grupo', 'LMS/Adalove', 'Envia material final'),
    ],
    'seq-pbl-25-encerramento-de-modulo': [
        ('A', 'Coordenação', 'Automação GitHub', 'Inicia fechamento do módulo'),
        ('B', 'Automação GitHub', 'Repositório', 'Consolida tags/releases'),
        ('C', 'Automação GitHub', 'EP (Escritório Projetos)', 'Envia dossiê técnico'),
        ('D', 'LMS/Adalove', 'Secretaria', 'Consolida notas/presenças/autoestudos'),
    ],
}

def build_puml_dt(title, participants, steps):
    lines = []
    lines.append("@startuml")
    lines.append("autonumber")
    aliases = {}
    for p in participants:
        a = sanitize(p)
        aliases[p] = a
        lines.append(f'participant "{p}" as {a}')
    lines.append(f'title {title}')
    flows = MANUAL_FLOWS_DT.get(title, [])
    if flows:
        for key, src, dst, label in flows:
            a_subj = aliases.get(src, sanitize(src))
            a_tgt = aliases.get(dst, sanitize(dst))
            lines.append(f'{a_subj} -> {a_tgt} : [{key}] {label}')
    else:
        for key, text in steps:
            s, t = guess_subject_target(text, participants)
            lines.append(f'{aliases[s]} -> {aliases[t]} : [{key}] {text}')
    lines.append("@enduml")
    return "\n".join(lines)+"\n"

MANUAL_FLOWS_DT = {
    'SEQ-B22-coleta-periodica-de-eventos': [
        ('A','Agendador','Conectores','Dispara coleta'),
        ('B','Conectores','Camada de Coleta','Extrai e normaliza'),
        ('C','Camada de Coleta','CEP','Envia lote validado'),
    ],
    'SEQ-B23-deteccao-de-anomalia-de-atividade': [
        ('A','CEP','Orientador','Alerta de anomalia'),
        ('B','Orientador','Grupo','Abre investigação/contato'),
        ('C','Grupo','Sistema Ágil','Atualiza plano/status'),
    ],
    'seq-dt-01-ingestao-lote-validacao-schema': [
        ('A','Sistema Fonte','Conector','Exporta lote'),
        ('B','Conector','Camada de Coleta','Normaliza e enriquece'),
        ('C','Camada de Coleta','ValidadorSchema','Valida schema'),
        ('D','Camada de Coleta','CEP','Entrega eventos válidos (com LoteIngestao)'),
    ],
    'seq-dt-02-evento-presenca-pipeline': [
        ('A','LMS (SistemaFonte)','Conector LMS','Emite EventoPresenca'),
        ('B','Conector LMS','Camada Coleta','Padroniza/pseudonimiza'),
        ('C','Camada Coleta','CEP','Valida e agrega ao lote'),
        ('D','CEP','Bronze','Persiste cru por data/fonte'),
        ('E','CEP','Conector LMS','Confirma recebimento'),
    ],
    'seq-dt-03-evento-entrega-artefato-rastreabilidade': [
        # Inclusão de participação explícita de Aluno e Grupo conforme revisão
        ('A','Aluno','Repositório','Commit/push gera webhook de entrega'),
        ('B','Repositório','Conector Git','Webhook push/tag/release'),
        ('C','Conector Git','Camada Coleta','Monta EventoEntrega (repo, sha, path)'),
        ('D','Camada Coleta','CEP','Valida e define vínculos (Sprint/Grupo)'),
        ('E','CEP','Silver','Grava ordenado/dedup por event_time'),
        ('F','CEP','Conector Git','Confirma referência Artefato↔Evento'),
        ('G','CEP','Grupo','Notifica registro de entrega (referendo/ack)'),
    ],
    'seq-dt-04-deduplicacao-idempotencia': [
        ('A','Conector','Coleta','Envia eventos com id e checksum'),
        ('B','Coleta','Deduplicador','Checa idempotência (chave id+checksum+origem)'),
        ('C','Deduplicador','CEP','Elimina duplicados; encaminha únicos'),
        ('D','CEP','Bronze/Silver','Persiste apenas novos eventos'),
    ],
    'seq-dt-05-eventos-atrasados-watermark': [
        ('A','Conector','Coleta','Evento atrasado chega'),
        ('B','Coleta','CEP (Janela)','Encaminha'),
        ('C','CEP (Janela)','Materialização','Reabre janela/recalcula ou roteia tardio'),
    ],
    'seq-dt-06-correlacao-join-por-chaves': [
        ('A','Eventos A (Entrega)','CEP (Join por keys)','Entrega'),
        ('B','Eventos B (Feedback)','CEP (Join por keys)','Feedback'),
        ('C','CEP (Join por keys)','Materialização','Visão correlacionada'),
    ],
    'seq-dt-07-validacao-versao-schema-migracao': [
        ('A','Conector','Catálogo de Schemas','Consulta vN'),
        ('B','Catálogo de Schemas','Conector','Regras compatibilidade'),
        ('C','Conector','ValidadorSchema','Migração vN-1→vN'),
        ('D','ValidadorSchema','CEP','Entrega eventos com VersaoSchema'),
    ],
    'seq-dt-08-erro-validacao-dlq-correcao': [
        ('A','Conector','Coleta','Envia lote'),
        ('B','Coleta','ValidadorSchema','Valida eventos'),
        ('C','ValidadorSchema','DLQ','Roteia inválidos'),
        ('D','Conector','Coleta','Corrige e reenvia'),
        ('E','Coleta','CEP','Entrega corrigidos'),
    ],
    'seq-dt-09-replay-reprocessamento-controlado': [
        ('A','Operação','CEP','Solicita replay de janela'),
        ('B','CEP','Bronze/Silver/Gold','Reprocessa camadas'),
        ('C','Bronze/Silver/Gold','Materialização','Atualiza materializações'),
    ],
    'seq-dt-10-materializacao-sinais-para-docente': [
        # Sinais para docentes e visões para grupo/aluno (notificação mínima)
        ('A','CEP (Agregações)','Silver','Calcula agregações'),
        ('B','Silver','Gold (Sinais)','Persiste sinais'),
        ('C','Gold (Sinais)','Painel Docente','Disponibiliza sinais consolidados'),
        ('D','Gold (Sinais)','Grupo','Disponibiliza/Notifica sinais por grupo e artefato'),
        ('E','Gold (Sinais)','Aluno','Disponibiliza/Notifica sinais individuais'),
    ],
    'seq-dt-11-compl-pbl-01-aluno-inicia-atividade': [
        ('A','Aluno','LMS/Adalove','Inicia tarefa'),
        ('B','Aluno','Repositório','Commit/push'),
        ('C','Conector Git','CEP','Webhook/EventoEntrega'),
        ('D','Aluno','LMS/Adalove','Finaliza/lock'),
        ('E','Conector Git','CEP','Evento de lock/entrega'),
        ('F','CEP','Grupo','Notifica status de atividade/entrega do grupo'),
        ('G','CEP','Aluno','Confirma registro de atividade/entrega'),
    ],
    'seq-dt-12-compl-pbl-02-professor-corrige-lanca-nota': [
        ('A','Professor','LMS/Adalove','Lança nota/feedback'),
        ('B','Conector LMS','CEP','EventoFeedback padronizado'),
        ('C','CEP','Grupo','Emite evento de nota por grupo/artefato'),
        ('D','CEP','Aluno','Emite evento de nota individual'),
    ],
    'seq-dt-13-compl-pbl-03-revisao-de-nota': [
        ('A','Aluno','LMS/Adalove','Solicita revisão'),
        ('B','LMS/Adalove','Professor','Encaminha pedido'),
        ('C','Conector LMS','CEP','EventoGenerico revisao_nota'),
        ('D','CEP','Grupo','Notifica revisão/ajuste de avaliação'),
        ('E','LMS/Adalove','Aluno','Resultado da revisão'),
    ],
    'seq-dt-14-compl-pbl-07-planning-kanban': [
        ('A','Grupo','Sistema Ágil','Criação/estimativas de cards'),
        ('B','Orientador','Sistema Ágil','Ajustes/aprovação'),
        ('C','Conector Ágil','CEP','kanban_change / estimation_set'),
    ],
    'seq-dt-15-compl-pbl-08-branch-github': [
        ('A','Aluno','Repositório','Create branch/push'),
        ('B','Repositório','Webhook GitHub','Evento create/ref'),
        ('C','Webhook GitHub','Conector Git','Entrega webhook'),
        ('D','Conector Git','CEP','Ingestão evento'),
    ],
    'seq-dt-16-compl-pbl-11-presenca': [
        ('A','Aluno','LMS/Adalove','Check-in'),
        ('B','Conector LMS','CEP','EventoPresenca padronizado'),
    ],
    'seq-dt-17-compl-pbl-15-autoestudo': [
        ('A','Aluno','LMS/Adalove','Entrega autoestudo'),
        ('B','Conector LMS','CEP','EventoAutoestudo padronizado'),
    ],
    'seq-dt-18-compl-pbl-18-pitch': [
        ('A','Grupo','Parceiro','Apresentação'),
        ('B','Parceiro','LMS/Adalove','Feedback/observações'),
        ('C','Conector LMS','CEP','Evento pitch_feedback'),
    ],
    'seq-dt-19-compl-pbl-23-encerramento-sprint': [
        ('A','Sistema Ágil','Automação GitHub','Fechar sprint'),
        ('B','Automação GitHub','Repositório','Tag/release snapshot'),
        ('C','Repositório','Conector Git','Eventos de release'),
        ('D','Conector Git','CEP','Materialização de encerramento'),
    ],
    'seq-dt-20-compl-pbl-25-encerramento-modulo': [
        ('A','Coordenação','Automação GitHub','Iniciar fechamento'),
        ('B','Repositório','Conector Git','Gerar pacote técnico'),
        ('C','Conector Git','CEP/EP','Enviar eventos e pacote'),
    ],
}

def main():
    # PBL
    pbl_files = sorted(BASE.glob('seq-pbl-*.txt'))
    for i, path in enumerate(pbl_files, 1):
        txt = path.read_text(encoding='utf-8').splitlines()
        parts = extract_participants(txt)
        steps = extract_steps([l.strip() for l in txt])
        title = Path(path).stem
        puml = build_puml(title, parts, steps)
        out = OUT_DIR / (Path(path).stem + '.puml')
        out.write_text(puml, encoding='utf-8')
    # Digital Twin
    dt_dir = BASE / 'digital-twin'
    dt_out = dt_dir / 'puml'
    dt_out.mkdir(parents=True, exist_ok=True)
    dt_files = sorted(dt_dir.glob('*.txt'))
    for path in dt_files:
        txt = path.read_text(encoding='utf-8').splitlines()
        parts = extract_participants(txt)
        steps = extract_steps([l.strip() for l in txt])
        title = Path(path).stem
        puml = build_puml_dt(title, parts, steps)
        out = dt_out / (Path(path).stem + '.puml')
        out.write_text(puml, encoding='utf-8')
    print(f"Generated {len(list(OUT_DIR.glob('*.puml')))} PUML files in {OUT_DIR} and {len(list(dt_out.glob('*.puml')))} in {dt_out}")

if __name__ == '__main__':
    main()
