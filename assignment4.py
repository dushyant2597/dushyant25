#Q1
a=[10,12,16,18]
print (a[::-1])
#Q2
a="Dushyant Learn Python"
for j in a:
    if j ==j.upper():
        print(j)
#Q3
a=input("enter the number in commas :")
b=a.split(',')
c=[]
for j in b:
    j=int(j)
    c.append(j)
print(c)
#Q4
a=input("enter the name")
if a==a[::-1]:
    print("palindrome")
else:
        print("not palindrome")

#Q5
import copy
a=[1,2,4,5]
b=copy.deepcopy(a)
print(a,b)
#deepcopy shallow copy difference
#in deep copy copied the original list
#in shallow copy change in the copied list


    
