for k in range(5):
    a = input().split(" ")
    count = 0
    for i in range (len(a[0])-int(a[1])+1):
        count += int(a[0][i:i+int(a[1])])
    print(k+1,end=". ")
    print(count)