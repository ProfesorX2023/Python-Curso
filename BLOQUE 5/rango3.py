sumaCuadrados = 0
valores = list(range(1,16))
for valor in valores:
    sumaCuadrados = sumaCuadrados + valor**2

print(f"""
Las suma de los cuadrados 
desde {valores[0]} hasta
{valores[14]} 
es {sumaCuadrados}""")