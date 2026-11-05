---
name: novo-modulo
description: Criar ou atualizar um módulo curricular de O Último Curso mantendo sincronia entre trilhas/, data/curriculum.json, README.md e o pacote criptografado.
---

# Criar ou atualizar módulo curricular

1. **Leia `docs/ESTILO.md` e `AGENTS.md`.** Zero travessão, zero emojis, zero clichês de IA e zero "Civic Tech". <!-- estilo: ok -->
2. **Edite ou crie a ementa** em `trilhas/ciclo-<N>-.../NN-<slug>.md` com o cabeçalho YAML completo (`code`, `title`, `slug`, `cycle`, `cycleOrder`, `moduleOrder`, `axisId`, `secondaryAxisIds`, `language`, `languageNotice`, `estimatedHours`, `status`, `progressPercent`, `prerequisites`, `tags`) e o aviso de idioma logo abaixo do frontmatter.
3. **Sincronize `data/curriculum.json` e `README.md`:**
   - Atualize `keyTopics`, `primaryResources`, `capstoneProject`, `estimatedHours` e `metadata.totalHours`.
   - Confira se todos os cursos e livros listados são gratuitos e em português do Brasil.
4. **Valide o estilo e a estrutura:**
   ```bash
   python3 scripts/revisar-estilo.py
   ```
5. **Recompile o pacote minificado e criptografado:**
   ```bash
   python3 scripts/build_and_encrypt.py --key "ultimato-ptbr"
   ```
