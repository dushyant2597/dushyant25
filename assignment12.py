#Q.NO.1
class Circle:
    def __init__(self,r):
        self.radius=r
    def getArea(self):
        return self.radius**2*3.14
    def getCircumference(self):
        return 2*self.radius*3.14
NewCircle=Circle(10)
print(NewCircle.getArea())
print(NewCircle.getCircumference())

#Q.NO.2
class Student():
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print(self.name)
        print(self.rollno)
    def setAge(self,age):
        self.age=age
        print(self.age)
    def setMarks(self,marks):
        self.marks=marks
        print(self.marks)
Stu_Info=Student('sam',1)
Stu_Info.display()
Stu_Info.setAge(20)
Stu_Info.setMarks(89)
#Q.No.3
class Temperature():
    cel=float(input("enter temperature in celsius:"))
    feh=float(input("enter temperature in farenheit:"))
    def __init__(self):
     pass
    def convert_cel(self):
        f=self.cel*(9/5)+32
        print("temperature in farenheit",f)
    def convert_feh(self):
        c=(self.feh-32)*(5/9)
        print("temperature in celsius",c)
t=Temperature()
t.convert_cel()
t.convert_feh()

#Q.NO.4
class Movie():
    def __init__(self):
        pass
    def display(self,movieName,artistName,yearofRelease):
        self.m= movieName
        self.a= artistName
        self.y =yearofRelease
        print(self.m,self.a,self.y)
    def update(self,movieName,artistName,yearofRelease):
        self.m=  input("enter the movie name:")
        self.a = input("enter the artist name:")
        self.y = input("enter the year of release:")
        print(self.m,self.a,self.y)
y=Movie()
y.display("dabbang:","salman khan","22 june 2015")
t=Movie()
t.update("m","a","y")


#Q.No.5
class Animal:
    def animal_attribute(self,name,attribute):
        print(name,"has atttribute",attribute)

class Tiger(Animal):
    def show_attribute(self,name,attribute):
        print(name,"has atttribute",attribute)
T=Tiger()
T.show_attribute("tiger","roar")


#Q.NO.6
class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'
a=A()
b=B()
print(a.f(),b.f())
print(a.g(),b.g())

#Q.NO.7
class Shape:
    length=float()
    breadth=float()
    def area(self,l,b):
        self.length=l
        self.breadth=b
        return self.length*self.breadth
class Rectangle(Shape) :
    def display_area(self):
        l=float(input("enter length of rectangle:"))
        b=float(input("enter breadth of rectangle:"))
        print("area of rectangle:",self.area(l,b))
r=Rectangle()
r.display_area()
class Square(Shape) :
    def display_area(self):
        a=float(input("enter side of square:"))
        print("area of square:",self.area(a,a))
s=Square()
s.display_area()
