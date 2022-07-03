a = int(input())
charge = 0
max = 0
for i in range(a):
    b,c = input().split(",")
    b = int(b)
    c = int(c)
    if  c > 0:
        charge += b + c/10
        if charge > max:
            max = charge
    elif c == 0:
        charge += b
        if charge > max:
            max = charge
    else:
        if (charge + c/10 > 0):
            charge += c/10
        else:
            charge = 0
print(int(max))

