def func(n):
    if (n == 0):
        return 0
    elif (n % 2 == 0):
        func(n/2)
    else:
        print("*", end="")
        func(n-1)

a = int(input())
func(a)