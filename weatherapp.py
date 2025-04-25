from tkinter import *
from tkinter import ttk

win=Tk()
win.title("Jay")
win.config(bg="Bisque")
win.geometry("500x570")


name_label=Label(win,text="Jay Weather App",font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=50,height=70,width=450)

list_name=[ "Andhra Pradesh",
    "Arunachal Pradesh",
    "Andaman and Nicobar Islands",
    "Assam",
    "Bihar",
    "Chandigarh",
    "Chhattisgarh",
    "Dadra and Nagar Haveli and",
    "Delhi",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu & Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Ladakh",
    "Lakshadweep",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Puducherry",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"]
com=ttk.Combobox(win,text="Jay Weather App",values=list_name,font=("Times New Roman",20,"bold"))
com.place(x=25,y=140,height=50,width=450)




done_button=Button(win,text="Search",font=("Times New Roman",20,"bold"))
done_button.place(y=210,height=50,width=100,x=200)



W_label=Label(win,text="Weather Climate",font=("Times New Roman",20))
W_label.place(x=25,y=280,height=50,width=210)

Wb_label=Label(win,text="Weather Description",font=("Times New Roman",17))
Wb_label.place(x=25,y=340,height=50,width=210)

temp_label=Label(win,text="Temperature",font=("Times New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)


per_label=Label(win,text="Pressure",font=("Times New Roman",20))
per_label.place(x=25,y=470,height=50,width=210)




win.mainloop()