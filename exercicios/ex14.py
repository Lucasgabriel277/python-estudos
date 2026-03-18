'''Ex 8: Programa que pergunta um número N e imprime "Fizz" N vezes se N for múltiplo de 3, senão imprime "Buzz" N vezes'''

n = int(input("Digite um número: "))
if n % 3 == 0:
    for i in range(n):
            print("Fizz")
else:
    for i in range(n):
            print("Buzz")