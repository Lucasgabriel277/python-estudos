def header(texto):
    largura = 55
    print("-" * largura)
    print(texto.center(largura))
    print("-" * largura) 
    
lista_livros = []

while True:
    
    livros = {}
    
    header("CADASTRO DE LIVROS")
    
    livros ["nome"] = input("Digite o nome do livro: ").title()
    livros ["autor"] = input("Digite o nome do autor do livro: ").title()
    livros ["ano"] = int(input("Digite o ano do lançamento do livro: "))
    
    lista_livros.append(livros)
    print("Livro cadastrado com sucesso!")
    
    resposta = int(input("Deseja continuar? responda com 1 para sim e 2 para não: "))
    if resposta == 2:
        break
    
header("ACERVO LITERÁRIO")

for c, livro in enumerate(lista_livros, start=1):
    print(f'{c}ª {livro}')