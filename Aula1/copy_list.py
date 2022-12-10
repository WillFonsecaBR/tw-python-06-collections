# COPIANDO LISTAS EM PYTHON

import copy

## Listas
lista_simples_inteiro = [1, 2, 5, 12, 56, 98]  # Lista normal de inteiros
lista_simples_string = ["Meu", "nome", "é", "Willian"]  # Lista normal de strings

## Deep Copy
"""
DEEP COPY => Este metodo copia todo os elementos da lista para um novo
            espaço de memoria, então, se a lista for alterada não ira alterar 
            a outra antiga;
"""
nova_lista= copy.deepcopy(lista_simples_inteiro)
nova_lista.append("Roberval")

print("=============================")
print("========| DEEP COPY |========")
print(lista_simples_inteiro)
print(nova_lista)

## Shallow Copy
"""
DEEP COPY => Este metodo copia todo os elementos da lista mais apontando 
            para o antigo endereõ de memoria, caso você altere a nova lista
            tambem alterara a lista antiga;
"""
nova_lista_02 = copy.copy(lista_simples_inteiro)
lista_simples_inteiro.append(1200)
nova_lista_02.append(3000)

print("=============================")
print("========| DEEP COPY |========")
print(lista_simples_inteiro)
print(f"LISTA ANTIGA: {lista_simples_inteiro}")
print(f"LISTA NOVA: {nova_lista_02}")