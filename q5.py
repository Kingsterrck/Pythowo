a = input().split(",")
print("E A D G B E")
print("===========")
for i in range(5):
    for k in range (6):
        if (int(a[k]) == i+1):
            print("x ",end="")
        else:
            print("| ",end="")
    print("")
    print("-----------")