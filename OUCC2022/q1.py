a = input()
b = ""
for i in a:
    if i == "A":
        b+= "T"
    elif i == "T":
        b += "A"
    elif i == "C":
        b += "G"
    elif i == "G":
        b += "C"
print(b)