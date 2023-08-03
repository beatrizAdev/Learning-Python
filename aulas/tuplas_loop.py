# Para criar um loop em uma tupla, usamos o for
roupas = ("casaco", "calça", "meia", "blusa")
for x in roupas:
    print(x)


separar = '''==================================='''
print(separar)

# Percorrer os itens do número de índice
roupas = ("casaco", "calça", "meia", "blusa", "vestido", "short")
for x in range(0, len(roupas)):
    print(roupas[x])

# Passar por todos os números de índices, repetindo tod o conjunto da tupla
roupas = ("casaco", "calça", "meia", "blusa", "vestido", "short")
i = 0
while i < len(roupas):
    print(roupas)
    i += 1

# no método count(), é para saber quantas vezes um item se repete numa tupla
lanches = ("hambúrguer", "pastel", "pizza", "cerveja", "batata", "cerveja")
suco = lanches.count("cerveja")
print(suco)

# no método index(), é para saber a primeira posição do número que se repete
lanches = ("hambúrguer", "pastel", "pizza", "cerveja", "batata", "cerveja")
suco = lanches.index("cerveja")
print(suco)

# Para por na ordem alfabética
frutas = ("banana", "uva", "morango", "abacaxi", "limão")
print(sorted(frutas))