'''Crie um programa que:

O usuário digita vários números.

O programa deve mostrar:

✅ Quantos números foram digitados
✅ A soma dos números
✅ O maior número
✅ O menor númerox
✅ A média

Parar quando digitar 999'''
contador = 0
soma = 0
maior = None
menor = None
par = 0
impar = 0
media = 0


while True:
    valores = float(input("Digite um número: "))
    if valores == 999:
        break
    contador += 1 
    soma += valores
    
    if valores % 2 == 0:
        par += 1
    else:
        impar += 1

    
    if maior is None or valores > maior:
        maior = valores
        
    elif menor is None or valores < menor:
        menor = valores
        
if contador > 0:       
    media = soma / contador

else:
    media = 0
    
print(f"O total de números digitados foi {contador}")
print(f"A soma dos números digitados foi {soma}")
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
print(f"Quantidade de pares: {par}")
print(f"Quantidade de impares: {impar}")
print(f"A média dos números é {media}")


    