a = input()
board = []
board2 = []
for i in range(5):
    temp = []
    for k in range(6):
        temp.append(a[6*i+k])
    board.append(temp)
for i in range(6):
    temp = []
    for k in range(5):
        temp.append(board[k][i])
    board2.append(temp)
R = 0
Y = 0
for i in range(len(board)):
    for k in range(4):
        temp = [board[i][k], board[i][k+1], board[i][k+2]]
        if (temp[0] == temp[1] and temp[1] == temp[2]):
            if int(temp[0]) == 1:
                R += 1
            else:
                Y += 1
for i in range(len(board2)):
    for k in range(3):
        temp = [board2[i][k], board2[i][k+1], board2[i][k+2]]
        if (temp[0] == temp[1] and temp[1] == temp[2]):
            if int(temp[0]) == 1:
                R += 1
            else:
                Y += 1
print("R",R)
print("Y",Y)
if (R>Y):
    print("R")
elif (Y>R):
    print("Y")
else:
    print("tie")