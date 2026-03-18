def header(texto):
    largura = 55
    print("-" * largura)
    print(texto.center(largura))
    print("-" * largura) 

lista_alunos = []
while True:
    
    header("CADASTRO DE ALUNOS")
    
    alunos = {}
    
    alunos ["nome"] = input("Digite o nome do aluno: ").title()
    alunos ["idade"] = int(input("Digite a idade do aluno: "))
    
    lista_alunos.append(alunos)
        
    resposta = int(input("Deseja continuar? responda com 1 para sim e 2 para não: "))
    if resposta == 2:
        break
    
header("DADOS")
    
for alunos in lista_alunos:
    print(f'Aluno: {alunos["nome"]} - Idade: {alunos["idade"]}')
    
print(f"A quantidade de alunos cadastrados é de {len(lista_alunos)}.")