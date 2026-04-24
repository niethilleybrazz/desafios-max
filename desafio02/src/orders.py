from .data import products, sales

def orderRegister():
    if not products:
        print("\nErro: Nenhum produto cadastrado. Cadastre um produto primeiro.")
        return

    print("\n==== Realizar Venda ====")

    customer_name = input("Digite o nome do cliente: ")
    customer_cpf = input("Digite o CPF do cliente: ")

    if not customer_name or not customer_cpf:
        print("Erro: Por favor, informe o nome e o CPF do cliente.")
        return
    
    print("\n====== Produtos disponíveis ======")
    for product in products:
        print(f"ID: {product['id']} | Nome: {product['name']} | Preço: R${product['price']:.2f} | Estoque: {product['quantity']}")

    try:
        product_id = int(input("\nDigite o ID do produto: "))
        selected_product = next((p for p in products if p['id'] == product_id), None)

        if not selected_product:
            print("Erro: Produto não encontrado!")
            return

        if selected_product['quantity'] <= 0:
            print(f"Erro: Produto '{selected_product['name']}' esgotado!")
            return

        quantity = int(input(f"Digite a quantidade desejada de '{selected_product['name']}': "))
        
        if quantity <= 0:
            print("Erro: A quantidade deve ser maior que zero.")
            return
            
        if quantity > selected_product['quantity']:
            print(f"Erro: Quantidade insuficiente em estoque! (Disponível: {selected_product['quantity']})")
            return
        
        # Cálculo do total e desconto
        unit_price = selected_product['price']
        total_price = unit_price * quantity
        discount = 0
        
        if quantity > 10:
            discount = total_price * 0.05
            total_price -= discount
            print(f"\n>>> Desconto de 5% aplicado por levar mais de 10 itens! Economia: R$ {discount:.2f}")

        # Atualiza estoque
        selected_product['quantity'] -= quantity

        # Registra a venda
        order = {
            "customer_name": customer_name,
            "customer_cpf": customer_cpf,
            "product_name": selected_product['name'],
            "unit_price": unit_price,
            "quantity": quantity,
            "total_price": total_price,
            "discount": discount
        }
        sales.append(order)
        
        print("\n===== Venda Realizada com Sucesso! =====")
        print(f"Cliente: {customer_name} (CPF: {customer_cpf})")
        print(f"Produto: {selected_product['name']}")
        print(f"Quantidade: {quantity}")
        print(f"Total a pagar: R${total_price:.2f}")

    except ValueError:
        print("Erro: Entrada inválida. Digite números para ID e quantidade.")
