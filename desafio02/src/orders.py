from .data import products, sales

def orderRegister():
    if not products:
        print("\nErro: Nenhum produto cadastrado. Cadastre um produto primeiro.")
        return

    print("\n--- Fazer um Pedido ---")
    print("Produtos disponíveis:")
    for product in products:
        print(f"{product['id']} - {product['name']} (R$ {product['price']:.2f})")

    try:
        product_id = int(input("Digite o ID do produto: "))
        selected_product = next((p for p in products if p['id'] == product_id), None)

        if not selected_product:
            print("Erro: Produto não encontrado.")
            return

        quantity = int(input(f"Quantidade de '{selected_product['name']}': "))
        if quantity <= 0:
            print("Erro: A quantidade deve ser maior que zero.")
            return

        total_price = selected_product['price'] * quantity
        discount = 0
        if quantity > 10:
            discount = total_price * 0.05
            total_price -= discount
            print(f"Desconto de 5% aplicado! Valor economizado: R$ {discount:.2f}")

        sale = {
            "product_name": selected_product['name'],
            "quantity": quantity,
            "total_price": total_price,
            "discount": discount
        }
        sales.append(sale)
        print(f"Pedido realizado! Total: R$ {total_price:.2f}")

    except ValueError:
        print("Erro: Entrada inválida. Digite números para ID e quantidade.")
