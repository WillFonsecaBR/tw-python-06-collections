## O que são ranges?

Ranges são sequências de números imutáveis e muito utilizadas para determinar a quantidade de interações de um loop for. Um range retorna uma lista de elementos no intervalo especificado em sua construção, porém, possui uma grande vantagem quando comparada a uma lista ou uma tupla: apesar de retornar uma lista de elementos, o range utiliza o menor espaço possível para isso.

Por exemplo, quando queremos criar uma lista com 10 elementos, é alocado na memória o espaço necessário para armazenar estes 10 elementos. Quando criamos uma lista com 10 elementos utilizando o range, é utilizado um espaço mínimo para armazenar estes dados, já que os elementos são calculados para cada interação e não armazenados no momento de sua criação.