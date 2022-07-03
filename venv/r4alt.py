list4 = input().split(" ")
total = []
sum = 0
for i in list4:
    for j in list4:
        if i[1] == j[0]:
            temp = int(str(i)+str(j[1]))
            if temp not in total and i[0] != j[1] and i[0] != i[1] and j[0] != j[1]:
                total.append(temp)
        if j[1] == i[0]:
            temp = int(str(j)+str(i[1]))
            if temp not in total and i[1] != j[0] and i[0] != i[1] and j[0] != j[1]:
                total.append(temp)
for i in total:
    sum += i
print(sum)


sum = (a + b)*100/2

for i in range(1,101):
