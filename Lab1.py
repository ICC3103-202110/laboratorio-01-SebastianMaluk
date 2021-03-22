import random

#n = int(input("Cuantas cartas van a jugar?"))
n = 8
cards = []
for i in range(1, n+1):
    cards.append(i)
    cards.append(i)
random.shuffle(cards)
t = (2*n)**(1/2)
t = int(t)
tablero = []
print(cards)
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

x = True
while x:
    print("Juega J1")
    vuelta = "1, 1" #str(input("Qué carta quiere dar vuelta? fila, columna\n"))
    pos = vuelta.split(", ")
    pos[0] = int(pos[0])
    pos[1] = int(pos[1])
    print(pos)
    ast[pos[0]][pos[1]] = tablero[pos[0]][pos[1]]
    for i in ast:
        print(*i)
    print("")
    vuelta2 = "2, 2" #str(input("Dónde está su par? fila, columna\n"))
    pos2 = vuelta2.split(", ")
    pos2[0] = int(pos2[0])
    pos2[1] = int(pos2[1])
    ast[pos2[0]][pos2[1]] = tablero[pos2[0]][pos2[1]]
    for i in ast:
        print(*i)
    x = False
