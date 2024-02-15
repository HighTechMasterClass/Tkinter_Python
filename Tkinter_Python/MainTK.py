from tkinter import *
from tkinter import ttk
from Database import Data
from tkinter import messagebox

Database=Data("Student.db")
obj=Tk()
obj.title("Student Management System")
obj.geometry("1300x700+0+0")
obj.config(bg="Tan")
obj.state("zoomed")

name=StringVar()
dob=StringVar()
gender=StringVar()
age=StringVar()
department=StringVar()
year=StringVar()
email=StringVar()
contact=StringVar()
address=StringVar()

#Entries Frame
entry_frame=Frame(obj,bg="Teal")
entry_frame.pack(side=TOP,fill=X)

title=Label(entry_frame,text="Student Management System",font=("Calibri",22,"bold"),bg="Teal",fg="white")
title.grid(row=0,column=0,columnspan=2,padx=10,pady=20,sticky="w")

labelName=Label(entry_frame,text="Name",font=("Ruby",13),bg="Teal",fg="white")
labelName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
textName=Entry(entry_frame,textvariable=name,font=("Ruby",13),width=30)
textName.grid(row=1,column=1,padx=10,sticky="w")

labelDob=Label(entry_frame,text="D.O.B",font=("Ruby",13),bg="Teal",fg="white")
labelDob.grid(row=1,column=2,padx=10,pady=10,sticky="w")
textDob=Entry(entry_frame,textvariable=dob,font=("Ruby",13),width=30)
textDob.grid(row=1,column=3,padx=10,sticky="w")

labelGender=Label(entry_frame,text="Gender",font=("Ruby",13),bg="Teal",fg="white")
labelGender.grid(row=2,column=0,padx=10,pady=10,sticky="w")
comboGender=ttk.Combobox(entry_frame,textvariable=gender,font=("Ruby",13),width=28,state="readonly")
comboGender['values']=('Male','Female')
comboGender.grid(row=2,column=1,padx=10,sticky="w")

labelAge=Label(entry_frame,text="Age",font=("Ruby",13),bg="Teal",fg="white")
labelAge.grid(row=2,column=2,padx=10,pady=10,sticky="w")
textAge=Entry(entry_frame,textvariable=age,font=("Ruby",13),width=30)
textAge.grid(row=2,column=3,padx=10,sticky="w")

labelDepartment=Label(entry_frame,text="Department",font=("Ruby",13),bg="Teal",fg="white")
labelDepartment.grid(row=3,column=0,padx=10,pady=10,sticky="w")
comboDepartment=ttk.Combobox(entry_frame,textvariable=department,font=("Ruby",13),width=28,state="readonly")
comboDepartment['values']=('ECE','CSE','EEE','IT','AERO','AUTO','MECH','MECHTRONICS')
comboDepartment.grid(row=3,column=1,padx=10,sticky="w")

labelYear=Label(entry_frame,text="Batch",font=("Ruby",13),bg="Teal",fg="white")
labelYear.grid(row=3,column=2,padx=10,pady=10,sticky="w")
comboYear=ttk.Combobox(entry_frame,textvariable=year,font=("Ruby",13),width=28,state="readonly")
comboYear['values']=('2017 - 2021','2018 - 2022','2019 - 2023','2020 - 2024','2021 - 2025','2022 - 2026','2023 - 2027','2024 - 2028','2025 - 2029')
comboYear.grid(row=3,column=3,padx=10,sticky="w")

labelEmail=Label(entry_frame,text="Email",font=("Ruby",13),bg="Teal",fg="white")
labelEmail.grid(row=4,column=0,padx=10,pady=10,sticky="w")
textEmail=Entry(entry_frame,textvariable=email,font=("Ruby",13),width=30)
textEmail.grid(row=4,column=1,padx=10,sticky="w")

labelContact=Label(entry_frame,text="ContactNo",font=("Ruby",13),bg="Teal",fg="white")
labelContact.grid(row=4,column=2,padx=10,pady=10,sticky="w")
textContact=Entry(entry_frame,textvariable=contact,font=("Ruby",13),width=30)
textContact.grid(row=4,column=3,padx=10,sticky="w")

labelAddress=Label(entry_frame,text="Address",font=("Ruby",13),bg="Teal",fg="white")
labelAddress.grid(row=5,column=0,padx=10,pady=10,sticky="w")
textAddress=(Text(entry_frame,font=("Ruby",13),width=80,height=3.5))
textAddress.grid(row=6,column=0,columnspan=4,padx=10,sticky="w")

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    name.set(row[1])
    dob.set(row[2])
    gender.set(row[3])
    age.set(row[4])
    department.set(row[5])
    year.set(row[6])
    email.set(row[7])
    contact.set(row[8])
    textAddress.delete(1.0,END)
    textAddress.insert(END,row[9])

def RetriveDetails():
    tv.delete(*tv.get_children())
    for result in Database.Retrive():
        tv.insert("",END,values=result)
def createDetails():
    if textName.get()=="" or textDob.get()=="" or comboGender.get()=="" or textAge.get()=="" or comboDepartment.get()=="" or comboYear.get()=="" or textEmail.get()=="" or textContact.get()=="" or textAddress.get(1.0,END)=="":
        messagebox.showerror("Fill all Details")
        return
    Database.Create(textName.get(),textDob.get(),comboGender.get(),textAge.get(),comboDepartment.get(),comboYear.get(),textEmail.get(),textContact.get(),textAddress.get(1.0,END))
    messagebox.showinfo("Success Inserted")
    RetriveDetails()
    clearDetails()

def updateDetails():
    if textName.get()=="" or textDob.get()=="" or comboGender.get()=="" or textAge.get()=="" or comboDepartment.get()=="" or comboYear.get()=="" or textEmail.get()=="" or textContact.get()=="" or textAddress.get(1.0, END)=="":
        messagebox.showerror("Fill all Details")
        return
    Database.Update(row[0],textName.get(),textDob.get(),comboGender.get(),textAge.get(),comboDepartment.get(),comboYear.get(),textEmail.get(),textContact.get(),textAddress.get(1.0, END))
    messagebox.showinfo("Success Updated")
    RetriveDetails()
    clearDetails()

def deleteDetails():
    Database.Delete(row[0])
    RetriveDetails()
    clearDetails()

def clearDetails():
    name.set("")
    dob.set("")
    gender.set("")
    age.set("")
    department.set("")
    year.set("")
    email.set("")
    contact.set("")
    textAddress.delete(1.0,END)

button_frame=Frame(entry_frame,bg="Teal")
button_frame.grid(row=7,column=0,columnspan=4,padx=10,pady=10,sticky="w")

createButton=Button(button_frame,command=createDetails,text="Add Details",width=12,font=("Ruby",13,"bold"),bg="sea Green",fg="white",bd=0).grid(row=0,column=0,padx=10)

updateButton=Button(button_frame,command=updateDetails,text="Update Details",width=12,font=("Ruby",13,"bold"),bg="Hot pink",fg="white",bd=0).grid(row=0,column=1,padx=10)

deleteButton=Button(button_frame,command=deleteDetails,text="Delete Details",width=12,font=("Ruby",13,"bold"),bg="Red",fg="white",bd=0).grid(row=0,column=2,padx=10)

clearButton=Button(button_frame,command=clearDetails,text="Clear Details",width=12,font=("Ruby",13,"bold"),bg="Orange",fg="white",bd=0).grid(row=0,column=3,padx=10)

#Table Frame
tree_frame=Frame(obj,bg="olive")
tree_frame.place(x=0,y=440,width="1366",height="768")

style=ttk.Style()
style.configure("mystyle_treeview",font=("Ruby",16),rowheight=25)
style.configure("mystyle_treeview.Heading",font=("Ruby",16))


tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8,9,10),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=15)
tv.heading("2",text="NAME")
tv.column("2",width=15)
tv.heading("3",text="D.O.B")
tv.column("3",width=15)
tv.heading("4",text="GENDER")
tv.column("4",width=15)
tv.heading("5",text="AGE")
tv.column("5",width=15)
tv.heading("6",text="DEPARTMENT")
tv.column("6",width=15)
tv.heading("7",text="BATCH")
tv.column("7",width=15)
tv.heading("8",text="EMAIL")
tv.column("8",width=15)
tv.heading("9",text="CONTACTNO")
tv.column("9",width=15)
tv.heading("10",text="ADDRESS")
tv.column("10",width=15)

tv['show']='headings'
tv.pack(fill=X)
tv.bind("<ButtonRelease-1>",getData)


RetriveDetails()
obj.mainloop()
