a = input().split(" ")
b = max(a)
for i in range(int(b)):
    for k in a:
        if (int(b)-i <= int(k)):
            if k == a[2]:
                print("x", end="")
            else:
                print("x ",end="")
        else:
            print("  ",end="")
    print("")