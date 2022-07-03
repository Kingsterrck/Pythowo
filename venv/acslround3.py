# a = int(input("enter rows: "))
# for i in range (1, a+1):
#     for l in range (1, 2*i):
#         print("*", end="")
#     print("")
# for i in range (1,a+1):
#     for l in range (1, 2*a-2*i):
#         print("*", end="")
#     print("")
# for i in range (1,a+1):
#     for l in range(a-i):
#         print(" ", end="")
#     for j in range(1,2*i):
#         print("*", end="")
#     for k in range(a-i):
#         print(" ", end="")
#     print("")

#------------------#

a = int(input("enter row"))
b = int(input("enter column"))
c = list(input("array 1:"))
d = list(input("array 2:"))
e = list(input("array 3:"))

f = list(c[2])#one on the right
g = list(c[2*b])#one below
f.append(d[2])
g.append(d[2*b])
f.append(e[2])
g.append(e[2*b])

h = max(f)
i = max(g)

if h > i: #first step to the right
    j = min(f)
    f.clear()
    g.clear()
    f.append(c[4])#one on the right
    g.append(c[2*b+2])#one below
    f.append(d[4])
    g.append(d[2 * b + 2])
    f.append(e[4])
    g.append(e[2 * b + 2])
    h = max(f)
    i = max(g)
    if h > i:
        j = j + min(f)
    else:
        j = j + min(g)
else:
    j = min(g)
    f.clear()
    g.clear()
    f.append(c[2*b+2])
    g.append(c[4*b])
    f.append(d[2*b+2])
    g.append(d[4*b])
    f.append(e[2*b+2])
    g.append(e[4*b])
    h = max(f)
    i = max(g)
    if h > i:
        j = j + min(f)
    else:
        j = j + min(g)

print(j)