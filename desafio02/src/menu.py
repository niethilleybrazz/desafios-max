from .product_register import productRegister
from .orders import orderRegister
from .sales_report import salesReport

def show_menu():
    switch = 0
    while switch != 4:
        print("\n==== Bem vindos ao sistema de cadastro ====")
        print("1 - Cadastrar produto")
        print("2 - Realizar venda")
        print("3 - Relatorio de vendas")
        print("4 - Sair")
        try:
            switch = int(input("Digite a opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if switch == 1:
            productRegister()
        elif switch == 2:
            orderRegister()
        elif switch == 3:
            salesReport()
        elif switch == 4:
            print("Saindo...")
        else:
            print("Opção inválida")
