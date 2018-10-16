#Q.NO.1
from datetime import date
import calendar
my_date=date.today()
print(calendar.day_name[my_date.weekday()])


#Q.NO.2
import webbrowser
import time

total_breaks=3
break_count=0
while(break_count<total_breaks):
    print("this is program on:"+time.ctime())
    time.sleep(10)
    webbrowser.open("https://www.youtu.be/9bGyzj7Y")
    break_count+=1
    
    
#Q.NO.3
import os
path=r'C:\Users\HP\Programs\Python\Python36\xyz12'
files=os.listdir(path)
i=1

for file in files:
    os.rename(os.path.join(path,file),os.path.join(path,str(i)+'.jpg'))

    i+=1
