a = input()
letterCount = 0
unique = []
wordCount = 1
capitalCount = 0
for i in a:
    if i == " ":
        wordCount +=1
    else:
        letterCount += 1
        if i.lower() not in unique:
            unique.append(i.lower())
        if i.isupper():
            capitalCount += 1
print(letterCount)
print(wordCount)
print(capitalCount)
print(len(unique))
for i in range(len(a)):
    print(a[len(a)-1-i],end="")
