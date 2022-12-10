## DEFININDO LISTAS

lista_simples_inteiro = [1, 2, 5, 12, 56, 98]  # Lista normal de inteiros
lista_simples_string = ["Meu", "nome", "é", "Willian"]  # Lista normal de strings
lista_simples_mesclada = ["lista", 5, 20, "mesclada"]  # Lista com elementos diferentes
nested_list = [[20, True, 35, False], ["Willian", 6, "bonitão"]]  # Lista composta por outras listas

## MANIPULANDO AS LISTAS

### Utilizando len()
"""
DESCRIÇÃO => A função lenth retorna o tamanho do vetor
"""
print("================================")
print("========| FUNÇÃO LEN() |========")

print(len(lista_simples_mesclada))
print(len(lista_simples_inteiro))

### Utilizando append()
"""
DESCRIÇÃO => A função append adiciona o elemento no final do vetor;
"""
print("===================================")
print("========| FUNÇÃO APPEND() |========")
lista_simples_inteiro.append(50)
lista_simples_string.append("Ricardo")

print(lista_simples_inteiro)
print(lista_simples_string)

### Utilizando insert()
"""
DESCRIÇÃO => A função insert adiciona o elemento na posição desejada;
"""
print("===================================")
print("========| FUNÇÃO INSERT() |========")
lista_simples_inteiro.insert(1, 100)
lista_simples_string.insert(2, "Gabriel")

print(lista_simples_inteiro)
print(lista_simples_string)

### Utilizando remove()
"""
DESCRIÇÃO => A função remove faz uma busca no vetor e apaga o elemento desejado;
"""
print("===================================")
print("========| FUNÇÃO REMOVE() |========")
lista_simples_inteiro.remove(1)
lista_simples_string.remove("Meu")

print(lista_simples_inteiro)
print(lista_simples_string)

### Utilizando index()
"""
DESCRIÇÃO => A função index percorre o vetor e busca o elemento informado retornando sua posição;
"""
print("==================================")
print("========| FUNÇÃO INDEX() |========")
index = lista_simples_inteiro.index(2)
index_2 = lista_simples_string.index("Willian")
print(index)
print(index_2)

### Utilizando count()
"""
DESCRIÇÃO => A função count conta os elementos presentes no vetor;
"""
print("==================================")
print("========| FUNÇÃO COUNT() |========")
contador_01 = lista_simples_mesclada.count(2)
contador_02 = lista_simples_string.count(3)

print(contador_01)
print(contador_02)

### Utilizando sort()
"""
DESCRIÇÃO => A função sort ordena o vetor de acordo com o reverse 
            TRUE= DECRESCENTE
            FALSE= CRESCENTE
"""

print("=================================")
print("========| FUNÇÃO SORT() |========")
lista_simples_string.sort(reverse=True)
lista_simples_inteiro.sort(reverse=False)

print(lista_simples_string)
print(lista_simples_inteiro)
