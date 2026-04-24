from .data import products

def productRegister():
    print("\n==== Cadastro de Produto ====")

    try:
        name = input("Digite o nome do produto: ")
        if not name:
            print("Erro: O nome do produto não pode ser vazio.")
            return
            
        price = float(input("Digite o preço do produto: "))
        if price <= 0:
            print("Erro: O preço deve ser maior que zero.")
            return
            
        quantity = int(input("Digite a quantidade inicial em estoque: "))
        if quantity < 0:
            print("Erro: A quantidade não pode ser negativa.")
            return

        product = {
            "id": len(products) + 1,
            "name": name,
            "price": price,
            "quantity": quantity
        }
        products.append(product)
        
        print("\nCadastro realizado com sucesso!")
        print("====== Resumo do Cadastro ======")
        print(f"ID: {product['id']}")
        print(f"Nome: {name}")
        print(f"Preço: R${price:.2f}")
        print(f"Estoque: {quantity}")
        
    except ValueError:
        print("Erro: Entrada inválida. Preço e quantidade devem ser números.")
