a = input()
b = ""
stat = False
for i in a:
    if (i == "0"):
        b+="1"
    else:
        b+="0"
        stat = True
finished = False
k = len(b)-1
if (stat == False):
    b = "1"+len(b)*"0"
    finished = True
while finished == False:
    if (b[k] == "0" and k != 0):
        #b[k] = "1"
        b = b[0:k] + "1" + b[k+1:]
        finished = True
    else:
        if k == 0:
            b = "1"+b
            finished = True
        else:
            #b[k] = "0"
            b = b[0:k] + "0" + b[k+1:]
            k-=1
ind = b.find("1")
print(b[ind:])