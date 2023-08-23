# adicionar a chave com o valor escolhido
contatos_loja = {
    "biaarantes@yahoo.com.br": {"nome": "Ana Beatriz", "telefone": "(21)97004-7801"}
}

contatos_loja.setdefault("idade", 19)
print(contatos_loja)

# atualiza o dicionario com mais um dicionario

contatos = {
    "beatrizarantes.dev@gmail.com": {"nome": "Ana Beatriz", "telefone": "970047801"}
}

contatos.update({"beatrizarantes.dev@gmail.com": {"nome": "Bia"}})
print(contatos)

contatos.update({"karen_rejane@yahoo.com.br": {"nome": "Karen", "telefone": "(21)99317-9311"}})
print(contatos)

lista = {
"biaarantes@yahoo.com.br": {"nome": "Ana Beatriz", "telefone": "(21)97004-7801"},
    "karen_rejane@yahoo.com.br": {"nome": "Karen", "telefone": "(21)99317-9311"},
    "arthurnina.dev@gmail.com": {"nome": "Arthur", "telefone": "(21)96681-6052"},
}
resultado = "idade" in lista["karen_rejane@yahoo.com.br"]
print(resultado)
