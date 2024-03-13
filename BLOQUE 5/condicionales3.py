hablaIngles = False
sabePython = True
if hablaIngles == True and sabePython == True:
    print("Cumples con los requisitos para postularte")
elif hablaIngles == False and sabePython == False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif hablaIngles == False and sabePython == True:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, ncesitas tener saber programar en Python")