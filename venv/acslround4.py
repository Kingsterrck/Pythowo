data = input() #the initial input
length = len(data)
sumlist = []
list2 = []

for i in range (0,length):
    if data[i] != " ":
        sumlist.append(int(data[i]))
maximum = max(sumlist)
length2 = len(sumlist)

for i in range (0,length2, 2):
    temp1 = sumlist[i]
    temp2 = sumlist[i+1]
    temp3 = str(temp1)+str(temp2)
    list2.append(int(temp3))

pos1 = []

for i in range (1,maximum+1): #each of the number as a starting point
    for l in range(1,maximum+1): #each of the number as the second spot
        route1 = int(str(i)+ str(l)) #every possible route
        for r in list2:
            if route1 == r:
                pos1.append(int(route1))
#now, pos1 is all the possibilities for the first line

secondstart = []
for i in pos1:
    temp = str(i)
    temp1 = temp[1]
    secondstart.append(int(temp1))

secondstart.sort()
helpeli = []
repeat = False

for i in secondstart: #eliminate repetitive terms
    for r in helpeli:
        if i == r:
            secondstart.remove(i)
            repeat = True
    if repeat == False:
        helpeli.append(i)

total = 0
# ----------------
list4 = [12,23,34,41,31]
total = []
sum = 0
for i in list4:
    for j in list4:
        if i[1] == j[0]:
            temp = int(str(i)+str(j[1]))
            if temp not in total:
                total.append(temp)
        if j[1] == i[0]:
            temp = int(str(j)+str(i[1]))
            if temp not in total:
                total.append(temp)
for i in total:
    sum =+ total
print(sum)



# ----------------
for i in secondstart: #each of the number as the second starting point
    for l in range(1,maximum+1): #each of the number as the third spot
        route2 = int(str(i)+ str(l)) #every possible route
        if route2 not in list2:   #  12   list2=[12,34,41,31,23]
            list2.append(route2)


        for r in list2:
            if route2 == r:
                #here we need to find the value in list2 that has the same ending as i
                for k in list2:
                    temp3 = str(k)
                    temp4 = int(temp3[0])
                    if temp4 == i:
                        temp = int(str(k)+str(l))
                        total = total + temp
print(total)
#问题：给定一个有向图，找出所有长度为 2 的简单路径，并输出这些路径之和。
# #例如，在下图中，从顶点 1 开始，长度为 2 的路径为 123。从顶点 2 开始，路径为 231 和 234。从顶点 3 开始， 路径为 341 和 312。从顶点 4 开始，路径为 412。因此路径之和为 123 + 231 + 234 + 341 + 312 + 412 = 1653.
#Input	Expected Output
12 23 34 41 31     123  234 341 412 312
1653
12 23 34 41 13 32     =>  12 23    34 41    41 13
1789
76 75 12 13 23 31 34 41 56
2956
34 45 56 63 64 61 13
4515
12 21 13 15 53 33
581