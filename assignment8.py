#Q.No.1
def AreaOfSphere(radius):
    return(4*3.14*radius**2)
a=int(input("enter the radius."))
print(AreaOfSphere(a))


#Q.NO.2
def perf_num(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    if sum(l)==n:
        return True
for i in range(1,78):
    if perf_num(i):
        print(i,"is perfect number")    

#Q.NO.3
def multi_table(n):
    for i in range(1,11):
        print(n,'*',i,"=",n*i)
n=int(input("enter the number:"))
multi_table(n)

#Q.NO.4
def power(base,exp):
    if(exp==1):
        return base
    if(exp!=1):
        return (base*power(base,exp-1))
base=int(input('enter the base:'))
exp=int(input('enter the exponent:'))
print(power(base,exp))
