b = int(input())
a = input()
a = a[1:].split("x")
coll = []
maxx = 0

for i in range(b):
    coll.append(0)
for i in range(len(a)):
    if a[i] == "1":
        coll[i%b] += 1
print(max(coll))

