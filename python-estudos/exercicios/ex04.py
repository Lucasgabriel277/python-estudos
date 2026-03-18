'''DESAFIO 4:
Faz um programa que pergunta a idade de uma pessoa e diz em qual categoria ela se encaixa:

"Criança" se idade < 12
"Adolescente" se idade entre 12 e 17 (inclusive)
"Adulto" se idade entre 18 e 59 (inclusive)
"Idoso" se idade >= 60'''

for i in range (10):
    idade = int(input("Digite a sua idade: "))
    
    if idade < 12:
        print("Criança!")
    elif idade > 12 and idade <= 17:
        print("Adolescente!")
    elif idade >= 18 and idade <= 60:
        print("Adulto!")
    else:
        print("Idoso!")

        
        