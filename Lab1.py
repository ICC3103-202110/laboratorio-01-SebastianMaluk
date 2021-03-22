import random

def print_board(board):
    for i in board:
        print(*i)
    print("")

#n = int(input("Cuantas cartas van a jugar?"))
n = 8
cards = []
for i in range(1, n+1):
    cards.append(i)
    cards.append(i)
random.shuffle(cards)
t = int((2*n)**(1/2))
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


def choose_pos(z, game):
    try:
        x = False
        while not x:
            coord = str(input(z + "\n"))
            pos = coord.split(",")
            pos[0] = int(pos[0])
            pos[1] = int(pos[1])
            if game[pos[0]][pos[1]] == " ":
                print("Coordenadas no válidas")
                continue
            else:
                x = True
            game[pos[0]][pos[1]] = board[pos[0]][pos[1]]
        return pos, game
    except:
        print("Coordenadas no válidas")
        choose_pos(z, game)

def check_result(game, pos, pos2, P, txt):
    if game[pos[0]][pos[1]] == game[pos2[0]][pos2[1]]:
            print(txt[2])
            P += 1
            game[pos[0]][pos[1]] = " "
            game[pos2[0]][pos2[1]] = " "
    else:
        print(txt[3])
        game[pos[0]][pos[1]] = "*"
        game[pos2[0]][pos2[1]] = "*"
    return game, P

txt = ["Qué carta quiere dar vuelta? fila,columna", 
       "Dónde está su par? fila,columna",
       "Correcto! Encontraste un par.\n",
       "Mala suerte :( Sigue intentando\n"]

x = True
T = 1
while x == True:
    print_board(game)
    if T == 1:
        print("Juega J1")
        P1_old = P1
        pos, game = choose_pos(txt[0], game)
        print_board(game)
        
        pos2, game = choose_pos(txt[1], game)
        print_board(game)
        game, pos = check_result(game, pos, pos2, P1, txt)
        if P1 == P1_old:
            T = 2
        if P1 + P2 == n:
            break
    
    if T == 2:
        print("Juega J2")
        P2_old = P2
        pos, game = choose_pos(txt[0], game)
        print_board(game)
        pos2, game = choose_pos(txt[1], game)
        print_board(game)
        game, pos = check_result(game, pos, pos2, P2, txt)
        if P2 == P2_old:
            T = 1
        if P1 + P2 == n:
            break
    
print(f"J1: {P1}\nJ2: {P2}")
if P1 > P2:
    print("Ganó el jugador 1")
elif P1 < P2:
    print("Ganó el jugador 2")
else:
    print("Empate")
