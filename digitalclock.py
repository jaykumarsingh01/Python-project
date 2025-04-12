from tkinter import *
from tkinter import messagebox
import datetime
import time
import threading
import random
import calendar
import pytz
import requests


is_24_hour = False
stopwatch_running = False
stopwatch_counter = 0
is_dark = False
alarm_thread = None

# === Quote List ===
quotes = [
    "Stay positive, work hard, make it happen.",
    "Discipline is the bridge between goals and accomplishment.",
    "Success is no accident.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones."
]

# === Weather ===
# import requests 

def get_weather():
    try:
        api_key = "bd6f1dd81d2f2eb8414a656ec18c6ef5"  # You can generate a new one if needed
        city = "Delhi"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        res = response.json()
        
        print("API Response:", res)  # See the exact data received
        
        if response.status_code != 200:
            raise Exception(res.get("message", "API error"))
        
        temp = res['main']['temp']
        condition = res['weather'][0]['description'].capitalize()
        
        weather_label.config(text=f"{city}: {temp}°C, {condition}")
    
    except Exception as e:
        print("Weather fetch error:", e)
        weather_label.config(text="Weather: Unable to fetch")



# print(datetime.datetime.now())

def toggle_format():
    global is_24_hour
    is_24_hour = not is_24_hour

def date_time():
        
    time =datetime.datetime.now()

    if is_24_hour:
        hr = time.strftime('%H')
        am = ''
    else:
        hr = time.strftime('%I')
        am = time.strftime('%p')
    
    # hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    # am = time.strftime('%p ')
    date =time.strftime("%d")
    month =time.strftime("%m")
    year =time.strftime("%Y")
    day =time.strftime("%a")
  

    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    label_greeting.config(text=get_greeting())
    label_timezone.config(text="Indian Standard Time (IST)")



    world_time_label.config(text=f"Tokyo: {get_world_time('Asia/Tokyo')} | New York: {get_world_time('America/New_York')}")

    lab_hr.after(200,date_time)



# === Stopwatch ===
def start_stopwatch():
    global stopwatch_running
    stopwatch_running = True
    update_stopwatch()

def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False

def reset_stopwatch():
    global stopwatch_counter
    stopwatch_counter = 0
    stopwatch_label.config(text="00:00:00")

def update_stopwatch():
    global stopwatch_counter
    if stopwatch_running:
        stopwatch_counter += 1
        hrs = stopwatch_counter // 3600
        mins = (stopwatch_counter % 3600) // 60
        secs = stopwatch_counter % 60
        stopwatch_label.config(text=f"{hrs:02}:{mins:02}:{secs:02}")
        stopwatch_label.after(1000, update_stopwatch)


# === Alarm ===
def set_alarm():
    alarm_time = simpledialog.askstring("Set Alarm", "Enter time in HH:MM format:") # type: ignore
    if alarm_time:
        threading.Thread(target=check_alarm, args=(alarm_time,), daemon=True).start()

def check_alarm(alarm_time):
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == alarm_time:
            messagebox.showinfo("Alarm", "⏰ Time's up!")
            break
        time.sleep(1)

# === World Clock ===
def get_world_time(city):
    tz = pytz.timezone(city)
    return datetime.datetime.now(tz).strftime('%H:%M:%S')

# === Quotes ===
def update_quote():
    quote_label.config(text=random.choice(quotes))
    clock.after(10000, update_quote)

# === Calendar ===
def show_calendar():
    now = datetime.datetime.now()
    cal_text = calendar.month(now.year, now.month)
    messagebox.showinfo("📅 Calendar", cal_text)

# === Theme Toggle ===
def toggle_theme():
    global is_dark
    bg = 'black' if not is_dark else 'Wheat'
    fg = 'white' if not is_dark else 'black'
    clock.config(bg=bg)
    for widget in clock.winfo_children():
        try:
            widget.config(bg=bg, fg=fg)
        except:
            pass
    is_dark = not is_dark




# UI setup
clock=Tk()
clock.title('Digital Clock')
clock.geometry('1000x600')
clock.config(bg='Wheat')





# label_full_date = Label(clock, text="Digital Clock", font=('Helvetica', 20, "bold"), bg='Wheat', fg='red')
# label_full_date.pack(pady=10)

label_greeting = Label(clock, font=('Helvetica', 25, 'bold'), bg='Wheat', fg='green')
label_greeting.pack()


def get_greeting():
    hour = int(datetime.datetime.now().strftime('%H'))
    if hour < 12:
        return "Good Morning ☀️"
    elif hour < 18:
        return "Good Afternoon 🌞"
    else:
        return "Good Evening 🌙"


# Time*


lab_hr=Label(clock,text="00",font=('Times New Roman',60,"bold"),
             bg='black',fg="white")

lab_hr.place(x=120,y=50,height=110,width=100)
lab_hr_txt=Label(clock,text="Hour",font=('Times New Roman',20,"bold"),
             bg='black',fg="white")
lab_hr_txt.place(x=120,y=190,height=40,width=100)


lab_min=Label(clock,text="00",font=('Times New Roman',60,"bold"),
             bg='black',fg="white")

lab_min.place(x=340,y=50,height=110,width=100)
lab_min_txt=Label(clock,text="Min.",font=('Times New Roman',20,"bold"),
             bg='black',fg="white")
lab_min_txt.place(x=340,y=190,height=40,width=100)


lab_sec=Label(clock,text="00",font=('Times New Roman',60,"bold"),
             bg='black',fg="white")

lab_sec.place(x=560,y=50,height=110,width=100)
lab_sec_txt=Label(clock,text="Sec.",font=('Times New Roman',20,"bold"),
             bg='black',fg="white")
lab_sec_txt.place(x=560,y=190,height=40,width=100)


lab_am=Label(clock,text="00",font=('Times New Roman',40,"bold"),
             bg='black',fg="white")

lab_am.place(x=780,y=50,height=110,width=100)
lab_am_txt=Label(clock,text="Am/Pm",font=('Times New Roman',20,"bold"),
             bg='black',fg="white")
lab_am_txt.place(x=780,y=190,height=40,width=100)


# Date


lab_date=Label(clock,text="00",font=('Times New Roman',60,"bold"),
             bg='black',fg="white")

lab_date.place(x=120,y=270,height=110,width=100)
lab_date_txt=Label(clock,text="Date",font=('Times New Roman',20,"bold"),
             bg='black',fg="white")
lab_date_txt.place(x=120,y=410,height=40,width=100)



lab_mon=Label(clock,text="00",font=('Times New Roman',60,"bold"),
             bg='black',fg="white")

lab_mon.place(x=340,y=270,height=110,width=100)
lab_mon_txt=Label(clock,text="Month",font=('Times New Roman',20,"bold"),
             bg='black',fg="white")
lab_mon_txt.place(x=340,y=410,height=40,width=100)


lab_year=Label(clock,text="00",font=('Times New Roman',45,"bold"),
             bg='black',fg="white")

lab_year.place(x=560,y=270,height=110,width=120)
lab_year_txt=Label(clock,text="Year",font=('Times New Roman',20,"bold"),
             bg='black',fg="white")
lab_year_txt.place(x=560,y=410,height=40,width=110)


lab_day=Label(clock,text="00",font=('Times New Roman',50,"bold"),
             bg='black',fg="white")

lab_day.place(x=780,y=270,height=110,width=100)
lab_day_txt=Label(clock,text="Day",font=('Times New Roman',20,"bold"),
             bg='black',fg="white")
lab_day_txt.place(x=780,y=410,height=40,width=100)



#labels

label_timezone = Label(clock, text="", font=('Arial', 14, 'italic'), bg='Wheat', fg='black')
label_timezone.place(x=20, y=520)

world_time_label = Label(clock, text="", font=('Arial', 12), bg='Wheat', fg='darkblue')
world_time_label.place(x=20, y=558)

quote_label = Label(clock, font=('Arial', 14, 'italic'), bg='Wheat', fg='darkblue')
quote_label.place(x=400, y=550)

weather_label = Label(clock, text="", font=('Arial', 12), bg='Wheat', fg='blue')
weather_label.place(x=700, y=580)



toggle_btn = Button(clock, text="12/24 Hour", command=toggle_format, font=('Arial', 14), bg='Blue', fg='white')
toggle_btn.place(x=720, y=480, width=130, height=40)


#  Exit Button 
exit_btn = Button(clock, text="Exit", command=clock.quit, font=('Arial', 14), bg='red', fg='white')
exit_btn.place(x=870, y=480, width=100, height=40)





#  Stopwatch 

# === Stopwatch ===

stopwatch_label = Label(clock, text="00:00:00", font=('Arial', 20, 'bold'), bg='Wheat', fg='blue')
stopwatch_label.place(x=20, y=480)  # Moved up

Button(clock, text="Start", command=start_stopwatch, font=('Arial', 12), bg='Green', fg='white').place(x=150, y=480)
Button(clock, text="Stop", command=stop_stopwatch, font=('Arial', 12), bg='Orange', fg='white').place(x=210, y=480)
Button(clock, text="Reset", command=reset_stopwatch, font=('Arial', 12), bg='Gray', fg='white').place(x=270, y=480)




Button(clock, text="Set Alarm", command=set_alarm, font=('Arial', 12), bg='brown', fg='white').place(x=340, y=480)
Button(clock, text="Calendar", command=show_calendar, font=('Arial', 12), bg='purple', fg='white').place(x=440, y=480)
Button(clock, text="Toggle Theme", command=toggle_theme, font=('Arial', 12), bg='black', fg='white').place(x=550, y=480)


get_weather()
update_quote()
date_time()
clock.mainloop()




                                                     #Jay Kumar Singh
