# Questão 2 - Sistema de Pedidos de Pizzaria
# Mensagem de Boas-vindas com nome do criador.
print("---------- Bem-vindo a Pizzaria do Jonatha Figueiredo ----------")
print("--------------------------- Cardápio ---------------------------")
print("----------------------------------------------------------------")
print("---|  Tamanho  |   Pizza Salgada(PS)   |   Pizza Doce(PD)   |---")
print("---|     P     |       R$ 30.00        |      R$ 34.00      |---")
print("---|     M     |       R$ 45.00        |      R$ 48.00      |---")
print("---|     G     |       R$ 60.00        |      R$ 66.00      |---")
print("----------------------------------------------------------------")

# O valor total cobrado
valorCobrado = 0

# While para fazer o sistema de loop da "Pizzaria".
while True:
    # Comprador digitar o sabor da pizza, caso erre, necessário escrever novamente.
    sabor = input("Entre com o sabor desejado (PS/PD): ")
    # Altera o "valor" de ambas para ser mostrado no valor final.
    if sabor == "PS":
        sabor = "Pizza Salgada"
    elif sabor == "PD":
        sabor = "Pizza Doce"
    # Pergunta o sabor novamente.
    else:
        print("Sabor inválido. Tente novamente.")
        print("")
        continue

    # Comprador digitar o tamanho da pizza, caso erre, necessário escrever novamente.
    tamanho = input("Entre com o tamanho do desejado (P/M/G): ")
    # Pergunta o sabor novamente.
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.")
        print("")
        continue

    # Preços da pizza salgada de acordo com tamanho.
    if sabor == "Pizza Salgada":
        if tamanho == "P":
            valor = 30
        elif tamanho == "M":
            valor = 45
        else:
            valor = 60

    # Preços da pizza doce de acordo com tamanho.
    elif sabor == "Pizza Doce":
        if tamanho == "P":
            valor = 34
        elif tamanho == "M":
            valor = 48
        else:
            valor = 66

    # Valor da Pizza que foi pedida de acordo com tipo e tamanho.
    valorCobrado += valor
    print(f"Você pediu uma {sabor} no tamanho {tamanho}: R$ {valor}")
    print("")

    # Loop para não fechar sem o pedido ter sido completado pelo comprador corretamente.
    while True:
        maisPizza = input("Deseja mais alguma coisa? (S/N): ")
        print("")
        # Volta para o loop de pedir Pizza.
        if maisPizza == "S":
            break
        # Da o valor total e fecha o programa.
        elif maisPizza == "N":
            print(f"O valor total a ser pago: R$ {valorCobrado}")
            exit()
        # Volta para a pergunta se deseja mais alguma coisa.
        else:
            print("Opção inválida. Por favor, responda com S ou N.")
            print("")
