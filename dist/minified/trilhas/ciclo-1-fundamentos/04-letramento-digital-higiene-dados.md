---
code: "MOD-104"
title: "Letramento Digital, Arquitetura da Rede e Higiene Crítica de Dados"
slug: "letramento-digital-higiene-dados"
cycle: "ciclo-1"
cycleOrder: 1
moduleOrder: 4
axisId: "eixo-3"
secondaryAxisIds: ["eixo-4"]
language: "pt-BR"
languageNotice: "Aviso de Idioma: Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em Português (PT-BR)."
estimatedHours: 50
status: "not_started"
progressPercent: 0
prerequisites: []
tags:
  - "privacidade"
  - "seguranca-digital"
  - "metadados"
  - "redes"
  - "criptografia"
  - "soberania-tecnologica"
---

> **Aviso de Idioma:** Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em **Português (PT-BR)**.

# MOD-104: Letramento Digital, Arquitetura da Rede e Higiene Crítica de Dados

## 1. Eixo e Carga Horária
- **Ciclo:** Ciclo 1: Fundamentos Ontológicos, Clássicos e Computacionais
- **Eixo principal:** Letramento Digital e Higiene Crítica de Dados
- **Carga horária estimada:** 50 horas
- **Pré-requisitos:** Nenhum

## 2. Tópicos e Autores Centrais
- Arquitetura da Internet: DNS, TCP/IP, HTTP/HTTPS, TLS e inspeção de tráfego.
- Domínio do terminal POSIX/Unix, permissões e automação shell.
- Anatomia de arquivos digitais e metadados ocultos (EXIF, PDF Info, XMP).
- Modelagem de ameaças (Threat Modeling) para pesquisadores e ativistas.
- Criptografia prática (AES-256-GCM, PBKDF2, GPG, chaves SSH) e navegação anônima (Tor).

## 3. Bibliografia e Cursos Base Gratuitos (PT-BR)
- [Autodefesa Contra Vigilância (Surveillance Self-Defense)](https://ssd.eff.org/pt-br) (Electronic Frontier Foundation (EFF PT-BR))
- [Redes de Computadores: Fundamentos da Internet](https://www.youtube.com/user/univesptv) (UNIVESP)

## 4. Projeto Prático Avaliativo: Kit de Auditoria e Sanitização de Metadados (meta-limpa)
Ferramenta CLI acompanhada de um Modelo de Ameaças capaz de varrer diretórios, gerar laudo de metadados expostos e produzir cópias sanitizadas verificadas por SHA-256.

### Entregáveis Obrigatórios
- Utilitário CLI em Python para inspeção e limpeza de metadados.
- Documento de Modelo de Ameaças aplicado à pesquisa social.

### Critérios de Avaliação
- Integridade criptográfica e remoção completa de rastros identificadores.
- Rigor analítico no modelo de risco.

### Diretório de Entrega
`projetos/ciclo-1/mod-104-meta-limpa`