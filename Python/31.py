# n=int(input("enter a no::"))
# for i in range(1,n+1):
#     if i%3==0 or i%5==0:
#         print("fizz and buzz")
#     else:
#         print("invalid no",i)
# x=5
# y=0
# print(x/y)
# try:
#     x=5
#     y=0
#     print(x/y)
# except:
#     print("this is an error")
# else:
#     print("code is perfectly executed")
# finally:
#     print("important code")

# try:
#     x=5
#     y=0
#     print(x/y)
# except Exception as e:
#     print(e)
# else:
#     print("code is perfectly executed")
# finally:
#     print("important code")

x="mukesh"
y=8
z= 0
try:
    print(x)
    print(y)
    print(y/z)
except NameError as n:
    print(n)
except ZeroDivisionError as e:
     print(e)
# except:
#     print("something else wrong")
else:
     print("no error")
finally:
   print("important code")

# try:
#   x = float("hello")
# except ValueError:
#   print("The value has wrong format")
# except:
#   print("Something else went wrong")

# try:
#     x=8
#     y=2
#     print(x/y)
# except ZeroDivisionError as e:
#     print(e)
# except:
#     print("this is an error")
# else:
#     print("there is no error")
# finally:
#     print("important code")

