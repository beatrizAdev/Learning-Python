# necessário que seja um dentro das chaves algo imutavel e o valor pode ou nao ser mutavel

pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

# ouuu

pessoa1 = dict(nome="Beatriz", idade=19)

# quando ja tiver um dicionario criado e quiser adicionar mais uma informaçao nele

pessoa1["telefone"] = "21970047801"

print(pessoa1)

# para acessar um valor dentro de um dicionario:
print(pessoa1["nome"])
print(pessoa1["idade"])

# lista de todas as chaves do dicionario
x = pessoa1.keys()
print(x)

# lista de todos os valores do dicionario
y = pessoa1.values()
print(y)

# lista dos pares de chaves e o valor de cada
z = pessoa1.items()
print(z)

# dicionarios aninhados
contatos = {
    "biaarantes@yahoo.com.br": {"nome": "Ana Beatriz", "telefone": "(21)97004-7801"},
    "karen_rejane@yahoo.com.br": {"nome": "Karen", "telefone": "(21)99317-9311"},
    "arthurnina.dev@gmail.com": {"nome": "Arthur", "telefone": "(21)96681-6052"},
    }
print(contatos["biaarantes@yahoo.com.br"]["nome"])

for chave, valor in contatos.items():
    print(chave, valor)