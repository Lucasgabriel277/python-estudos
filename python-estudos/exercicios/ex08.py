'''Ex 2: Programa que pergunta dois números e diz qual é o maior (ou se são iguais)'''
for i in range (5):
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um número: "))
    
    if num1 > num2:
        print(f"O número {num1} é maior que o número {num2}")
    elif num1 < num2:
         print(f"O número {num1} é menor que o número {num2}")
    else:
        print("Os números são iguais")