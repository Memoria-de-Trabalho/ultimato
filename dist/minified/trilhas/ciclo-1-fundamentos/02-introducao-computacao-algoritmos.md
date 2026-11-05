---
code: "MOD-101"
title: "Introdução à Computação e Pensamento Algorítmico"
slug: "introducao-computacao-algoritmos"
cycle: "ciclo-1"
cycleOrder: 1
moduleOrder: 1
axisId: "eixo-1"
secondaryAxisIds:
  - "eixo-2"
language: "pt-BR"
languageNotice: "Aviso de Idioma: Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em Português (PT-BR)."
estimatedHours: 70
status: "in_progress"
progressPercent: 35
prerequisites: []
tags:
  - "algoritmos"
  - "cs50"
  - "estruturas-de-dados"
  - "complexidade"
  - "fundamentos"
primaryResources:
  - title: "CC50: Ciência da Computação de Harvard no Brasil"
    provider: "Fundação Estudar / Harvard CS50 (PT-BR)"
    type: "course"
    url: "https://www.estudarfora.org.br/cc50/"
    isFree: true
    language: "pt-BR"
  - title: "Algoritmos e Programação de Computadores I e II"
    provider: "UNIVESP"
    type: "video_series"
    url: "https://www.youtube.com/user/univesptv"
    isFree: true
    language: "pt-BR"
capstoneProject:
  title: "CLI de Indexação e Busca em Acervo Público de Decretos"
  repositoryPath: "projetos/ciclo-1/mod-101-indexador-acervo"
---

> **Aviso de Idioma:** Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em **Português (PT-BR)**.

# MOD-101: Introdução à Computação e Pensamento Algorítmico

## 1. Ementa e Justificativa Interdisciplinar
Compreender como computadores representam informações, alocam memória e executam instruções sequenciais é condição indispensável não apenas para programar, mas para **desmistificar a caixa-preta algorítmica** que organiza a vida social contemporânea. Neste módulo inaugural, adotamos a filosofia pedagógica do **CS50 de Harvard (via CC50 em Português)** aliada às disciplinas de base da **UNIVESP**: rigor conceitual focado na resolução pragmática de problemas, sem afogar o estudante em demonstrações matemáticas abstratas.

## 2. Objetivos de Aprendizagem
Ao concluir este módulo (70 horas), você será capaz de:
- Explicar como textos, números e documentos públicos são representados em binário, ASCII e Unicode (`UTF-8`).
- Decompor problemas complexos do mundo social em algoritmos determinísticos e finitos.
- Distinguir empiricamente e analiticamente a eficiência de uma **busca linear** ($O(n)$), uma **busca binária** ($O(\log n)$) e uma **tabela de dispersão / hash** ($O(1)$ médio).
- Escolher a estrutura de dados adequada (lista, pilha, fila, conjunto ou dicionário) para processar registros públicos.

## 3. Roteiro de Estudo Semanal (7 Semanas × 10h)
1. **Semana 1: Abstração, Binário e Representação da Informação:** Bits, bytes, tabela ASCII, Unicode (`UTF-8`) e por que arquivos governamentais antigos quebram acentuação (`ISO-8859-1`).
2. **Semana 2: Pensamento Algorítmico e Controle de Fluxo:** Condicionais, laços de repetição, invariantes simples e decomposição funcional.
3. **Semana 3: Memória, Arranjos e Listas:** Contiguidade em memória, custo de inserção vs. leitura posicional.
4. **Semana 4: Algoritmos de Busca e Ordenação:** Busca linear, busca binária, ordenação por seleção e ordenação por intercalação (*Merge Sort* conceitual).
5. **Semana 5: Complexidade Computacional Sem Formalismo Excessivo:** Intuição prática da notação Big-O ($O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$) medida no relógio real com bases públicas.
6. **Semana 6: Pilhas, Filas, Árvores de Decisão e Tabelas Hash:** Como dicionários e índices permitem localizar um CNPJ ou decreto instantaneamente entre milhões de registros.
7. **Semana 7: Desenvolvimento do Projeto Prático Avaliativo (`mod-101-indexador-acervo`).**

## 4. Projeto Prático Avaliativo
Construa uma ferramenta de linha de comando (`indexador_acervo.py`) em Python puro que carregue um conjunto de **10.000 ementas de decretos ou leis** e compare o tempo real de resposta (em milissegundos) de três estratégias de consulta:
1. Varredura sequencial completa ($O(n)$);
2. Busca binária sobre lista ordenada por número de decreto ($O(\log n)$);
3. Índice invertido / Tabela Hash em memória por palavra-chave e identificador ($O(1)$).