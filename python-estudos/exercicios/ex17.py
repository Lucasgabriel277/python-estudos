
res = ""

while res != "n":
    
    print("--------------------------------------")
    print("Bem vindo ao game de calcular números")
    print("--------------------------------------")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    print("----------------------------------------------------------")
    print("Selecione a operação que você deseja realizar o calculo:")
    print("[1] - Adição")
    print("[2] - Subtração")
    print("[3] - Multiplicação")
    print("[4] - Divisão")
    print("----------------------------------------------------------")

    resposta = (input("Digite o número da operação: "))

    if resposta == "1":
        resultado = num1 + num2
        print(f"O resultado da adição é {resultado}")
        
    elif resposta == "2":
        resultado = num1 - num2
        print(f"O resultado da subtração é {resultado}")
        
    elif resposta == "3":
        resultado = num1 * num2
        print(f"O resultado da multiplicação é {resultado}")
        
    elif resposta == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é {resultado}")
        else:
            print("Não é possível dividir por zero!")

    else:
        print("Opção inválida!")

    res = str(input("Deseja continuar? S/N: ")).lower()

print("FIM")
 
