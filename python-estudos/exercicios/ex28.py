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
    print("1 - Cadastrar livro com título, autor e ano")
    print("2 - Listar todos os livros")
    print("3 - Buscar livro pelo título")
    print("4 - Remover livro pelo título")
    print("5 - Atualizar ano do livro")
    print("6 - Ver total de livros por autor")
    print("7 - Sair")
    
lista_livros = []

while True:
    livros = {}
    
    header("Acervo literário de Alcântara")
    menu()
    
    opcao = int(input("Escolha uma opção entre 1 a 7: "))
    
    if opcao == 1:
        limpar_tela()
        header("Cadastro de dados dos livros")
        
        livros["titulo_livro"] = input("Digite o titulo do livro: ").strip().title()
        livros["nome_autor"] = input("Digite o nome do autor do livro: ").strip().title()
        livros["ano_livro"] = int(input("Digite o ano do livro: "))
        
        lista_livros.append(livros)
        print(f"\nLivro {livros['titulo_livro'].upper()} cadastrado com sucesso!")
        
    elif opcao == 2:
        header("Exibir dados dos livros do acervo")
        
        if len(lista_livros) == 0:
            print("Nenhum livro cadastrado no sistema.")
            
        else:
            limpar_tela()
            header("Exibir dados dos livros do acervo")
            
            for livros in lista_livros:
                print(f"\nTitulo do livro: {livros['titulo_livro'].upper()}\nNome do autor: {livros['nome_autor'].upper()}\nAno de lançameto: {livros['ano_livro']}\n")
        
        print(f"O total de livros disponiveis é de: {len(lista_livros)} livros.")
        
    elif opcao == 3:
        limpar_tela()
        header("Pesquise pelo acervo")
        
        busca = input("Digite o titulo do livro: ").strip().title()
        
        for livro in lista_livros:
            if livro["titulo_livro"] == busca:
                print(f"\nO livro {busca} encontrado!")
                print(f"\nTitulo do livro: {livro['titulo_livro'].upper()}\nNome do autor: {livro['nome_autor'].upper()}\nAno de lançameto: {livro['ano_livro']}\n")
                break
            
        else:
            print(f"O livro {busca} não encontrado!")
            
    elif opcao == 4:
        limpar_tela()
        header("Remover livro")
        
        for livros in lista_livros:
            print(f"\nTitulo do livro: {livros['titulo_livro'].upper()}\nNome do autor: {livros['nome_autor'].upper()}\nAno de lançameto: {livros['ano_livro']}\n")
        
        print(f"O total de livros disponiveis é de: {len(lista_livros)} livros.")
            
        remove = input("Digite o titulo do livro para remove-lo: ").strip().title()
        
        for livro in lista_livros:
            if livro["titulo_livro"] == remove:
                lista_livros.remove(livro)
                print(f"\nLivro {remove} excluido com sucesso.")
                break
               
        else:
            print(f"Livro {remove} não encontrado!")
            
    elif opcao == 5:
        limpar_tela()
        header("Atualização dos dados do livro")
        
        atualiza = input("Digite o titulo do livro que terá atualização: ").strip().title()
        novo_ano = int(input("Digite o nome do novo ano do do livro: "))
        
        for livro in lista_livros:
            if livro["titulo_livro"] == atualiza:
                livro["ano_livro"] = novo_ano
                print(f"\nDados do livro {atualiza} atualizados com sucesso.")
                break
        
        else:
            print(f"Livro {atualiza} não encontrado!")
            
    elif opcao == 6:
        limpar_tela()
        header("Quantidade de livros por autor")
        
        autor = input("Digite o nome do autor do livro: ").strip().title()
        
        for livro in lista_livros:
            if livro["nome_autor"] == autor:
                print(f"O autor {autor} tem {len(lista_livros)} livros publicados")
                break
                
        else:
            print(f"O autor {autor} não tem nenhum livro publicado.")
    
    elif opcao == 7:
        header("Encerrando o sistema do Acervo literário de Alcântara")
        break

    else:
        print("\nOpção inválida!\nTente novamente!")
     