# De acordo com valor total do pedido, informe ao usuário se ele pode receber um brinde especial
# Se o valor total do pedido for maior ou igual a R$ 50.00, o usuário receberá uma sobremesa grátis.
# Caso contrário, o usuário não receberá nenhum brinde

valorPedido = float(input("Qual foi o valor final do seu pedido? "))
if valorPedido >= 50.0:
    print("Parabéns, você ganhou uma sobremesa grátis!")
else:
    print("Que pena, você nao ganhou nenhum brinde especial.")
