# Questão 4 - Sistema de Gerenciamento de Contatos
# Mensagem de Boas-vindas com nome do criador.
print("Bem vindo a Lista de Contatos do Jonatha Figueiredo")

# Lista de contatos.
lista_contatos = []
# Id para começar a contagem iniciando no meu RU.
id_global = 5476526
# Importa o módulo copy para copiar os cadastros.
import copy

# Função cadastrar contato.
def cadastrar_contato(id):
    print("---------------------------------------------------")
    print("------------- MENU CADASTRAR CONTATO --------------")

    id = print(f"Id do Contato: {id_global}")
    nome = input("Por favor entre com o nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do contato: ")
    telefone = input("Por favor entre com o telefone do contato: ")
    # Biblioteca do contato com id, nome, atividade e telefone.
    contato = {
        "id": id_global,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }
    # Copia o cadastro para a lista de contatos e diz o nome do contato que foi cadastrado.
    lista_contatos.append(copy.deepcopy(contato))
    print(f"Contato {contato['nome']} cadastrado com sucesso!")

# Função para consulta de contatos.
def consultar_contatos():
    while True:
        print("---------------------------------------------------")
        print("------------- MENU CONSULTAR CONTATO --------------")
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Contato")
        print("2 - Consultar Contato por id")
        print("3 - Consultar Contato(s) por Atividade")
        print("4 - Retornar")
        consulta = input(">> ")

        # Seleciona consultar todos os contatos existentes e mostra eles corretamente em ordem.
        if consulta == "1":
            print("---------------------------------------------------")
            # Se não estiver na listagem de contatos, terá essa mensagem de erro.
            if not lista_contatos:
                print("Ainda não tem nenhum contato cadastrado.")
            # Mostra TODOS os contatos em ordem de Id.
            else:
                for contato in lista_contatos:
                    print(f"Id: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}")
                    print("")

        # Seleciona consultar contato por id.
        elif consulta == "2":
            try:
                buscaid = int(input("Informe o ID do contato: "))
                print("---------------------------------------------------")
                # Variável encontrado para que ache ou não ache o id.
                encontradoid = False
                # Mostra o contato de acordo com o exato valor digitado no input acima.
                for contato in lista_contatos:
                    if contato['id'] == buscaid:
                        print(f"Id: {contato['id']}")
                        print(f"Nome: {contato['nome']}")
                        print(f"Atividade: {contato['atividade']}")
                        print(f"Telefone: {contato['telefone']}")
                        print("")
                        encontradoid = True
                        break
                # Se não for encontrado, terá essa mensagem de erro.
                if not encontradoid:
                    print("Contato não encontrado. Tente novamente.")
            # Se digitar qualquer coisa que não seja um número inteiro, dará mensagem de erro.
            except ValueError:
                print("Id inválido. Digite um número corretamente.")

        # Seleciona consultar contato(s) por atividade e mostra eles(se tiver mais de um com essa atividade) em ordem.
        elif consulta == "3":
            buscaatividade = input("Informe a atividade: ")
            print("---------------------------------------------------")
            # Mostra o(s) contato(s) de acordo com a exata atividade digitada no input acima.
            encontrados = [c for c in lista_contatos if c["atividade"].lower() == buscaatividade.lower()]
            if encontrados:
                for contato in encontrados:
                    print(f"Id: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}")
                    print("")
            # Caso nenhum contato for encontrado, ele volta a função consultar_contatos().
            if not lista_contatos:
                print("Nenhum contato foi encontrado com essa atividade.")
                print('')
        # Retorna a função principal cadastrar_contatos()
        elif consulta == "4":
            break
        # Erro caso digite uma opção que não seja 1, 2, 3 ou 4.
        else:
            print("Insira uma das opções listadas acima corretamente.")
            print("")
            continue

# Função com menu de remover contato
def remover_contato():
    while True:
        try:
            print("---------------------------------------------------")
            print("-------------- MENU REMOVER CONTATO ---------------")
            id_remover = int(input("Digite o Id do contato a ser removido: "))
            # Para contato na lista de contatos.
            for contato in lista_contatos:
                # Se o id para remover for correto, ele remove o contato e fala qual nome e contato foi removido.
                if contato['id'] == id_remover:
                    lista_contatos.remove(contato)
                    print(f"Contato com o nome {contato['nome']} e id {contato['id']} removido com sucesso!")
                    return
            # Caso o id não existir ou faltar número, dará esse erro.
            print("Id inválido. Nenhum contato com esse Id. Tente novamente.")
        # Caso não for um número inteiro, dará esse erro.
        except ValueError:
            print("Id inválido. Digite um número corretamente.")

# Menu principal com as opções principais.
while True:
    print("---------------------------------------------------")
    print("----------------- MENU PRINCIPAL ------------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Contato")
    print("2 - Consultar Contato(s)")
    print("3 - Remover Contato")
    print("4 - Sair")
    opcaoMenu = input(">> ")
    # Se escolher cadastrar, irá aumentar em +1 o número global do id e entrará na função cadastrar_contato(id_global).
    if opcaoMenu == "1":
        cadastrar_contato(id_global)
        id_global += 1
    # Se escolher consultar, irá entrar na função consultar_contatos()
    elif opcaoMenu == "2":
        consultar_contatos()
    # Se escolher remover, irá entrar na função remover_contato()
    elif opcaoMenu == "3":
        remover_contato()
    # Se escolher sair, encerrará o programa.
    elif opcaoMenu == "4":
        print("Encerrando o programa...")
        break
    # Se escolher uma opção errada, dará esse erro.
    else:
        print("Insira uma das opções listadas acima corretamente.")
        print("")
        continue
