from src.data import products
from src.data import sales

def productRegister():
    print("\n==== Cadastro de Produto ====")

    name = input("Digite o nome do produto: ")
    price = float(input("Digite o preço do produto: "))
    quantity = int(input("Digite a quantidade do produto: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    products.append(product)
    print("\nCadastro realizado com sucesso!")

    print("====== Resumo do Cadastro ======")
    print(f"Nome: {name}")
    print(f"Preço: R${price:.2f}")
    print(f"Quantidade: {quantity}")
    

