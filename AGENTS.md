# O Último Curso (ultimato): instruções para agentes

Repositório oficial de **O Último Curso**, formação aberta, gratuita e interdisciplinar em Engenharia de Software, Letramento Digital, Filosofia Política e Ciências Sociais Computacionais (1.320 horas, 20 módulos, 3 ciclos). O repositório pertence à organização **Memória de Trabalho** (`Memoria-de-Trabalho/ultimato`) e é publicado pelo GitHub Pages em `https://memoria-de-trabalho.github.io/ultimato/`.

## Regras obrigatórias

- **Idioma:** todo o currículo, ementas, códigos, comentários, commits e documentação são escritos exclusivamente em português do Brasil (`pt-BR`). O aviso de idioma deve permanecer visível no `README.md`, nas páginas HTML e no topo de cada ementa em `trilhas/`.
- **Commits em nome da organização:** autor e committer são sempre `Memória de Trabalho <noreply@memoria-de-trabalho.github.io>` (configurado no `git config` local). Nunca use nome pessoal nos metadados do commit e nunca inclua linha `Co-Authored-By`, nem de pessoa nem de IA.
- **Contato público:** conteúdo e tecnicalidades com Lucas Rafaldini, pelo e-mail `thothandson@icloud.com` (Thoth & Son).
- **Estilo de escrita e vocabulário:** todo texto segue `docs/ESTILO.md` e é validado por `scripts/revisar-estilo.py`. Resumo das proibições:
  - Zero travessão ou meia-risca e zero hífen solto usado como travessão;
  - Zero emojis em qualquer arquivo do repositório;
  - Zero exclamações e zero clichês de IA ("não é sobre X, é sobre Y", "não se trata de", "vale ressaltar", "mergulhar", "robusto", "alavancar"); <!-- estilo: ok -->
  - Zero anglicismos de moda ou jargão de fundação liberal (como "Civic Tech": use sempre "Ferramentas de Interesse Público" ou "Software Livre de Interesse Público"). <!-- estilo: ok -->
- **Rigor teórico nas Ciências Sociais:** os módulos teóricos estudam diretamente as fontes primárias em português de Platão, Aristóteles, Hegel, Feuerbach, Heidegger, Marx, Engels, Durkheim, Weber, Bakunin, Kropotkin, Lênin (amplo), Trótski (amplo), Gramsci (amplo), Lukács, Walter Benjamin (amplo), Ortega y Gasset e Ezra Pound (incluindo o estudo metodológico da necessidade de separar analiticamente obra e pessoa), Foucault, Habermas, Frantz Fanon, Sérgio Buarque de Holanda e Florestan Fernandes.
- **Identidade visual do Memória de Trabalho:** papel `#F2EBDD`, tinta `#141414`, vermelho `#C8102E`, amarelo `#FFE600`, suave `#5B544A`, linha `#D8CDB8`; títulos em `Anton`, chapéus/metadados em `Special Elite`, corpo em `Inter`.
- **Autenticação simplificada por minificação e criptografia:** nunca crie servidores complexos de login. O script `scripts/build_and_encrypt.py` minifica todos os arquivos do repositório em `dist/minified/`, empacota o currículo e os arquivos, cifra o pacote inteiro com `PBKDF2-HMAC-SHA256` (250.000 iterações) + `AES-256-GCM` usando a senha como chave e gera `index.html` (na raiz e em `viewer/index.html`) com o cofre embutido.
- **Aulas:** siga a seção "Recursos didáticos das aulas" de `docs/ESTILO.md` (estrutura, tooltips com `<abbr>`, diagramas Mermaid, imagens só da Wikimedia Commons com licença conferida e crédito em `docs/CREDITOS-IMAGENS.md`, código Python testado).
- **Não edite à mão o que é compilado:** `index.html`, `viewer/index.html`, `assets/curriculum.enc.json`, `viewer/assets/curriculum.enc.json` e `dist/minified/` são gerados por `scripts/build_and_encrypt.py`. Edite sempre a fonte (`data/curriculum.json`, `README.md`, `trilhas/**/*.md`, `scripts/build_and_encrypt.py`) e rode o compilador.

## Estrutura do repositório

| Caminho | O que é |
|---|---|
| `AGENTS.md` / `CLAUDE.md` | Contexto operacional, regras de estilo, arquitetura e comandos para agentes |
| `README.md` | Manifesto, cânone teórico, matriz curricular de 20 módulos (1.320h) e instruções |
| `data/curriculum.json` | Fonte de dados estruturada dos 5 eixos, 3 ciclos e 20 módulos |
| `schemas/curriculum.schema.json` | JSON Schema (Draft 2020-12) para validação da matriz curricular |
| `trilhas/ciclo-*/` | Guias dos 20 módulos em Markdown com cabeçalho YAML |
| `trilhas/ciclo-*/mod-XXX/` | Aulas de cada módulo (`aula-NN-<slug>.md`), com tooltips, diagramas Mermaid, imagens da Wikimedia Commons e exercícios com gabarito |
| `docs/COMO-ESTUDAR.md`, `docs/LINHA-DO-TEMPO.md`, `docs/GLOSSARIO.md`, `docs/CREDITOS-IMAGENS.md` | Guias de entrada do aluno, glossário geral dos tooltips e créditos de todas as imagens |
| `vendor/` | Cópias locais de marked, DOMPurify e Mermaid, usadas pelo leitor de aulas do portal (não editar) |
| `templates/` | Modelos de fichamento teórico (`FICHAMENTO_TEORICO.md`), entrega de projeto (`ENTREGA_PROJETO.md`) e progresso (`PROGRESSO_ALUNO.md`) |
| `docs/ESTILO.md` | Guia de estilo editorial e terminológico |
| `docs/arquitetura-hospedagem/` | Documentação da criptografia estática e ponte com `lucasrafaldini.github.io` |
| `scripts/revisar-estilo.py` | Validador automático de estilo editorial e integridade do currículo |
| `scripts/build_and_encrypt.py` | Higieniza, minifica todos os arquivos do repositório e gera o portal criptografado |
| `index.html` / `viewer/index.html` | Portal estático minificado com cofre `AES-256-GCM` embutido (gerado por script) |
| `viewer/redirect-lucasrafaldini.html` | Página de redirecionamento para usar em `lucasrafaldini.github.io/o-ultimo-curso/` |
| `dist/minified/` | Versão minificada de todos os arquivos do repositório (gerada por script) |
| `TAREFAS.md` / `REGISTRO.md` | Backlog de evolução do curso e registro de decisões arquiteturais |

## Comandos principais

```bash
# 1. Conferir estilo editorial e integridade dos 20 módulos
python3 scripts/revisar-estilo.py

# 2. Minificar todo o repositório e criptografar com a chave (senha)
python3 scripts/build_and_encrypt.py --key "ultimato-ptbr"

# 3. Servir localmente para conferência (desktop e 375 px)
python3 -m http.server 8080
```

## Skills e subagentes disponíveis

- `.claude/agents/curador-pedagogico.md`: audita ementas e módulos quanto ao rigor teórico nas Ciências Sociais e na Engenharia de Software, fontes gratuitas em PT-BR e aderência ao guia de estilo.
- `.claude/skills/novo-modulo/SKILL.md` (e `.agents/skills/novo-modulo/SKILL.md`): fluxo passo a passo para criar ou atualizar módulos em `trilhas/` e `data/curriculum.json`.
- `.claude/skills/compilar-e-publicar/SKILL.md` (e `.agents/skills/compilar-e-publicar/SKILL.md`): fluxo seguro para validar estilo, minificar, criptografar, commitar como `Memória de Trabalho` e publicar no GitHub.
