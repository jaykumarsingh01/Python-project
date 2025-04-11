from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime
import time as tm
import threading
import random

# === Global Variables ===
is_24_hour = False
dark_theme = False
stopwatch_running = False
stopwatch_counter = 0

# === Greetings ===
quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Dream it. Wish it. Do it.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Little things make big days."
]

# === Functions ===
def toggle_format():
    global is_24_hour
    is_24_hour = not is_24_hour

def toggle_theme():
    global dark_theme
    dark_theme = not dark_theme
    apply_theme()

def apply_theme():
    bg_color = "black" if dark_theme else "Wheat"
    fg_color = "white" if dark_theme else "black"
    clock.config(bg=bg_color)
    label_greeting.config(bg=bg_color, fg='green')
    label_timezone.config(bg=bg_color, fg=fg_color)
    quote_label.config(bg=bg_color, fg='purple')
    for widget in clock.winfo_children():
        if isinstance(widget, Label) and "clock" not in str(widget):
            widget.config(bg=bg_color, fg=fg_color)

def get_greeting():
    hour = int(datetime.datetime.now().strftime('%H'))
    if hour < 12:
        return "Good Morning ☀️"
    elif hour < 18:
        return "Good Afternoon 🌞"
    else:
        return "Good Evening 🌙"

def update_quote():
    quote_label.config(text=random.choice(quotes))
    quote_label.after(10000, update_quote)

def update_time():
    time_now = datetime.datetime.now()
    hr = time_now.strftime('%H' if is_24_hour else '%I')
    am_pm = '' if is_24_hour else time_now.strftime('%p')
    min = time_now.strftime('%M')
    sec = time_now.strftime('%S')
    date = time_now.strftime("%d")
    month = time_now.strftime("%m")
    year = time_now.strftime("%Y")
    day = time_now.strftime("%A")

    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am_pm)
    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    label_greeting.config(text=get_greeting())
    label_timezone.config(text="Indian Standard Time (IST)")
    world_clock.config(text="UTC Time: " + datetime.datetime.utcnow().strftime('%H:%M:%S'))
    lab_hr.after(1000, update_time)

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
    alarm_time = alarm_entry.get()
    if alarm_time:
        threading.Thread(target=check_alarm, args=(alarm_time,), daemon=True).start()

def check_alarm(alarm_time):
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == alarm_time:
            messagebox.showinfo("Alarm", f"⏰ It's {alarm_time} now!")
            break
        tm.sleep(30)

# === GUI Setup ===
clock = Tk()
clock.title("Advanced Digital Clock")
clock.geometry("1050x650")
clock.resizable(False, False)
clock.config(bg="Wheat")

# === Greeting ===
label_greeting = Label(clock, font=('Helvetica', 25, 'bold'), bg='Wheat', fg='green')
label_greeting.pack()

# === Main Time Labels ===
lab_hr = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_hr.place(x=120, y=50, height=110, width=100)
Label(clock, text="Hour", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=120, y=170)

lab_min = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_min.place(x=340, y=50, height=110, width=100)
Label(clock, text="Min.", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=340, y=170)

lab_sec = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_sec.place(x=560, y=50, height=110, width=100)
Label(clock, text="Sec.", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=560, y=170)

lab_am = Label(clock, text="AM", font=('Times New Roman', 40, "bold"), bg='black', fg="white")
lab_am.place(x=780, y=50, height=110, width=100)
Label(clock, text="AM/PM", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=780, y=170)

# === Date ===
lab_date = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_date.place(x=120, y=270, height=110, width=100)
Label(clock, text="Date", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=120, y=390)

lab_mon = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_mon.place(x=340, y=270, height=110, width=100)
Label(clock, text="Month", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=340, y=390)

lab_year = Label(clock, text="0000", font=('Times New Roman', 45, "bold"), bg='black', fg="white")
lab_year.place(x=560, y=270, height=110, width=120)
Label(clock, text="Year", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=560, y=390)

lab_day = Label(clock, text="Day", font=('Times New Roman', 50, "bold"), bg='black', fg="white")
lab_day.place(x=780, y=270, height=110, width=120)
Label(clock, text="Day", font=('Times New Roman', 20, "bold"), bg='black', fg="white").place(x=780, y=390)

# === Extra Info ===
label_timezone = Label(clock, text="Indian Standard Time (IST)", font=('Arial', 14, 'italic'), bg='Wheat', fg='black')
label_timezone.place(x=20, y=600)

world_clock = Label(clock, text="", font=('Arial', 14, 'italic'), bg='Wheat', fg='black')
world_clock.place(x=350, y=600)

quote_label = Label(clock, text="", font=('Courier', 14, 'italic'), bg='Wheat', fg='purple')
quote_label.place(x=20, y=570)

# === Buttons ===
Button(clock, text="Toggle 12/24", command=toggle_format, font=('Arial', 12), bg='Blue', fg='white').place(x=720, y=570)
Button(clock, text="Theme", command=toggle_theme, font=('Arial', 12), bg='Gray', fg='white').place(x=860, y=570)
Button(clock, text="Exit", command=clock.quit, font=('Arial', 12), bg='Red', fg='white').place(x=960, y=570)

# === Stopwatch ===
stopwatch_label = Label(clock, text="00:00:00", font=('Arial', 20, 'bold'), bg='Wheat', fg='blue')
stopwatch_label.place(x=50, y=460)
Button(clock, text="Start", command=start_stopwatch, font=('Arial', 10), bg='Green', fg='white').place(x=200, y=460)
Button(clock, text="Stop", command=stop_stopwatch, font=('Arial', 10), bg='Orange', fg='white').place(x=260, y=460)
Button(clock, text="Reset", command=reset_stopwatch, font=('Arial', 10), bg='Gray', fg='white').place(x=320, y=460)

# === Alarm Section ===
alarm_entry = Entry(clock, font=('Arial', 14), width=10)
alarm_entry.place(x=600, y=460)
alarm_entry.insert(0, "HH:MM")
Button(clock, text="Set Alarm", command=set_alarm, font=('Arial', 12), bg='purple', fg='white').place(x=720, y=460)

# === Start Clock ===
update_time()
update_quote()
clock.mainloop()
