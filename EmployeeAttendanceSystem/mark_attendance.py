import cv2
import pyzbar.pyzbar as pyzbar
import time
from datetime import datetime


employee_file = open('employee_details.txt','r')
employee_data = employee_file.read().split("\n")
employee_id=[]
employee_name=[]
department=[]
for i in range(len(employee_data)):
    temp=[]
    temp=employee_data[i].split(",")
    employee_id.append(temp[0])
    employee_name.append(temp[1])
    department.append(temp[2])

cap = cv2.VideoCapture(0)
attend=[]

try:
    fob=open('Attendance'+'.csv','x')
    fob.write("EmployeeID"+',')
    fob.write("Name"+',')
    fob.write("Department"+',')
    fob.write("Date"+',')
    fob.write("InTime"+'\n')
except:
    fob=open('Attendance'+'.csv','a')

def enterData(d):
    if d in employee_id:
        if d in attend:
            print("Attendance already marked")
        else:
            it=datetime.now()
            attend.append(d)
            indate = str(it.strftime("%m-%d-%Y"))
            intime = str(it.strftime("%H:%M:%S"))
            fob.write(str(d)+','+employee_name[employee_id.index(d)]+','+department[employee_id.index(d)]+','+indate+','+intime+'\n')

    else:
        print(d,"invalid employee")
    return attend 
    
print('Reading...')

def checkData(data):   
    if data in attend:
        print('Already Present')
    else:
        print('\n'+'Attendance Marked for EmployeeID:'+str(data))
        data=data.decode('utf-8')
        enterData(data)

while True:
    _, frame = cap.read()         
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)
       
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1)&0xFF == ord('g'):
        cv2.destroyAllWindows()
        fob.close()
        break
