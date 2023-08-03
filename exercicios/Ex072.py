# informar se um número esta entre 0 a 20.

cont = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
numero = int(input("Digite um número entre 0 e 20: "))
while True:
        if 0 <= numero <= 20:
            print(f"O número {numero} está entre 0 e 20!")
            break
        else:
            erro = int(input("Tente novamente. Digite um número entre o e 20: "))