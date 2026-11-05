---
code: "MOD-204"
title: "Qualidade de Software, Testes Automatizados, CI/CD e Auditoria de Código"
slug: "qualidade-testes-cicd-auditoria"
cycle: "ciclo-2"
cycleOrder: 2
moduleOrder: 4
axisId: "eixo-2"
secondaryAxisIds: ["eixo-3"]
language: "pt-BR"
languageNotice: "Aviso de Idioma: Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em Português (PT-BR)."
estimatedHours: 60
status: "not_started"
progressPercent: 0
prerequisites: ["MOD-202"]
tags:
  - "pytest"
  - "tdd"
  - "ci-cd"
  - "github-actions"
  - "auditoria-de-codigo"
  - "reprodutibilidade"
---

> **Aviso de Idioma:** Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em **Português (PT-BR)**.

# MOD-204: Qualidade de Software, Testes Automatizados, CI/CD e Auditoria de Código

## 1. Eixo e Carga Horária
- **Ciclo:** Ciclo 2: Teoria Revolucionária, Marxismo Ocidental, Crítica Cultural, Brasil e Engenharia de Software
- **Eixo principal:** Engenharia de Software Prática com Python
- **Carga horária estimada:** 60 horas
- **Pré-requisitos:** MOD-202

## 2. Tópicos e Autores Centrais
- Pirâmide de testes: testes unitários, de integração e de contrato com pytest.
- Isolamento de dependências externas com mocks, fixtures e gravação de respostas HTTP.
- Análise estática, formatação, minificação e auditoria de vulnerabilidades (ruff, pip-audit).
- Integração Contínua (CI) com GitHub Actions e reprodutibilidade científica de código.

## 3. Bibliografia e Cursos Base Gratuitos (PT-BR)
- [Engenharia de Software Moderna: Capítulos 8 (Testes) e 10 (DevOps)](https://engsoftmoderna.info/) (Prof. Marco Tulio Valente (DCC/UFMG))

## 4. Projeto Prático Avaliativo: Suíte de Testes (>85%), CI/CD e Laudo de Auditoria de Dependências
Instrumentar o SDK do MOD-202 e o Motor de Constelações do MOD-203 com cobertura de testes superior a 85%, pipeline GitHub Actions e relatório SBOM.

### Entregáveis Obrigatórios
- Suíte pytest com fixtures e mocks determinísticos.
- Workflow .github/workflows/ci.yml e relatório de auditoria.

### Critérios de Avaliação
- Execução 100% determinística e offline da suíte de testes.
- Rigor na verificação de segurança e licenças.

### Diretório de Entrega
`projetos/ciclo-2/mod-204-auditoria-e-testes`
