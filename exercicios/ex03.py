#Faz um programa que pergunta a nota de um aluno (0 a 10) e diz:
#"Aprovado" se nota >= 7
#"Recuperação" se nota >= 5 e < 7
#"Reprovado" se nota < 5
#Aqui você vai precisar de duas condições ao mesmo tempo no elif (nota >= 5 E nota < 7).
#Dica: usa and pra juntar condições.

nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado!")

elif nota >= 5 and nota < 7:
    print("Recuperação!")
    
else:
    print("Reprovado!")