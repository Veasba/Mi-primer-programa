
input_usuario = input("Que numero quieres adivinar: ")


numero_ganador = input("Que numero eliges?: ")

while input_usuario != numero_ganador:
    print("Vuelve a intentarlo: ")
    numero_ganador = input("Que numero es?: ")


print("Haz ganado!!")