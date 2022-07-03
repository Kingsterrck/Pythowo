a = input()
a=a.lower()
count = 0
detected = False
cons = [" ",".",",",":",";","'",'"',"!","?"]
while (a.find("and") != -1):
    detected = False
    temp = a.find("and")
    if (temp == 0):
        if (a[temp+3] in cons):
            detected = True
    elif (temp +3 == len(a)):
        if (a[temp-1] in cons):
            detected = True
    else:
        if (a[temp-1] in cons and a[temp+3] in cons):
            detected = True
    if detected == True:
        count += 1
        a = a[temp+3:]
    else:
        a = a[temp+3:]
print(count)