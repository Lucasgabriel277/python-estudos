def header(texto):
    largura = 55
    print("-" * largura)
    print(texto.center(largura))
    print("-" * largura) 

lista_filmes = []
while True:
    
    header("CINE ALCÂNTARA")
    
    filmes = {}
    
    filmes ["Nome do filme"] = input("Digite o nome do filme: ").title()
    filmes ["Ano de lançamento"] = int(input("Digite o ano de lançamento: "))
    
    lista_filmes.append(filmes)
       
    resposta = int(input("Deseja continuar? responda com 1 para sim e 2 para não: "))
    if resposta == 2:
        break
    
header("CATÁLAGO DE FILMES")

for filmes in lista_filmes:
    print(f'{filmes["Nome do filme"]} - {filmes["Ano de lançamento"]}')