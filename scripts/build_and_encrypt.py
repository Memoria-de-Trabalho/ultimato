#!/usr/bin/env python3
"""
Compilador, higienizador de estilo, minificador e criptografador de O Último Curso.
Segue a identidade visual e o guia de estilo do Memória de Trabalho:
- Zero travessão ou meia-risca.
- Zero emojis decorativos.
- Tokens visuais do Memória de Trabalho: papel #F2EBDD, tinta #141414, vermelho #C8102E, amarelo #FFE600;
  fontes Anton, Special Elite e Inter.
"""

import argparse
import base64
import hashlib
import json
import os
import re
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ROOT_DIR = Path(__file__).resolve().parent.parent
CURRICULUM_JSON = ROOT_DIR / "data" / "curriculum.json"
VIEWER_DIR = ROOT_DIR / "viewer"
ASSETS_DIR = VIEWER_DIR / "assets"
DIST_MIN_DIR = ROOT_DIR / "dist" / "minified"

EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0001F1E6-\U0001F1FF"
    "\U0000FE0F"
    "]+",
    flags=re.UNICODE,
)


def _sanitize_prose(text: str) -> str:
    text = EMOJI_RE.sub("", text)
    text = re.sub(r"(\d)\s*[\u2014\u2013]\s*(\d)", r"\1 a \2", text)
    text = re.sub(r"\s+[\u2014\u2013]\s+", ": ", text)
    text = re.sub(r"[\u2014\u2013]", ": ", text)
    return text


def sanitize_style(text: str, is_json: bool = False) -> str:
    """Remove emojis e substitui travessões e meia-riscas conforme o guia de estilo do Memória de Trabalho.

    Em Markdown, blocos de código (entre crases triplas) são preservados intactos: lá valem a sintaxe
    da linguagem e endereços como `2001:db8::1`, que a limpeza de prosa estragaria.
    """
    if is_json:
        return _sanitize_prose(text)
    saida = []
    em_codigo = False
    for linha in text.split("\n"):
        if linha.lstrip().startswith("```"):
            em_codigo = not em_codigo
            saida.append(linha)
            continue
        if em_codigo:
            saida.append(EMOJI_RE.sub("", linha))
            continue
        limpa = _sanitize_prose(linha)
        # Limpa espaços duplos criados pela remoção de emojis no início de títulos
        limpa = re.sub(r"^(#+)\s+", r"\1 ", limpa)
        # Desfaz ": :" criado pela troca de travessões, sem tocar em "::" legítimo
        limpa = re.sub(r":\s+:", ":", limpa)
        saida.append(limpa)
    return "\n".join(saida)


def sanitize_repository_files() -> None:
    """Garante que todos os arquivos-fonte do repositório sigam o guia de estilo sem emojis e sem travessão."""
    skip_dirs = {".git", "dist", "viewer", "scripts", "__pycache__", ".venv"}
    for path in sorted(ROOT_DIR.rglob("*")):
        if not path.is_file() or path.name.startswith("."):
            continue
        if any(p in skip_dirs or p.startswith(".") for p in path.relative_to(ROOT_DIR).parts):
            continue
        if path.suffix not in {".md", ".json"} and path.name != "LICENSE":
            continue
        raw = path.read_text(encoding="utf-8")
        cleaned = sanitize_style(raw, is_json=(path.suffix == ".json"))
        if path.suffix == ".json":
            parsed = json.loads(cleaned)
            cleaned = json.dumps(parsed, indent=2, ensure_ascii=False) + "\n"
        if cleaned != raw:
            path.write_text(cleaned, encoding="utf-8")


def minify_json(content: str) -> str:
    return json.dumps(json.loads(content), separators=(",", ":"), ensure_ascii=False)


def minify_markdown(content: str) -> str:
    lines = [line.rstrip() for line in content.splitlines()]
    collapsed = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    return collapsed.strip()


def minify_python(content: str) -> str:
    out = []
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        out.append(line.rstrip())
    return "\n".join(out)


def minify_html(content: str) -> str:
    content = re.sub(r"<!--(?!\[if).*?-->", "", content, flags=re.DOTALL)
    content = re.sub(r"/\*.*?\*/", "", content, flags=re.DOTALL)
    content = re.sub(r">\s+<", "><", content)
    content = re.sub(r"\s{2,}", " ", content)
    return content.strip()


def collect_and_minify_repo() -> dict:
    included_exts = {".json", ".md", ".py"}
    skip_dirs = {".git", "dist", "viewer", "__pycache__", ".venv"}
    minified_files: dict[str, str] = {}

    DIST_MIN_DIR.mkdir(parents=True, exist_ok=True)

    for path in sorted(ROOT_DIR.rglob("*")):
        if not path.is_file() or path.name.startswith("."):
            continue
        rel_parts = path.relative_to(ROOT_DIR).parts
        if any(part in skip_dirs or part.startswith(".") for part in rel_parts):
            continue
        if path.suffix not in included_exts and path.name != "LICENSE":
            continue

        rel_path = str(path.relative_to(ROOT_DIR))
        raw_text = path.read_text(encoding="utf-8")

        if path.suffix == ".json":
            min_text = minify_json(raw_text)
        elif path.suffix == ".py":
            min_text = minify_python(raw_text)
        else:
            min_text = minify_markdown(raw_text)

        minified_files[rel_path] = min_text

        target_min_file = DIST_MIN_DIR / rel_path
        target_min_file.parent.mkdir(parents=True, exist_ok=True)
        target_min_file.write_text(min_text, encoding="utf-8")

    curriculum_data = json.loads(CURRICULUM_JSON.read_text(encoding="utf-8"))
    return {
        "curriculum": curriculum_data,
        "repoFiles": minified_files,
    }


def encrypt_with_key(plaintext_bytes: bytes, key_password: str, iterations: int = 250_000) -> dict:
    salt = os.urandom(16)
    iv = os.urandom(12)
    derived_key = hashlib.pbkdf2_hmac(
        "sha256",
        key_password.encode("utf-8"),
        salt,
        iterations,
        dklen=32,
    )
    ciphertext = AESGCM(derived_key).encrypt(iv, plaintext_bytes, None)
    return {
        "kdf": "PBKDF2-SHA256",
        "cipher": "AES-256-GCM",
        "iterations": iterations,
        "salt": base64.b64encode(salt).decode("ascii"),
        "iv": base64.b64encode(iv).decode("ascii"),
        "ciphertext": base64.b64encode(ciphertext).decode("ascii"),
    }


def build_viewer_html(encrypted_bundle_json: str, vendor_prefix: str = "vendor/") -> str:
    html_template = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>O Último Curso · Memória de Trabalho</title>
  <meta name="description" content="O Último Curso: formação aberta em Engenharia de Software, Letramento Digital, Filosofia Política e Ciências Sociais Computacionais.">
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Anton&family=Special+Elite&family=Inter:wght@400;600&display=swap");

    :root {{
      --papel: #f2ebdd;
      --tinta: #141414;
      --vermelho: #c8102e;
      --amarelo: #ffe600;
      --suave: #5b544a;
      --linha: #d8cdb8;
    }}

    * {{ box-sizing: border-box; }}
    html {{ -webkit-text-size-adjust: 100%; }}

    body {{
      margin: 0;
      background: var(--papel);
      color: var(--tinta);
      font: 17px/1.6 Inter, system-ui, sans-serif;
      background-image: radial-gradient(rgba(0,0,0,.035) 1px, transparent 1px);
      background-size: 4px 4px;
    }}

    a {{ color: var(--vermelho); }}

    .wrap {{ max-width: 1040px; margin: 0 auto; padding: 0 16px; }}

    h1, h2, h3 {{
      font-family: Anton, Impact, sans-serif;
      font-weight: 400;
      letter-spacing: .01em;
      line-height: 1.05;
      text-transform: uppercase;
    }}
    h2 {{ font-size: clamp(2rem, 5vw, 3rem); margin: 0 0 .4em; }}

    .kicker {{
      font-family: "Special Elite", "Courier New", monospace;
      color: var(--vermelho);
      text-transform: uppercase;
      letter-spacing: .08em;
      margin: 0;
    }}

    .topo {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px 20px;
      padding-top: 20px;
      padding-bottom: 4px;
      font-family: "Special Elite", "Courier New", monospace;
    }}
    .topo a {{ color: var(--tinta); text-decoration: none; }}
    .topo a:first-child {{
      font-family: Anton, Impact, sans-serif;
      text-transform: uppercase;
      color: var(--vermelho);
      margin-right: auto;
      font-size: 1.15rem;
    }}
    .topo a:hover {{ text-decoration: underline; }}

    .page-head {{ padding: 40px 0 24px; }}
    .page-head h1 {{ font-size: clamp(2.4rem, 7vw, 4rem); margin: .1em 0 .2em; }}
    .page-head .linha-fina {{ font-size: 1.2rem; line-height: 1.5; margin: 0 0 16px; max-width: 68ch; }}

    .aviso-idioma {{
      margin: 16px 0 0;
      padding: 10px 18px;
      border-left: 6px solid var(--vermelho);
      background: #fff8;
      font-size: .95rem;
    }}

    section {{ padding: 40px 0; border-top: 3px solid var(--tinta); }}
    .cols {{ display: grid; gap: 32px; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }}

    /* Caixa de autenticação */
    #auth-sec {{ padding: 40px 0 64px; border-top: 3px solid var(--tinta); }}
    .auth-card {{
      max-width: 520px;
      border: 3px solid var(--tinta);
      background: #fff8;
      padding: 24px;
    }}
    .auth-card h2 {{ font-size: 2rem; margin: 4px 0 12px; }}
    .auth-card p {{ margin: 0 0 16px; }}
    .campo-senha {{
      width: 100%;
      padding: 12px 14px;
      border: 3px solid var(--tinta);
      background: var(--papel);
      color: var(--tinta);
      font: 1rem "Special Elite", "Courier New", monospace;
      margin-bottom: 14px;
    }}
    .campo-senha:focus {{ outline: 2px solid var(--vermelho); }}
    .botao {{
      display: inline-block;
      padding: 10px 18px;
      border: 3px solid var(--tinta);
      color: var(--tinta);
      text-decoration: none;
      font: 600 1rem Inter, system-ui, sans-serif;
      background: var(--amarelo);
      cursor: pointer;
    }}
    .botao:hover, .botao.ativo {{ background: var(--tinta); color: var(--amarelo); }}
    .erro-chave {{
      display: none;
      margin-top: 14px;
      padding: 8px 14px;
      border-left: 6px solid var(--vermelho);
      background: #fff8;
      font-family: "Special Elite", monospace;
      color: var(--vermelho);
      font-size: .95rem;
    }}

    /* Painel desbloqueado */
    #app {{ display: none; }}

    .pautas {{
      list-style: none;
      padding: 0;
      margin: 0;
      display: grid;
      gap: 12px;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    }}
    .pautas li {{ border: 3px solid var(--tinta); padding: 14px 16px; background: #fff8; }}
    .pautas b {{
      display: block;
      font-family: Anton, Impact, sans-serif;
      font-weight: 400;
      font-size: 1.45rem;
      text-transform: uppercase;
    }}

    .plataformas {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      list-style: none;
      padding: 0;
      margin: 0 0 24px;
    }}

    .lista-artigos {{
      list-style: none;
      padding: 0;
      margin: 0;
      display: grid;
      gap: 16px;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 310px), 1fr));
    }}
    .cartao-artigo {{
      border: 3px solid var(--tinta);
      background: #fff8;
      padding: 16px 18px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .cartao-artigo h3 {{ font-size: 1.5rem; margin: 6px 0 10px; }}
    .cartao-artigo ul {{ margin: 0 0 14px; padding-left: 1.2em; font-size: .95rem; }}
    .cartao-artigo li {{ margin: .25em 0; }}
    .caixa-projeto {{
      border-top: 2px solid var(--tinta);
      padding-top: 10px;
      margin-top: auto;
      font-size: .92rem;
    }}
    .caixa-projeto .rotulo {{
      font-family: "Special Elite", monospace;
      color: var(--vermelho);
      text-transform: uppercase;
      font-size: .82rem;
      display: block;
    }}
    .fontes-mod {{
      margin-top: 8px;
      font-size: .86rem;
      color: var(--suave);
    }}

    /* Explorador de arquivos */
    .explorador {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 16px;
      align-items: start;
    }}
    .lista-arquivos {{
      list-style: none;
      padding: 0;
      margin: 0;
      border: 3px solid var(--tinta);
      background: #fff8;
    }}
    .lista-arquivos li {{ border-bottom: 1px solid var(--linha); }}
    .lista-arquivos li:last-child {{ border-bottom: 0; }}
    .btn-arq {{
      width: 100%;
      text-align: left;
      background: transparent;
      border: 0;
      padding: 10px 12px;
      font: .88rem "Special Elite", "Courier New", monospace;
      color: var(--tinta);
      cursor: pointer;
    }}
    .btn-arq:hover {{ background: var(--amarelo); }}
    .btn-arq.ativo {{ background: var(--tinta); color: var(--amarelo); }}
    .visor-codigo {{
      border: 3px solid var(--tinta);
      background: #fff8;
      padding: 18px;
      margin: 0;
      overflow-x: auto;
      font: .88rem/1.55 "Courier New", monospace;
      white-space: pre-wrap;
      word-break: break-word;
      max-height: 680px;
      overflow-y: auto;
    }}

    footer {{
      border-top: 3px solid var(--tinta);
      padding: 24px 0 48px;
      font-family: "Special Elite", monospace;
      font-size: .95rem;
      color: var(--suave);
    }}

    /* Leitor de aulas */
    .leitor {{
      display: grid;
      grid-template-columns: 300px minmax(0, 1fr);
      gap: 20px;
      align-items: start;
    }}
    .sumario {{
      border: 3px solid var(--tinta);
      background: #fff8;
      max-height: 80vh;
      overflow-y: auto;
      position: sticky;
      top: 12px;
    }}
    .sumario details {{ border-bottom: 1px solid var(--linha); }}
    .sumario summary {{
      cursor: pointer;
      padding: 10px 12px;
      font: .9rem "Special Elite", "Courier New", monospace;
      list-style-position: inside;
    }}
    .sumario summary b {{ color: var(--vermelho); font-weight: 400; }}
    .sumario ul {{ list-style: none; margin: 0; padding: 0 0 8px; }}
    .sumario .btn-arq {{ padding: 6px 12px 6px 26px; font-size: .84rem; }}
    .sumario .ciclo-rotulo {{
      font-family: Anton, Impact, sans-serif;
      text-transform: uppercase;
      background: var(--tinta);
      color: var(--amarelo);
      padding: 6px 12px;
      margin: 0;
      font-size: 1rem;
      font-weight: 400;
    }}
    .aula {{
      border: 3px solid var(--tinta);
      background: #fffc;
      padding: clamp(16px, 4vw, 40px);
      min-width: 0;
      overflow-wrap: break-word;
    }}
    .aula h1 {{ font-size: clamp(2rem, 5vw, 3rem); margin: .2em 0 .5em; }}
    .aula h2 {{ font-size: clamp(1.5rem, 3.5vw, 2.1rem); margin: 1.6em 0 .5em; border-top: 2px solid var(--tinta); padding-top: .6em; }}
    .aula h3 {{ font-size: 1.3rem; margin: 1.4em 0 .4em; }}
    .aula h4 {{ font-family: "Special Elite", monospace; color: var(--vermelho); margin: 1.2em 0 .3em; }}
    .aula p, .aula li {{ max-width: 76ch; }}
    .aula blockquote {{
      margin: 1.2em 0;
      padding: 10px 18px;
      border-left: 6px solid var(--vermelho);
      background: #f2ebdd99;
    }}
    .aula img {{ max-width: 100%; height: auto; border: 3px solid var(--tinta); background: #fff; display: block; margin: 1em auto .3em; }}
    .aula img + em, .aula p > em:only-child {{ display: block; text-align: center; color: var(--suave); font-size: .88rem; }}
    .aula table {{ border-collapse: collapse; width: 100%; margin: 1em 0; display: block; overflow-x: auto; font-size: .92rem; }}
    .aula th, .aula td {{ border: 2px solid var(--tinta); padding: 6px 10px; text-align: left; vertical-align: top; }}
    .aula th {{ background: var(--tinta); color: var(--amarelo); font-weight: 600; }}
    .aula code {{ background: #14141412; padding: 1px 5px; font-size: .9em; }}
    .aula pre {{ background: var(--tinta); color: var(--papel); padding: 14px 16px; overflow-x: auto; font-size: .86rem; line-height: 1.5; }}
    .aula pre code {{ background: transparent; padding: 0; }}
    .aula details {{ border: 2px dashed var(--tinta); padding: 8px 14px; margin: 1em 0; background: #fff8; }}
    .aula summary {{ cursor: pointer; font-weight: 600; }}
    .aula .mermaid {{ background: #fff; border: 3px solid var(--tinta); padding: 12px; margin: 1.2em 0; overflow-x: auto; text-align: center; }}
    .aula .mermaid svg {{ max-width: 100%; height: auto; }}
    .aula abbr[title] {{
      text-decoration: underline dotted var(--vermelho);
      text-underline-offset: 3px;
      cursor: help;
      position: relative;
    }}
    .dica {{
      position: absolute;
      z-index: 30;
      max-width: min(340px, 86vw);
      background: var(--tinta);
      color: var(--papel);
      padding: 10px 12px;
      font: .86rem/1.45 Inter, system-ui, sans-serif;
      border-left: 5px solid var(--amarelo);
      box-shadow: 4px 4px 0 var(--vermelho);
      pointer-events: none;
    }}
    .navegacao-aula {{ display: flex; flex-wrap: wrap; gap: 10px; justify-content: space-between; margin-top: 32px; }}

    @media (max-width: 720px) {{
      .explorador {{ grid-template-columns: 1fr; }}
      .leitor {{ grid-template-columns: 1fr; }}
      .sumario {{ position: static; max-height: 50vh; }}
    }}
  </style>
</head>
<body>
  <nav class="topo wrap">
    <a href="https://memoria-de-trabalho.github.io/">Memória de Trabalho</a>
    <a href="https://memoria-de-trabalho.github.io/artigos/">Artigos</a>
    <a href="https://memoria-de-trabalho.github.io/artes/">Artes</a>
  </nav>

  <main class="wrap">
    <header class="page-head">
      <p class="kicker">Memória de Trabalho · Formação Livre</p>
      <h1 id="t-title">O Último Curso</h1>
      <p class="linha-fina" id="t-sub">Engenharia de Software, Letramento Digital, Filosofia Política e Ciências Sociais Computacionais.</p>
      <blockquote class="aviso-idioma">
        <b>Aviso de Idioma:</b> Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em <b>Português (PT-BR)</b>.
      </blockquote>
    </header>

    <section id="auth-sec">
      <div class="auth-card">
        <p class="kicker">Acesso por chave</p>
        <h2>Desbloquear currículo</h2>
        <p>Todo o repositório do curso está minificado e criptografado com <code>AES-256-GCM</code>. Digite a chave para decifrar os 20 módulos e os arquivos em memória.</p>
        <form id="f-login">
          <input class="campo-senha" type="password" id="pwd" placeholder="Digite a chave de acesso" required autocomplete="current-password">
          <button type="submit" class="botao">Destravar conteúdo</button>
          <p id="err" class="erro-chave">Chave incorreta. Confira a senha e tente de novo.</p>
        </form>
      </div>
    </section>

    <div id="app">
      <section id="resumo">
        <div class="cols">
          <div>
            <p class="kicker">Estrutura</p>
            <h2>Quem programa também precisa ler o mundo</h2>
          </div>
          <div>
            <p>Uma trilha aberta que junta algoritmos, Python, testes automatizados e higiene digital com leitura direta de Platão, Aristóteles, Hegel, Feuerbach, Heidegger, Marx, Engels, Durkheim, Weber, Bakunin, Kropotkin, Lênin, Trótski, Gramsci, Lukács, Walter Benjamin, Ortega y Gasset, Ezra Pound, Foucault, Habermas, Frantz Fanon, Sérgio Buarque de Holanda e Florestan Fernandes.</p>
          </div>
        </div>
        <ul class="pautas" id="stats" style="margin-top:24px"></ul>
      </section>

      <section id="navegacao-curso">
        <p class="kicker">Visualização</p>
        <h2>Escolha o modo</h2>
        <div class="plataformas">
          <button type="button" class="botao ativo" id="tab-curr">Matriz Curricular (20 Módulos)</button>
          <button type="button" class="botao" id="tab-aulas">Aulas e Ementas</button>
          <button type="button" class="botao" id="tab-files">Arquivos do Repositório Minificado</button>
        </div>

        <div id="view-aulas" style="display:none">
          <p class="kicker" style="margin-bottom:10px">Passe o mouse ou toque nos termos sublinhados para ver a explicação</p>
          <div class="leitor">
            <nav class="sumario" id="a-list" aria-label="Sumário das aulas"></nav>
            <article class="aula" id="a-content"></article>
          </div>
        </div>

        <div id="view-curr">
          <p class="kicker" style="margin-bottom:8px">Filtrar por eixo</p>
          <div class="plataformas" id="flts"></div>
          <div id="cycles"></div>
        </div>

        <div id="view-files" style="display:none">
          <p class="kicker" style="margin-bottom:10px">Código-fonte e ementas decifrados em memória</p>
          <div class="explorador">
            <ul class="lista-arquivos" id="f-list"></ul>
            <pre class="visor-codigo" id="f-content"></pre>
          </div>
        </div>
      </section>

      <section id="expediente">
        <p class="kicker">Expediente</p>
        <h2>Quem responde por isso aqui</h2>
        <div class="cols">
          <div>
            <p><b>Conteúdo e tecnicalidades:</b> Lucas Rafaldini.</p>
            <p><b>Contato:</b> <a href="mailto:thothandson@icloud.com">thothandson@icloud.com</a>, o e-mail da Thoth &amp; Son, empresa do Lucas.</p>
          </div>
          <div>
            <p>Repositório-fonte mantido na pasta local <code>ultimato</code>, minificado e criptografado por chave via script Python para publicação estática.</p>
          </div>
        </div>
      </section>
    </div>

    <footer>
      Memória de Trabalho · feito por trabalhadores · <a href="https://memoria-de-trabalho.github.io/artes/">artes para baixar</a> · <a href="#expediente">expediente</a>
    </footer>
  </main>

  <script id="enc-payload" type="application/json">{encrypted_bundle_json}</script>
  <script>
    const b64 = s => Uint8Array.from(atob(s), c => c.charCodeAt(0));

    async function unlock(bundle, password) {{
      const enc = new TextEncoder();
      const km = await crypto.subtle.importKey("raw", enc.encode(password), {{ name: "PBKDF2" }}, false, ["deriveKey"]);
      const key = await crypto.subtle.deriveKey(
        {{ name: "PBKDF2", salt: b64(bundle.salt), iterations: bundle.iterations, hash: "SHA-256" }},
        km,
        {{ name: "AES-GCM", length: 256 }},
        false,
        ["decrypt"]
      );
      const pt = await crypto.subtle.decrypt({{ name: "AES-GCM", iv: b64(bundle.iv) }}, key, b64(bundle.ciphertext));
      return JSON.parse(new TextDecoder().decode(pt));
    }}

    function renderApp(payload, axis = "all") {{
      const d = payload.curriculum;
      const files = payload.repoFiles;
      document.getElementById("t-title").textContent = d.metadata.title;
      document.getElementById("t-sub").textContent = d.metadata.subtitle;

      const mods = d.cycles.flatMap(c => c.modules);
      document.getElementById("stats").innerHTML = `
        <li><b>${{d.metadata.totalHours}} horas</b> Carga horária total dividida em 3 ciclos formativos.</li>
        <li><b>${{mods.length}} módulos</b> 670h de teoria nas fontes primárias e 650h de engenharia e dados.</li>
        <li><b>${{Object.keys(files).length}} arquivos</b> Repositório inteiro minificado e decifrado localmente.</li>
        <li><b>100% PT-BR</b> Obras, aulas abertas e documentação em português do Brasil.</li>
      `;

      const flts = document.getElementById("flts");
      flts.innerHTML = `<button type="button" class="botao ${{axis === 'all' ? 'ativo' : ''}}" data-ax="all">Todos os eixos (${{mods.length}})</button>` +
        d.axes.map(a => `<button type="button" class="botao ${{axis === a.id ? 'ativo' : ''}}" data-ax="${{a.id}}">${{a.name}}</button>`).join("");
      flts.querySelectorAll("button").forEach(b => b.onclick = () => renderApp(payload, b.dataset.ax));

      const axMap = Object.fromEntries(d.axes.map(a => [a.id, a]));
      document.getElementById("cycles").innerHTML = d.cycles.map(c => {{
        const ms = c.modules.filter(m => axis === "all" || m.axisId === axis || (m.secondaryAxisIds || []).includes(axis));
        if (!ms.length) return "";
        return `
          <section>
            <p class="kicker">Ciclo ${{c.order}} · ${{c.estimatedHours}} horas</p>
            <h2>${{c.title}}</h2>
            <p style="max-width:72ch;margin-bottom:24px">${{c.objective}}</p>
            <ul class="lista-artigos">
              ${{ms.map(m => {{
                const axName = (axMap[m.axisId] || {{}}).name || m.axisId;
                const resLinks = (m.primaryResources || []).map(r => `<a href="${{r.url}}" target="_blank" rel="noopener">${{r.title}}</a>`).join(" · ");
                return `
                  <li class="cartao-artigo">
                    <div>
                      <p class="kicker">${{m.code}} · ${{m.estimatedHours}}h · ${{axName}}</p>
                      <h3>${{m.title}}</h3>
                      <ul>
                        ${{m.keyTopics.map(t => `<li>${{t}}</li>`).join("")}}
                      </ul>
                    </div>
                    <div class="caixa-projeto">
                      <span class="rotulo">Projeto prático avaliativo</span>
                      <b>${{m.capstoneProject.title}}:</b> ${{m.capstoneProject.description}}
                      <div class="fontes-mod">Base gratuita: ${{resLinks}}</div>
                      <button type="button" class="botao" data-abrir="${{m.markdownPath}}" style="margin-top:12px">Abrir aulas do módulo</button>
                    </div>
                  </li>
                `;
              }}).join("")}}
            </ul>
          </section>
        `;
      }}).join("");

      const fKeys = Object.keys(files);
      const fList = document.getElementById("f-list");
      const fCont = document.getElementById("f-content");
      function selectFile(k) {{
        fList.querySelectorAll(".btn-arq").forEach(el => el.classList.toggle("ativo", el.dataset.k === k));
        fCont.textContent = files[k];
      }}
      fList.innerHTML = fKeys.map(k => `<li><button type="button" class="btn-arq" data-k="${{k}}">${{k}}</button></li>`).join("");
      fList.querySelectorAll(".btn-arq").forEach(btn => btn.onclick = () => selectFile(btn.dataset.k));
      if (fKeys.length && !fCont.textContent) selectFile(fKeys[0]);

      document.querySelectorAll("[data-abrir]").forEach(b => b.onclick = () => {{
        mostrarAba("aulas");
        abrirDoc(b.dataset.abrir);
      }});
    }}

    /* Abas */
    function mostrarAba(id) {{
      ["curr", "aulas", "files"].forEach(t => {{
        document.getElementById("tab-" + t).classList.toggle("ativo", t === id);
        document.getElementById("view-" + t).style.display = t === id ? "block" : "none";
      }});
    }}
    document.getElementById("tab-curr").onclick = () => mostrarAba("curr");
    document.getElementById("tab-files").onclick = () => mostrarAba("files");
    document.getElementById("tab-aulas").onclick = () => {{
      mostrarAba("aulas");
      if (!document.getElementById("a-content").innerHTML) abrirDoc(ORDEM[0]);
    }};

    /* Leitor de aulas: Markdown, Mermaid e tooltips de glossário */
    const VENDOR = "{vendor_prefix}";
    let PAYLOAD = null;
    let ORDEM = [];
    let RENDER = 0;
    let libs = null;

    function carregarScript(src) {{
      return new Promise((ok, falha) => {{
        const s = document.createElement("script");
        s.src = src;
        s.onload = ok;
        s.onerror = falha;
        document.head.appendChild(s);
      }});
    }}
    function carregarBibliotecas() {{
      if (!libs) {{
        libs = Promise.all([
          carregarScript(VENDOR + "marked.min.js"),
          carregarScript(VENDOR + "purify.min.js"),
          carregarScript(VENDOR + "mermaid.min.js")
        ]).then(() => {{
          mermaid.initialize({{
            startOnLoad: false,
            securityLevel: "strict",
            theme: "base",
            themeVariables: {{
              primaryColor: "#FFE600",
              primaryTextColor: "#141414",
              primaryBorderColor: "#141414",
              lineColor: "#C8102E",
              secondaryColor: "#F2EBDD",
              tertiaryColor: "#FFFFFF",
              fontFamily: "Inter, system-ui, sans-serif"
            }}
          }});
        }});
      }}
      return libs;
    }}

    function separarCabecalho(texto) {{
      const m = texto.match(/^---\\n([\\s\\S]*?)\\n---\\n?/);
      const meta = {{}};
      if (!m) return {{ meta, corpo: texto }};
      m[1].split("\\n").forEach(l => {{
        const k = l.match(/^(\\w+):\\s*"?(.*?)"?\\s*$/);
        if (k) meta[k[1]] = k[2];
      }});
      return {{ meta, corpo: texto.slice(m[0].length) }};
    }}
    const esc = s => String(s).replace(/[&<>"]/g, c => ({{ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }})[c]);
    function tituloDoc(k) {{
      const {{ meta, corpo }} = separarCabecalho(PAYLOAD.repoFiles[k]);
      if (meta.titulo) return meta.titulo;
      const h = corpo.match(/^#\\s+(.+)$/m);
      return h ? h[1].replace(/[*_`]/g, "") : k;
    }}
    function resolverCaminho(base, rel) {{
      const partes = base.split("/");
      partes.pop();
      rel.split("/").forEach(seg => {{
        if (seg === "..") partes.pop();
        else if (seg && seg !== ".") partes.push(seg);
      }});
      return partes.join("/");
    }}
    const ancora = t => t.toLowerCase().replace(/[^\\p{{L}}\\p{{N}}\\s-]/gu, "").trim().replace(/\\s/g, "-");

    function montarSumario() {{
      const d = PAYLOAD.curriculum;
      const files = PAYLOAD.repoFiles;
      const chaves = Object.keys(files);
      const item = (k, rotulo) => `<li><button type="button" class="btn-arq" data-doc="${{esc(k)}}">${{esc(rotulo || tituloDoc(k))}}</button></li>`;
      const geral = ["README.md", "docs/COMO-ESTUDAR.md", "docs/GLOSSARIO.md", "docs/LINHA-DO-TEMPO.md", "docs/CREDITOS-IMAGENS.md"].filter(k => files[k] != null);
      ORDEM = [...geral];
      let html = `<p class="ciclo-rotulo">Comece aqui</p><ul>${{geral.map(k => item(k)).join("")}}</ul>`;
      d.cycles.forEach(c => {{
        html += `<p class="ciclo-rotulo">Ciclo ${{c.order}}</p>`;
        c.modules.forEach(m => {{
          const pasta = m.markdownPath.replace(/[^/]+$/, "") + m.code.toLowerCase() + "/";
          const aulas = chaves.filter(k => k.startsWith(pasta) && k.endsWith(".md")).sort();
          ORDEM.push(m.markdownPath, ...aulas);
          html += `<details data-mod="${{esc(m.markdownPath)}}"><summary><b>${{esc(m.code)}}</b> ${{esc(m.title)}} <small>(${{aulas.length === 1 ? "1 aula" : aulas.length + " aulas"}})</small></summary><ul>${{item(m.markdownPath, "Guia do módulo")}}${{aulas.map(k => item(k)).join("")}}</ul></details>`;
        }});
      }});
      const nav = document.getElementById("a-list");
      nav.innerHTML = html;
      nav.querySelectorAll("[data-doc]").forEach(b => b.onclick = () => abrirDoc(b.dataset.doc));
    }}

    async function abrirDoc(caminho) {{
      const files = PAYLOAD.repoFiles;
      if (files[caminho] == null) return;
      const art = document.getElementById("a-content");
      const pedido = ++RENDER;
      art.innerHTML = "<p>Carregando aula...</p>";
      try {{
        await carregarBibliotecas();
      }} catch (_) {{
        art.innerHTML = "<p>Não foi possível carregar o leitor. Confira a conexão e recarregue a página.</p>";
        return;
      }}
      const {{ corpo }} = separarCabecalho(files[caminho]);
      const html = marked.parse(corpo, {{ gfm: true }});
      art.innerHTML = DOMPurify.sanitize(html, {{ ADD_TAGS: ["abbr"], ADD_ATTR: ["title", "target"] }});

      art.querySelectorAll("pre > code.language-mermaid").forEach(code => {{
        const div = document.createElement("div");
        div.className = "mermaid";
        div.textContent = code.textContent;
        code.parentElement.replaceWith(div);
      }});
      art.querySelectorAll("h1, h2, h3, h4").forEach(h => h.id = ancora(h.textContent));
      art.querySelectorAll("img").forEach(img => {{
        img.loading = "lazy";
        img.decoding = "async";
        img.referrerPolicy = "no-referrer";
      }});
      art.querySelectorAll("abbr[title]").forEach(a => {{
        a.dataset.dica = a.title;
        a.removeAttribute("title");
        a.tabIndex = 0;
        a.setAttribute("aria-label", a.textContent + ": " + a.dataset.dica);
      }});
      art.querySelectorAll("a[href]").forEach(a => {{
        const href = a.getAttribute("href");
        if (/^(https?:|mailto:)/.test(href)) {{
          a.target = "_blank";
          a.rel = "noopener";
          return;
        }}
        const [p, frag] = href.split("#");
        const alvo = p ? resolverCaminho(caminho, decodeURIComponent(p)) : caminho;
        a.onclick = e => {{
          e.preventDefault();
          if (alvo !== caminho && files[alvo] != null) abrirDoc(alvo).then(() => frag && irPara(frag));
          else if (frag) irPara(frag);
        }};
      }});
      try {{
        await mermaid.run({{ nodes: art.querySelectorAll(".mermaid") }});
      }} catch (erro) {{
        if (pedido === RENDER) console.error(erro);
      }}
      if (pedido !== RENDER) return;

      const i = ORDEM.indexOf(caminho);
      const ant = ORDEM[i - 1];
      const prox = ORDEM[i + 1];
      const navAula = document.createElement("nav");
      navAula.className = "navegacao-aula";
      navAula.innerHTML = (ant ? `<button type="button" class="botao" data-doc="${{esc(ant)}}">Anterior: ${{esc(tituloDoc(ant))}}</button>` : "<span></span>") +
        (prox ? `<button type="button" class="botao" data-doc="${{esc(prox)}}">Próxima: ${{esc(tituloDoc(prox))}}</button>` : "");
      navAula.querySelectorAll("[data-doc]").forEach(b => b.onclick = () => abrirDoc(b.dataset.doc));
      art.appendChild(navAula);

      document.querySelectorAll("#a-list .btn-arq").forEach(b => b.classList.toggle("ativo", b.dataset.doc === caminho));
      document.querySelectorAll("#a-list details").forEach(det => {{
        if (det.querySelector(`[data-doc="${{CSS.escape(caminho)}}"]`)) det.open = true;
      }});
      history.replaceState(null, "", "#aula=" + encodeURIComponent(caminho));
      art.scrollIntoView({{ block: "start" }});
    }}
    function irPara(frag) {{
      const alvo = document.getElementById(decodeURIComponent(frag));
      if (alvo) alvo.scrollIntoView({{ block: "start" }});
    }}

    /* Tooltip acessível: mouse, teclado e toque */
    const dica = document.createElement("div");
    dica.className = "dica";
    dica.hidden = true;
    dica.setAttribute("role", "tooltip");
    document.body.appendChild(dica);
    function mostrarDica(el) {{
      dica.textContent = el.dataset.dica;
      dica.hidden = false;
      const r = el.getBoundingClientRect();
      const largura = dica.offsetWidth;
      const maxEsq = window.scrollX + document.documentElement.clientWidth - largura - 8;
      dica.style.left = Math.max(8, Math.min(r.left + window.scrollX, maxEsq)) + "px";
      dica.style.top = (r.bottom + window.scrollY + 6) + "px";
    }}
    const esconderDica = () => {{ dica.hidden = true; }};
    document.addEventListener("mouseover", e => {{
      const a = e.target.closest && e.target.closest("abbr[data-dica]");
      if (a) mostrarDica(a);
    }});
    document.addEventListener("mouseout", e => {{
      if (e.target.closest && e.target.closest("abbr[data-dica]")) esconderDica();
    }});
    document.addEventListener("focusin", e => {{
      const a = e.target.closest && e.target.closest("abbr[data-dica]");
      if (a) mostrarDica(a);
    }});
    document.addEventListener("focusout", esconderDica);
    document.addEventListener("keydown", e => {{ if (e.key === "Escape") esconderDica(); }});

    document.getElementById("f-login").onsubmit = async e => {{
      e.preventDefault();
      const err = document.getElementById("err");
      err.style.display = "none";
      try {{
        const bundle = JSON.parse(document.getElementById("enc-payload").textContent);
        const payload = await unlock(bundle, document.getElementById("pwd").value);
        document.getElementById("auth-sec").style.display = "none";
        document.getElementById("app").style.display = "block";
        PAYLOAD = payload;
        renderApp(payload);
        montarSumario();
        const pedido = decodeURIComponent((location.hash.match(/^#aula=(.+)$/) || [])[1] || "");
        if (pedido && payload.repoFiles[pedido] != null) {{
          mostrarAba("aulas");
          abrirDoc(pedido);
        }}
      }} catch (_) {{
        err.style.display = "block";
      }}
    }};
  </script>
</body>
</html>"""
    return minify_html(html_template)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Higieniza estilo, minifica todos os arquivos do repositório e criptografa com chave."
    )
    parser.add_argument(
        "--key",
        "--password",
        dest="key",
        required=True,
        help="Chave/senha que será usada para criptografar todo o repositório minificado.",
    )
    args = parser.parse_args()

    sanitize_repository_files()
    payload_dict = collect_and_minify_repo()
    minified_payload_bytes = json.dumps(
        payload_dict, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")

    encrypted_bundle = encrypt_with_key(minified_payload_bytes, args.key)
    encrypted_bundle_str = json.dumps(encrypted_bundle, separators=(",", ":"), ensure_ascii=False)

    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    (ASSETS_DIR / "curriculum.enc.json").write_text(encrypted_bundle_str, encoding="utf-8")
    root_assets = ROOT_DIR / "assets"
    root_assets.mkdir(parents=True, exist_ok=True)
    (root_assets / "curriculum.enc.json").write_text(encrypted_bundle_str, encoding="utf-8")

    # O leitor de aulas carrega marked, DOMPurify e Mermaid de vendor/ (cópias locais, sem CDN externa).
    (VIEWER_DIR / "index.html").write_text(build_viewer_html(encrypted_bundle_str, "../vendor/"), encoding="utf-8")
    (ROOT_DIR / "index.html").write_text(build_viewer_html(encrypted_bundle_str, "vendor/"), encoding="utf-8")

    redirect_path = VIEWER_DIR / "redirect-lucasrafaldini.html"
    if redirect_path.exists():
        redirect_min = minify_html(redirect_path.read_text(encoding="utf-8"))
        redirect_path.write_text(redirect_min, encoding="utf-8")

    print(f"OK: {len(payload_dict['repoFiles'])} arquivos higienizados e minificados em {DIST_MIN_DIR}")
    print(f"OK: Pacote criptografado salvo em {ASSETS_DIR / 'curriculum.enc.json'}")
    print(f"OK: Portal Memória de Trabalho minificado e cifrado gerado em {VIEWER_DIR / 'index.html'}")


if __name__ == "__main__":
    main()
