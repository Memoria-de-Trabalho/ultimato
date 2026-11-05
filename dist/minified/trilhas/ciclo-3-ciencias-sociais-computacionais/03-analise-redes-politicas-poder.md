---
code: "MOD-303"
title: "Análise de Redes de Poder, Imperialismo, Elites e Estado Integral com Grafos (NetworkX)"
slug: "analise-redes-poder-imperialismo-grafos"
cycle: "ciclo-3"
cycleOrder: 3
moduleOrder: 3
axisId: "eixo-5"
secondaryAxisIds: ["eixo-1", "eixo-4"]
language: "pt-BR"
languageNotice: "Aviso de Idioma: Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em Português (PT-BR)."
estimatedHours: 60
status: "not_started"
progressPercent: 0
prerequisites: ["MOD-201", "MOD-203", "MOD-206", "MOD-207"]
tags:
  - "grafos"
  - "networkx"
  - "redes-politicas"
  - "lenin"
  - "gramsci"
  - "florestan-fernandes"
  - "elites"
---

> **Aviso de Idioma:** Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em **Português (PT-BR)**.

# MOD-303: Análise de Redes de Poder, Imperialismo, Elites e Estado Integral com Grafos (NetworkX)

## 1. Eixo e Carga Horária
- **Ciclo:** Ciclo 3: Ciências Sociais Computacionais, Políticas Públicas e Ferramentas de Interesse Público
- **Eixo principal:** Humanidades Digitais, Ciências Sociais Computacionais e Interesse Público
- **Carga horária estimada:** 60 horas
- **Pré-requisitos:** MOD-201, MOD-203, MOD-206, MOD-207

## 2. Tópicos e Autores Centrais
- Teoria dos Grafos aplicada à sociologia do poder: modelando conselhos cruzados de bancos e indústrias (Imperialismo de Lênin), redes de aparelhos privados de hegemonia e intelectuais (Gramsci) e laços patrimoniais/autocráticos (Sérgio Buarque & Florestan).
- Redes unimodais e bipartidas (doadores-candidatos, empresas-conselheiros, deputados-proposições) e projeções ponderadas.
- Métricas estruturais com NetworkX: centralidade de grau, intermediação (betweenness / brokers), proximidade, autovetor (PageRank) e detecção de comunidades (Louvain).

## 3. Bibliografia e Cursos Base Gratuitos (PT-BR)
- [Análise de Redes Sociais Aplicada à Ciência Política](https://escoladedados.org/) (Escola de Dados / IPEA Publicações Abertas)

## 4. Projeto Prático Avaliativo: Cartografia Computacional de Coalizões, Financiamento e Blocos de Poder
Sistema em Python com NetworkX que constrói e analisa o grafo de coautoria legislativa, frentes parlamentares e financiamento eleitoral, identificando os nós centrais e os brokers de coalizão.

### Entregáveis Obrigatórios
- Módulo Python de análise de grafos e exportação interativa.
- Dossiê sociopolítico interpretando a estrutura da rede encontrada.

### Critérios de Avaliação
- Correspondência rigorosa entre métrica matemática de grafo e conceito sociopolítico.
- Reprodutibilidade completa dos resultados.

### Diretório de Entrega
`projetos/ciclo-3/mod-303-redes-de-poder`