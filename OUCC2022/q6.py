a = int(input())
b = int(input())
count = 0
for i in range(a,b+1):
    # if (float(int(i^0.5)) == float(i^0.5)):
    #     count += 1
    for k in range(1000):
        if (k*k == i):
            count += 1
            break
print(count)
