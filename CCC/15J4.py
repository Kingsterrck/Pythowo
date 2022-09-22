a = int(input())
ppl = []
for i in range(a):
    b = input().split(" ")

    if b[0] == "S":
        for k in range(len(ppl)):
            if ppl[k][0] == int(b[1]):
                ppl[k][1] = False

    if b[0] == "W":
        for k in range(len(ppl)):
            if ppl[k][1] == True:
                ppl[k][2] += int(b[1])
    else:
        for k in range(len(ppl)):
            if ppl[k][1] == True:
                ppl[k][2] += 1

    found = False
    if b[0] == "R":
        # b[1] is the name of the person
        for k in range(len(ppl)):
            if ppl[k][0] == int(b[1]):
                ppl[k][1] = True
                found = True
        if not found:
            ppl.append([int(b[1]),True,0])

for i in range(len(ppl)):
    min = 0
    for k in range(len(ppl)):
        if (ppl[k][0] < ppl[min][0]):
            min = k
    if not ppl[min][1]:
        print(str(ppl[min][0]) + " " + str(ppl[min][2]))
    else:
        print(str(ppl[min][0]) + " -1")
    ppl.remove(ppl[min])