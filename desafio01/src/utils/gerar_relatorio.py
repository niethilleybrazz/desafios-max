def gerar_relatorio(lista_dados):
    print("\n" + "="*95)
    print(f"{'RELATÓRIO DE FUNCIONÁRIOS':^95}")
    print("="*95)
    
    if not lista_dados:
        print(f"{'Nenhum funcionário cadastrado até o momento.':^95}")
    else:
        # Cabeçalho da tabela
        print(f"{'Nome':<20} | {'Tipo':<12} | {'Bruto':<12} | {'INSS':<10} | {'IRRF':<10} | {'Líquido':<12}")
        print("-" * 95)
        
        total_pago = 0.0
        for f in lista_dados:
            nome = f.get('nome', 'N/A')
            tipo = f.get('tipo', 'N/A')
            bruto = f.get('salario_bruto', 0.0)
            inss = f.get('desconto_inss', 0.0)
            irrf = f.get('desconto_irrf', 0.0)
            liquido = f.get('salario_liquido', 0.0)
            
            total_pago += liquido
            
            print(f"{nome:<20} | {tipo:<12} | R$ {bruto:>8.2f} | R$ {inss:>7.2f} | R$ {irrf:>7.2f} | R$ {liquido:>8.2f}")
            
        print("-" * 95)
        print(f"{'TOTAL PAGO PELA EMPRESA:':<78} R$ {total_pago:>10.2f}")
            
    print("="*95 + "\n")
