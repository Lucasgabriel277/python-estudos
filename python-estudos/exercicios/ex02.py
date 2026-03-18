#DESAFIO 2:
#Faz um programa que pergunta um número e diz se ele é
#Positivo (maior que 0)
#Negativo (menor que 0)
#Ou zero

num = int(input('digite um número: '))

if num > 0:
    print("Positivo")

elif num < 0:
    print("Negativo")
    
else: 
    print("O número é zero")