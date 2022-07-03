a = str(input())
b = len(a)
c = [[1,2],[3,4]]
if a.count("V")%2 == 1:
    for i in range(len(c)):
        d = c[i][0]
        c[i][0] = c[i][1]
        c[i][1] = d
if a.count("H")%2 == 1:
    d = c[0]
    c[0] = c[1]
    c[1] = d
print(c[0][0],c[0][1])
print(c[1][0],c[1][1])