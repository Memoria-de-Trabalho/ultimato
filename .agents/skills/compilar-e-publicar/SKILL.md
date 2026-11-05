---
name: compilar-e-publicar
description: Validar estilo, minificar todo o repositório, criptografar com chave AES-256-GCM e publicar no GitHub da organização Memória de Trabalho sem vazar arquivos privados.
---

# Compilar e publicar O Último Curso

1. **Rode a verificação de estilo e integridade curricular:**
   ```bash
   python3 scripts/revisar-estilo.py
   ```
   Corrija qualquer erro antes de prosseguir.
2. **Compile o repositório minificado e o portal criptografado:**
   ```bash
   python3 scripts/build_and_encrypt.py --key "SUA_CHAVE"
   ```
   Isso atualiza `dist/minified/`, `assets/curriculum.enc.json`, `viewer/assets/curriculum.enc.json`, `index.html` e `viewer/index.html`.
3. **Verifique o status do Git e a autoria:**
   ```bash
   git config user.name    # deve ser: Memória de Trabalho
   git config user.email   # deve ser: noreply@memoria-de-trabalho.github.io
   git status --short      # nada de notas/, manuais/, PAUTAS.md ou arquivos ._*
   ```
4. **Faça o commit em português, sem `Co-Authored-By`, e envie para `origin main`:**
   ```bash
   git add -A
   git commit -m "Descrição direta da mudança"
   git push origin main
   ```
5. **Confira o build do GitHub Pages:**
   ```bash
   gh api repos/Memoria-de-Trabalho/ultimato/pages/builds/latest --jq .status
   ```
