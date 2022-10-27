a = input().split(" ")
start = eval("0o"+a[0])
delta = eval("0o"+a[1])
triArr = [[int(a[0])]]
for i in range(1,int(a[2])+1):
    tempArr = []
    for k in range(i+1):
        start += delta
        tempArr.append(start)
    triArr.append(tempArr.copy())
count = 0
for i in triArr[int(a[2])-1]:
    count2 = 0
    temp = oct(i)[2:]
    for k in temp:
        count2 += int(k)
    count += count2
print(count)