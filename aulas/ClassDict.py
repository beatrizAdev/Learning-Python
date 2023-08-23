# apaga todos os valores do dicionario.
contatos = {
    "biaarantes@yahoo.com.br": {"nome": "Ana Beatriz", "telefone": "(21)97004-7801"},
    "karen_rejane@yahoo.com.br": {"nome": "Karen", "telefone": "(21)99317-9311"},
    "arthurnina.dev@gmail.com": {"nome": "Arthur", "telefone": "(21)96681-6052"},
}
print(contatos.clear())

# tira uma copia do dicionario copy()


# ele te da o valor que ta pedindo mas sem dar ero no programa, utiliza tbm quando nao se sabe se existe ou nao no dic
print(contatos.get("beaidu@gmail.com", {}))

# keys mostra todas as chaves presentes no seu dicionario
contatos1 = {
    "biaarantes@yahoo.com.br": {"nome": "Ana Beatriz", "telefone": "(21)97004-7801"},
    "karen_rejane@yahoo.com.br": {"nome": "Karen", "telefone": "(21)99317-9311"},
    "arthurnina.dev@gmail.com": {"nome": "Arthur", "telefone": "(21)96681-6052"},
}
print(contatos1.keys())

