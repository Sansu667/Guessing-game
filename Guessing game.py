import random

print("¡Bienvenido al juego de adivinanzas!")

player = input("¿Cuál es tu nombre?: ")
intentos = 8
numero_random = int(random.uniform(1, 10))

while intentos > 0:

    intentos -= 1
    numero_player = int(input("Ingrese un numero entre el 1 al 10: "))
    if numero_player < 1 or numero_player >= 10:
        print("Este número no está permitido")
    elif numero_player < numero_random:
        print("Tu número es menor al pensado")
    elif numero_player > numero_random:
        print("Tu número es superior al pensado")
    elif numero_player == numero_random:
        print(f"¡Felicitaciones, {player}! Adivinaste el numero secreto \nTe quedaron {intentos} intentos")
        break
else:
    print("GAME OVER")