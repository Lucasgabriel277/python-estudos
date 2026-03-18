'''DESAFIO:
Faz um programa que:

Pergunta um número pro usuário
Se o número for par, imprime "PAR" 10 vezes
Se o número for ímpar, imprime "ÍMPAR" 5 vezes'''

for i in range (10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        for i in range (11):
            print("É par!")
    else:
        for i in range (5):
            print("É impar!")