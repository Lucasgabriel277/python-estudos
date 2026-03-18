while True:

    numero = int(input("Digite um número: "))

    if numero == 0:
        break

    contador = 1

    while contador <= 10:

        print(numero, "x", contador, "=", numero * contador)

        contador += 1
