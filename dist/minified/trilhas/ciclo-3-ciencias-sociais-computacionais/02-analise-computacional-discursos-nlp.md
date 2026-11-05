---
code: "MOD-302"
title: "Análise Computacional de Discursos Políticos, Ideologia e Hegemonia (NLP em Português)"
slug: "analise-computacional-discursos-hegemonia-nlp"
cycle: "ciclo-3"
cycleOrder: 3
moduleOrder: 2
axisId: "eixo-5"
secondaryAxisIds: ["eixo-4"]
language: "pt-BR"
languageNotice: "Aviso de Idioma: Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em Português (PT-BR)."
estimatedHours: 70
status: "not_started"
progressPercent: 0
prerequisites: ["MOD-203", "MOD-205", "MOD-207"]
tags:
  - "nlp"
  - "gramsci"
  - "foucault"
  - "spacy"
  - "tf-idf"
  - "hegemonia"
  - "analise-de-discurso"
---

> **Aviso de Idioma:** Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em **Português (PT-BR)**.

# MOD-302: Análise Computacional de Discursos Políticos, Ideologia e Hegemonia (NLP em Português)

## 1. Eixo e Carga Horária
- **Ciclo:** Ciclo 3: Ciências Sociais Computacionais, Políticas Públicas e Ferramentas de Interesse Público
- **Eixo principal:** Humanidades Digitais, Ciências Sociais Computacionais e Interesse Público
- **Carga horária estimada:** 70 horas
- **Pré-requisitos:** MOD-203, MOD-205, MOD-207

## 2. Tópicos e Autores Centrais
- Pontes teórico-computacionais: como traduzir Hegemonia e Aparelhos de Imprensa (Gramsci), Formações Discursivas (Foucault) e Logopeia/Precisão Semântica (Pound) em análise quantitativa e qualitativa de corpus.
- Processamento de Linguagem Natural em Português: tokenização, lematização, POS-tagging e Entidades Nomeadas (NER) com spaCy (pt_core_news).
- Vetorização TF-IDF, coocorrência lexical, modelagem de tópicos e deslocamento semântico diacronico.
- Leitura distante (Moretti) combinada com leitura próxima (close reading) em pronunciamentos parlamentares, manifestos e editoriais.

## 3. Bibliografia e Cursos Base Gratuitos (PT-BR)
- [Processamento de Linguagem Natural em Português: Materiais Abertos](https://eaulas.usp.br/) (USP / ICMC & Comunidade PLN-BR)

## 4. Projeto Prático Avaliativo: Radar Computacional de Hegemonia e Disputa Semântica Parlamentar
Pipeline em Python que processa milhares de pronunciamentos na Câmara/Senado ou artigos de imprensa para medir a ascensão de vocabulários hegemônicos, enquadramentos morais e clivagens ideológicas.

### Entregáveis Obrigatórios
- Módulo Python de NLP com spaCy e scikit-learn.
- Artigo analítico interpretando os clusters semânticos à luz de Gramsci, Foucault e Habermas.

### Critérios de Avaliação
- Validação metodológica rigorosa (evitando leituras ingênuas de frequência de palavras sem contexto).
- Qualidade técnica do pipeline em português.

### Diretório de Entrega
`projetos/ciclo-3/mod-302-radar-hegemonia-nlp`