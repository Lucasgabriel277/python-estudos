'''Ex 9: Programa que conta de 1 a 30, mas:

Se o número for múltiplo de 3, imprime "Fizz"
Se for múltiplo de 5, imprime "Buzz"
Se for múltiplo de ambos (3 e 5), imprime "FizzBuzz"
Senão, imprime o número'''

for i in range (1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  # múltiplo de 3 E 5
    elif i % 3 == 0:
        print("Fizz")      # só múltiplo de 3
    elif i % 5 == 0:
        print("Buzz")      # só múltiplo de 5
    else:
        print(i)