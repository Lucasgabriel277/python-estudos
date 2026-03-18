
senha = ""
while len(senha) < 4:
    senha = input("Digite uma senha")
    
    if len(senha) < 4:
        print("Accesso Negado")
    else:
        print("Acesso Liberado!")
        break
    
   
    