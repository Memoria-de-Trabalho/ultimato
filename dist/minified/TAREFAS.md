# Tarefas · O Último Curso

## Concluído na fundação (v2.0)

- [x] Estrutura completa do repositório em 3 ciclos, 5 eixos e 20 módulos (1.320 horas).
- [x] Inclusão integral do cânone de Filosofia, Sociologia, Marxismo, Anarquismo, Teoria Crítica e Pensamento Brasileiro: Platão, Aristóteles, Hegel, Feuerbach, Heidegger, Marx, Engels, Durkheim, Weber, Bakunin, Kropotkin, Lênin (amplo), Trótski (amplo), Gramsci (amplo), Lukács, Walter Benjamin (amplo), Ortega y Gasset e Ezra Pound (com separação analítica entre obra e pessoa), Foucault, Habermas, Frantz Fanon, Sérgio Buarque de Holanda e Florestan Fernandes.
- [x] Criação das 20 ementas individuais em Markdown dentro de `trilhas/`.
- [x] Adequação integral à identidade visual e ao guia de estilo do Memória de Trabalho (zero emojis, zero travessão, zero "Civic Tech"). <!-- estilo: ok -->
- [x] Pipeline unificado de minificação de todos os arquivos e criptografia por chave (`AES-256-GCM` + `PBKDF2-HMAC-SHA256`) em `scripts/build_and_encrypt.py`.
- [x] Configuração agêntica completa (`AGENTS.md`, `CLAUDE.md`, `docs/ESTILO.md`, `scripts/revisar-estilo.py`, `.claude/skills/`, `.claude/agents/`, `.agents/skills/`).

## Concluído na versão 2.1 (aulas do Ciclo 1)

- [x] Leitor de aulas no portal (aba Aulas e Ementas), com Markdown, diagramas Mermaid, tooltips acessíveis por mouse, teclado e toque, e navegação entre aulas.
- [x] Guias de entrada: `docs/COMO-ESTUDAR.md`, `docs/LINHA-DO-TEMPO.md`, `docs/GLOSSARIO.md` e `docs/CREDITOS-IMAGENS.md`.
- [x] Ciclo 1 completo: guias dos 7 módulos e 46 aulas (MOD-101 a MOD-107), com imagens históricas conferidas, diagramas, exercícios com gabarito e código Python testado.
- [x] Correção do cabeçalho do MOD-102, que dizia MOD-101.

## Próximos passos

- [ ] Escrever as aulas do Ciclo 2 (MOD-201 a MOD-207), começando por MOD-201 (Lênin e Trótski) e MOD-202 (engenharia de software).
- [ ] Escrever as aulas do Ciclo 3 (MOD-301 a MOD-306).
- [ ] Conferir na Wikimedia Commons as imagens do Ciclo 2 (Lênin, Trótski, Gramsci, Lukács, Benjamin, Ortega, Pound, Fanon, Sérgio Buarque, Florestan) e acrescentá-las aos créditos.
- [ ] Acrescentar um teste automático que execute os blocos Python das aulas e desenhe todos os diagramas Mermaid.

- [ ] Expandir a bibliografia comentada capítulo a capítulo em `recursos/bibliografia/`.
- [ ] Adicionar código-base inicial dos laboratórios Python em `projetos/ciclo-1/`.
- [ ] Incluir atalho ou redirecionamento em `lucasrafaldini.github.io` apontando para `https://memoria-de-trabalho.github.io/ultimato/`.