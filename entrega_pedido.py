# entrega de pedido

valor_total = float(input("Digite o valor total do pedido: "))
area_entrega = input("Digite a área de entrega: ")


if valor_total >= 50.00 and area_entrega == "Centro":
    print("Seu pedido será entregue!")
else:
    print("Desculpe, seu pedido não cumpre os requisitos de entrega")


