# a = int(input())
# b = int(input())
# print(a+b)
# a = 0
# b = int(input())  # 100  [1,2,3...100]
# for i in range(1,(b+1)):  # [0,1,2....99]   range(1,101)   range(1,101,2)  for(int i =1,i<101,i++){print(i)}
#     if i%2 != 0:
#         a = a + i  # a += i
# print(a)
# a = 0
# for i in range(1,101):
#     if i%2 == 0:
#         a = a + i
# print(a)
# def sum(c,d):  # c范围    d奇数偶数选择
#     a = 0
#     for i in range(1,(c+1)): # [0,1,2....99]   range(1,101)   range(1,101,2)  for(int i =1,i<101,i++){print(i)}
#         if d == "odd":
#             if i%2 != 0:
#                 a = a + i  # a += i
#         elif d == "even":
#             if i%2 == 0:
#                 a = a + i  # a += i
#     print(a)
#
#
# e = input("odd or even?")
# b = int(input())
# sum(b,e)
# def isPrime(a):
#     b = 0
#     for i in range(1,a):
#         if a%i == 0: #整除
#             b = b + 1
#     if b == 1 :    # b<1   b == 1   b>1
#         return "true"
#     else:
#         return "false"
#
#
# B = int(input())
# result = isPrime(B)
# if result == "true":
#     print("Prime")
# else:
#     print("No")

#  input number n  for  output n lines 1,3,5,7....
#  *
#  ***
#  *****
#  *******
#
#  *******
#  *****
#  ***
#  *

#    *   #i=1, 2 spaces
#   ***  #i=2, 1 space
#  *****
#
#
#  *******
#   *****
#    ***
#     *

#print in ascending order
# a = int(input("enter line number"))
# for i in range(1, a + 1):
#     for l in range (1,2*i):
#         print("*",end="")
#     print("\n")

#print in descending order
# a = int(input("enter line number"))
# for i in range(1, a+1):
#     for l in range (1,2*a+2-2*i):
#         print("*", end="")
#     print("")

a = int(input())
for i in range (1,a+1):
    for l in range(a-i):
        print(" ", end="")
    for j in range(1,2*i):
        print("*", end="")
    for k in range(a-i):
        print(" ", end="")
    print("")
