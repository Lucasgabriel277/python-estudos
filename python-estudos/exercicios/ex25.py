def header(texto):
    largura = 55
    print("-" * largura)
    print(texto.center(largura))
    print("-" * largura) 
    
def menu():
    print("1 - Cadastrar contato com nome e telefone")
    print("2 - Listar todos os contatos")
    print("3 - Buscar contato pelo nome")
    print("4 - Sair")

lista_contatos = []
while True:
    
    contatos = {}
    
    header("Sistema de cadastro")
    
    menu()
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        
        header("Coleta de dados")
        
        contatos["nome"] = input("Nome: ").title()
        contatos["email"] = input("Email: ").lower().strip()
        contatos["telefone"] = int(input("Telefone: "))
        
        lista_contatos.append(contatos)
        print("Contato cadastrado com sucesso!")
    
    elif opcao == 2:
        
        header("Lista de contatos")
        
        if len(lista_contatos) == 0:
            print("Nenhum contato salvo!")
        
        else: 
            for contatos in lista_contatos:
                print(f"{contatos['nome']} | {contatos['email']} | {contatos['telefone']}")
                
            print(f"Total contatos: {len(lista_contatos)}")
            
    elif opcao == 3:
        
        header("Buscar contatos")

        busca = input("Digite o nome do contato: ").title()

        for contato in lista_contatos:
            if contato["nome"] == busca:
                print(f"Encontrado! {contato['nome']} | {contato['email']} | {contato['telefone']}")
                break
        else:
            print("Contato não encontrado!")
            
    elif opcao == 4:
        
        header("Sistema encerrado!")
        break
    
    else:
        print("Opção inválida!\nTente novamente!")
            