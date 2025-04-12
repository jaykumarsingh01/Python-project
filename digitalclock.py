from tkinter import *
from tkinter import messagebox, simpledialog
import datetime
import time
import threading
import random
import calendar
import pytz
import requests
import pyttsx3
import json
import os
from tkinter import PhotoImage


is_24_hour = False
stopwatch_running = False
stopwatch_counter = 0
is_dark = False
alarm_times = []
preferences_file = "preferences.json"
city = "Delhi"
speech_engine = pyttsx3.init()

# === Quote List ===
quotes = [
    "Stay positive, work hard, make it happen.",
    "Discipline is the bridge between goals and accomplishment.",
    "Success is no accident.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Keep your face always toward the sunshine—and shadows will fall behind you",
    "There is nothing either good or bad, but thinking makes it so.",
    "All that we are is the result of what we have thought",
    "Positive anything is better than negative nothing",
    "The energy of the mind is the essence of life",
    "Energy and persistence conquer all things.",
    "Light tomorrow with today!",
    "It does not matter how slowly you go as long as you do not stop.",
    "Every day may not be good... but there's something good in every day.!",
    "Happiness depends upon ourselves.",
    "It is not length of life, but depth of life.”",
    "The journey of a thousand miles begins with one step.”"
]

# === Weather ===
# import requests 

def get_weather():
    try:
        # api_key = "bd6f1dd81d2f2eb8414a656ec18c6ef5"  
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

def announce_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speech_engine.say(f"The time is {now}")
    speech_engine.runAndWait()

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
    alarm_time = simpledialog.askstring("Set Alarm", "Enter time in HH:MM format:")
    if alarm_time:
        alarm_times.append(alarm_time)
        threading.Thread(target=check_alarm, daemon=True).start()
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")

def check_alarm():
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now in alarm_times:
            messagebox.showinfo("Alarm", "⏰ Time's up!")
            alarm_times.remove(now)
        time.sleep(30)

# === World Clock ===
def get_world_time(city):
    tz = pytz.timezone(city)
    return datetime.datetime.now(tz).strftime('%H:%M:%S')

# === Quotes ===
def update_quote():
    quote_label.config(text=random.choice(quotes))
    clock.after(5000, update_quote)

# === Calendar ===
def show_calendar():
    now = datetime.datetime.now()
    cal_text = calendar.month(now.year, now.month)
    messagebox.showinfo(f"📅 Calendar ({now.year})", cal_text)

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

# === Countdown ===
def countdown_timer():
    t = simpledialog.askinteger("Countdown", "Enter seconds:")
    if t:
        def run():
            for i in range(t, 0, -1):
                countdown_display.config(text=f"Countdown: {i}s")
                time.sleep(1)
            countdown_display.config(text="")  # Clear after countdown
            messagebox.showinfo("Countdown", "⌛ Time's up!")
        threading.Thread(target=run, daemon=True).start()

from tkinter import simpledialog

def add_note():
    task = simpledialog.askstring("Add Note", "Enter your note:")
    if task:
        notes_text.insert(END, f"- {task}\n")

def remove_note():
    try:
        notes_text.delete("end-2l", "end-1l")  # Deletes the last line
    except:
        pass


# UI setup
clock=Tk()
clock.title('Digital Clock')
clock.geometry('1000x600')
clock.config(bg='Wheat')


# label_full_date = Label(clock, text="Digital Clock", font=('Helvetica', 20, "bold"), bg='Wheat', fg='red')
# label_full_date.pack(pady=10)

countdown_display = Label(clock, font=('Helvetica', 22, 'bold'), bg='Wheat', fg='red')
# countdown_display.pack(pady=5)
countdown_display.place(relx=0.5, y=60, anchor="center")  # Above greeting



label_greeting = Label(clock, font=('Helvetica', 25, 'bold'), bg='Wheat', fg='green')
# label_greeting.pack()
label_greeting.place(relx=0.5, y=20, anchor="center")  # Top center



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
quote_label.place(x=300, y=570)

weather_label = Label(clock, text="", font=('Arial', 12), bg='Wheat', fg='blue')
weather_label.place(x=800, y=540)



toggle_btn = Button(clock, text="12/24 Hour", command=toggle_format, font=('Arial', 14), bg='Blue', fg='white')
toggle_btn.place(x=720, y=480, width=130, height=40)


#  Exit Button 
exit_btn = Button(clock, text="Exit", command=clock.quit, font=('Arial', 14), bg='red', fg='white')
exit_btn.place(x=870, y=480, width=100, height=40)


#  Stopwatch 


stopwatch_label = Label(clock, text="00:00:00", font=('Arial', 20, 'bold'), bg='Wheat', fg='blue')
stopwatch_label.place(x=20, y=480)  # Moved up

Button(clock, text="Start", command=start_stopwatch, font=('Arial', 12), bg='Green', fg='white').place(x=150, y=480)
Button(clock, text="Stop", command=stop_stopwatch, font=('Arial', 12), bg='Orange', fg='white').place(x=210, y=480)
Button(clock, text="Reset", command=reset_stopwatch, font=('Arial', 12), bg='Gray', fg='white').place(x=270, y=480)

# Button(clock, text="Countdown", command=countdown_timer).place(x=650, y=520)
# Button(clock, text="Speak Time", command=announce_time).place(x=750, y=520)

Button(clock, text="Set Alarm", command=set_alarm, font=('Arial', 12), bg='brown', fg='white').place(x=340, y=480)
# Button(clock, text="Calendar", command=show_calendar, font=('Arial', 12), bg='purple', fg='white').place(x=440, y=480)
Button(clock, text="Toggle Theme", command=toggle_theme, font=('Arial', 12), bg='black', fg='white').place(x=550, y=480)


# speaker_img = PhotoImage(file="C:/Users/Dell/OneDrive/Desktop/sonal/project/ChatGPT Image Apr 12, 2025, 12_09_59 PM.png")  # <-- your speaker image path
speaker_button = Button(clock, text="🔊", command=announce_time, bg='Wheat', bd=0 ,font=("Arial",18))
speaker_button.place(x=950, y=50, width=32, height=32)

countdown_icon_btn = Button(clock, text="⏳", command=countdown_timer, font=("Arial", 18), bg='Wheat', bd=0)
countdown_icon_btn.place(x=950, y=90, width=32, height=32)

# Calendar Icon Button
# calendar_img = PhotoImage(file="C:/Users/Dell/OneDrive/Desktop/sonal/project/calendar_icon.png.png")
calendar_button = Button(clock, text="📅", command=show_calendar, font=("Arial", 18), bg='Wheat', bd=0)
calendar_button.place(x=950, y=10, width=32, height=32)  



# notes_list = Listbox(clock, height=6)
# notes_list.place(x=20, y=500, width=250)

# Top-left Notes section (adjusted size and position)
notes_text = Text(clock, height=7, width=10)
notes_text.place(x=10, y=35)  # Top-left corner

add_note_button = Button(clock, text="Add Note", command=add_note)
add_note_button.place(x=10, y=160)
remove_note_button = Button(clock, text="Remove", command=remove_note)
remove_note_button.place(x=10, y=190)



#function call 
get_weather()
update_quote()
date_time()
clock.mainloop()




                                                     #Jay Kumar Singh
