#disranum
#whileloop
'''
num=int(input("enter a nummber::"))
m=num
length=len(str(num))
sum_val=0
while num>0:
    digit=num%10
    sum_val+=digit**length
    num=num//10
    length -= 1

if sum_val==m:
   print("is a disarum number")
else:
   print("is not a disarum number")
'''
#forloop
n=int(input("enter a number::"))
s=str(n)
sum=0
for i in range(len(s)):
   digit=int(s[i])
   sum+=digit**(i+1)
if sum==n:
   print("is a disarium number")
else:
   print("not a disarium number")
