# Enhanced Digital Clock App - All features in one

from tkinter import *
from tkinter import messagebox, simpledialog
import datetime
import time
import threading
import random
import calendar
import pytz
import requests

# === Settings and Globals ===
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
def get_weather():
    try:
        api_key = "YOUR_OPENWEATHERMAP_API_KEY"
        city = "Delhi"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        res = requests.get(url).json()
        temp = res['main']['temp']
        condition = res['weather'][0]['description'].capitalize()
        weather_label.config(text=f"{city}: {temp}°C, {condition}")
    except:
        weather_label.config(text="Weather: Unable to fetch")

# === Clock Update ===
def toggle_format():
    global is_24_hour
    is_24_hour = not is_24_hour

def date_time():
    time_now = datetime.datetime.now()
    hr = time_now.strftime('%H') if is_24_hour else time_now.strftime('%I')
    am = '' if is_24_hour else time_now.strftime('%p')
    lab_hr.config(text=hr)
    lab_min.config(text=time_now.strftime('%M'))
    lab_sec.config(text=time_now.strftime('%S'))
    lab_am.config(text=am)
    lab_date.config(text=time_now.strftime('%d'))
    lab_mon.config(text=time_now.strftime('%m'))
    lab_year.config(text=time_now.strftime('%Y'))
    lab_day.config(text=time_now.strftime('%a'))
    label_greeting.config(text=get_greeting())
    label_timezone.config(text="Indian Standard Time (IST)")
    world_time_label.config(text=f"Tokyo: {get_world_time('Asia/Tokyo')} | New York: {get_world_time('America/New_York')}")
    lab_hr.after(200, date_time)

# === Greeting ===
def get_greeting():
    hour = int(datetime.datetime.now().strftime('%H'))
    if hour < 12:
        return "Good Morning ☀️"
    elif hour < 18:
        return "Good Afternoon 🌞"
    else:
        return "Good Evening 🌙"

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

# === GUI Setup ===
clock = Tk()
clock.title('🌟 Enhanced Digital Clock')
clock.geometry('1000x650')
clock.config(bg='Wheat')

# Greeting
label_greeting = Label(clock, font=('Helvetica', 25, 'bold'), bg='Wheat', fg='green')
label_greeting.pack()

# Time Labels
def create_time_label(text, x, y, font_size=60):
    label = Label(clock, text="00", font=('Times New Roman', font_size, "bold"), bg='black', fg="white")
    label.place(x=x, y=y, height=110, width=100)
    Label(clock, text=text, font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=x, y=y+140, height=40, width=100)
    return label

lab_hr = create_time_label("Hour", 120, 50)
lab_min = create_time_label("Min.", 340, 50)
lab_sec = create_time_label("Sec.", 560, 50)
lab_am = create_time_label("AM/PM", 780, 50, font_size=40)
lab_date = create_time_label("Date", 120, 270)
lab_mon = create_time_label("Month", 340, 270)
lab_year = create_time_label("Year", 560, 270, font_size=45)
lab_day = create_time_label("Day", 780, 270, font_size=50)

# Labels
label_timezone = Label(clock, text="", font=('Arial', 14, 'italic'), bg='Wheat', fg='black')
label_timezone.place(x=20, y=580)

world_time_label = Label(clock, text="", font=('Arial', 12), bg='Wheat', fg='darkblue')
world_time_label.place(x=20, y=610)

quote_label = Label(clock, font=('Arial', 14, 'italic'), bg='Wheat', fg='darkblue')
quote_label.place(x=300, y=610)

weather_label = Label(clock, text="", font=('Arial', 12), bg='Wheat', fg='blue')
weather_label.place(x=700, y=580)

# Buttons
Button(clock, text="12/24 Hour", command=toggle_format, font=('Arial', 14), bg='blue', fg='white').place(x=720, y=480, width=130, height=40)
Button(clock, text="Exit", command=clock.quit, font=('Arial', 14), bg='red', fg='white').place(x=870, y=480, width=100, height=40)
Button(clock, text="Start", command=start_stopwatch, font=('Arial', 12), bg='green', fg='white').place(x=150, y=480)
Button(clock, text="Stop", command=stop_stopwatch, font=('Arial', 12), bg='orange', fg='white').place(x=210, y=480)
Button(clock, text="Reset", command=reset_stopwatch, font=('Arial', 12), bg='gray', fg='white').place(x=270, y=480)
stopwatch_label = Label(clock, text="00:00:00", font=('Arial', 20, 'bold'), bg='Wheat', fg='blue')
stopwatch_label.place(x=20, y=480)

Button(clock, text="Set Alarm", command=set_alarm, font=('Arial', 12), bg='brown', fg='white').place(x=340, y=480)
Button(clock, text="Calendar", command=show_calendar, font=('Arial', 12), bg='purple', fg='white').place(x=440, y=480)
Button(clock, text="Toggle Theme", command=toggle_theme, font=('Arial', 12), bg='black', fg='white').place(x=550, y=480)

# Start Functions
update_quote()
get_weather()
date_time()
clock.mainloop()
