# Guia de Contribuição (`CONTRIBUTING.md`)

> **Aviso de Idioma:** Este currículo e todos os seus recursos de apoio foram estruturados exclusivamente em **Português (PT-BR)**.

Obrigado pelo interesse em contribuir com **O Último Curso**! Nossa governança curricular inspira-se nas boas práticas da **Open Source Society University (OSSU)** e da **Universidade Livre (UBL)**.

## 1. Critérios Rigorosos de Curadoria
Qualquer sugestão de novo curso, livro, artigo ou ferramenta deve obedecer obrigatoriamente aos **4 Pilares do Currículo**:
1. **100% em Português (PT-BR):** O material didático principal deve estar em língua portuguesa (original, tradução oficial ou legendagem completa de excelência).
2. **Acesso Gratuito e Aberto:** Nenhum recurso obrigatório pode exigir pagamento para acesso ao conteúdo de aprendizagem.
3. **Rigor Acadêmico e Pragmatismo Técnico:** Na Engenharia de Software, priorizamos código limpo, testável e documentado; nas Ciências Sociais e Ciência Política, priorizamos obras canônicas, periódicos revisados por pares (SciELO, IPEA, CEBRAP) e cátedras públicas (USP, UNIVESP, UNICAMP, UFMG, ENAP).
4. **Sincronia entre Markdown e JSON:** Toda alteração na matriz do `README.md` ou nos arquivos de `trilhas/` **deve** ser refletida no arquivo [`data/curriculum.json`](./data/curriculum.json) e validada contra [`schemas/curriculum.schema.json`](./schemas/curriculum.schema.json).

## 2. Fluxo de Pull Request
1. Crie uma branch descritiva (`git checkout -b feat/atualiza-mod-203`).
2. Atualize o Markdown correspondente e o `data/curriculum.json`.
3. Se utilizar o visualizador cifrado, regere o pacote de visualização conforme instruções em `docs/arquitetura-hospedagem/DEPLOY_GITHUB_PAGES_AUTENTICADO.md`.
4. Abra o Pull Request detalhando a justificativa pedagógica da mudança.