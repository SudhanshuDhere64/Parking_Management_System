from tkinter import *
import datetime
from tkinter import messagebox

import mysql.connector as mysql
import pandas as pd

connectiondb=mysql.connect(host="localhost",user="root",passwd="",database="parking_management_system")
cursordb=connectiondb.cursor()


k = datetime.datetime.now()
a = str(k.date())

def add():
    root = Tk()
    root.geometry("439x250")
    # root.config(bg="blue")
    root.minsize(439, 250)
    root.maxsize(439, 250)
    root.title("Parking Management System")

    heading = Label(root, text="PARKING MANAGEMANT SYSTEM", bg="black", fg="white", font=("Times New Roman", 20))
    heading.grid(columnspan=20, pady=10)
    l1 = Label(root, text="Owner name:")
    l1.grid(row=1, column=0)
    l2 = Label(root, text="Vehical No:")
    l2.grid(row=2, column=0)
    global owner
    owner= StringVar()
    global vno
    vno= StringVar()
    i=1

    ownerentry = Entry(root, textvariable=owner)
    ownerentry.grid(row=1, column=1)

    vnoentry = Entry(root, textvariable=vno)
    vnoentry.grid(row=2, column=1)

    l3 = Label(root, text="Vehicle Type:")
    l3.grid(row=3, column=0)

    def bikee():

        o = ownerentry.get()
        v = vnoentry.get()
        if len(o)!=0 and len(v)!=0:
            vtype="Bike"
            sql="insert into entry(Owner_name,Vehicle_number,Vehicle_type) values (%s,%s,%s)"
            valuesss=(o,v,vtype)
            cursordb.execute(sql,valuesss)
            connectiondb.commit()
        else:
            messagebox.showerror("showerror", "Fill the Details First")



    def care():
        i=1
        o = ownerentry.get()
        v = vnoentry.get()
        if len(o) != 0 and len(v) != 0:
            vtype = "Car"
            sql = "insert into entry(Owner_name,Vehicle_number,Vehicle_type) values (%s,%s,%s)"
            valuesss = (o, v, vtype)
            cursordb.execute(sql, valuesss)
            connectiondb.commit()
            i = i + 1
        else:
            messagebox.showerror("showerror", "Fill the Details First")

    def lve():
        i=1
        o = ownerentry.get()
        v = vnoentry.get()
        if len(o) != 0 and len(v) != 0:
            vtype = "Lightvehicle"
            sql = "insert into entry(Owner_name,Vehicle_number,Vehicle_type) values (%s,%s,%s)"
            valuesss = (o, v, vtype)
            cursordb.execute(sql, valuesss)
            connectiondb.commit()
            i = i + 1
        else:
            messagebox.showerror("showerror", "Fill the Details First")

    def hve():
        i=1
        o = ownerentry.get()
        v = vnoentry.get()
        if len(o) != 0 and len(v) != 0:
            vtype = "Heavyvehicle"
            sql = "insert into entry(Owner_name,Vehicle_number,Vehicle_type) values (%s,%s,%s)"
            valuesss = (o, v, vtype)
            cursordb.execute(sql, valuesss)
            connectiondb.commit()
            i = i + 1
        else:
            messagebox.showerror("showerror", "Fill the Details First")

    def thankyou():
        l = Label(root, text="Parking Done!!!", font=10).grid(row=6, column=1)

    bikebutton = Button(root, text="Bike", command=bikee, borderwidth=6, padx=32, bg="red", fg="white").grid(row=4,
                                                                                                               column=0,
                                                                                                               pady=5)
    carbutton = Button(root, text="Car", command=care, borderwidth=6, padx=32, bg="red", fg="white").grid(row=4,
                                                                                                            column=1)
    lvbutton = Button(root, text="LightVehicle", command=lve, borderwidth=6, bg="red", fg="white", padx=5).grid(row=4,
                                                                                                                  column=2, )
    hvbutton = Button(root, text="HeavyVehicle", command=hve, borderwidth=6, bg="red", fg="white", padx=5).grid(row=4,
                                                                                                                  column=3,
                                                                                                                  padx=10)
    s = Button(root, text="Submit", borderwidth=8, padx=25, bg="gray", command=thankyou).grid(row=5, column=1, pady=10)

    root.mainloop()


def display():
    disp = Tk()
    disp.title("display")
    disp.geometry("439x600")
    disp.minsize(439, 600)
    disp.maxsize(439, 600)
    heading = Label(disp, text="PARKING MANAGEMANT SYSTEM", bg="black", fg="white", font=("Times New Roman", 20))
    heading.grid(row=0,columnspan=20, pady=10)
    values1 = "Bike"
    sql1="select * from entry"
    cursordb.execute(sql1)
    myresult = cursordb.fetchall()
    for row in myresult:
        roww=' '.join(row)
        w = print(roww)
        file=open("file.txt","a")
        file.write(roww+"\n")
        file.close()


    read_file=open("file.txt",'r')
    file_read=read_file.read()
    file = open("file.txt", 'w')
    file.write(" ")
    file.close()
    lab = Label(disp, text=file_read)
    lab.grid(row=6, columnspan=10)

    disp.mainloop()


intro = Tk()
intro.geometry("439x200")
intro.minsize(439, 200)
intro.maxsize(439, 200)
intro.title("Parking Management System")

heading = Label(intro, text="PARKING MANAGEMANT SYSTEM", bg="black", fg="white", font=("Times New Roman", 20))
heading.grid(columnspan=20, pady=10, sticky="nw")
entryfram = Frame(intro, borderwidth=9)
b1 = Button(intro, text="Entry", command=add, borderwidth=8, bg="gray").grid(row=1, column=5, pady=30)
b2 = Button(intro, text="Show", command=display, borderwidth=8, bg="gray").grid(row=1, column=8, pady=30)


def search():
    sea = Tk()
    sea.geometry("439x300")
    sea.minsize(439, 300)
    sea.maxsize(439, 300)
    heading = Label(sea, text="PARKING MANAGEMANT SYSTEM", bg="black", fg="white", font=("Times New Roman", 20))
    heading.grid(columnspan=20, pady=10)
    l1 = Label(sea, text="Owner name:")
    l1.grid(row=3, column=0, pady=10)
    sowner = StringVar()
    sownerentry = Entry(sea, textvariable=sowner)
    sownerentry.grid(row=3, column=1, pady=10)
    def traa():
            key = sownerentry.get()

            sql1 = "SELECT * FROM entry WHERE Owner_name='%s'" % (key)
            cursordb.execute(sql1)
            myresult = cursordb.fetchall()
            for row in myresult:
                roww = ' '.join(row)
                w = print(roww)
                file = open("files.txt", "a")
                file.write(roww + "\n")
                file.close()

            read_file = open("files.txt", 'r')
            file_read = read_file.read()
            file = open("files.txt", 'w')
            file.write(" ")
            file.close()

            lab = Label(sea, text=file_read)
            lab.grid(row=6, columnspan=10)
    tr = Button(sea, text="submit", command=traa, borderwidth=8, padx=10, bg="gray").grid(row=4, column=1, sticky="w",
                                                                                            pady=10)






    sea.mainloop()


b3 = Button(intro, text="Search", borderwidth=8, bg="gray", command=search).grid(row=1, column=11, pady=30)

intro.mainloop()