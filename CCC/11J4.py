positionList = [[0,-1],[0,-2],[0,-3],[1,-3],[2,-3],[3,-3],[3,-4],[3,-5],[4,-5],[5,-5],[5,-4],[5,-3],[6,-3],[7,-3],[7,-4],[7,-5],[7,-6],[7,-7],[6,-7],[5,-7],[4,-7],[3,-7],[2,-7],[1,-7],[0,-7],[-1,-7],[-1,-6],[-1,-5]]

current = [-1,-5]
isDanger = False # there is danger ahead
isQ = False
result = []
while (isDanger == False and isQ == False):
    instruction = input()
    if (instruction[0] == "d"):
        for i in range (int(instruction[2:])):
            current[1] -= 1
            if (current in positionList or current[1]>=0):
                # danger
                isDanger = True
            else:
                positionList.append([current[0],current[1]])
    elif (instruction[0] == "u"):
        for i in range (int(instruction[2:])):
            current[1] += 1
            if (current in positionList or current[1]>=0):
                # danger
                isDanger = True
            else:
                positionList.append([current[0],current[1]])
    elif (instruction[0] == "l"):
        for i in range (int(instruction[2:])):
            current[0] -= 1
            if (current in positionList or current[1]>=0):
                # danger
                isDanger = True
            else:
                positionList.append([current[0],current[1]])
    elif (instruction[0] == "r"):
        for i in range (int(instruction[2:])):
            current[0] += 1
            if (current in positionList or current[1]>=0):
                # danger
                isDanger = True
            else:
                positionList.append([current[0],current[1]])
    elif (instruction[0] == "q"):
        isQ = True

    if (isQ == False):
        temp = str(current[0]) + " " + str(current[1]) + " "
        if (isDanger == False):
            temp += "safe"
        else:
            temp += "DANGER"
        result.append(temp)
for i in result:
    print(i)