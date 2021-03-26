import random


def print_board(board):
    for i in board:
        print(*i)
    print("")

print("Rows and columns start at 1,1")
n = int(input("How many pairs of cards would you like to play with?\n"))
print("")
cards = []
for i in range(1, n+1):
    cards.append(i)
    cards.append(i)

random.shuffle(cards)
t = int((2*n)**(1/2))
board = []

for i in range(0, len(cards), t):
    board.append(cards[i: i+t])

P1, P2 = 0, 0
game = []
for i in board:
    row = []
    for j in i:
        row.append("*")
    game.append(row)


def choose_pos(txt, game):
    try:
        x = False
        while not x:
            coord = str(input(txt))
            print("")
            pos = coord.split(",")
            pos[0] = int(pos[0])-1
            pos[1] = int(pos[1])-1
            if game[pos[0]][pos[1]] == " ":
                print(txt[4])
                continue
            else:
                x = True
            game[pos[0]][pos[1]] = board[pos[0]][pos[1]]
        return pos, game
    except:
        print(txt[4])
        return choose_pos(txt, game)


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


txt = ["Which card do you want to flip? row,column\n", 
       "where is the pair? row,column\n",
       "Correct! You found a pair.\n",
       "Bad luck :( Keep trying\n",
       "Coordinates not valid"]

x = True
T = 1
while x:
    print_board(game)
    if T == 1:
        print("Player 1 turn")
        P1_old = P1
        pos, game = choose_pos(txt[0], game)
        print_board(game)
        pos2, game = choose_pos(txt[1], game)
        print_board(game)
        game, P1 = check_result(game, pos, pos2, P1, txt)
        if P1 == P1_old:
            T = 2
        if P1 + P2 == n:
            break
    
    elif T == 2:
        print("Player 2 turn")
        P2_old = P2
        pos, game = choose_pos(txt[0], game)
        print_board(game)
        pos2, game = choose_pos(txt[1], game)
        print_board(game)
        game, P2 = check_result(game, pos, pos2, P2, txt)
        if P2 == P2_old:
            T = 1
        if P1 + P2 == n:
            break
    
print(f"P1: {P1}\nP2: {P2}")
if P1 > P2:
    print("Player 1 wins")
elif P1 < P2:
    print("Player 2 wins")
else:
    print("Tie")
