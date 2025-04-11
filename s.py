from tkinter import *
from tkinter import messagebox
import datetime

# 🕰️ Only needed for IST
try:
    from zoneinfo import ZoneInfo  # Python 3.9+
except ImportError:
    from backports.zoneinfo import ZoneInfo   # if using older Python + pip install backports.zoneinfo


# ✅ Greeting based on IST
def get_greeting():
    ist = datetime.datetime.now(ZoneInfo("Asia/Kolkata"))
    hour = ist.hour
    if hour < 12:
        return "Good Morning ☀️"
    elif hour < 18:
        return "Good Afternoon 🌞"
    else:
        return "Good Evening 🌙"

# 🕒 Update all labels
def date_time():
    ist = datetime.datetime.now(ZoneInfo("Asia/Kolkata"))
    hr = ist.strftime('%I')
    min = ist.strftime('%M')
    sec = ist.strftime('%S')
    am = ist.strftime('%p ')
    date = ist.strftime("%d")
    month = ist.strftime("%m")
    year = ist.strftime("%Y")
    day = ist.strftime("%a")

    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    label_greeting.config(text=get_greeting())

    lab_hr.after(200, date_time)


# === UI SETUP ===
clock = Tk()
clock.title('Digital Clock')
clock.geometry('1000x530')
clock.config(bg='Wheat')

label_greeting = Label(clock, font=('Helvetica', 25, 'bold'), bg='Wheat', fg='green')
label_greeting.pack()

# Time Labels
lab_hr = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_hr.place(x=120, y=50, height=110, width=100)
Label(clock, text="Hour", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=120, y=190, height=40, width=100)

lab_min = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_min.place(x=340, y=50, height=110, width=100)
Label(clock, text="Min.", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=340, y=190, height=40, width=100)

lab_sec = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_sec.place(x=560, y=50, height=110, width=100)
Label(clock, text="Sec.", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=560, y=190, height=40, width=100)

lab_am = Label(clock, text="00", font=('Times New Roman', 40, "bold"), bg='black', fg="white")
lab_am.place(x=780, y=50, height=110, width=100)
Label(clock, text="Am/Pm", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=780, y=190, height=40, width=100)

# Date Labels
lab_date = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_date.place(x=120, y=270, height=110, width=100)
Label(clock, text="Date", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=120, y=410, height=40, width=100)

lab_mon = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_mon.place(x=340, y=270, height=110, width=100)
Label(clock, text="Month", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=340, y=410, height=40, width=100)

lab_year = Label(clock, text="00", font=('Times New Roman', 45, "bold"), bg='black', fg="white")
lab_year.place(x=560, y=270, height=110, width=120)
Label(clock, text="Year", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=560, y=410, height=40, width=110)

lab_day = Label(clock, text="00", font=('Times New Roman', 50, "bold"), bg='black', fg="white")
lab_day.place(x=780, y=270, height=110, width=100)
Label(clock, text="Day", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=780, y=410, height=40, width=100)

# Exit Button
exit_btn = Button(clock, text="Exit", command=clock.quit, font=('Arial', 14), bg='black', fg='white')
exit_btn.place(x=870, y=480, width=100, height=40)

# Start
date_time()
clock.mainloop()
