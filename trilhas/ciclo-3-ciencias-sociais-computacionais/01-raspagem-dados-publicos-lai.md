---
code: "MOD-301"
title: "Engenharia de Raspagem de Dados Públicos (Web Scraping), LAI e Arquivo a Contrapelo"
slug: "raspagem-dados-publicos-lai-arquivo-contrapelo"
cycle: "ciclo-3"
cycleOrder: 3
moduleOrder: 1
axisId: "eixo-5"
secondaryAxisIds: ["eixo-2", "eixo-3"]
language: "pt-BR"
languageNotice: "Aviso de Idioma: Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em Português (PT-BR)."
estimatedHours: 60
status: "not_started"
progressPercent: 0
prerequisites: ["MOD-202", "MOD-203", "MOD-207"]
tags:
  - "web-scraping"
  - "lai"
  - "httpx"
  - "beautifulsoup"
  - "walter-benjamin"
  - "diarios-oficiais"
---

> **Aviso de Idioma:** Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em **Português (PT-BR)**.

# MOD-301: Engenharia de Raspagem de Dados Públicos (Web Scraping), LAI e Arquivo a Contrapelo

## 1. Eixo e Carga Horária
- **Ciclo:** Ciclo 3: Ciências Sociais Computacionais, Políticas Públicas e Ferramentas de Interesse Público
- **Eixo principal:** Humanidades Digitais, Ciências Sociais Computacionais e Interesse Público
- **Carga horária estimada:** 60 horas
- **Pré-requisitos:** MOD-202, MOD-203, MOD-207

## 2. Tópicos e Autores Centrais
- Lei de Acesso à Informação (LAI: Lei 12.527/2011) e transparência ativa vs. passiva.
- Construção de coletores resilientes com httpx, BeautifulSoup4, Playwright e pdfplumber.
- Raspagem ética: rate-limiting, cache imutável de evidências brutas e logs estruturados.
- O raspador como 'Colecionador Benjaminiano': preservar rastros administrativos e contratos públicos contra o apagamento oficial ('escovar a história a contrapelo').

## 3. Bibliografia e Cursos Base Gratuitos (PT-BR)
- [Tutoriais de Raspagem de Dados e LAI](https://escoladedados.org/tutoriais/) (Escola de Dados / Open Knowledge Brasil)
- [Arquitetura do Projeto Querido Diário](https://queridodiario.ok.org.br/) (Open Knowledge Brasil)

## 4. Projeto Prático Avaliativo: Coletor Resiliente de Diários Oficiais e Atos Administrativos
Raspador automatizado em Python com testes offline e banco SQLite auditável para extrair contratos, licitações ou nomeações de um portal público opaco.

### Entregáveis Obrigatórios
- Pacote coletor em Python com retry exponencial e suíte pytest.
- Base de dados exportada com hash de integridade de cada documento coletado.

### Critérios de Avaliação
- Resiliência técnica e rastreabilidade integral da fonte.
- Documentação clara para reutilização por outros pesquisadores.

### Diretório de Entrega
`projetos/ciclo-3/mod-301-coletor-publico`
