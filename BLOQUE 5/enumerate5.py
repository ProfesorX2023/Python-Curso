listaNombres = ["Marcos","Laura","Mónica","Javier","Celina","Marta","Dario","Emiliano","Melissa"]
for indice,nombre in enumerate(listaNombres):
    if nombre.startswith('M'):
        print(f"{indice}. {nombre}")