#Q1 create a list with user defined input
mylist=[]
no=int(input("enter the length of list"))
print (no)
for j in range(no):
    data=int(input())
    mylist.append(data)
    print(mylist)
#Q2 add the following list to above created list
a=["google","apple"]
b=["facebook","microsoft","tesla"]
c=a+b
print(c)
#Q3 Count the number of time an object occurs in a list.
d=["Apple",56,"mango","mango"]
d=d.count('mango')
print(d)
#Q4
a=[123,2,455,35,7,67,23,54,345,6]
a.sort()
print(a)
#Q5
arr1=[10,5,4,8,9,11]
arr2=[12,2,6,76,13,14]
c=arr1+arr2
c.sort()
print(c)
#Q6
a=[1,56,23,44,21,66]
count_odd = 0
count_even = 0
for i in a:
    if (i%2)==0:
        count_even+=1
    else:
       count_odd+=1
       print(count_even)
       print(count_odd)
#Q7
b=('z','a','d','e','f')
print (b[::-1])
#Q8
a =(9,5,6,7,8)
min(a)
max(a)

#Q9
s="dushyant"
s.upper()
#Q10
str=("ramesh")
str.replace("ramesh","dushyant")










        
        
    
        

