tablero=[[' ', 'M', ' ', ' ', ' '],
[' ', ' ', ' ', 'M', ' '],
[' ', ' ', ' ', ' ', ' '],
['M', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', 'M']]
while True:
    fila = int(input("Fila (0-4): "))
    columna = int(input("Columna (0-4): "))

    if tablero[fila][columna] == 'M':
        print(" acabas de pisar una mina")
        break
    else:
        print("buen posicionamiento")