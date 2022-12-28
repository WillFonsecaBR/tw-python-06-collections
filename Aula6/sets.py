# UTILIZANDO SETS

# Declarando os sets
set_01 = {1, 23, 3, 50}
set_02 = set([1, 2, 3, 4, 20, 18, 25, 5, 9])

# Adicionando SETS com o metodo add()
print("========| ADD() |========")
set_01.add(20)
set_02.add(20)
print(f"SET_1 = {set_01}")
print(f"SET_2 = {set_02}")
print("")


# Atualizando SETS com o metodo update()
print("========| UPDATE() |========")
set_01.update([10, 2, 4, 6, 12])
set_02.update([5, 2, 8, 3, 18])
print(f"SET_1 = {set_01}")
print(f"SET_2 = {set_02}")
print("")


# Discartando SETS com o metodo discard()
print("========| DISCARD() |========")
set_01.discard(5)
set_02.discard(1)
print(f"SET_1 = {set_01}")
print(f"SET_2 = {set_02}")
print("")


# Unindo SETS com metodo union()
print("========| UNION() |========")
print(f"UNIÃO 1: {set_01 | set_02}")
print(f"UNIÃO 2: {set_01.union(set_02)}")
print(f"SET_1 = {set_01}")
print(f"SET_2 = {set_02}")
print("")


# Interceção de SETS com metodo intersection()
print("========| INTERSECTION() |========")
print(f"INTERSECTION 1: {set_01 & set_02}")
print(f"INTERSECTION 2: {set_01.intersection(set_02)}")
print(f"SET_1 = {set_01}")
print(f"SET_2 = {set_02}")
print("")


# Diferença entre SETS com metodo differrence()
print("========| DIFFERENCE() |========")
print(f"DIFFERENCE 1: {set_01 - set_02}")
print(f"DIFFERENCE 2: {set_01.difference(set_02)}")
print(f"SET_1 = {set_01}")
print(f"SET_2 = {set_02}")
print("")


# Diferença simétrica entre SETS com metodo differrence()
print("========| SIMMETRIC.DIFFERENCE() |========")
print(f"DIFFERENCE 1: {set_01 ^ set_02}")
print(f"DIFFERENCE 2: {set_01.symmetric_difference(set_02)}")
print(f"SET_1 = {set_01}")
print(f"SET_2 = {set_02}")
print("")
