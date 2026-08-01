#n=5
#fact=1
#for i in range(5,0,-1):
    #fact=fact*i
#print(fact)
#num=int(input("enter a number"))
#fact=1
#for i in range(1,num+1):
    #fact=fact*i

#print("factorial number is::",fact)

num=int(input("enter a number::"))
fact=1
i=1
while i<=num:
    fact=fact*i
    i+=1
print("factorial :",fact)