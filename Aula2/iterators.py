# ITERATORS 

lista_simples_inteiro = [1, 2, 5, 12, 56, 98]

## trabalhando com a função iter():

meu_iter = iter(lista_simples_inteiro) # Definindo o iterator

for i in meu_iter:
  print(i)
  """
  O for é baseado em um while infinito, que utiliza de uma 
  condição para parar a iteração como o proximo evento;  
  """
  

## Exemplo de como funciona o iterator:
while true:
  try:
    elemento = next(meu_iter)
    print(elemento)
  except StopIteration:
    break

"""
Todos os iterators quando terminarem o vetor manda a seguinte exception
StopIteration, que permite o for ou o while acionar a condição de parada;
"""
