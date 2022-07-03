wid, hei = input().split()
wid = int(wid)
hei = int(hei)
puz = []
for i in range(hei):
    temp = input()
    puz.append(temp)
puz2 = []
for i in range(wid):
    temp = ""
    for k in range(hei):
        temp += puz[k][i]
    puz2.append(temp)
count = 0
for i in range(hei):
    current = 0
    for k in puz[i]:
        if k == "X":
            current = 0
        else:
            current += 1
            if current > count:
                count = current
for i in range(wid):
    current = 0
    for k in puz2[i]:
        if k == "X":
            current = 0
        else:
            current += 1
            if current > count:
                count = current

print(count)