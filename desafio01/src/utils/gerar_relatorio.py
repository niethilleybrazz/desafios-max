def gerar_relatorio(lista_dados):
    print("\n" + "="*40)
    print(f"{'RELATÓRIO DE FUNCIONÁRIOS':^40}")
    print("="*40)
    
    if not lista_dados:
        print("Nenhum funcionário cadastrado até o momento.")
    else:
        # Cabeçalho da tabela
        print(f"{'Nome':<20} | {'Tipo':<12} | {'Salário':<10} | {'Horas'}")
        print("-" * 55)
        
        for f in lista_dados:
            nome = f.get('nome', 'N/A')
            tipo = f.get('tipo', 'N/A')
            salario = f.get('salario', 0.0)
            horas = f.get('horas', 0.0)
            
            print(f"{nome:<20} | {tipo:<12} | R$ {salario:>8.2f} | {horas:>5.1f}h")
            
    print("="*40 + "\n")
