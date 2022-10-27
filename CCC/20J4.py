a = input()
b = input()
found = False
for i in range(len(b)):
    if b in a:
        found = True
        break
    b = b[1:]+b[0]
if found:
    print("yes")
else:
    print("no")