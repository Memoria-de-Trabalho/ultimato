---
code: "MOD-106"
title: "Fundamentos de Python e Controle de Versão (Git/GitHub)"
slug: "fundamentos-python-git"
cycle: "ciclo-1"
cycleOrder: 1
moduleOrder: 6
axisId: "eixo-2"
secondaryAxisIds: ["eixo-1"]
language: "pt-BR"
languageNotice: "Aviso de Idioma: Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em Português (PT-BR)."
estimatedHours: 60
status: "not_started"
progressPercent: 0
prerequisites: ["MOD-102"]
tags:
  - "python"
  - "git"
  - "github"
  - "automacao"
  - "arquivos"
  - "cli"
---

> **Aviso de Idioma:** Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em **Português (PT-BR)**.

# MOD-106: Fundamentos de Python e Controle de Versão (Git/GitHub)

## 1. Eixo e Carga Horária
- **Ciclo:** Ciclo 1: Fundamentos Ontológicos, Clássicos e Computacionais
- **Eixo principal:** Engenharia de Software Prática com Python
- **Carga horária estimada:** 60 horas
- **Pré-requisitos:** MOD-102

## 2. Tópicos e Autores Centrais
- Tipos nativos, compreensões de listas/dicionários, funções e modularização em Python 3.
- Manipulação robusta de arquivos (CSV, JSON, Markdown) e codificações de caracteres (UTF-8 vs ISO-8859-1).
- Tratamento de exceções, ambientes virtuais isolados (venv) e linha de comando (argparse).
- Fluxo profissional de Git: commits atômicos, branches, merge, rebase e Pull Requests.

## 3. Bibliografia e Cursos Base Gratuitos (PT-BR)
- [Introdução à Ciência da Computação com Python (Partes 1 e 2)](https://www.coursera.org/learn/ciencia-computacao-python-conceitos) (USP / Coursera (Modo Ouvinte Gratuito))
- [Pro Git Book (2ª Edição em Português)](https://git-scm.com/book/pt-br/v2) (Scott Chacon & Ben Straub (Oficial Git))

## 4. Projeto Prático Avaliativo: Higienizador e Validador de Dados Eleitorais e Demográficos Brutos
Ferramenta em Python versionada com Git que ingere arquivos CSV brutos do TSE/IBGE, corrige problemas de codificação, valida esquemas e gera relatórios em JSON e Markdown.

### Entregáveis Obrigatórios
- Repositório Git com histórico limpo de commits semânticos em PT-BR.
- Módulo Python de ingestão, limpeza e exportação.

### Critérios de Avaliação
- Tratamento seguro de erros de I/O e codificação.
- Organização modular limpa.

### Diretório de Entrega
`projetos/ciclo-1/mod-106-validador-dados`