#Cria um programa que pergunta a idade de uma pessoa e diz se ela pode:
#Tirar carteira de motorista (18 anos ou mais) OU se ainda não pode.

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Pode tirar carteira!")
    
else:
    print("Não pode tirar carteira!")
    
