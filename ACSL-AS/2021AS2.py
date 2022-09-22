a = int(input())
dic = []
indexAndNumberDic = []
for i in range(a):
    temp = input().split(" ")
    temp2 = [temp[0],0]
    temp.remove(temp[0])
    dic.append(temp)
    indexAndNumberDic.append(temp2)
output = ""
ind = input()
sym = ""
article = False
first = True
for i in ind:
    if i == " ":
        output = output.rstrip(" ")
        output += sym
        sym = ""
        first = True
    elif i == "D" or i == "I":
        sym = ". "
    elif i == "Q":
        sym = "? "
        output += "What "
        first = False
    elif i == "E":
        sym = "! "
    elif i == "T":
        if first:
            output += "The "
            first = False
        else:
            output += "the "
    elif i == "A":
        article = True
    else:
        for k in range(len(indexAndNumberDic)):
            if indexAndNumberDic[k][0] == i:
                tempIndex = indexAndNumberDic[k][1] % len(dic[k])
                temp = dic[k][tempIndex]
                if article:
                    if temp[0] == "a" or temp[0] == "e" or temp[0] == "i" or temp[0] == "o" or temp[0] == "u":
                        output += "an " + temp + " "
                    else:
                        output += "a " + temp + " "
                else:
                    if first:
                        temp = temp.capitalize()
                        first = False
                    output += temp + " "
                article = False
                indexAndNumberDic[k][1] += 1
output = output.rstrip(" ")
output += sym
print(output)