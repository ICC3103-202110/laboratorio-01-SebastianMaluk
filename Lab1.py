import random

def print_board(board)
    for i in board:
        print(*i)

#n = int(input("Cuantas cartas van a jugar?"))
n = 50
cards = []
for i in range(1, n+1):
    cards.append(i)
    cards.append(i)
random.shuffle(cards)
t = (2*n)**(1/2)
t = int(t)
board = []

for i in range(0, len(cards), t):
    board.append(cards[i: i+t])
print_board(board)

print("")

P1, P2 = 0, 0
game = []
for i in board:
    row = []
    for j in i:
        row.append("*")
    game.append(row)
print_board(game)
print("")
x = True
T = 1


def choose_pos(z, game):
    try:
        vuelta = str(input(z + "\n"))
        pos = vuelta.split(",")
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
        game[pos[0]][pos[1]] = board[pos[0]][pos[1]]
        return pos, game
    except:
        print("Coordinadas no válidas")
        choose_pos(z, game)


while x == True:
    if T == 1:
        print("Juega J1")
        P1_old = P1
        z = "Qué carta quiere dar vuelta? fila,columna"
        pos, game = choose_pos(z, game)
        print_board(game)
        print("")
        z = "Dónde está su par? fila,columna"
        pos2, game = choose_pos(z, game)
        for i in game:
            print(*i)
        if game[pos[0]][pos[1]] == game[pos2[0]][pos2[1]]:
            print("Correcto! Encontraste un par.\n")
            P1 += 1
            game[pos[0]][pos[1]] = " "
            game[pos2[0]][pos2[1]] = " "
        else:
            print("Mala suerte :( Sigue intentando\n")
            game[pos[0]][pos[1]] = "*"
            game[pos2[0]][pos2[1]] = "*"
        if P1 == P1_old:
            T = 2
        if P1 + P2 == 50:
            break
    if T == 2:
        print("Juega J2")
        P2_old = P2
        z = "Qué carta quiere dar vuelta? fila,columna"
        pos, game = choose_pos(z, game)
        print_board(game)
        print("")
        z = "Dónde está su par? fila,columna"
        pos2, game = choose_pos(z, game)
        print_board(game)
        if game[pos[0]][pos[1]] == game[pos2[0]][pos2[1]]:
            print("Correcto! Encontraste un par.\n")
            P2 += 1
            game[pos[0]][pos[1]] = " "
            game[pos2[0]][pos2[1]] = " "
        else:
            print("Mala suerte :( Sigue intentando\n")
            game[pos[0]][pos[1]] = "*"
            game[pos2[0]][pos2[1]] = "*"
        if P2 == P2_old:
            T = 1
        if P1 + P2 == 50:
            break
    print_board(game)

print(f"J1: {P1}\nJ2: {P2}")
if P1 > P2:
    print("Ganó el jugador 1")
elif P1 < P2:
    print("Ganó el jugador 2")
else:
    print("Empate")
