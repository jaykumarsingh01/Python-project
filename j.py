from tkinter import *
import datetime

# ==== Function to create time/date block ====
def create_label(parent, text, x, y, font_size=60):
    label = Label(parent, text="00", font=('Times New Roman', font_size, "bold"), bg='black', fg="white")
    label.place(x=x, y=y, height=110, width=100)
    return label

def create_text_label(parent, text, x, y):
    label = Label(parent, text=text, font=('Times New Roman', 20, "bold"), bg='black', fg="white")
    label.place(x=x, y=y, height=40, width=100)
    return label

# ==== Time Update Logic ====
def update_time():
    now = datetime.datetime.now()

    label_hour.config(text=now.strftime('%I'))
    label_minute.config(text=now.strftime('%M'))
    label_second.config(text=now.strftime('%S'))
    label_am_pm.config(text=now.strftime('%p'))

    label_day.config(text=now.strftime('%a'))
    label_date.config(text=now.strftime('%d'))
    label_month.config(text=now.strftime('%b'))  # abbreviated month name
    label_year.config(text=now.strftime('%Y'))

    label_full_date.config(text=now.strftime("%A, %B %d, %Y"))  # Full date string

    clock.after(1000, update_time)  # update every second

# ==== Setup GUI ====
clock = Tk()
clock.title('Digital Clock')
clock.geometry('1000x600')
clock.config(bg='Wheat')

# ==== Top Full Date Label ====
label_full_date = Label(clock, text="", font=('Helvetica', 20, "bold"), bg='Wheat', fg='black')
label_full_date.pack(pady=10)

# ==== Time Section ====
label_hour = create_label(clock, "00", 100, 70)
create_text_label(clock, "Hour", 100, 190)

label_minute = create_label(clock, "00", 280, 70)
create_text_label(clock, "Min.", 280, 190)

label_second = create_label(clock, "00", 460, 70)
create_text_label(clock, "Sec.", 460, 190)

label_am_pm = create_label(clock, "AM", 640, 70, font_size=40)
create_text_label(clock, "AM/PM", 640, 190)

# ==== Date Section ====
label_date = create_label(clock, "00", 100, 300)
create_text_label(clock, "Date", 100, 440)

label_month = create_label(clock, "00", 280, 300)
create_text_label(clock, "Month", 280, 440)

label_year = create_label(clock, "00", 460, 300)
create_text_label(clock, "Year", 460, 440)

label_day = create_label(clock, "Day", 640, 300, font_size=50)
create_text_label(clock, "Day", 640, 440)

# ==== Exit Button ====
exit_btn = Button(clock, text="Exit", command=clock.quit, font=('Arial', 14), bg='black', fg='white')
exit_btn.place(x=870, y=520, width=100, height=40)

# Start the clock
update_time()
clock.mainloop()
