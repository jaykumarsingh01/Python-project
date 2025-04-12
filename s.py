# Enhanced version of your Digital Clock
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

# === Globals ===
is_24_hour = False
stopwatch_running = False
stopwatch_counter = 0
is_dark = False
alarm_times = []
preferences_file = "preferences.json"
city = "Delhi"
speech_engine = pyttsx3.init()

# === Load Preferences ===
def load_preferences():
    global is_24_hour, is_dark, city
    if os.path.exists(preferences_file):
        with open(preferences_file, "r") as f:
            prefs = json.load(f)
            is_24_hour = prefs.get("is_24_hour", False)
            is_dark = prefs.get("is_dark", False)
            city = prefs.get("city", "Delhi")

def save_preferences():
    with open(preferences_file, "w") as f:
        json.dump({"is_24_hour": is_24_hour, "is_dark": is_dark, "city": city}, f)

# === Weather ===
def get_weather():
    try:
        api_key = "bd6f1dd81d2f2eb8414a656ec18c6ef5"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        res = requests.get(url).json()
        temp = res['main']['temp']
        condition = res['weather'][0]['description'].capitalize()
        weather_label.config(text=f"{city}: {temp}°C, {condition}")
    except Exception as e:
        weather_label.config(text="Weather: Error")

# === Time Functions ===
def toggle_format():
    global is_24_hour
    is_24_hour = not is_24_hour
    save_preferences()

def announce_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speech_engine.say(f"The time is {now}")
    speech_engine.runAndWait()

def get_greeting():
    hour = int(datetime.datetime.now().strftime('%H'))
    if hour < 12:
        return "Good Morning ☀️"
    elif hour < 18:
        return "Good Afternoon 🌞"
    else:
        return "Good Evening 🌙"

def date_time():
    now = datetime.datetime.now()
    if is_24_hour:
        hr = now.strftime('%H')
        am = ''
    else:
        hr = now.strftime('%I')
        am = now.strftime('%p')
    
    lab_hr.config(text=hr)
    lab_min.config(text=now.strftime('%M'))
    lab_sec.config(text=now.strftime('%S'))
    lab_am.config(text=am)
    lab_date.config(text=now.strftime('%d'))
    lab_mon.config(text=now.strftime('%m'))
    lab_year.config(text=now.strftime('%Y'))
    lab_day.config(text=now.strftime('%A'))
    label_greeting.config(text=get_greeting())
    label_timezone.config(text="Indian Standard Time (IST)")
    world_time_label.config(text=f"Tokyo: {get_world_time('Asia/Tokyo')} | NY: {get_world_time('America/New_York')}")
    lab_hr.after(1000, date_time)

# === Stopwatch ===
def update_stopwatch():
    global stopwatch_counter
    if stopwatch_running:
        stopwatch_counter += 1
        hrs = stopwatch_counter // 3600
        mins = (stopwatch_counter % 3600) // 60
        secs = stopwatch_counter % 60
        stopwatch_label.config(text=f"{hrs:02}:{mins:02}:{secs:02}")
        stopwatch_label.after(1000, update_stopwatch)

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

# === Quote ===
def update_quote():
    quote_label.config(text=random.choice(quotes))
    clock.after(5000, update_quote)

quotes = [
    "Stay positive, work hard, make it happen.",
    "Success is no accident.",
    "Push yourself, no one else will.",
    "Great things come from stepping out of comfort.",
    "Light tomorrow with today!"
]

# === Theme ===
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
    save_preferences()

# === Countdown ===
def countdown_timer():
    t = simpledialog.askinteger("Countdown", "Enter seconds:")
    if t:
        def run():
            for i in range(t, 0, -1):
                stopwatch_label.config(text=f"Countdown: {i}s")
                time.sleep(1)
            messagebox.showinfo("Countdown", "⌛ Time's up!")
        threading.Thread(target=run, daemon=True).start()

# === To-Do ===
def add_note():
    task = simpledialog.askstring("Add Task", "Enter your note:")
    if task:
        notes_list.insert(END, task)

def remove_note():
    selected = notes_list.curselection()
    for i in selected[::-1]:
        notes_list.delete(i)

# === Main UI ===
clock = Tk()
clock.title('Enhanced Digital Clock')
clock.geometry('1000x650')
clock.config(bg='Wheat')
# clock.iconbitmap("C:/Users/Dell/OneDrive/Desktop/sonal/project/clock_icon.ico")

label_greeting = Label(clock, font=('Helvetica', 25, 'bold'), bg='Wheat', fg='green')
label_greeting.pack()

lab_hr = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_hr.place(x=120, y=50, height=110, width=100)
lab_min = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_min.place(x=340, y=50, height=110, width=100)
lab_sec = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_sec.place(x=560, y=50, height=110, width=100)
lab_am = Label(clock, text="AM", font=('Times New Roman', 40, "bold"), bg='black', fg="white")
lab_am.place(x=780, y=50, height=110, width=100)

lab_date = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_date.place(x=120, y=270, height=110, width=100)
lab_mon = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_mon.place(x=340, y=270, height=110, width=100)
lab_year = Label(clock, text="0000", font=('Times New Roman', 45, "bold"), bg='black', fg="white")
lab_year.place(x=560, y=270, height=110, width=120)
lab_day = Label(clock, text="Day", font=('Times New Roman', 50, "bold"), bg='black', fg="white")
lab_day.place(x=780, y=270, height=110, width=100)

label_timezone = Label(clock, text="", font=('Arial', 14, 'italic'), bg='Wheat', fg='black')
label_timezone.place(x=20, y=520)
world_time_label = Label(clock, text="", font=('Arial', 12), bg='Wheat', fg='darkblue')
world_time_label.place(x=20, y=558)
quote_label = Label(clock, font=('Arial', 14, 'italic'), bg='Wheat', fg='darkblue')
quote_label.place(x=300, y=570)
weather_label = Label(clock, text="", font=('Arial', 12), bg='Wheat', fg='blue')
weather_label.place(x=800, y=540)

stopwatch_label = Label(clock, text="00:00:00", font=('Arial', 20, 'bold'), bg='Wheat', fg='blue')
stopwatch_label.place(x=20, y=480)

Button(clock, text="Start", command=start_stopwatch).place(x=150, y=480)
Button(clock, text="Stop", command=stop_stopwatch).place(x=210, y=480)
Button(clock, text="Reset", command=reset_stopwatch).place(x=270, y=480)
Button(clock, text="Set Alarm", command=set_alarm).place(x=340, y=480)
Button(clock, text="Theme", command=toggle_theme).place(x=550, y=480)
Button(clock, text="Toggle Format", command=toggle_format).place(x=720, y=480)
Button(clock, text="Exit", command=clock.quit).place(x=870, y=480)
Button(clock, text="Countdown", command=countdown_timer).place(x=650, y=520)
Button(clock, text="Speak Time", command=announce_time).place(x=750, y=520)

calendar_img = PhotoImage(file="C:/Users/Dell/OneDrive/Desktop/sonal/project/calendar_icon.png.png")
calendar_button = Button(clock, image=calendar_img, command=lambda: messagebox.showinfo("Calendar", calendar.month(datetime.datetime.now().year, datetime.datetime.now().month)), bg='Wheat', bd=0)
calendar_button.place(x=950, y=10, width=32, height=32)

# === Notes Section ===
notes_list = Listbox(clock, height=6)
notes_list.place(x=20, y=580, width=250)
Button(clock, text="Add Note", command=add_note).place(x=280, y=580)
Button(clock, text="Remove", command=remove_note).place(x=360, y=580)

# Start App
# load_preferences()
get_weather()
update_quote()
date_time()
clock.mainloop()
