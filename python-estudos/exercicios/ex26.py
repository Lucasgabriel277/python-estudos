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
    print("1 - Cadastrar produto com nome e preço")
    print("2 - Listar todos os produto")
    print("3 - Buscar pelo nome do produto")
    print("4 - Remover pelo nome do produto")
    print("5 - Sair")
    
    
lista_produto = []

while True:
    
    produtos = {}
    
    header("Bem vindo ao sistema de estoque de produtos")
    
    menu()
    
    opcao = int(input("Escolha uma opção entre 1 a 5: ")) 
    
    if opcao == 1:
        
        limpar_tela()
        header("Cadastro de produtos")
        
        produtos["nome"] = input("Nome do produto: ").title().strip()
        produtos["preço"] = float(input("Preço do produto: R$ "))
        
        lista_produto.append(produtos)
        print("\nProduto cadastrado com sucesso!\n")
    
    elif opcao == 2:
        
        header("Exibir produtos cadastrados")
        
        if len(lista_produto) == 0:
            print("\nNenhum produto cadastrado ainda.\n")
            
        else:
            
            limpar_tela()
            
            header("Exibir produtos cadastrados")
            
            for produtos in lista_produto:
                print(f'\n{produtos["nome"]} | R$ {produtos["preço"]}')
                
        print(f"\nO total de produtos cadastrado é de {len(lista_produto)}\n")

    elif opcao == 3:
        
        limpar_tela()
        
        header("Pesquisar produtos")
        
        busca = input("Digite o nome do produto: ").title()

        for produto in lista_produto:
            if produto["nome"] == busca:
                print(f"Produto {produto['nome']} encontrado!")
                print(f'{produto["nome"]} | R$ {produto["preço"]}\n')

                break
            
        else:
            print(f"Produto {busca} não encontrado!")
            
    elif opcao == 4:
        
        limpar_tela()
        
        header("Remover produto")
        
        for produtos in lista_produto:
            
            print(f'\n{produtos["nome"]} | R$ {produtos["preço"]}')
                
        print(f"\nO total de produtos cadastrado é de {len(lista_produto)}\n")
        
        remove = input("Digite o nome do produto para remove-lo: ").title()
        
        for produto in lista_produto:
            
            if produto["nome"] == remove:
                lista_produto.remove(produto)
                print(f"Produto {remove} removido com sucesso!")
                break
            
        else:
                print(f"Produto {remove} não encontrado!")
        
    elif opcao == 5:
        
        header("Encerrando sistema de estoque de produtos")
        break

    else: 
         print("Opção inválida!\nTente novamente!")