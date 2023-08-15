# Calcular o preço final do pedido do usuário.
# Calcular o troco, se houver.

valorHamburguer = float(input("Qual valor do hambúrguer? "))
quantidadeHamburguer = int(input("Quantos hambúrgueres deseja? "))
valorBebida = float(input("Qual valor da bebida? "))
quantidadeBebida = int(input("Quantas bebidas deseja? "))
valorPago = float(input("Qual o valor que pagou? "))

totalHamburguer = valorHamburguer * quantidadeHamburguer
totalBebida = valorBebida * quantidadeBebida
totalPago = totalHamburguer + totalBebida
troco = valorPago - totalPago
trocoInsuficiente = totalPago - valorPago
print(f"O preço final do pedido é de R$ {totalPago:.2f}.")

if troco > 0:
    print(f"O seu troco é de R$ {troco:,.2f}.")
elif troco < 0:
    print(f"O valor pago não foi suficiente.É necessário pagar R$ {trocoInsuficiente:,.2f}.")
else:
    pass
