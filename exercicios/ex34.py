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
    print("-" * largura) 
    
def menu():
    print("[1] - Cadastrar EPI com nome, código e quantidade em estoque")
    print("[2] - Listar todos os EPIs")
    print("[3] - Buscar EPI pelo código")
    print("[4] - Retirar EPI do estoque")
    print("[5] - Sair")
    
epis = []  # lista que guarda todos os EPIs
def cadastrar_epi():
    epi = {} #dicionario dos dados do epi
    epi['nome'] = input("Nome do EPI: ").title().strip()
    epi['codigo'] = input("Código do EPI: ").strip()
    epi['quantidade'] = int(input("Quantidade: "))
    epis.append(epi)
    print("\nEPI cadastrado com sucesso!")
    
def exibir_epi():
    if len(epis) == 0:
        return None
    else:
        for epi in epis:
            print(f"Epi: {epi['nome'].upper()} - Código: {epi['codigo']} - Quantidade: {epi['quantidade']}")
            
def buscar_epi(codigo):
    for epi in epis:
        if epi["codigo"] == codigo:
            return epi
    return None

def retirar_epi():
    
    codigo = input("Código do EPI: ").strip()
    resultado = buscar_epi(codigo)
    
    if resultado:                          # EPI encontrado?
        if resultado['quantidade'] > 0:    # tem estoque?
            resultado['quantidade'] -= 1
            print("Epi retirado com sucesso!")
            
        else:
            print("estoque zerado")        # aparece quando quantidade é zero
    else:
        print("EPI não encontrado")
        
def main():
    
    while True:
        
        header("Sistema de epis") 
        menu()
        
        opcao = int(input("Escolha uma opção entre 1 a 5: ")) 
        
        if opcao == 1:
            limpar_tela()
            header("Cadastro de epis")
            cadastrar_epi()
            
        elif opcao == 2:
            limpar_tela()
            header("exibir epis")
            exibir_epi() 
            
        elif opcao == 3:
            limpar_tela()
            header("buca de epis")
            
            codigo = input("Código do EPI: ").strip()
            resultado = buscar_epi(codigo)
            
            if resultado:
                print(f"EPI: {resultado['nome'].upper()} - Código: {resultado['codigo']} - Quantidade: {resultado['quantidade']}")
            else:
                print("EPI não encontrado!")
            
        elif opcao == 4: 
            limpar_tela()
            header("retirada de epi")
            retirar_epi()
        
        elif opcao == 5:
            header("encerrando o sistema de epis")
            break

        else:
            print("Opção invalida")
            
main()