
mi_lista = []

input_usuario = input("Que quieres comprar?: (Escribe FIN para terminar la lista)")

while input_usuario != "FIN":

    mi_lista.append(input_usuario)

    input_usuario = input("Que quieres comprar?: (Escribe FIN para terminar la lista)")


for item in mi_lista:
    print("Tengo que comprar {}".format(item))

print("Es la lista de la compra")