
contador = 0
soma = 0
positivo = 0
negativo = 0

while True:
    valores = int(input("Digite um número: "))
    if valores == 0:
        break
    contador += 1
    soma += valores
    
    if valores > 0:
        positivo += 1
        
    elif valores < 0:
        negativo += 1
        
print(f"O total de números digitados foi {contador}")
print(f"A soma dos números digitados foi {soma}")
print(f"Quantos números positivos {positivo}")
print(f"Quantos números negativos {negativo}")