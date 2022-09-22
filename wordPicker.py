stat = True
while stat:
    a = input()
    res = []
    temp = ""
    if a == "end":
        stat = False
    else:
        for i in range(len(a)):
            if a[i:i+1].isalpha():
                temp += a[i:i+1]
            else:
                if temp != "":
                    res.append(temp)
                    temp = ""
        for i in res:
            print(i)