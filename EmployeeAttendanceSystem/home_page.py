from tkinter.constants import RIDGE
import tkinter as tk 
import pandas as pd
from tkinter import Frame, ttk, messagebox
from tkinter import *
import pandas as pd
import subprocess
import sys
from tkinter import PhotoImage


window = tk.Tk()
window.title('Employee Attendance Portal')
window.geometry('900x600') 

EmployeeID = tk.StringVar()      
Department = tk.StringVar()
Date = tk.StringVar() 

title = tk.Label(window,text="Employee Attendance System",bd=10,relief=tk.GROOVE,font=("times new roman",40),bg="#66f999",fg="black")
title.pack(side=tk.TOP,fill=tk.X)
Manage_Frame=Frame(window,bg="#66f999")
Manage_Frame.place(x=0,y=80,width=1500,height=600)


# bg_image_path = "C:\Masters\sem-4\ASE\Project\EmployeeAttendanceSystem\QR_L-1.png" 
# bg_image = PhotoImage(file=bg_image_path)
# canvas = tk.Canvas(window, width=1500, height=600)
# canvas.pack(fill="both", expand=True)
# canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)


ttk.Label(window, text = "Search Options for the Employee",background="#66f999", foreground ="black",font = ("Verdana 15 underline")).place(x=125,y=200)
ttk.Label(window, text = "Enter one or more of the search parameters",background="#66f999", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=250)

ttk.Label(window, text = "EmployeeID",background="#66f999", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=300)
combo_search=ttk.Entry(window,textvariable=EmployeeID,width=10,font=("times new roman",13),state='readonly')
combo_search['state']='normal'
combo_search.place(x=300,y=300)

ttk.Label(window, text = "Department",background="#66f999", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=350)
combo_search=ttk.Combobox(window,textvariable=Department,width=15,font=("Times New Roman",12),state='readonly')
combo_search['values']=('Manager','Developer','HR','Tester')
combo_search.place(x=300,y=350)

ttk.Label(window, text = "Date (MM-DD-YYYY)",background="#66f999", foreground ="black",font = ("Times New Roman", 14)).place(x=100,y=400)
combo_search=ttk.Entry(window,textvariable=Date,width=10,font=("times new roman",13),state='readonly')
combo_search['state']='normal'
combo_search.place(x=300,y=400)

def scanner():
    subprocess.call(["python","mark_attendance.py"])
def search():
    employee_data=pd.read_csv("Attendance.csv")
    emp=EmployeeID.get()
    dept=Department.get()
    date=Date.get()
    if(emp != '' and dept == '' and date == ''):
        result=employee_data.loc[employee_data['EmployeeID']== int(emp)]
    elif(emp == '' and dept != '' and date == ''):
        result=employee_data.loc[employee_data['Department']==dept]
    elif(emp == '' and dept == '' and date != ''):
        result=employee_data.loc[employee_data['Date']==date]
    elif(emp != '' and dept != '' and date == ''):
        result=employee_data.loc[employee_data['EmployeeID'] == int(emp)]
        result=result.loc[result['Department']==dept]
    elif(emp != '' and dept == '' and date != ''):
        result=employee_data.loc[employee_data['EmployeeID'] == int(emp)]
        result=result.loc[result['Date']==date]
    elif(emp == '' and dept != '' and date != ''):
        result=employee_data.loc[employee_data['Department']==dept]
        result=result.loc[result['Date']==date]
    elif(emp != '' and dept != '' and date != ''):
        result=employee_data.loc[employee_data['EmployeeID'] == int(emp)]
        result=result.loc[result['Department']==dept]
        result=result.loc[result['Date']==date]
    else:
        messagebox.showwarning("Warning", "No Data Found!!")
    if(result.empty):
        messagebox.showwarning("Warning", "No Data Found!!")
    else:
        window_new = tk.Tk()
        window_new.geometry('900x600')
        window_new.title('Search Results')
        title = tk.Label(window_new,text="Employee Attendance",bd=10,relief=tk.GROOVE,font=("times new roman",40),bg="#66f999",fg="black")
        title.pack(side=tk.TOP,fill=tk.X)
        Manage_Frame=Frame(window_new,bg="#66f999")
        Manage_Frame.place(x=0,y=80,width=900,height=600)
        txt=Text(window_new)
        txt.pack()
        class PrintToTXT(object):
            def write(self,s):
                txt.insert(END,s)
            def flush(self):
                pass
        sys.stdout=PrintToTXT()
        print(result)

search_button = tk.Button(window,width=13, text="search",font=("Times New Roman", 12),command=search,bd=2,relief=RIDGE)
search_button.place(x=150,y=450)

scanner_button = tk.Button(window,width=20, text="Click to open QR Scanner",font=("Times New Roman", 12),command=scanner,bd=2,relief=RIDGE)
scanner_button.place(x=150,y=150)

Manag_Frame=Frame(window,bg="#66f999")
Manag_Frame.place(x=480,y=80,width=450,height=530)
window.mainloop()
