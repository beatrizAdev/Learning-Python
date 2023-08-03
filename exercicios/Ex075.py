# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# Mostre quantas vezes apareceu o valor 9.
# Mostre em que posição foi digitado o primeiro valor 3.
# E mostre quais foram os números pares.


num = (int(input("Digite um número: ")), int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")), int(input("Digite o último número: ")))

print(f"Você digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 not in num:
    print("O valor 3 não aparece nenhuma vez")
else:
    print(f"O valor 3 apareceu na {num.index(3)+1} posição")
for n in num:
    if n % 2 == 0:
        print(f"Os valores pares digitados foram {n}")
