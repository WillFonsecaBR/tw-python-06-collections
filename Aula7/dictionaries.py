# TRABALHANDO COM DICTIONARIES

# Declarandi um dicionario
dicionario_01 = {1: "João", 2: "José"}
dicionario_02 = dict({"nome": "João", "sobrenome": "Silva"})

# Acessando dicionarios:
print(dicionario_01[2])

for chave, valor in dicionario_02.items():
    print(f"CHAVE= {chave} VALOR = {valor}")
