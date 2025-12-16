# Questão 3 - Sistema de Vendas de Madeireira
# Mensagem de Boas-vindas com nome do criador.
print("Bem vindo a Madeireira do Lenhador Jonatha Figueiredo")
print("")

# Função do tipo de madeira que o cliente deseja.
def escolha_tipo():
    while True:
        print("Entre com o Tipo de Madeira desejado")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")
        # Coloca o tipo de madeira.
        tipoMadeira = input(">> ")

        # Valor conforme o tipo de madeira.
        if tipoMadeira == "PIN":
            return 150.40
        elif tipoMadeira == "PER":
            return 160.20
        elif tipoMadeira == "MOG":
            return 190.90
        elif tipoMadeira == "IPE":
            return 210.10
        elif tipoMadeira == "IMB":
            return 220.70
        # Volta com a tela inicial
        else:
            print('Escolha inválida, entre com o modelo novamente.')
            continue

# Função de descontos por quantidade de toras.
def qtd_Toras():
    while True:
        try:
            # Quantidade do pedido.
            quantia = int(input("Entre com a quantidade de toras (m³): "))
            # Desconto conforme a quantidade pedida.
            if 100 > quantia > 0:
                desconto = 0 / 100
            elif 100 <= quantia < 500:
                desconto = 4 / 100
            elif 500 <= quantia < 1000:
                desconto = 9 / 100
            elif 1000 <= quantia <= 2000:
                desconto = 16 / 100
            # Caso a quantia for maior que 2000, volta a pergunta de toras.
            elif quantia > 2000:
                print(f'Não aceitamos pedidos com {quantia}m³ de toras.')
                print('Por favor, entre com a quantidade novamente.')
                print("")
                continue
            return quantia, desconto
        except:
            print("Digite um número válido de quantidade.")
            print("")
            continue

# Função do tipo de transporte.
def transporte():
    while True:
        # Tipo de transporte do pedido.
        print("")
        print("Entre com o tipo de Transporte:")
        print("1 - Transporte Rodoviário - R$ 1000.00")
        print("2 - Transporte Ferroviário - R$ 2000.00")
        print("3 - Transporte Hidroviário - R$ 2500.00")
        tipotransporte = input(">> ")
        # Preço por cada opção de transporte.
        if tipotransporte == "1":
            return 1000.00
        elif tipotransporte == "2":
            return 2000.00
        elif tipotransporte == "3":
            return 2500.00
        else:
            print("Digite um número válido de acordo com as opções.")
            continue

# Chama as funções na sequência correta.
tipoMadeira = escolha_tipo()
quantia, desconto = qtd_Toras()
tipotransporte = transporte()

# Valor total do pedido calculado por tipo de madeira vezes a quantidade de tora vezes o desconto mais o tipo de transporte.
valorTotal = ((tipoMadeira * quantia) * (1 - desconto)) + tipotransporte
print(f"Total: R$ {valorTotal}")
