## O que são tuples?

Uma tupla é uma estrutura bastante similar a uma lista, com apenas uma diferença: os elementos inseridos em uma tupla não podem ser alterados, diferente de uma lista onde podem ser alterados livremente. Sendo assim, em um primeiro momento, podemos pensar em uma tupla como uma lista que não pode ser alterada, mas não é bem assim...

É certo que as tuplas possuem diversas características das listas, porém os usos são distintos. Phillip J. Eby, contribuidor de vários projetos do Python, certa vez disse:

"É um equívoco pensar nas tuplas como listas constantes. As listas são destinadas a serem sequências homogêneas, enquanto que os Tuplas são estruturas de dados heterogêneas.".

Sendo assim, apesar de bastante similares, a tupla é utilizada para armazenar dados de tipos diferentes, enquanto que a lista é para dados do mesmo tipo.

## Diferenças entre listas e tuplas

As tuplas possuem algumas vantagens com relação às listas, que são:

* Como as tuplas são imutáveis, a iteração sobre elas é mais rápida e, consequentemente, possuem um ganho de desempenho com relação às listas;
* Tuplas podem ser utilizadas como chave para um dicionário, já que seus elementos são imutáveis. Já com a lista, isso não é possível;
* Se for necessário armazenar dados que não serão alterados, utilize uma tupla. Isso garantirá que esses sejam protegidos de alterações posteriores.

