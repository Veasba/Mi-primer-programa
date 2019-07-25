
mayuscula_del_usuario = input("Introduzca su texto: ")

mayuscula = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "S", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

n_mayuscula = 0

for letra in mayuscula_del_usuario:
    if letra in mayuscula:
        n_mayuscula += 1


print("La cantidad de mayusculas es: {}".format(n_mayuscula))
