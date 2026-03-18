import os

def limpar_tela():
    # 'nt' é o identificador para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux ou macOS (posix)
    else:
        os.system('clear')

def header(texto):
    largura = 55
    print("-" * largura)
    print(texto.upper().center(largura))
    
def menu():
    largura = 55
    print("-" * largura)
    print("[1] - Cadastrar funcionário com nome, cargo e salário")
    print("[2] - Listar todos os funcionários")
    print("[3] - Buscar funcionário pelo nome")
    print("[4] - Remover funcionário pelo nome")
    print("[5] - Atualizar cargo e salário ao mesmo tempo")
    print("[6] - Exibir total de funcionários e maior salário")
    print("[7] - Sair")
    print("-" * largura)
    
def maior_menor_salario():
    print("1 - Para ver o maior salário")
    print("2 - Para ver o menor salário")
    
lista_funcionarios = []

while True: 
    
    funcionario = {}
    
    header("Sistema de funcionários completo")
    menu()
    
    opcao = int(input("Escolha uma opção entre [1] e [7] para acessar o menu: "))
    
    if opcao == 1:
        
        limpar_tela()
        header("Cadastro de funcionários")
        largura = 55
        print("-" * largura)
        
        funcionario["nome"] = input("Nome: ").strip().title()
        funcionario["cargo"] = input("Cargo: ").strip().title()
        funcionario["salário"] = float(input("Salário: R$")) 
        
        lista_funcionarios.append(funcionario)
        print(f"\nDados do funcionário {funcionario['nome'].upper()} cadastrado com sucesso.\n")     
    
    elif opcao == 2:
        
        limpar_tela()
        header("Exibir dados dos funcionários cadastrados")
        largura = 55
        print("-" * largura)
        
        if len(lista_funcionarios) == 0:
            print("\nNenhum funcionário cadastrado!\n")
        
        else:
            for funcionario in lista_funcionarios:
                
                print(f"\nNome: {funcionario['nome'].upper()} | Cargo: {funcionario['cargo'].upper()} | Salário: R${funcionario['salário']:.2f}.")
                
        print(f"Total de funcionários cadastrados é {len(lista_funcionarios)}.")
    
    elif opcao == 3:
        limpar_tela()
        header("Exibir dados dos funcionários cadastrados")
        largura = 55
        print("-" * largura)
        
        busca = input("Nome do funcionário: ").strip().title()
        
        for funcionario in lista_funcionarios:
            if funcionario["nome"] == busca:
                
                print(f"\nFuncionário {busca.upper()} encontrado!\n")
                print(f"Dados  do funcionário:\nNome: {funcionario['nome'].upper()} | Cargo: {funcionario['cargo'].upper()} | Salário: R${funcionario['salário']:.2f}.\n")
                
                break
        else:
            print(f"Funcionário {busca.upper()} não encontrado!")
        
    elif opcao == 4:
        limpar_tela()
        header("Remover funcionário")
        largura = 55
        print("-" * largura)
        
        for funcionario in lista_funcionarios:
            print(f"Dados do funcionário:\nNome: {funcionario['nome'].upper()} | Cargo: {funcionario['cargo'].upper()} | Salário: R${funcionario['salário']:.2f}.\n")
        
        print(f"O total de funcionários é de: {len(lista_funcionarios)}.")
            
        remove = input("Digite o nome do funcionário para remove-lo: ").strip().title()
        
        for funcionario in lista_funcionarios:
            if funcionario["nome"] == remove:
                
                lista_funcionarios.remove(funcionario)
                
                print(f"\nFuncionário {remove.upper()} excluido com sucesso.")
                break
               
        else:
            print(f"Funcionário {remove.upper()} não encontrado!")
            
    elif opcao == 5:
        
        limpar_tela()
        header("atualizar dados do funcionário")
        largura = 55
        print("-" * largura)
        
        nome = input("Digite o nome do funcionário: ").strip().title()
        
        for funcionario in lista_funcionarios:
            if funcionario["nome"] == nome:
            
                print(f"Dados do funcionário:\nNome: {funcionario['nome'].upper()} | Cargo: {funcionario['cargo'].upper()} | Salário: R${funcionario['salário']:.2f}.\n")
                
                atualiza_cargo = input("Novo cargo: ").strip().title()
                atualiza_salario = float(input("Novo salário: R$"))
                
                funcionario.update({"cargo": atualiza_cargo, "salário": atualiza_salario})
                
                print(f"\nDados do funcionário {nome.upper()} atualizado com sucesso.")
                break

        else:
            print(f"\nFuncionário {nome.upper()} não encontrado.\n")

    elif opcao == 6:
    
        limpar_tela()
        header("quantidade de funcionários")
        largura = 55
        print("-" * largura)
        
        if len(lista_funcionarios) == 0:
            print("\nNenhum funcionário cadastrado!\n")
        
        else:
            print(f"Total de funcionários cadastrados é {len(lista_funcionarios)}.")
        
        maior_menor_salario()
        
        opcao_menu2 = int(input("Digite um número entre 1 e dois para acessar o menu: "))
        
        if opcao_menu2 == 1: 
            maior = lista_funcionarios[0]
                   
            for funcionario in lista_funcionarios:
                if funcionario["salário"] > maior["salário"]:
                    
                    maior = funcionario
                    
            print(f"O maior salário é do funcionário {maior['nome'].upper()}\nSalário: R${maior['salário']}\n")
                
        elif opcao_menu2 == 2:
            
            menor = lista_funcionarios[0]
            
            for funcionario in lista_funcionarios:
                if funcionario["salário"] < menor["salário"]:
                    
                    menor = funcionario
                    
            print(f"O menor salário é do funcionário {menor['nome'].upper()}\nSalário: R${menor['salário']}\n")
                    
        else:
            print("\nOpção inválida!\nTente Novamente!\n")
            
    elif opcao == 7:
        
        header("encerrando o sistema de funcionários completo")
        
        break
    
    else:
        
        print("\nOpção inválida!\nTente novamente!")