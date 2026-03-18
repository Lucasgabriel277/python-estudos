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
    print(texto.center(largura))
    print("-" * largura) 
    
def menu():
    print("1 - Cadastrar funcionário com nome e cargo")
    print("2 - Listar todos os funcionários")
    print("3 - Buscar pelo nome do funcionário")
    print("4 - Remover pelo nome do funcionário")
    print("5 - Atualizar o cargo do funcionário")
    print("6 - Sair")
    

lista_funcionarios = []

while True:
    funcionarios = {}
    
    header("Sistema de dados dos funcionários")
    menu()
    
    opcao = int(input("Escolha uma opção entre 1 a 6: "))
    
    if opcao == 1:
        limpar_tela()
        header("Cadastro do funcionário")
        
        funcionarios["nome"] = input("Digite o nome do funcionário: ").strip().title()
        funcionarios["cargo"] = input("Digite o nome do cargo do funcionário: ").strip().title()
        
        lista_funcionarios.append(funcionarios)
        print(f'\nO funcionário {funcionarios["nome"]} cadastrado com sucesso!\n')
        
    elif opcao == 2:
        header("Exibir dados dos funcionários")
        
        if len(lista_funcionarios) == 0:
            print("\nNenhum funcionário cadastrado.\n")
        
        else:
            limpar_tela()
            header("Exibir dados dos funcionários")
            
            for funcionarios in lista_funcionarios:
                print(f'\nNome: {funcionarios["nome"]} - Cargo: {funcionarios["cargo"]}')
                
        print(f"\nO total de produtos cadastrado é de {len(lista_funcionarios)}\n")
        
    elif opcao == 3:
        limpar_tela()
        header("Procurar por funcionário")
        
        busca = input("Digite o nome do funcionário: ").strip().title()
        
        for funcionario in lista_funcionarios:
            if funcionario["nome"] == busca:
                print(f"\nBusca realizada com sucesso!\nSegue os dados do funcionário:")
                print(f'\nNome: {funcionario["nome"]} - Cargo: {funcionario["cargo"]}')
                break
            
        else:
            print(f"Funcionário {busca} não encontrado!")
    
    elif opcao == 4:
        limpar_tela()
        header("Remover funcionário")
        
        for funcionarios in lista_funcionarios:
                print(f'\nNome: {funcionarios["nome"]} - Cargo: {funcionarios["cargo"]}')
                
        print(f"\nO total de produtos cadastrado é de {len(lista_funcionarios)}\n")
        
        remove = input("Digite o nome do funcionário para remove-lo: ").strip().title()
        
        for funcionario in lista_funcionarios:
            if funcionario["nome"] == remove:
                lista_funcionarios.remove(funcionario)
                print(f"\nFuncinário {remove} excluido com sucesso.")
                break
               
        else:
            print(f"Funcionário {remove} não encontrado!")
                
    elif opcao == 5:
        limpar_tela()
        header("Atualização dos dados dos funcionários")
        
        atualiza = input("Digite o nome do funcionário que terá atualização: ").strip().title()
        novo_cargo = input("Digite o nome do novo cargo do funcionário: ").strip().title()
        
        for funcionario in lista_funcionarios:
            if funcionario["nome"] == atualiza:
                funcionario["cargo"] = novo_cargo
                print(f"\nDados do funcionário {atualiza} atualisados com sucesso.")
                break
        
        else:
            print(f"Funcionário {atualiza} não encontrado!")
        
    elif opcao == 6:
        header("Sistema de dados de funcionários encerrado.")
        break

    else:
        print("\nOpção inválida!\nTente novamente!")
        limpar_tela()