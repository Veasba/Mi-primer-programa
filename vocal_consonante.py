

frase_del_usuario = input("Dime una frase y yo contare todos los puntos, comas y espacios: ")

punto = "."
coma = ","
espacio = " "

n_punto = 0
n_coma = 0
n_espacio = 0

for frase in frase_del_usuario:
    if frase in punto:
        n_punto += 1
    elif frase in coma:
        n_coma += 1
    elif frase in espacio:
        n_espacio += 1

print("Numero de puntos es: {}".format(n_punto))
print("Numero de comas es: {}".format(n_coma))
print("Numero de espacios es: {}".format(n_espacio))

