from tkinter import *
import speedtest

sp =Tk()
sp.title("speed test")
sp.geometry("500x500")
sp.config(bg="pink")

lab= Label(sp,text="Speed test",font=("Time New Roman",40,"bold"),bg="pink",fg="black")
lab.place(x=70,y=40,height=50,width=380)

lab= Label(sp,text="Download speed",font=("Time New Roman",40,"bold"),bg="pink",fg="black")
lab.place(x=70,y=130,height=50,width=410)

lab= Label(sp,text="00",font=("Time New Roman",40,"bold"),bg="pink",fg="black")
lab.place(x=70,y=200,height=50,width=380)

lab= Label(sp,text="Upload speed",font=("Time New Roman",40,"bold"),bg="pink",fg="black")
lab.place(x=70,y=290,height=50,width=380)

lab= Label(sp,text="00",font=("Time New Roman",40,"bold"),bg="pink",fg="black")
lab.place(x=70,y=360,height=50,width=380)

sp.mainloop()