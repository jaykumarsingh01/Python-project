from tkinter import *
import os
st=Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="DeepSkyBlue")
r_buttom  = Button(st,text="Restart",font= ("time new roman",30,"bold"),relief=RAISED,cursor="plus")
r_buttom.place(x=150,y=60,height=50,width=200)

rt_buttom  = Button(st,text="Restart time",font= ("time new roman",20,"bold"),relief=RAISED,cursor="plus")
rt_buttom.place(x=150,y=170,height=50,width=200)

lg_buttom  = Button(st,text="Log-Out",font= ("time new roman",20,"bold"),relief=RAISED,cursor="plus")
lg_buttom.place(x=150,y=270,height=50,width=200)

st_buttom  = Button(st,text="Log-Out",font= ("time new roman",20,"bold"),relief=RAISED,cursor="plus")
st_buttom.place(x=150,y=370,height=50,width=200)

















st.mainloop()