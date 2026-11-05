# Arquitetura Simplificada: Minificação Total + Criptografia por Chave (GitHub Pages)

> **Aviso de Idioma:** Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em **Português (PT-BR)**.

## 1. Como funciona o novo fluxo simplificado (`scripts/build_and_encrypt.py`)

Em vez de manter sistemas complexos de autenticação, **todos os arquivos e códigos do repositório são minificados e criptografados com uma chave única (a sua senha)**:

1. **Minificação Total (`dist/minified/`):**
   O script [`scripts/build_and_encrypt.py`](../../scripts/build_and_encrypt.py) percorre todos os arquivos `.json`, `.md`, `.py` e `.html` do repositório, remove comentários, espaços e quebras supérfluas, e gera versões minificadas.
2. **Empacotamento + Criptografia por Chave (`AES-256-GCM`):**
   A partir da sua senha (`--key`), o script deriva uma chave criptográfica de 256 bits (`PBKDF2-HMAC-SHA256`, 250.000 iterações) e cifra **todo o repositório minificado** (a matriz curricular de 20 módulos + o conteúdo integral de todos os arquivos do curso).
3. **HTML Único Minificado e Autossuficiente (`viewer/index.html`):**
   O pacote criptografado é embutido diretamente dentro de [`viewer/index.html`](../../viewer/index.html) (que também é minificado). Assim, basta publicar **um único arquivo** no GitHub Pages do **Memória de Trabalho**, e redirecionar para ele a partir do seu GitHub Pages pessoal (**`lucasrafaldini.github.io`**) usando [`viewer/redirect-lucasrafaldini.html`](../../viewer/redirect-lucasrafaldini.html).

## 2. Como Gerar com a sua Chave (Senha)

```bash
python3 scripts/build_and_encrypt.py --key "SUA_CHAVE_SENHA_AQUI"
```
*(Por padrão, o repositório já foi compilado com a chave inicial de demonstração `ultimato-ptbr`.)*
