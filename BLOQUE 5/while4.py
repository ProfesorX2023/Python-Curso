numeros = [1,3,5,7,9]
buscar = 5
encontrado = False
while not encontrado and numeros:
    if numeros.pop(0) == buscar:
        encontrado = True