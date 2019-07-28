
input_usuario = int (input("Que numero quieres adivinar: "))


numero_ganador = input("Que numero eliges?: ")

while input_usuario != numero_ganador:
    print("Vuelve a intentarlo: ")
    print("--------------------")
    numero_ganador = int (input("Que numero es?: "))


print("Haz ganado!!")