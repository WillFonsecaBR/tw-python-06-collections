## TRABALHANDO COM FILAS

from collections import deque

# Vetor
fila_01 = [1, 2, 3, 4, 5, 6, 7, 8]
fila_02 = deque(1,2,3,4,5,6,7,8) # Utilizando o metodo DEQUE()

# Adicionando elemento na fila
fila_02.append(9)
fila_02.append(10)
print(fila_02)

# Removendo elemento dentro de uma fila
fila_02.popleft()
print(fila_02)




