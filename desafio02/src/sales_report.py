from .data import sales

def salesReport():
    if not sales:
        print("\nNenhuma venda realizada até o momento.")
        return

    print("\n" + "="*50)
    print(f"{'RELATÓRIO DE VENDAS':^50}")
    print("="*50)
    
    total_revenue = 0
    total_discounts = 0
    
    for i, sale in enumerate(sales, 1):
        print(f"Venda #{i}")
        print(f"  Cliente: {sale['customer_name']} (CPF: {sale['customer_cpf']})")
        print(f"  Produto: {sale['product_name']} | Qtd: {sale['quantity']} | Unit: R${sale['unit_price']:.2f}")
        
        if sale['discount'] > 0:
            print(f"  Subtotal: R${(sale['unit_price'] * sale['quantity']):.2f}")
            print(f"  Desconto (5%): -R${sale['discount']:.2f}")
            
        print(f"  Total Pago: R${sale['total_price']:.2f}")
        print("-" * 30)
        
        total_revenue += sale['total_price']
        total_discounts += sale['discount']
    
    print("="*50)
    print(f"RESUMO FINANCEIRO")
    if total_discounts > 0:
        print(f"  Total de Descontos Concedidos: R${total_discounts:.2f}")
    print(f"  Receita Total Líquida: R${total_revenue:.2f}")
    print("="*50)
