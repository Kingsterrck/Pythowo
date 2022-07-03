# a = int(input())
# b = int(input())
# c = int(input())
# d = 3*a + 2*b + c
# e = int(input())
# f = int(input())
# g = int(input())
# h = 3*e + 2*f + g
# if d > h:
#     print("A")
# elif d < h:
#     print("B")
# else:
#     print("T")

# a = int(input())
# e = []
# for i in range (1,a+1):
#     b = input()
#     c,d = b.split(" ")
#     e.append(d*int(c))
# for i in e:
#     print(i)

a = int(input())  # enter the line
g = []  # total output
h = []  # within each line
for i in range(1, a + 1):
    b = input()
    c = len(b)  # length of input
    d = 1  # how many different symbols are there
    e = [b[0]]
    str_output = ""
    for l in range(c-1):
        if b[l] != b[l + 1]:  # if the symbols are different
            d = d + 1
            e.append(b[l + 1])
    for l in e:  #for each of the symbols
        str_output+=" " + str(b.count(l)) + " " + l
    h.append(str_output)
for i in h:
    print(i.lstrip())
