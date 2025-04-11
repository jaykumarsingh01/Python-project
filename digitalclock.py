from tkinter import *

clock=Tk()
clock.title('Digital Clock')
clock.geometry('1000x500')
clock.config(bg='Wheat')


lab_hr=Label(clock,text="00",font=('Times New Roman',60,"bold"),
             bg='black',fg="white")

lab_hr.place(x=40,y=40,height=110,width=100)

























clock.mainloop()