# A = [1,3,5,2,5,7,8,9]
# b = len(A)
# c = 99999999 #minimum
# d = 0 #maximum
# for i in range(b):
#     if A[i] > d:
#         d = A[i]
#     if A[i] < c:
#         c = A[i]
# print(c)
# print(d)

# a = int(input())
# b = int(input())
# c = int(input())
# d = a + 2*b + 3*c
# if d >= 10:
#     print("happy")
# else:
#     print("sad")

target = int(input()) #target population
b = int(input()) #first day infectant
infectivity = int(input()) #infectivity
d = b #d is total number
d = b + b*infectivity #after first day
day = 1 #days
a = b*infectivity #current day infected
while d <= target:
    d = d + a*infectivity
    a = a*infectivity
    day += 1
print(day)

