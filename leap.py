#Q1 
year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year")
else:
    print("The year isn't a leap year")
#Q2
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
if (l==b):
    print("square")
else:
    print("rectangle")
#Q3
a=int(input("enter first age ="))
b=int(input("enter second age ="))
c=int(input("enter third age="))
if a>=b and b>=c:
    print("oldest age",a)
elif b<=a and c<=b:
    print("oldest age",b)
elif c<=a and c<=b:
    print("oldest age",c)
          
else:
    print("all are equal")
    
#q4
age= int(input("enter your age"))
sex=input("enter your sex(M orF):").upper()
marital_status =input("enter the marital ( Y or N):").upper()
if sex=="F":
    print("urban areas")
else:
    if age>=20 and age<40:
        print("Work anywhere")
    elif age>=40 and age<60:
        print("urban areas")
    else:
        print("error")
#Q5
quantatity=int(input("Enter quantatity"))
cost =(quantatity*100)
if cost>1000: 
    discount=(cost)*.10
    cost-=discount

    print("the cost of item is :",cost)
else:
    print("the cost of item is:",cost)
#Q6
for i in range(10):   
     n=int(input("enter a number :"))
     print("number",i+1,"is",n)
#Q7
while True:
    print("infinite loop")
#Q8
n=int(input("enter total no. of integer:"))
1=[]
for i in range(n):
    n1=int(input("enter integer: "))
    1.append(n1)
print ("first list is",1)
12=[]
for j in 1 :
    s=j**2
    12.append(s)
print("list contaning square of integers is",12)
#Q9
1=[1,"dushyant",2.3]
11=[]
12=[]
13=[]
for i in 1:
    if type(i)==int:
        11.append(i)
        print(11)
    elif type(i)==float:
        12.append(i)
        print(12)
    else:
        13.append(i)
        print(13)
#Q10
1=[]
for i in range(1,101)
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            1.append[i]
    print(1)
#Qno. 11
for i in range(1,5):
    print("*"*i)
#Qno. 12
n=int(input("enter tootal no of elements"))
1=[]
for i in range(n):
    n1=int(input("enter number:"))
    1.append(n1)
 print(1)
 n2=int(input("enter element to be searched:"))
 for j in 1:
     if j==n2:
         k=1.index(j)
         1.pop(k)
 print(1)
    

    



    
