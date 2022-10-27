res = []
for k in range(5):
    a = input().split()
    location = len(a[0])-int(a[1])
    result = ""
    for i in range(location):
        temp = a[0][i]
        if (int(temp) + int(a[0][location]) >= 10):
            result += str(int(temp) + int(a[0][location]) - 10)
        else:
            result += str(int(temp) + int(a[0][location]))
    result += a[0][location]
    for i in range (location+1,len(a[0])):
        temp = abs(int(a[0][i])-int(a[0][location]))
        result += str(temp)
    res.append(result)
for i in res:
    print(i)