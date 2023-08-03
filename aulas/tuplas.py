# Variáveis Compostas
# Armazena vários itens em uma única variável
# Não tem ordem alterada, não pode alterar/adicionar/remover
# Podem ter itens com o mesmo valor

lanches = ("hambúrguer", "1", "pizza", "cerveja", "batata", "cerveja")
print(lanches)
print(lanches[2])
print(lanches[0:3])

# Informa quantos itens tem em cada tupla
lanches = ("hambúrguer", "1", "pizza", "cerveja", "batata", "cerveja")
print(len(lanches))

# Repetir o valor de uma variável a quantidade de vezes que tiver itens na tupla
comida = ("arroz", "macarrão", "feijão", "frango")
for c in comida:
    print(f"Eu como {c} isso todo dia")

# Se quiser adicionar um item apenas numa tupla só adicionar uma vírgula após o item

# Se quiser alterar um valor de uma tupla, tera q transformar em lista depois tupla

comida = ("arroz", "macarrão", "suco", "frango")
suco = list(comida)
suco[2] = "feijão"
comida = tuple(suco)
print(comida)

roupa = ("blusa", "calça", "boné", "sapato")
sapato = list(roupa)
sapato[3] = "casaco"
roupa = tuple(sapato)
print(roupa)

# Para adicionar um item numa tupla

frutas = ("banana", "morango", "melão")
fruta = ("manga",)
frutas += fruta
print(frutas)

# Para deletar um item numa tupa
frutas = ("banana", "morango", "melão", "maça")
fruta = list(frutas)
fruta.remove("maça")
frutas = tuple(fruta)
print(frutas)

# Para deletar uma tupla inteira, o que ocasionará em um erro no código

frutas = ("banana", "morango", "melão")
del frutas
print(frutas)

