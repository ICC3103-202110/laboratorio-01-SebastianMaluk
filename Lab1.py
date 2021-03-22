import random

#n = int(input("Cuantas cartas van a jugar?"))
n = 50
cards = []
for i in range(1, n+1):
    cards.append(i)
    cards.append(i)
random.shuffle(cards)
t = (2*n)**(1/2)
t = int(t)
tablero = []

for i in range(0, len(cards), t):
    tablero.append(cards[i: i+t])
for i in tablero:
    print(*i)

print("")

P1 = 0
P2 = 0
ast= []
for i in tablero:
    row = []
    for j in i:
        row.append("*")
    ast.append(row)
for i in ast:
    print(*i)
print("")
x = True
T = 1


def choose_pos(z, ast):
    try:
        vuelta = str(input(z + "\n"))
        pos = vuelta.split(",")
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
        ast[pos[0]][pos[1]] = tablero[pos[0]][pos[1]]
        return pos, ast
    except:
        print("Coordinadas no válidas")
        choose_pos(z, ast)


while x == True:
    if T == 1:
        print("Juega J1")
        P1_old = P1
        z = "Qué carta quiere dar vuelta? fila,columna"
        pos, ast = choose_pos(z, ast)
        for i in ast:
            print(*i)
        print("")
        z = "Dónde está su par? fila,columna"
        pos2, ast = choose_pos(z, ast)
        for i in ast:
            print(*i)
        if ast[pos[0]][pos[1]] == ast[pos2[0]][pos2[1]]:
            print("Correcto! Encontraste un par.\n")
            P1 += 1
            ast[pos[0]][pos[1]] = " "
            ast[pos2[0]][pos2[1]] = " "
        else:
            print("Mala suerte :( Sigue intentando\n")
            ast[pos[0]][pos[1]] = "*"
            ast[pos2[0]][pos2[1]] = "*"
        if P1 == P1_old:
            T = 2
        if P1 + P2 == 50:
            break
    if T == 2:
        print("Juega J2")
        P2_old = P2
        z = "Qué carta quiere dar vuelta? fila,columna"
        pos, ast = choose_pos(z, ast)
        for i in ast:
            print(*i)
        print("")
        z = "Dónde está su par? fila,columna"
        pos2, ast = choose_pos(z, ast)
        for i in ast:
            print(*i)
        if ast[pos[0]][pos[1]] == ast[pos2[0]][pos2[1]]:
            print("Correcto! Encontraste un par.\n")
            P2 += 1
            ast[pos[0]][pos[1]] = " "
            ast[pos2[0]][pos2[1]] = " "
        else:
            print("Mala suerte :( Sigue intentando\n")
            ast[pos[0]][pos[1]] = "*"
            ast[pos2[0]][pos2[1]] = "*"
        if P2 == P2_old:
            T = 1
        if P1 + P2 == 50:
            break
    for i in ast:
        print(*i)

print(f"J1: {P1}\nJ2: {P2}")
if P1 > P2:
    print("Ganó el jugador 1")
elif P1 < P2:
    print("Ganó el jugador 2")
else:
    print("Empate")
