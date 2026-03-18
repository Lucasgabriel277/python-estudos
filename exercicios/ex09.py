'''Ex 3: Calculadora simples: pergunta dois números e uma operação (+, -, *, /) e faz o cálculo'''

for i in range(10):
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um número: "))
    
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
   
    print("Adição (+)")
    print("Subtração (-)")
    print("Multiplicação (*)")
    print("Divisão (/)")
    
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    
    res = str(input("Qual operação você deseja realizar? "))
    
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    
    if res == "Adição":
            cal = num1 + num2
            print(cal)
    elif res == "Subtração":
            cal = num1 - num2
            print(cal)
    elif res == "Multiplicação":
             cal = num1 * num2
             print(cal)
    elif res == "Divisão":
            cal = num1 / num2
            print(cal)
            
    print("Parabéns!")
    
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")