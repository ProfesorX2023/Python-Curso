def cantidad_pares(lista_numeros):
    contador = 0
    for n in lista_numeros:
        if n%2==0:
            contador += 1
        else:
            pass
    return contador

lista_numeros = list(range(101,567))

print(lista_numeros)

print(cantidad_pares(lista_numeros))