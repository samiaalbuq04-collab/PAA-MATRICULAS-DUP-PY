# PAA: Contagem de Operações, Tema 1 (Matrículas duplicadas)

**Equipe:** David Neves de Figueiredo, Samia Albuquerque dos Santos, Yara da Silva Vaz
**Disciplina:** Projeto e Análise de Algoritmos, CIESA, 4º período (Ciência da Computação)

## Como reproduzir

Requer Python 3 (testado com 3.13.3 no Windows) e o `trabalho_base.py` na mesma pasta, sem alterações.

```
python tema_1.py
```

O comando roda a verificação de correção, imprime as tabelas de todas as medições e grava `medicoes.csv`.

## Problema

Dada uma lista de n matrículas, decidir se há alguma repetida e, se houver, devolver uma delas. Devolve `(-1, contagem)` quando não há repetição.

## Operação básica

Comparação entre duas matrículas. Na versão esperta, as comparações da ordenação e as da varredura são contadas separadamente e somadas no final.

## Versões

**Ingênua.** Para cada posição i, compara com todas as posições j > i e para na primeira repetição encontrada.

**Esperta.** Ordena uma cópia com o `mergesort` da base e varre a lista ordenada comparando apenas vizinhos. Duplicadas ficam em sequência após a ordenação, então basta olhar pares adjacentes.

## Contagem à mão

Ingênua, pior caso (sem repetição):

T(n) = Σᵢ₌₀ⁿ⁻² Σⱼ₌ᵢ₊₁ⁿ⁻¹ 1 = n(n−1)/2, ou seja, Θ(n²).

Esperta:

- Ordenação (mergesort): no pior caso, n⌈log₂n⌉ − 2^⌈log₂n⌉ + 1 comparações (igual a n log₂n − n + 1 quando n é potência de 2); no melhor caso, cerca de (n/2) log₂n.
- Varredura: entre 1 e n − 1 comparações.
- Total no pior caso: ≈ n log₂n, ou seja, Θ(n log n). A varredura é linear e fica abaixo da ordenação; na soma, o termo dominante define a classe.

## Melhor e pior caso

| Versão | Melhor caso | Pior caso |
|---|---|---|
| Ingênua | `[5, 5, 100, 101, ...]`: repetição nas duas primeiras posições, 1 comparação | Entrada sem repetição (`distintos(n)`), n(n−1)/2 comparações |
| Esperta | `[5, 5, 100, 101, ...]`: a ordenação continua custando n log n, a varredura para na primeira posição | Entrada sem repetição (`distintos(n)`): a varredura percorre tudo, n − 1 comparações |

As entradas são construídas em `melhor_caso(n)` e `distintos(n)`, com semente 42.

## Caso médio

Hipótese declarada: valores aleatórios inteiros entre 0 e ⌊n/2⌋, gerados por `aleatorio(n, 0, n//2, semente=s)` com s = 0 a 29. Como há ⌊n/2⌋ + 1 valores possíveis e n elementos, para n ≥ 3 sempre existe repetição. A média dos 30 valores de contagem é reportada.

## Resultados: teste do dobro

| Medição | Razão que estabiliza | Coluna dobro |
|---|---|---|
| Ingênua, pior caso | c/n² ≈ 0,50 | 4,00 |
| Ingênua, melhor caso | c = 1 (constante) | 1,00 |
| Ingênua, caso médio | não estabilizou com 30 amostras | 1,62 a 2,29 |
| Esperta, pior caso | c/(n log₂n) ≈ 0,98 | 2,13 a 2,28 |
| Esperta, melhor caso | c/(n log₂n) de 0,48 a 0,49 | 2,13 a 2,31 |
| Esperta, caso médio | c/(n log₂n) sobe de 0,82 a 0,88 | 2,24 a 2,37 |
| Esperta, fase de ordenação (pior caso) | c/(n log₂n) de 0,83 a 0,93 | 2,14 a 2,33 |
| Esperta, fase de varredura (pior caso) | c/n = 1,00 | 2,00 |

A série grande (12 500 a 100 000) foi medida só nas versões espertas, em chamadas separadas, de modo que a primeira linha de cada série mostra `-` no dobro. A ingênua não foi medida nessa série porque cresce com n².

As tabelas completas estão na saída de `python tema_1.py` e em `medicoes.csv`.

## Confronto entre contagem à mão e medição

| n | Ingênua pior: n(n−1)/2 | Medido | Varredura: n−1 | Medido | Ordenação, pior caso exato | Medido |
|---|---|---|---|---|---|---|
| 100 | 4 950 | 4 950 | 99 | 99 | 573 | 553 |
| 400 | 79 800 | 79 800 | 399 | 399 | 3 089 | 2 942 |
| 1600 | 1 279 200 | 1 279 200 | 1 599 | 1 599 | 15 553 | 15 036 |

- A ingênua e a varredura batem exatamente com a conta à mão.
- A ordenação medida fica abaixo do pior caso exato porque a entrada `distintos(n)` é aleatória, e não o pior caso construído do mergesort.
- No melhor caso da ordenação, a conta (n/2) log₂n dá 332 para n = 100 e 8 515 para n = 1600, e o medido foi 316 e 8 256. A diferença vem de n não ser potência de 2: os pisos e tetos do log e da divisão da lista reduzem o total.

## Cobrança

- **Por que a varredura não define a classe:** ela custa no máximo n − 1, enquanto a ordenação custa cerca de n log₂n. Na soma, vale o termo maior, então a classe é n log n.
- **Peso da varredura:** 15% do total em n = 100 e 10% em n = 1600.
- **Ordem de grandeza (n = 1600):** a ingênua faz 1 279 200 comparações e a esperta faz 16 635, cerca de 77 vezes menos.

## Limitações

- O caso médio usa 30 entradas. A razão não estabilizou, então a classe do caso médio não é afirmada.
- A medição "pior caso" da esperta usa entrada aleatória, e não o pior caso construído do mergesort.
- Medimos contagem de comparações, não tempo de execução.

## Estrutura do repositório

- `trabalho_base.py`: base comum do professor, sem alterações.
- `tema_1.py`: versões ingênua e esperta, testes de correção, medições e geração do CSV.
- `medicoes.csv`: dados brutos gerados por `tema_1.py`, com uma linha por medição (versão, n, contagem).
- `README.md`: este arquivo.

## Divisão de trabalho

- **David:** versão ingênua e testes de correção.
- **Samia:** versão esperta, com as fases contadas separadamente.
- **Yara:** medições, caso médio, geração do CSV.
- **Todos:** revisão do README e funções misteriosas.

## Declaração de uso de IA

[Preencher pela equipe com o que de fato foi feito.] Modelo: usamos o Claude como apoio para [explicar o enunciado, sugerir a estrutura do código, revisar as contagens e redigir o README]. Aproveitamos [o que foi usado de fato]. Todas as medições foram executadas por nós, e cada integrante pode explicar qualquer linha do código ou contador.
