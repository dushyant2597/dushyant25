#Q.NO.1
dict={}
for i in range (int(input("Enter the key-value pairs you want to input:"))):
    dict[i]=i
n=int(input("Enter the value for which the key you want to search:"))
for key in dict.keys():
    if dict[key]==n:
        print(key)
    else:
        print("key not found!!! Error")
print("total elements present are:",dict[i])


#Q.NO.2

students={
          "john":{"data science":80,"c++":70,"ML":80,"java":90},
          #"ram":{"data science":86,"c++":96,"ML":80}
          }
stu_name=input("Enter the name of student you want to search:").title()
if stu_name in students:
    print("stu_name")
    for key,value in students[stu_name].items():
        print(key,value)
else:
    print("student not in the list")
