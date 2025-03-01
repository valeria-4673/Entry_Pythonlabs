import random

def display_board(board):
    print("+-------"*3 + "+")
    for row in board:
        print("|       |       |       |")
        print("|","     | " .join(str(cell) for cell in row),"    |")
        print("|       |       |       |")
        print("+-------"*3 + "+")
    return board

def poner_cruz(board):
    while True:
        move = int(input("number of the cell you wanna put your move? "))
        if 1 <= move <= 9:
            break

    fila = (move-1) // 3
    columna = (move-1) % 3
    board [fila] [columna] = "O"
    return board

def compu_movement (board):
    available = []
    for fila in range (3):
        for columna in range (3):
            if board [fila] [columna] != "O" and board [fila] [columna] != "X":
                available.append(board [fila] [columna])
    compu= random.choice(available)

    fila = (compu-1) // 3
    columna = (compu-1) % 3
    board [fila] [columna] = "X"
    return board

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
print("el board original es: ")
board = display_board(board)

flag = False
while not flag:
    for fila in range (3):
        counter = 0
        for columna in range (3):
            if board [fila] [columna] == "O" or board [fila] [columna] == "X":
                counter += 1
                if counter == 3:
                    flag = True
                    break
            else:
                counter = 0
        if flag:
            break

    poner_cruz(board)
    print("El actualizado con movimiento humano es: ")
    board = display_board(board)
    compu_movement(board)
    print("El actualizado con movimiento computador es: ")
    board = display_board(board)
