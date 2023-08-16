# Um conjunto é uma coleção desordenada de elementos, sem elementos repetidos usamos {} ou função set

usuarios_conta_corrente = {198, 14, 38907, 673}
usuarios_conta_universitaria = {199, 14, 38906, 673}

acessaram = usuarios_conta_corrente.copy()
acessaram.update(usuarios_conta_universitaria)
print(acessaram)
print(len(acessaram))
print(set(acessaram))
print(type(acessaram))

for usuario in set(acessaram):
    print(usuario)

usu = usuarios_conta_corrente | usuarios_conta_universitaria
print(usu)

usu_1 = usuarios_conta_corrente & usuarios_conta_universitaria
print(usu_1)

usu_2 = usuarios_conta_corrente - usuarios_conta_universitaria
print(usu_2)

usu_3 = usuarios_conta_corrente ^ usuarios_conta_universitaria
print(usu_3)

#.union une os dois conjuntos

#.intersection os itens que se repetem nos dois conjuntos

#.difference itens que nao se repetem nos dois conjuntos

#