---
code: "MOD-202"
title: "Engenharia de Software Moderna, POO e Arquitetura com Python"
slug: "engenharia-software-poo-arquitetura-python"
cycle: "ciclo-2"
cycleOrder: 2
moduleOrder: 2
axisId: "eixo-2"
secondaryAxisIds: []
language: "pt-BR"
languageNotice: "Aviso de Idioma: Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em Português (PT-BR)."
estimatedHours: 80
status: "not_started"
progressPercent: 0
prerequisites: ["MOD-102", "MOD-106"]
tags:
  - "engenharia-de-software"
  - "poo"
  - "design-patterns"
  - "solid"
  - "arquitetura"
  - "python"
---

> **Aviso de Idioma:** Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em **Português (PT-BR)**.

# MOD-202: Engenharia de Software Moderna, POO e Arquitetura com Python

## 1. Eixo e Carga Horária
- **Ciclo:** Ciclo 2: Teoria Revolucionária, Marxismo Ocidental, Crítica Cultural, Brasil e Engenharia de Software
- **Eixo principal:** Engenharia de Software Prática com Python
- **Carga horária estimada:** 80 horas
- **Pré-requisitos:** MOD-102, MOD-106

## 2. Tópicos e Autores Centrais
- Programação Orientada a Objetos em Python: classes, composição vs. herança, dataclasses e protocolos.
- Tipagem estática gradual e validação de esquemas com typing e Pydantic.
- Princípios SOLID, alta coesão, baixo acoplamento e inversão de dependência.
- Design Patterns pragmáticos: Repository, Adapter, Strategy e Factory.
- Arquitetura em camadas e empacotamento moderno com pyproject.toml.

## 3. Bibliografia e Cursos Base Gratuitos (PT-BR)
- [Engenharia de Software Moderna](https://engsoftmoderna.info/) (Prof. Marco Tulio Valente (DCC/UFMG))
- [Catálogo de Padrões de Projeto em Python](https://refactoring.guru/pt-br/design-patterns/python) (Refactoring.Guru (PT-BR))

## 4. Projeto Prático Avaliativo: SDK Python para APIs de Transparência Pública (br-transparencia-sdk)
Desenvolvimento de pacote Python instalável e desacoplado para consulta unificada às APIs da Câmara dos Deputados, Senado e Portal da Transparência com cache local e modelos tipados.

### Entregáveis Obrigatórios
- Pacote Python estruturado com pyproject.toml.
- Diagrama de arquitetura em Mermaid e documentação de API.

### Critérios de Avaliação
- Desacoplamento limpo entre cliente HTTP, adaptadores e domínio.
- Uso idiomático de tipagem e tratamento de falhas.

### Diretório de Entrega
`projetos/ciclo-2/mod-202-sdk-transparencia`
