empresas = {}

while True: 
    
    nome_empresas = input("Digite o nome da empresa: ").strip().title()
    
    empresas[nome_empresas] = {}
    
    empresas[nome_empresas]["responsavel"] = input("Nome do responsavel: ").strip().title()
    empresas[nome_empresas]["contato"] = int(input("Contato do responsavel: "))
    
    print("\nDados cadastrados!\n")
    
    nome = input("Digite o nome da empresa: ").strip().title()
    break
    
if nome in empresas:
    
    for nome, dados in empresas.items():
        print(f"\nEmpresa: {nome} - Responsavel: {dados['responsavel']} - Contato: {dados['contato']}\n")
            
else:
    print("Dados incorretos!")