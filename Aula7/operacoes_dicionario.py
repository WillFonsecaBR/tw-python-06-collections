# OPERAÇÕES EM DICIONARIOS

dicionario_01 = {1: "João", 2: "José", 3: "Valdomiro Santiago",
                 4: "Edir Macedo", 5: "Silas Malafaia"}
dicionario_02 = dict({"nome": "João", "sobrenome": "Silva", "idade": 29})

# Metodo adicionando elementos
print("=====| ADICIONANDO ELEMENTOS |=====")
dicionario_01[6] = "Josefina"
print(dicionario_01)
dicionario_02.update({"Profissão":"programador"})
print(dicionario_02)
print("")

# Metodo GET() = Seleciona
print("=====| METODO GET() |=====")
print(dicionario_01[2])
print(dicionario_01.get(3))
print("")

# Metodo LENGTH() = Tamanho do vetor
print("=====| METODO LENGTH() |=====")
print(len(dicionario_02))
print("")

# Metodo POP() = Remover
print("=====| METODO POP() |=====")
dicionario_02.pop("idade")
print(dicionario_02)
print("")

# Metodo CLEAR() = Remover todos os elementos
print("=====| METODO CLEAR() |=====")
dicionario_01.clear()
print(dicionario_01)
print("")

# Metodo KEYS() = Remover todos os elementos
print("=====| METODO KEYS() |=====")
print(dicionario_01.keys())
print("")


