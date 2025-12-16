# Questão 1 - Cálculo de Plano de Saúde por Faixa Etária
# Mensagem de Boas-vindas com nome do criador.
nome = "Jonatha"
sobrenome = "Figueiredo"
print(f'Bem vindo ao Sistema do {nome} {sobrenome}')

# Informar o valor base do plano que será multiplicado de acordo com a “porcentagem” da idade.
valorBase = int(input("Informe o valor Base do plano: R$ "))
idade = int(input('Informe a idade do cliente: '))

# 100% do valor base
if idade >= 0 and idade < 19:
    valorMensal = valorBase * (100/100)
    print(f"O valor mensal do plano é de: R$ {valorMensal}")
# 150% do valor base
elif idade >= 19 and idade < 29:
    valorMensal = valorBase * (150/100)
    print(f"O valor mensal do plano é de: R$ {valorMensal}")
# 225% do valor base
elif idade >= 29 and idade < 39:
    valorMensal = valorBase * (225/100)
    print(f"O valor mensal do plano é de: R$ {valorMensal}")
# 240% do valor base
elif idade >= 39 and idade < 49:
    valorMensal = valorBase * (240/100)
    print(f"O valor mensal do plano é de: R$ {valorMensal}")
# 350% do valor base
elif idade >= 49 and idade < 59:
    valorMensal = valorBase * (350/100)
    print(f"O valor mensal do plano é de: R$ {valorMensal}")
# 600% do valor base
elif idade >= 59:
    valorMensal = valorBase * (600/100)
    print(f"O valor mensal do plano é de: R$ {valorMensal}")
else:
    print("Algo deu errado. Tente novamente.")
