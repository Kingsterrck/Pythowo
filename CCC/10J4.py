arr = input().split(" ")
while True:
    if (int(arr[0]) == 0):
        break
    arr = arr[1:]
    longest = 0
    for i in range(1,len(arr)): # length of repetition
        changeArr = []
        for k in range (i):
            changeArr.append(int(arr[k+1])-int(arr[k]))
        newArr = [int(arr[0])]
        for k in range(len(arr)-1):
            newArr.append(newArr[k]+changeArr[k%len(changeArr)])
        same = True
        for k in range(len(arr)):
            if (int(arr[k]) != newArr[k]):
                same = False
        if (same):
            longest = i
            break
    print(longest)
    arr = input().split(" ")