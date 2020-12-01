from tkinter import *
def add():
    root=Tk()
    root.geometry("439x300")
    root.title("Parking Management System")
    # fheading=Frame(root,borderwidth=5,relief=SUNKEN)
    # fheading.grid(column=3)
    heading=Label(root,text="PARKING MANAGEMANT SYSTEM",bg="black",fg="white",font=("Times New Roman",20))
    heading.grid(columnspan=20,pady=10)
    l1=Label(root,text="Owner name:")
    l1.grid(row=1,column=0)
    l2=Label(root,text="Vehical No:")
    l2.grid(row=2,column=0)
    owner=StringVar()
    vno=StringVar()

    ownerentry=Entry(root,textvariable=owner)
    ownerentry.grid(row=1,column=1)

    vnoentry=Entry(root,textvariable=vno)
    vnoentry.grid(row=2,column=1)

    l3=Label(root,text="Vehicle Type:")
    l3.grid(row=3,column=0)

    # def select():
    #    a=str(radio.get())
    #    print(a)
    #    o=ownerentry.get()
    #    v=vnoentry.get()
    #    if a==0:
    #         f=open("bike.txt",'a')
    #         f.write(o+" "+v+"\r\n")
    #    elif a==1:
    #         f1=open("car.txt",'a')
    #         f1.write(o+" "+v+"\r\n")
    #    elif a==2:
    #         f2=open("lv.txt",'a')
    #         f2.write(o+" "+v+"\r\n")
    #    elif a==3:
    #         f3=open("hv.txt",'a')
    #         f3.write(o+" "+v+"\r\n")
    # key=0
    # def sub():
    def bikee():    
        o=ownerentry.get()
        v=vnoentry.get()
        f=open("bike.txt",'a')
        f.write(o+" "+v+"\r\n")
    
    def care():    
        o=ownerentry.get()
        v=vnoentry.get()
        f=open("car.txt",'a')
        f.write(o+" "+v+"\r\n")

    def lve():    
        o=ownerentry.get()
        v=vnoentry.get()
        f=open("lv.txt",'a')
        f.write(o+" "+v+"\r\n")

    def hve():    
        o=ownerentry.get()
        v=vnoentry.get()
        f=open("hv.txt",'a')
        f.write(o+" "+v+"\r\n")
    
    def thankyou():
        l=Label(root,text="Parking Done!!!",font=10).grid(row=6,column=1)

    # b=Button(root,text="sSubmit",borderwidth=5,command=sub).grid(row=6,column=0,sticky="w",pady=10)
    # photo = PhotoImage(file =r"motorbike.png")
    bikebutton=Button(root,text="Bike",command=bikee,borderwidth=4,padx=32,bg="black",fg="white").grid(row=4,column=0,pady=5)
    carbutton=Button(root,text="Car",command=care,borderwidth=4,padx=32,bg="black",fg="white").grid(row=4,column=1)
    lvbutton=Button(root,text="LightVehicle",command=lve,borderwidth=4,bg="black",fg="white",padx=5).grid(row=4,column=2,)
    hvbutton=Button(root,text="HeavyVehicle",command=hve,borderwidth=4,bg="black",fg="white",padx=5).grid(row=4,column=3,padx=10)
    s=Button(root,text="Submit",borderwidth=8,padx=25,bg="gray",command=thankyou).grid(row=5,column=1,pady=10)
    
    root.mainloop()

def display():
    disp=Tk()
    def bikef():
        f=open("bike.txt")
        txt=f.read()
        flable=Label(disp,text=txt).grid(row=2,columnspan=4)

    def carf():
        f=open("car.txt")
        txt=f.read()
        flable=Label(disp,text=txt).grid(row=2,columnspan=4)

    def lvf():
        f=open("lv.txt")
        txt=f.read()
        flable=Label(disp,text=txt).grid(row=2,columnspan=4)

    def hvf():
        f=open("hv.txt")
        txt=f.read()
        flable=Label(disp,text=txt).grid(row=2,columnspan=4)        
        
    disp.geometry("439x500")
    heading=Label(disp,text="PARKING MANAGEMANT SYSTEM",bg="black",fg="white",font=("Times New Roman",20))
    heading.grid(columnspan=20,pady=10)
    bikebutton=Button(disp,text="Bike",command=bikef,borderwidth=8,bg="gray",padx=20).grid(row=1,column=3,pady=30,padx=5)
    carbutton=Button(disp,text="Car",command=carf,borderwidth=8,bg="gray",padx=20).grid(row=1,column=6,pady=30,padx=5)
    lvbutton=Button(disp,text="LightVehicle",command=lvf,borderwidth=8,bg="gray").grid(row=1,column=9,pady=30,padx=5)
    hvbutton=Button(disp,text="HeavyVehicle",command=hvf,borderwidth=8,bg="gray").grid(row=1,column=12,pady=30,padx=5)
    disp.mainloop()
intro=Tk()
intro.geometry("439x200")
intro.title("Parking Management System")
# fheading=Frame(root,borderwidth=5,relief=SUNKEN)
# fheading.grid(column=3)
heading=Label(intro,text="PARKING MANAGEMANT SYSTEM",bg="black",fg="white",font=("Times New Roman",20))
heading.grid(columnspan=20,pady=10)
entryfram=Frame(intro,borderwidth=9)
b1=Button(intro,text="Entry",command=add,borderwidth=8,bg="gray").grid(row=1,column=5,pady=30)
b2=Button(intro,text="Show",command=display,borderwidth=8,bg="gray").grid(row=1,column=8,pady=30)

def search():
    sea=Tk()
    sea.geometry("439x500")
    heading=Label(sea,text="PARKING MANAGEMANT SYSTEM",bg="black",fg="white",font=("Times New Roman",20))
    heading.grid(columnspan=20,pady=10)
    def bikes():
        b=Tk()
        b.geometry("439x500")
        heading=Label(b,text="PARKING MANAGEMANT SYSTEM",bg="black",fg="white",font=("Times New Roman",20))
        heading.grid(columnspan=20,pady=10)   

        l1=Label(b,text="Owner name:")
        l1.grid(row=3,column=0,pady=10)
        sowner=StringVar()
        sownerentry=Entry(b,textvariable=sowner)
        sownerentry.grid(row=3,column=1,pady=10)
        def tra():
            key=sownerentry.get()
            f=open("bike.txt")
            for line in f:
                line=line.rstrip()
                if line.startswith(key):
                    lab=Label(b,text=line)
                    lab.grid(row=6)
        tr=Button(b,text="submit",command=tra,borderwidth=8,padx=10,bg="gray").grid(row=4,column=1)
        

     
    
    def cars():
        b=Tk()
        b.geometry("439x500")
        heading=Label(b,text="PARKING MANAGEMANT SYSTEM",bg="black",fg="white",font=("Times New Roman",20))
        heading.grid(columnspan=20,pady=10)   

        l1=Label(b,text="Owner name:")
        l1.grid(row=3,column=0,pady=10)
        sowner=StringVar()
        sownerentry=Entry(b,textvariable=sowner)
        sownerentry.grid(row=3,column=1,pady=10)
        def traa():
            key=sownerentry.get()
            f=open("car.txt")
            for line in f:
                line=line.rstrip()
                if line.startswith(key):
                    lab=Label(b,text=line)
                    lab.grid(row=6)
        tr=Button(b,text="submit",command=traa,borderwidth=8,padx=10,bg="gray").grid(row=4,column=1,sticky="w",pady=10)
        
        
    def lvs():
        b=Tk()
        b.geometry("439x500")
        heading=Label(b,text="PARKING MANAGEMANT SYSTEM",bg="black",fg="white",font=("Times New Roman",20))
        heading.grid(columnspan=20,pady=10)   

        l1=Label(b,text="Owner name:")
        l1.grid(row=3,column=0,pady=10)
        sowner=StringVar()
        sownerentry=Entry(b,textvariable=sowner)
        sownerentry.grid(row=3,column=1,pady=10)
        def trae():
            key=sownerentry.get()
            f=open("lv.txt")
            for line in f:
                line=line.rstrip()
                if line.startswith(key):
                    lab=Label(b,text=line)
                    lab.grid(row=6)
        tr=Button(b,text="submit",command=trae,borderwidth=8,padx=10,bg="gray").grid(row=4,column=1,sticky="w",pady=10)
        

    def hvs():
        b=Tk()
        b.geometry("439x500")
        heading=Label(b,text="PARKING MANAGEMANT SYSTEM",bg="black",fg="white",font=("Times New Roman",20))
        heading.grid(columnspan=20,pady=10)   

        l1=Label(b,text="Owner name:")
        l1.grid(row=3,column=0,pady=10)
        sowner=StringVar()
        sownerentry=Entry(b,textvariable=sowner)
        sownerentry.grid(row=3,column=1,pady=10)
        def traaa():
            key=sownerentry.get()
            f=open("hv.txt")
            for line in f:
                line=line.rstrip()
                if line.startswith(key):
                    lab=Label(b,text=line)
                    lab.grid(row=6)
        tr=Button(b,text="submit",command=traaa,borderwidth=8,padx=10,bg="gray").grid(row=4,column=1,sticky="w",pady=10)
        
                 
        
        
            
    bikebutton=Button(sea,text="Bike",command=bikes,borderwidth=8,bg="gray",padx=20).grid(row=2,column=3,pady=30,padx=5)
    carbutton=Button(sea,text="Car",borderwidth=8,bg="gray",padx=20,command=cars).grid(row=2,column=6,pady=30,padx=5)
    lvbutton=Button(sea,text="LightVehicle",borderwidth=8,bg="gray",command=lvs).grid(row=2,column=9,pady=30,padx=5)
    hvbutton=Button(sea,text="HeavyVehicle",borderwidth=8,bg="gray",command=hvs).grid(row=2,column=12,pady=30,padx=5)
    
    
    
    
    sea.mainloop()
b3=Button(intro,text="Search",borderwidth=8,bg="gray",command=search).grid(row=1,column=11,pady=30)


intro.mainloop()  