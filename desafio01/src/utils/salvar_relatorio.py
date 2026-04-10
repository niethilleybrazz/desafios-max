import os

def salvar_relatorio(lista_dados):
    if not lista_dados:
        print("\nErro: Não há dados para salvar. Cadastre pelo menos um funcionário.")
        return

    diretorio_tests = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "tests")
    
    if not os.path.exists(diretorio_tests):
        os.makedirs(diretorio_tests)
        
    caminho_arquivo = os.path.join(diretorio_tests, "relatorio_funcionarios.txt")
    
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("="*95 + "\n")
            arquivo.write(f"{'RELATÓRIO DE FUNCIONÁRIOS':^95}\n")
            arquivo.write("="*95 + "\n")
            
            # Cabeçalho da tabela
            arquivo.write(f"{'Nome':<20} | {'Tipo':<12} | {'Bruto':<12} | {'INSS':<10} | {'IRRF':<10} | {'Líquido':<12}\n")
            arquivo.write("-" * 95 + "\n")
            
            total_pago = 0.0
            for f in lista_dados:
                nome = f.get('nome', 'N/A')
                tipo = f.get('tipo', 'N/A')
                bruto = f.get('salario_bruto', 0.0)
                inss = f.get('desconto_inss', 0.0)
                irrf = f.get('desconto_irrf', 0.0)
                liquido = f.get('salario_liquido', 0.0)
                
                total_pago += liquido
                
                arquivo.write(f"{nome:<20} | {tipo:<12} | R$ {bruto:>8.2f} | R$ {inss:>7.2f} | R$ {irrf:>7.2f} | R$ {liquido:>8.2f}\n")
                
            arquivo.write("-" * 95 + "\n")
            arquivo.write(f"{'TOTAL PAGO PELA EMPRESA:':<78} R$ {total_pago:>10.2f}\n")
            arquivo.write("="*95 + "\n")
            
        print(f"\nRelatório salvo com sucesso no arquivo: {os.path.abspath(caminho_arquivo)}")
        
    except Exception as e:
        print(f"\nErro ao salvar o arquivo: {e}")
