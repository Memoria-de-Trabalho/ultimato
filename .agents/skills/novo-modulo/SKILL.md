---
name: novo-modulo
description: Criar ou atualizar um módulo curricular de O Último Curso mantendo sincronia entre trilhas/, data/curriculum.json, README.md e o pacote criptografado.
---

# Criar ou atualizar módulo curricular

1. **Leia `docs/ESTILO.md` (inclusive a seção "Recursos didáticos das aulas") e `AGENTS.md`.** Zero travessão, zero emojis, zero clichês de IA e zero "Civic Tech". <!-- estilo: ok -->
2. **Edite ou crie o guia do módulo** em `trilhas/ciclo-<N>-.../NN-<slug>.md` com o cabeçalho YAML completo (`code`, `title`, `slug`, `cycle`, `cycleOrder`, `moduleOrder`, `axisId`, `secondaryAxisIds`, `language`, `languageNotice`, `estimatedHours`, `status`, `progressPercent`, `prerequisites`, `tags`), o aviso de idioma, apresentação, mapa do módulo e linha do tempo em Mermaid, objetivos, tabela de aulas, leituras gratuitas em PT-BR, projeto avaliativo com rubrica e glossário do módulo.
3. **Escreva as aulas** em `trilhas/ciclo-<N>-.../mod-XXX/aula-NN-<slug>.md` (o nome da pasta é o código do módulo em minúsculas). Cada aula tem cabeçalho YAML (`tipo: "aula"`, `modulo`, `ordem`, `titulo`, `duracao`, `language`), tooltips `<abbr>` em todo jargão, pelo menos um diagrama Mermaid para os conceitos difíceis, exercícios com gabarito em `<details>` e resumo. O portal descobre as aulas sozinho pela pasta.
4. **Imagens:** só arquivos da Wikimedia Commons com existência e licença conferidas, via `Special:FilePath`, com legenda e linha nova em `docs/CREDITOS-IMAGENS.md`.
5. **Glossário:** acrescente em `docs/GLOSSARIO.md` um verbete para cada termo novo com tooltip.
6. **Sincronize `data/curriculum.json` e `README.md`** (`keyTopics`, `primaryResources`, `capstoneProject`, `estimatedHours`, `metadata.totalHours` e a tabela "Estado atual do conteúdo" do README). Confira se todos os cursos e livros listados são gratuitos e em português do Brasil.
7. **Valide o estilo, a estrutura e o código:**
   ```bash
   python3 scripts/revisar-estilo.py
   ```
   Execute os blocos ```` ```python ```` de cada aula nova e confira que todos os diagramas são desenhados no portal (`python3 -m http.server 8080` e aba "Aulas e Ementas").
8. **Recompile o pacote minificado e criptografado:**
   ```bash
   python3 scripts/build_and_encrypt.py --key "ultimato-ptbr"
   ```
