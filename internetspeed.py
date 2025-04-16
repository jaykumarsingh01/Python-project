from tkinter import *
import speedtest

def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+"Mbps"
    up= str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp =Tk()
sp.title("speed test")
sp.geometry("500x650")
sp.config(bg="pink")

lab= Label(sp,text="Speed test",font=("Time New Roman",40,"bold"),bg="pink",fg="black")
lab.place(x=70,y=40,height=50,width=380)

lab= Label(sp,text="Download speed",font=("Time New Roman",40,"bold"),bg="pink",fg="black")
lab.place(x=70,y=130,height=50,width=410)

lab_down= Label(sp,text="00",font=("Time New Roman",40,"bold"),bg="pink",fg="black")
lab_down.place(x=70,y=200,height=50,width=380)

lab= Label(sp,text="Upload speed",font=("Time New Roman",40,"bold"),bg="pink",fg="black")
lab.place(x=70,y=290,height=50,width=380)

lab_up= Label(sp,text="00",font=("Time New Roman",40,"bold"),bg="pink",fg="black")
lab_up.place(x=70,y=360,height=50,width=380)



button= Button(sp,text='Check Speed',font=("Time New Roman",40,"bold"),relief=RAISED,bg="green",command=speedcheck)
button.place(x=70,y=460,height=50,width=380)







sp.mainloop()