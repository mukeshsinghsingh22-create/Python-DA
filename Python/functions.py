#functions
#def function():
#    print("mukesh")
#function()
#print(function())
#def name():
  #  return "mukesh singh"
#print(name())
#def add(a,b):
 #   return a+b
#print(add(2,3))
#def add(a,b,c,d):
 #   return a+b+c+d
#print(add(2,3,4,5))
#args
#def name(*agrs):
#    return agrs
#print(name("mukesh",332,"ankit",'kumar','nutan'))
def sum(*a):
    sum=0
    for i in a:
        sum+=i
    return sum
print(sum(1,2,3,4))
def name(**k):
    return k
print(name(father='krshna nand singh', mother='asha'))
def my_function():
    return ['mukesh','singh']
name=my_function()
print(name[0])
print(name[1])
def function(animal,name,age):
    print("i have",age,"year old",animal,"name",name)
print(function("dog", name="buddy", age=25))


a=int(input("enter number or elements::"))
elmentslist=[]
for i in range(a):
    element=input(f"enter elements {i+1}:")
    elmentslist.append(element)
print('your list is:',elmentslist)