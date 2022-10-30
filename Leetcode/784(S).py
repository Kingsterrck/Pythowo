def letterCasePermutation(s):
    strList = []
    for i in range(len(s)):
        currentChar = s[i]
        if len(strList) == 0:
            if currentChar.isalpha():
                strList.append(currentChar.upper())
                strList.append(currentChar.lower())
            else:
                strList.append(currentChar)
        else:
            if currentChar.isalpha():
                for k in range(len(strList)):
                    strList[k] += currentChar.upper()
                for k in range(len(strList)):
                    temp = strList[k]
                    strList.append(temp[0:len(temp)-1]+currentChar.lower())
            else:
                for k in range(len(strList)):
                    strList[k] += currentChar
    return strList

print(letterCasePermutation("3z4"))