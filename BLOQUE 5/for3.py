listaNumeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sumaPares = 0
sumaImpares = 0
for numero in listaNumeros:
    if numero%2==0:
        sumaPares += numero
    else:
        sumaImpares += numero

print(f"La suma de pares es: {sumaPares}")
print(f"La suma de imares es: {sumaImpares}")

print(f"Total {sumaPares+sumaImpares}")