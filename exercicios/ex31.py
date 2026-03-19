def header(texto):
    largura = 55
    print("*" * largura)
    print(texto.upper().center(largura))
    print("*" * largura)
 
dicionario_empresas = {} 
   
def menu_principal():
    print("1 - Cadastrar dados da empresa com nome e cnpj".upper())
    print("2 - Ver empresas cadastradas".upper())
    print("3 - Buscar empresa pelo nome".upper())
    print("4 - Sair".upper())
    
def cadastro():
    
    ramo_empresa = input("Digite o ramo da empresa: ").strip().title()
    
    dicionario_empresas[ramo_empresa] = {}
    
    dicionario_empresas[ramo_empresa]["nome"] = input("Digite o nome da empresa: ").strip().title()
    dicionario_empresas[ramo_empresa]["cnpj"] = input("Digite o CNPJ da empresa: ").strip().title()
   
    
def listar():
    for ramo, empresa in dicionario_empresas.items():
        print(f"{ramo} -> {empresa['nome']} | {empresa['cnpj']}")    

def buscar(ramo):
    if ramo in dicionario_empresas:
        empresa = dicionario_empresas[ramo]
        print(f"Empresa: {empresa['nome']} - CNPJ: {empresa['cnpj']}")
    else:
        print("Empresa não encontrada")
        
        
def main():
    
    while True:
        
        header("bem vindo ao Sitema de cadastro de empresas")
        menu_principal()
        
        opcao = int(input("\nDigite um número para acessar o menu: "))
        
        if opcao == 1:
            
            cadastro()
            
        elif opcao == 2:
            
            listar()
            
        elif opcao == 3: 
            
            ramo = input("\nDigite o ramo da empresa: ").strip().title()
            buscar(ramo)
            
        elif opcao == 4:
            
            header("Encerrando sistema.")
            break

        else:
            print("Opção incorreta")
            
            
main()
            
            