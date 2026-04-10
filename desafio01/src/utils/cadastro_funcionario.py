def cadastro_funcionario(lista_dados):
    print("\n===== Cadastro de Funcionário =====")
    
    while True:
        nome = input("Nome do Funcionário: ").strip()
        if nome:
            break
        print("Erro: O nome não pode estar vazio.")

    while True:
        tipo = input("Tipo (CLT|ESTAGIARIO|FREELANCER): ").strip().upper()
        if tipo in ["CLT", "ESTAGIARIO", "FREELANCER"]:
            break
        print("Erro: Tipo inválido. Escolha entre CLT, ESTAGIARIO ou FREELANCER.")

    while True:
        try:
            salario = float(input("Salário: "))
            if salario < 0:
                print("Erro: O salário deve ser um valor positivo.")
                continue
            break
        except ValueError:
            print("Erro: Por favor, digite um valor numérico válido para o salário.")

    while True:
        try:
            horas = float(input("Horas trabalhadas: "))
            if horas < 0:
                print("Erro: As horas trabalhadas devem ser um valor positivo.")
                continue
            break
        except ValueError:
            print("Erro: Por favor, digite um valor numérico válido para as horas.")

    funcionario = {
        "nome": nome,
        "tipo": tipo,
        "salario": salario,
        "horas": horas
    }
    
    lista_dados.append(funcionario)
    print(f"\nFuncionário {nome} cadastrado com sucesso!")