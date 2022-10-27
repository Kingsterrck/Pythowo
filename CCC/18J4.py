import copy
a = int(input())
arr = []
for i in range (a):
    tempArr = input().split(" ")
    arr.append(tempArr)

isCorrect = True

for i in range(a - 1):
    if int(arr[0][i]) > int(arr[0][i + 1]):
        isCorrect = False
for i in range(a - 1):
    if int(arr[i][0]) > int(arr[i + 1][0]):
        isCorrect = False

while not isCorrect:
    arr2 = copy.deepcopy(arr)
    for i in range (a):
        tempArr = []
        for k in range (a):
            tempArr.append(int(arr2[a-k-1][i]))
        arr[i] = copy.deepcopy(tempArr)

    isCorrect = True
    for i in range(a - 1):
        if int(arr[0][i]) > int(arr[0][i + 1]):
            isCorrect = False
    for i in range(a - 1):
        if int(arr[i][0]) > int(arr[i + 1][0]):
            isCorrect = False
for i in arr:
    for k in range(a):
        print(i[k], end=" ")
    print()