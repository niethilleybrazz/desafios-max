from .data import sales

def salesReport():
    if not sales:
        print("\nNenhuma venda realizada até o momento.")
        return

    print("\n--- Relatório de Vendas ---")
    total_revenue = 0
    total_discounts = 0
    for sale in sales:
        discount_info = f" (Desc: R$ {sale['discount']:.2f})" if sale.get('discount', 0) > 0 else ""
        print(f"Produto: {sale['product_name']} | Qtd: {sale['quantity']} | Total: R$ {sale['total_price']:.2f}{discount_info}")
        total_revenue += sale['total_price']
        total_discounts += sale.get('discount', 0)
    
    print("-" * 30)
    if total_discounts > 0:
        print(f"Total de Descontos Concedidos: R$ {total_discounts:.2f}")
    print(f"Receita Total Líquida: R$ {total_revenue:.2f}")
