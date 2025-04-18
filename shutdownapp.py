

from tkinter import *
import os


def Restart():
    os.system("shutdown /r /t 1")

def Restart_time():
     os.system("shutdown /r /t 20")

def logout():
     os.system("shutdown -l")

def shutdown():
     os.system("shutdown /s /t 1")


st=Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="DeepSkyBlue")



r_buttom  = Button(st,text="Restart",font= ("time new roman",20,"bold"),relief=RAISED,cursor="plus",command=Restart)
r_buttom.place(x=150,y=60,height=50,width=200)

rt_buttom  = Button(st,text="Restart time",font= ("time new roman",20,"bold"),relief=RAISED,cursor="plus",command= Restart_time)
rt_buttom.place(x=150,y=170,height=50,width=200)

lg_buttom  = Button(st,text="Log-Out",font= ("time new roman",20,"bold"),relief=RAISED,cursor="plus",command= logout)
lg_buttom.place(x=150,y=270,height=50,width=200)

st_buttom  = Button(st,text="Shutdown",font= ("time new roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
st_buttom.place(x=150,y=370,height=50,width=200)







st.mainloop()













                                                                 #Jay Kumar Singh
