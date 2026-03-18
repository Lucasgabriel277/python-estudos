'''NÍVEL 1: Aquecimento (if/elif/else)
Ex 1: Programa que pergunta a temperatura e diz:

"Frio" se < 15
"Agradável" se entre 15 e 25
"Quente" se > 25'''


for i in range (6):
    temp = int(input("Qual a temperatura de hoje? "))
    
    if temp < 15:
        print("Hoje está bastante frio então.")
    
    elif temp >= 15 and temp < 25:
        print("Hoje está bastante agradável.")
        
    else:
        print("Hoje está quente!")

