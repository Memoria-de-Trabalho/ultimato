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