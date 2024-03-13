from random import randint

intentos = 0
estimado = 0
numeroSecreto = randint(1,100)
nombre = input("Dime tu nombre")

print(f"Bueno {nombre}, he pensado un número entre 1 100\nTienes 8 intentos para adivinar")

while intentos<8:
    estimado = int(input("¿Cuál es el número?"))
    intentos += 1

    if estimado < numeroSecreto:
        print("Parece que acabas de elegir un número muy chico, prueba con uno más grande")
    elif estimado > numeroSecreto:
        print("Parece que acabas de elegir un número muy grande, prueba con uno más chico")
    else:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")

if estimado != numeroSecreto:
    print(f"Lo siento, se han agotado los intentos. el número secreto era {numeroSecreto}")