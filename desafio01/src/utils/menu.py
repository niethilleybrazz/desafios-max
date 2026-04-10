from utils.cadastro_funcionario import cadastro_funcionario
from utils.gerar_relatorio import gerar_relatorio

def gerar_menu(lista_dados):
    while True:
        print("\n===== Bem vindo(a) =====")
        print("1 - Cadastrar Funcionario")
        print("2 - Gerar Relatorio")
        print("3 - Salvar relatorio")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha a opcao desejada: "))
        except ValueError:
            print("Por favor, digite um numero valido!")
            continue

        match opcao:
            case 1:
                cadastro_funcionario(lista_dados)
            case 2:
                gerar_relatorio(lista_dados)
            case 3:
                print("Salvando relatorio...")
            case 0:
                print("Saindo...")
                break
            case _:
                print("Opcao Invalida! Tente Novamente")