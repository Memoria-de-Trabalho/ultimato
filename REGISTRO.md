# Registro de decisões · O Último Curso

## 2026-11-05 · Arquitetura, estilo e publicação na org Memória de Trabalho

- **Repositório de produção:** publicado em `Memoria-de-Trabalho/ultimato` com GitHub Pages ativo em `https://memoria-de-trabalho.github.io/ultimato/`.
- **Identidade visual:** replicada diretamente do site principal do Memória de Trabalho (`#F2EBDD`, `#141414`, `#C8102E`, `#FFE600`, fontes `Anton`, `Special Elite` e `Inter`).
- **Higiene editorial e terminológica:** removidos todos os emojis, travessões, meia-riscas e o anglicismo "Civic Tech" (substituído por "Ferramentas de Interesse Público"). <!-- estilo: ok -->
- **Autenticação e empacotamento:** adotada minificação de todos os arquivos do repositório em `dist/minified/` combinada com criptografia simétrica `AES-256-GCM` derivada da senha via `PBKDF2-HMAC-SHA256` (250.000 iterações) embutida no `index.html`.
- **Densidade em Ciências Sociais:** currículo expandido para 20 módulos (1.320 horas, sendo 670 horas de leitura direta de fontes primárias em português).

## 2026-11-05 · Aulas, leitor no portal e recursos didáticos

- **Guia e aulas:** cada módulo passa a ter um guia (`trilhas/<ciclo>/NN-<slug>.md`, o mesmo arquivo apontado por `markdownPath`) e uma pasta de aulas (`trilhas/<ciclo>/mod-XXX/`). O portal descobre as aulas pela pasta, sem mudar o esquema de `data/curriculum.json`.
- **Leitor no portal:** a aba "Aulas e Ementas" renderiza o Markdown decifrado com marked, sanitiza o HTML com DOMPurify e desenha os diagramas com Mermaid. As três bibliotecas ficam em `vendor/`, servidas pelo próprio GitHub Pages, sem CDN externa.
- **Tooltips:** `<abbr title>` funciona no GitHub e, no portal, vira um tooltip acessível por mouse, teclado e toque.
- **Imagens:** carregadas da Wikimedia Commons por `Special:FilePath`, sem copiar arquivos para o repositório; cada uma foi conferida e tem crédito em `docs/CREDITOS-IMAGENS.md`.
- **Validador:** `scripts/revisar-estilo.py` passou a ignorar blocos de código e trechos em crase para as regras de prosa e a acusar exclamações no texto.
