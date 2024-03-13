marcas = {'nike','adidas','puma'}
productos = {'zapatos','pantalon','camisola'}

miZip = zip(marcas,productos)

for marca,producto in miZip:
    print(marca,producto)