a = int(input())  # enter
g = []  # total output
for i in range(a):
    b = input()
    c = len(b)  # length of input
    d = 0  # how many consecutive symbols
    e = b[0]
    str_output = ""
    for l in b:
        if l==e:  # if the symbols are the same
            d = d + 1
        else:
            str_output += " "+str(d)+ " "+ e
            e = l
            d = 1
    str_output += " " + str(d) + " " + e
    g.append(str_output.lstrip().rstrip())
for i in g:
    print(i)