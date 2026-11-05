---
code: "MOD-207"
title: "Metodologia de Pesquisa Social (Quali/Quanti) e Ciência de Dados com Python (Pandas & SQL)"
slug: "metodologia-pesquisa-ciencia-dados-python-sql"
cycle: "ciclo-2"
cycleOrder: 2
moduleOrder: 7
axisId: "eixo-5"
secondaryAxisIds: ["eixo-2", "eixo-4"]
language: "pt-BR"
languageNotice: "Aviso de Idioma: Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em Português (PT-BR)."
estimatedHours: 50
status: "not_started"
progressPercent: 0
prerequisites: ["MOD-106", "MOD-206"]
tags:
  - "metodologia"
  - "pandas"
  - "sql"
  - "sqlite"
  - "ibge"
  - "base-dos-dados"
  - "pesquisa-social"
---

> **Aviso de Idioma:** Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em **Português (PT-BR)**.

# MOD-207: Metodologia de Pesquisa Social (Quali/Quanti) e Ciência de Dados com Python (Pandas & SQL)

## 1. Eixo e Carga Horária
- **Ciclo:** Ciclo 2: Teoria Revolucionária, Marxismo Ocidental, Crítica Cultural, Brasil e Engenharia de Software
- **Eixo principal:** Humanidades Digitais, Ciências Sociais Computacionais e Interesse Público
- **Carga horária estimada:** 50 horas
- **Pré-requisitos:** MOD-106, MOD-206

## 2. Tópicos e Autores Centrais
- Desenho de pesquisa: operacionalização de categorias teóricas (classe, anomia, patrimonialismo, segregação) em variáveis e indicadores empíricos.
- Métodos qualitativos e quantitativos: validade interna/externa, correlação vs. causalidade, viés de seleção e ética (LGPD).
- Consultas analíticas em SQL (SQLite/DuckDB) e manipulação vetorial com Pandas.
- Microdados públicos brasileiros (IBGE Censo/PNAD, TSE, INEP, DataSUS, RAIS) e visualização crítica com Matplotlib/Seaborn.

## 3. Bibliografia e Cursos Base Gratuitos (PT-BR)
- [Métodos de Pesquisa em Ciências Sociais (Bloco Quali e Quanti)](https://cebrap.org.br/) (CEBRAP / Sesc (Acesso Aberto))
- [Trilha de Dados Públicos com Python e SQL](https://basedosdados.org/docs/home) (ONG Base dos Dados (PT-BR))

## 4. Projeto Prático Avaliativo: Atlas Reprodutível de Estratificação Social e Capacidade Estatal Municipal
Pipeline SQL + Pandas cruzando indicadores socioeconômicos, demográficos e orçamentários dos 5.570 municípios brasileiros para testar hipóteses formuladas a partir do Ciclo 2.

### Entregáveis Obrigatórios
- Pipeline ETL reprodutível em Python + banco SQLite.
- Relatório metodológico com 5 visualizações de alta precisão analítica.

### Critérios de Avaliação
- Rigor metodológico e estatístico (taxas padronizadas, índices de Gini/Theil, deflação).
- Qualidade e reprodutibilidade do código.

### Diretório de Entrega
`projetos/ciclo-2/mod-207-atlas-estratificacao`
