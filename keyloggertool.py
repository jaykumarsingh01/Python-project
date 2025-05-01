import tkinter as tk
from tkinter import messagebox
import psutil
import datetime
import threading

# List of suspicious keywords
SUSPICIOUS_KEYWORDS = ['keylog', 'hook', 'logger', 'spy', 'capture', 'record', 'keyboard']
log_file = "keylogger_alerts.txt"

# Scan running processes for suspicious activity
def scan_processes():
    detected = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pname = proc.info['name'].lower()
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in pname:
                    detected.append(f"{pname} (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return detected

# Log detections to file with timestamp
def log_to_file(entries):
    with open(log_file, "a") as f:
        f.write(f"\n[{datetime.datetime.now()}] Suspicious Process Detected:\n")
        for entry in entries:
            f.write(f" - {entry}\n")


# GUI output
def update_gui():
    results = scan_processes()
    output_text.delete(1.0, tk.END)
    if results:
        output_text.insert(tk.END, "Suspicious processes detected:\n\n")
        for res in results:
            output_text.insert(tk.END, f"- {res}\n")
        log_to_file(results)
    else:
        output_text.insert(tk.END, "No suspicious processes found.\n")

# Real-time monitor (runs every 10 seconds)
def real_time_monitor():
    while True:
        update_gui()
        threading.Event().wait(10)

# Start real-time scanning in a thread
def start_monitor():
    monitor_thread = threading.Thread(target=real_time_monitor, daemon=True)
    monitor_thread.start()
    messagebox.showinfo("Monitor Started", "Real-time monitoring activated.")

# GUI setup
root = tk.Tk()
root.title("Advanced Keylogger Detection Tool")
root.geometry("550x430")
root.resizable(False, False)

title = tk.Label(root, text="Keylogger Detection Tool", font=("Arial", 16, "bold"))
title.pack(pady=10)

scan_btn = tk.Button(root, text="Run One-Time Scan", command=update_gui, bg="#4682B4", fg="white", font=("Arial", 12))
scan_btn.pack(pady=5)

start_btn = tk.Button(root, text="Start Real-Time Monitor", command=start_monitor, bg="#dc143c", fg="white", font=("Arial", 12))
start_btn.pack(pady=5)

output_text = tk.Text(root, height=15, width=65, wrap="word")
output_text.pack(pady=10)

footer = tk.Label(root, text="Suspicious activity is also logged to keylogger_alerts.txt", font=("Arial", 9), fg="gray")
footer.pack(pady=5)

root.mainloop()
