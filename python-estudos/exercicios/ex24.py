def header(texto):
    largura = 55
    print("-" * largura)
    print(texto.center(largura))
    print("-" * largura) 
    
lista_contatos = []

while True:
    
    contatos = {}
    
    header("CADASTRO DE CONTATOS")
    
    contatos["nome"] = input("Nome: ").title()
    contatos["email"] = input("Emil: ").lower().strip()
    contatos["telefone"] = int(input("Telefone: "))
    
    lista_contatos.append(contatos)
    print("Contato cadastrado com sucesso!")
    
    resposta = int(input("Deseja continuar? responda com 1 para sim e 2 para não: "))
    if resposta == 2:
        break

header("AGENDA DE CONTATOS")

for contatos in lista_contatos:
    
    print(f"{contatos['nome']} | {contatos['email']} | {contatos['telefone']}")
    
print(f"Total contatos: {len(lista_contatos)}")