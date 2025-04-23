import pyautogui
from tkinter import *
def take_ss():
        # print(entry.get())
        add_data=entry.get()
        path= add_data+"\\test.png"
        print(path)

        ss=pyautogui.screenshot()
        ss.save("test1.png")

win=Tk()
win.title("jay ss")
win.geometry("700x400")
win.config(bg="pink")
win.resizable(False,False)

entry=Entry(win,font=('times new roman',30))
entry.place(x=10,height=70,width=660,y=50)


button=Button(win,text="Done",font=('times new roman',50),command=take_ss)
button.place(x=250,y=140,height=100,width=200)


win.mainloop()
















