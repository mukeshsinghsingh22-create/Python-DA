#recursion
# def num(n):
#     if n<=0:
#         return 0
#     else:
#         print(n)
#         return num(n-1)
# print(num(10))
# def num(n):
#     if n<=0:
#         return
#     else:
#         num(n-1)
#         print(n)
#         return 0
# num(7)
# def num(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*num(n-1)
# print(num(10))
#decor
# def decor(func):
#     def wrap():
#         print("Welcome")
#         print(func().upper())
#         print("thank you")
#     return wrap
# @decor
# def function():
#     return "hi welcome to the Python AI classes"
# function()
# def muk(m):
#     def kum():
#         return m().upper()
#     return kum
# @muk
# def func():
#     return "hello"
# print(func())
# @muk
# def func1():
#     return "my name is mukesh singh"
# print(func1())
# def changecase(n):
#     def changecase(func):
#         def muk():
#             if n==1:
#                 a=func().upper()
#             else:
#                 a=func().lower()
#             return a
#         return muk
#     return changecase
# @changecase(0)
# def function():
#     return "my name is mukesh singh"
# print(function())
#prime no:
# def prime(n,i=2):
#     if n<=1:
#         return False
#     if i*i>n:
#         return True
#     if n%i==0:
#         return False
#     return prime(n,i+1)
# num=int(input("enter a number here::"))
# if prime(num):
#     print("prime no")
# else:
#     print("Not a prime no")

# def primeno(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#         return True
    
# print(primeno(3))
def armstrong(n,m):
    if n==0:
        return 0
    return(n%10)**m+armstrong(n//10,m)
num=int(input("Enter a number here::"))
s=len(str(num))
if armstrong(num,s)==num:
    print("Armstrong number")
else:
    print("not a Armstrong number")