arr = (input().split(" "))[1:]
stat = True
while stat:
    difArr = []
    max = 1
    possible = []
    cyc = len(arr)
    for i in range(cyc-1):
        difArr.append(int(arr[i+1])-int(arr[i]))
    for i in range(1,cyc): # length of the cycle
        addingArr = []
        for k in range(i):
            addingArr.append(int(difArr[k]))
        res = [arr[0]]
        for k in range(cyc-1):
            res.append(str(addingArr[k % i] + int(res[k])))
        if res == arr:
            max = i
            break
    print(max)
    arr = input().split(" ")
    if arr[0] == "0":
        stat = False
