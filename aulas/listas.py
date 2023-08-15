# quantidade de itens em uma lista
comida = ['arroz', 'feijão', 'frango', 'batata']
print(len(comida))

# acessar um item em uma lista é necessário informar sua posição
nomes = ['karen', 'caio', 'bia', 'arthur']
print(f"Minha mãe se chama {nomes[0]}")

lanches = ['pizza', 'hambúrguer', 'batata-frita', 'açaí']
print(f"Eu amo {lanches[3]}")

# alterar um item em uma lista
lanches = ['pizza', 'hambúrguer', 'batata', 'casaco']
lanches[3] = 'açaí'
print(lanches)

# insere um item na lista sem comprometer os outros itens
frutas = ['banana', 'morango', 'mamao', 'melao']
frutas.insert(4, 'melancia')
print(frutas)

# adicionar um item no final da lista, utiliza-se o append()
# remover um item específico em uma lista, utiliza-se o remove()
# remover um índice específico em uma lista, utiliza-se o del ou pop()

# ordem crescente alfanumérica
nomes = ['karen', 'caio', 'bia', 'arthur']
nomes.sort()
print(nomes)

# ordem decrescente alfanumérica
numeros = [100, 8000, 7, 41, 1]
numeros.sort(reverse=True)
print(numeros)

# inverte a ordem sem depender de ser alfanumérica
numeros = [100, 8000, 7, 41, 1]
numeros.reverse()
print(numeros)

print('======================================================================================================')

carros = ['gol', 'celta', 'palio', 'civik']
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
