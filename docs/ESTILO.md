# Guia de estilo · O Último Curso (Memória de Trabalho)

Vale para tudo o que entra neste repositório: `README.md`, `data/curriculum.json`, ementas em `trilhas/`, templates, documentação e interface HTML. Quem escreve aqui (pessoa ou agente) lê isto antes e roda `python3 scripts/revisar-estilo.py` depois.

## A voz

Escrevemos com clareza, precisão conceitual e sem pose. O curso trata de filosofia clássica, dialética, marxismo, anarquismo, sociologia, pensamento brasileiro e engenharia de software, mas rigor teórico não é sinônimo de texto empolado nem de jargão importado.

- **Direto ao ponto:** apresente o conceito, a obra de origem e o problema concreto que ele resolve ou explica.
- **Português do Brasil de ponta a ponta:** evite anglicismos de moda quando existe termo preciso em português.
- **Fidelidade às fontes primárias:** ao tratar de Marx, Engels, Lênin, Trótski, Gramsci, Lukács, Benjamin, Ortega y Gasset, Ezra Pound, Foucault, Habermas, Fanon, Sérgio Buarque de Holanda ou Florestan Fernandes, nomeie as obras e use as categorias exatas de cada autor.

## Proibido

O script `scripts/revisar-estilo.py` barra automaticamente os itens abaixo:

1. **Emojis:** nenhum arquivo do repositório pode conter emojis.
2. **Travessão e meia-risca** como pausa ou aposto. Use dois-pontos, vírgula, ponto, parênteses ou ponto-médio (`·`) em cabeçalhos de metadados (`MOD-101 · 70h`). Em intervalos numéricos, escreva `1914 a 1915`.
3. **Hífen solto usado como travessão** (`palavra - palavra`). <!-- estilo: ok -->
4. **A fórmula da correção dramática:** "não é sobre X, é sobre Y", "não se trata de X, mas de Y", "mais do que X, é Y". <!-- estilo: ok -->
5. **Clichês de texto gerado:** "vale ressaltar", "vale destacar", "é importante destacar", "no fim do dia", "em suma", "mergulhar", "navegar por", "desvendar", "potencializar", "alavancar", "robusto", "divisor de águas".
6. **Anglicismos de ONG/consultoria:** "Civic Tech" ou "civic-tech". Use sempre "Ferramentas de Interesse Público" ou "Software Livre de Interesse Público". <!-- estilo: ok -->
7. **Exclamação** em títulos, textos ou avisos.

## Recursos didáticos das aulas

As aulas em `trilhas/<ciclo>/mod-XXX/aula-NN-<slug>.md` seguem regras próprias, além das proibições acima.

### Estrutura

Cabeçalho YAML com `tipo: "aula"`, `modulo`, `ordem`, `titulo` (no formato `Aula N · Título`), `duracao` e `language`; aviso de idioma; e as seções, nesta ordem: "O que você vai aprender", "Pergunta de abertura", a exposição em seções numeradas, "Leitura guiada", "Exercícios" (gabarito dentro de `<details>`), "Resumo da aula" e "Para ir além".

### Tooltips

Todo jargão (grego, alemão, marxista, sociológico, computacional) recebe tooltip na primeira vez que aparece em cada aula, com a sintaxe `<abbr title="Termo: definição curta.">termo</abbr>`. O texto do `title` não pode conter aspas duplas nem a barra vertical. Todo termo com tooltip deve ter verbete correspondente em `docs/GLOSSARIO.md`.

### Diagramas

Conceitos com muitas peças móveis ganham um diagrama Mermaid (fluxograma, linha do tempo, sequência ou `gitGraph`). Rótulos com caracteres especiais vão entre aspas; quebras de linha usam `<br/>`. Não use a barra vertical dentro de rótulos. Todo diagrama precisa ser desenhado sem erro no portal (o leitor do `index.html`) e no GitHub.

### Imagens

Só entram imagens da Wikimedia Commons cuja existência e licença tenham sido conferidas, referenciadas pelo endereço `https://commons.wikimedia.org/wiki/Special:FilePath/<arquivo>?width=500` (sem o parâmetro `width` quando a imagem original tiver menos de 500 pixels de largura). Cada imagem tem legenda em itálico logo abaixo, com autor, data e licença, e uma linha em `docs/CREDITOS-IMAGENS.md`. Não publique retratos de licença duvidosa.

### Código

Todo bloco ```` ```python ```` de uma aula precisa rodar sem erro, na ordem em que aparece no arquivo. Trechos ilustrativos que dependem de arquivos ou módulos externos usam ```` ```text ````. O validador `scripts/revisar-estilo.py` não aplica as regras de hífen e exclamação dentro de blocos de código e trechos em crase, porque ali vale a sintaxe da linguagem.

### Citações

Citações de fontes primárias trazem a obra e, quando a tradução for do curso, a indicação "tradução livre". Uma citação literal que contenha exclamação pode ser mantida com o marcador `<!-- estilo: ok -->` no fim da linha.
