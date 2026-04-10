def cadastro_funcionario(lista_dados):
    print("\n" + "="*40)
    print(f"{'CADASTRO DE FUNCIONÁRIO':^40}")
    print("="*40)
    
    while True:
        nome = input("Nome do Funcionário: ").strip()
        if nome:
            break
        print("Erro: O nome não pode estar vazio.")

    while True:
        tipo_input = input("Tipo (ESTAGIARIO | CLT | FREELANCER): ").strip().lower()
        if tipo_input in ["estagiario", "clt", "freelancer"]:
            tipo = tipo_input.capitalize() if tipo_input != "clt" else "CLT"
            break
        print("Erro: Tipo inválido. Escolha entre Estagiário, CLT ou Freelancer.")

    salario_bruto = 0.0
    desconto_inss = 0.0
    desconto_irrf = 0.0
    salario_liquido = 0.0

    if tipo_input == "estagiario":
        while True:
            try:
                salario_bruto = float(input("Salário Fixo: "))
                if salario_bruto <= 0:
                    print("Erro: O salário deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print("Erro: Digite um valor numérico válido.")
        
        salario_liquido = salario_bruto

    elif tipo_input == "clt":
        while True:
            try:
                salario_bruto = float(input("Salário Bruto Mensal: "))
                if salario_bruto <= 0:
                    print("Erro: O salário deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print("Erro: Digite um valor numérico válido.")
        
        desconto_inss = salario_bruto * 0.08
        if salario_bruto > 2000.00:
            desconto_irrf = salario_bruto * 0.10
        
        salario_liquido = salario_bruto - desconto_inss - desconto_irrf

    elif tipo_input == "freelancer":
        while True:
            try:
                valor_hora = float(input("Valor por hora: "))
                if valor_hora <= 0:
                    print("Erro: O valor/hora deve ser maior que zero.")
                    continue
                horas = float(input("Horas trabalhadas: "))
                if horas <= 0:
                    print("Erro: As horas devem ser maiores que zero.")
                    continue
                break
            except ValueError:
                print("Erro: Digite um valor numérico válido.")
        
        salario_bruto = valor_hora * horas
        desconto_fixo = salario_bruto * 0.05
        desconto_inss = desconto_fixo 
        salario_liquido = salario_bruto - desconto_fixo

    funcionario = {
        "nome": nome,
        "tipo": tipo,
        "salario_bruto": salario_bruto,
        "desconto_inss": desconto_inss,
        "desconto_irrf": desconto_irrf,
        "salario_liquido": salario_liquido
    }
    
    lista_dados.append(funcionario)
    print(f"\nFuncionário {nome} cadastrado com sucesso!")