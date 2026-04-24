from .data import products

def productRegister():
    print("\n--- Cadastro de Produto ---")
    name = input("Nome do produto: ")
    try:
        price = float(input("Preço do produto: "))
        product = {
            "id": len(products) + 1,
            "name": name,
            "price": price
        }
        products.append(product)
        print(f"Produto '{name}' cadastrado com sucesso!")
    except ValueError:
        print("Erro: Preço inválido. O produto não foi cadastrado.")
