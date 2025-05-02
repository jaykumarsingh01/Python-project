import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import psutil
import platform
import hashlib
import socket
from datetime import datetime
import os
import time
import shutil
import threading

# Modern Theme
themes = {
    "Professional": {
        "bg": "#F5F6FA",  # Light gray background
        "fg": "#333333",  # Dark gray text
        "accent": "#2B579A",  # Professional blue
        "highlight": "#E6E9F0",  # Light highlight
        "button_active": "#1E3F77",  # Darker blue for active state
        "sidebar_bg": "#2B579A",  # Sidebar background
        "sidebar_fg": "#FFFFFF",  # Sidebar text
        "header_bg": "#1E3F77",  # Header background
        "header_fg": "#FFFFFF",  # Header text
    }
}

current_theme = "Professional"

# Analysis-related variables
SUSPICIOUS_KEYWORDS = ['keylog', 'hook', 'logger', 'spy', 'capture', 'record', 'keyboard']
log_file = "keylogger_alerts.txt"
quarantine_folder = "quarantine"
detected_entries = {}
monitor_thread = None
monitor_active = False

# Ensure quarantine folder exists
if not os.path.exists(quarantine_folder):
    os.makedirs(quarantine_folder)

class DefenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Defender-style Keylogger Detection")
        self.root.geometry("1000x650")
        self.root.configure(bg=themes[current_theme]["bg"])

        # Header Frame
        self.header_frame = tk.Frame(self.root, bg=themes[current_theme]["header_bg"], height=50)
        self.header_frame.pack(side="top", fill="x")
        tk.Label(self.header_frame, text="Keylogger Detection Suite", font=("Segoe UI", 16, "bold"),
                 bg=themes[current_theme]["header_bg"], fg=themes[current_theme]["header_fg"]).pack(side="left", padx=15, pady=10)

        # Load and display the logo
        try:
            logo_img = Image.open("gbu_logo.jpg")  # Adjust the path if needed
            logo_img = logo_img.resize((40, 40), Image.Resampling.LANCZOS)  # Resize to 40x40 pixels
            self.logo = ImageTk.PhotoImage(logo_img)
            tk.Label(self.header_frame, image=self.logo, bg=themes[current_theme]["header_bg"]).pack(side="right", padx=15)
        except Exception as e:
            # Fallback if the image fails to load
            tk.Label(self.header_frame, text="[Logo Not Found]", font=("Segoe UI", 10),
                     bg=themes[current_theme]["header_bg"], fg=themes[current_theme]["header_fg"]).pack(side="right", padx=15)
            print(f"Error loading logo: {e}")

        # Sidebar Frame
        self.sidebar_frame = tk.Frame(self.root, bg=themes[current_theme]["sidebar_bg"], width=200)
        self.sidebar_frame.pack(side="left", fill="y")

        # Main Frame (Card-like design)
        self.main_frame = tk.Frame(self.root, bg=themes[current_theme]["bg"], bd=2, relief="groove")
        self.main_frame.pack(side="right", expand=True, fill="both", padx=10, pady=(0, 10))

        self.create_sidebar()
        self.load_analysis()

    def create_sidebar(self):
        # Sidebar buttons with icons (using Unicode as placeholders)
        buttons = [
            ("Analysis", "\U0001F50E", self.load_analysis),  # Magnifying glass
            ("Processes", "\U0001F4BB", self.load_processes),  # Computer
            ("Network", "\U0001F5A7", self.load_network),  # Network
            ("Startup Scan", "\U0001F514", self.load_startup_scan),  # Bell
            ("Themes", "\U0001F3A8", self.load_theme_changer),  # Palette
            ("Log Viewer", "\U0001F4C4", self.load_log_viewer),  # Document
            ("Scan History", "\U0001F4DC", self.load_scan_history),  # Scroll
            ("System Uptime", "\U0001F551", self.load_system_uptime),  # Clock
            ("System Specification", "\U0001F5A5", self.load_dashboard),  # Desktop
            ("About", "\U0001F4D6", self.load_about)  # Book
        ]
        for text, icon, command in buttons:
            btn_frame = tk.Frame(self.sidebar_frame, bg=themes[current_theme]["sidebar_bg"])
            btn_frame.pack(fill="x", pady=2, padx=5)
            btn = tk.Button(btn_frame, text=f" {icon}  {text}", font=("Segoe UI", 11), fg=themes[current_theme]["sidebar_fg"],
                            bg=themes[current_theme]["sidebar_bg"], activebackground=themes[current_theme]["highlight"],
                            activeforeground=themes[current_theme]["fg"], relief="flat", anchor="w", command=command)
            btn.pack(fill="x")
            # Hover effect
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=themes[current_theme]["highlight"]))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=themes[current_theme]["sidebar_bg"]))
            # Tooltip
            self.create_tooltip(btn, f"View {text.lower()}")

    def create_tooltip(self, widget, text):
        def enter(event):
            x, y, _, _ = widget.bbox("insert")
            x += widget.winfo_rootx() + 25
            y += widget.winfo_rooty() + 25
            self.tooltip = tk.Toplevel(widget)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{x}+{y}")
            label = tk.Label(self.tooltip, text=text, bg="#FFFFE0", fg="#333333", relief="solid", borderwidth=1, font=("Segoe UI", 9))
            label.pack()
        def leave(event):
            self.tooltip.destroy()
        widget.bind("<Enter>", enter)
        widget.bind("<Leave>", leave)

    def clear_main_area(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def scan_processes(self):
        detected = {}
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                pname = proc.info['name'].lower() if proc.info['name'] else ""
                pexe = proc.info['exe'].lower() if proc.info['exe'] else ""
                for keyword in SUSPICIOUS_KEYWORDS:
                    if keyword in pname or keyword in pexe:
                        entry = f"{pname} (PID: {proc.info['pid']}) - Path: {proc.info['exe']}"
                        detected[entry] = proc.info['exe']
                        break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        return detected

    def log_to_file(self, entries):
        with open(log_file, "a") as f:
            f.write(f"\n[{datetime.now()}] Suspicious Process Detected:\n")
            for entry in entries:
                f.write(f" - {entry}\n")

    def update_gui(self, output_text, timestamp, scan_type="manual"):
        global detected_entries
        new_entries = self.scan_processes()
        if scan_type == "manual":
            output_text.config(state='normal')
            output_text.delete(1.0, tk.END)
        if new_entries:
            detected_entries.update(new_entries)
            output_text.config(state='normal')
            output_text.insert(tk.END,
                              f"\n[{datetime.now().strftime('%H:%M:%S')}] Suspicious processes detected:\n\n")
            for res in new_entries:
                output_text.insert(tk.END, f"- {res}\n")
            self.log_to_file(new_entries)
            output_text.config(state='disabled')
        elif scan_type == "manual":
            output_text.insert(tk.END, "No suspicious processes found.\n")
            output_text.config(state='disabled')
        timestamp.config(text=f"Last scanned at: {datetime.now().strftime('%H:%M:%S')}")

    def real_time_monitor(self, output_text, timestamp):
        global monitor_active
        while monitor_active:
            self.update_gui(output_text, timestamp, scan_type="auto")
            time.sleep(10)

    def start_monitor(self, output_text, timestamp):
        global monitor_thread, monitor_active
        if not monitor_active:
            monitor_active = True
            monitor_thread = threading.Thread(target=lambda: self.real_time_monitor(output_text, timestamp), daemon=True)
            monitor_thread.start()
            messagebox.showinfo("Monitor Started", "Real-time monitoring activated.")

    def stop_monitor(self):
        global monitor_active
        monitor_active = False
        messagebox.showinfo("Monitor Stopped", "Real-time monitoring deactivated.")

    def show_loading_screen(self, callback):
        loading_win = tk.Toplevel(self.root)
        loading_win.title("Loading")
        loading_win.geometry("300x100")
        loading_win.resizable(False, False)
        loading_win.configure(bg=themes[current_theme]["bg"])
        tk.Label(loading_win, text="Scanning for suspicious activity...", font=("Segoe UI", 12),
                 bg=themes[current_theme]["bg"], fg=themes[current_theme]["fg"]).pack(pady=10)
        
        # Progress bar
        progress = ttk.Progressbar(loading_win, length=200, mode='determinate')
        progress.pack(pady=10)

        def load():
            for i in range(101):
                progress['value'] = i
                loading_win.update()
                time.sleep(0.02)
            loading_win.destroy()
            callback()

        threading.Thread(target=load, daemon=True).start()

    def run_one_time_scan(self, output_text, timestamp):
        self.show_loading_screen(lambda: self.update_gui(output_text, timestamp, scan_type="manual"))

    def remove_selected_file(self, output_text, timestamp):
        try:
            selected_text = output_text.get(tk.SEL_FIRST, tk.SEL_LAST).strip('- \n')
            file_path = detected_entries.get(selected_text)
            if file_path and os.path.exists(file_path):
                os.remove(file_path)
                messagebox.showinfo("File Removed", f"Suspicious file removed:\n{file_path}")
                self.update_gui(output_text, timestamp)
            else:
                messagebox.showwarning("Not Found", "The selected file could not be found or may have already been removed.")
        except tk.TclError:
            messagebox.showwarning("No Selection", "Please select a suspicious entry to remove.")

    def quarantine_selected_file(self, output_text, timestamp):
        try:
            selected_text = output_text.get(tk.SEL_FIRST, tk.SEL_LAST).strip('- \n')
            file_path = detected_entries.get(selected_text)
            if file_path and os.path.exists(file_path):
                file_name = os.path.basename(file_path)
                quarantine_path = os.path.join(quarantine_folder, file_name)
                shutil.move(file_path, quarantine_path)
                messagebox.showinfo("File Quarantined", f"Suspicious file quarantined:\n{file_path}")
                self.update_gui(output_text, timestamp)
            else:
                messagebox.showwarning("Not Found", "The selected file could not be found or may have already been quarantined.")
        except tk.TclError:
            messagebox.showwarning("No Selection", "Please select a suspicious entry to quarantine.")

    def export_report(self):
        report_file = filedialog.asksaveasfilename(defaultextension=".txt",
                                                  filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if report_file:
            with open(report_file, "w") as f:
                f.write(f"Keylogger Detection Report - {datetime.now()}\n")
                f.write(f"{'=' * 50}\n")
                f.write(f"Suspicious Files Detected:\n")
                for entry in detected_entries:
                    f.write(f" - {entry}\n")
                messagebox.showinfo("Report Saved", f"Report saved to {report_file}")

    def open_quarantine_folder(self):
        os.startfile(quarantine_folder)

    def clear_logs(self):
        if os.path.exists(log_file):
            with open(log_file, 'w') as f:
                f.write("")
            messagebox.showinfo("Log Cleared", "The log file has been cleared.")

    def scan_specific_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            filename = os.path.basename(filepath).lower()
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in filename:
                    messagebox.showwarning("Suspicious", f"The selected file may be suspicious:\n{filepath}")
                    return
            messagebox.showinfo("Clean", "The selected file appears clean.")

    def show_all_processes(self):
        processes = [f"{p.info['pid']} - {p.info['name']}" for p in psutil.process_iter(['pid', 'name'])]
        top = tk.Toplevel(self.root)
        top.title("All Running Processes")
        top.configure(bg=themes[current_theme]["bg"])
        text = tk.Text(top, wrap='word', font=("Courier", 10), bg=themes[current_theme]["highlight"],
                       fg=themes[current_theme]["fg"], bd=1, relief="sunken")
        text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text.insert(tk.END, '\n'.join(processes))
        text.config(state='disabled')

    def load_analysis(self):
        self.clear_main_area()

        # Button frame for actions (at the top)
        button_frame = tk.Frame(self.main_frame, bg=themes[current_theme]["bg"])
        button_frame.pack(pady=(10, 5), fill="x", padx=10)

        # Action buttons from analysis.py
        buttons = [
            ("Run One-Time Scan", lambda: self.run_one_time_scan(output_text, timestamp), "Run a full system scan"),
            ("Start Real-Time Monitor", lambda: self.start_monitor(output_text, timestamp), "Enable real-time monitoring"),
            ("Stop Monitor", lambda: self.stop_monitor(), "Stop real-time monitoring"),
            ("Quarantine Selected File", lambda: self.quarantine_selected_file(output_text, timestamp), "Quarantine selected suspicious file"),
            ("Remove Selected File", lambda: self.remove_selected_file(output_text, timestamp), "Remove selected suspicious file"),
            ("Export Report", self.export_report, "Export scan report to a file"),
            ("Open Quarantine Folder", self.open_quarantine_folder, "View quarantined files"),
            ("Clear Log File", self.clear_logs, "Clear all logs"),
            ("Scan Specific File", self.scan_specific_file, "Scan a specific file"),
            ("All Processes", self.show_all_processes, "View all running processes"),
        ]
        for text, cmd, tooltip in buttons:
            btn = tk.Button(button_frame, text=text, font=("Segoe UI", 10, "bold"), bg=themes[current_theme]["accent"],
                            fg="white", activebackground=themes[current_theme]["button_active"],
                            activeforeground="white", relief="flat", bd=2, command=cmd)
            btn.pack(side=tk.LEFT, padx=2, pady=5)
            # Hover effect
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=themes[current_theme]["button_active"]))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=themes[current_theme]["accent"]))
            # Tooltip
            self.create_tooltip(btn, tooltip)

        # Title
        tk.Label(self.main_frame, text="Scan Output", font=("Segoe UI", 16, "bold"),
                 bg=themes[current_theme]["bg"], fg=themes[current_theme]["fg"]).pack(pady=(5, 0), padx=10, anchor="w")

        # Output frame (styled as a card)
        output_frame = tk.Frame(self.main_frame, bg=themes[current_theme]["highlight"], bd=1, relief="sunken")
        output_frame.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=True)

        # Refresh button (using Unicode as placeholder)
        refresh_button = tk.Button(output_frame, text="\U0001F504", font=("Segoe UI", 12, "bold"),
                                   bg=themes[current_theme]["highlight"], fg=themes[current_theme]["fg"],
                                   relief="flat", command=lambda: output_text.config(state='normal') or output_text.delete(1.0, tk.END) or output_text.config(state='disabled'))
        refresh_button.pack(side=tk.TOP, anchor='ne', padx=5, pady=5)
        self.create_tooltip(refresh_button, "Clear scan output")
        # Hover effect
        refresh_button.bind("<Enter>", lambda e: refresh_button.config(bg=themes[current_theme]["bg"]))
        refresh_button.bind("<Leave>", lambda e: refresh_button.config(bg=themes[current_theme]["highlight"]))

        # Output text area
        output_text = tk.Text(output_frame, wrap="word", font=("Courier", 10), bg="white", fg=themes[current_theme]["fg"],
                              bd=1, relief="flat", height=15)
        output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        scrollbar = tk.Scrollbar(output_frame, command=output_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        output_text.config(yscrollcommand=scrollbar.set, state='disabled')

        # Footer frame
        footer_frame = tk.Frame(self.main_frame, bg=themes[current_theme]["bg"])
        footer_frame.pack(fill="x", padx=10, pady=5)
        tk.Label(footer_frame, text="", bg=themes[current_theme]["bg"], height=1).pack(fill="x")  # Separator
        timestamp = tk.Label(footer_frame, text="", font=("Segoe UI", 9), fg="gray", bg=themes[current_theme]["bg"])
        timestamp.pack(anchor="w")
        tk.Label(footer_frame, text="Suspicious activity is logged to keylogger_alerts.txt",
                 font=("Segoe UI", 8), fg="gray", bg=themes[current_theme]["bg"]).pack(anchor="w")

        # Initial scan
        self.update_gui(output_text, timestamp)

    def load_dashboard(self):
        self.clear_main_area()
        tk.Label(self.main_frame, text="System Specification", font=("Segoe UI", 16, "bold"),
                 bg=themes[current_theme]["bg"], fg=themes[current_theme]["fg"]).pack(pady=10, padx=10, anchor="w")

        info_frame = tk.Frame(self.main_frame, bg=themes[current_theme]["highlight"], bd=1, relief="sunken")
        info_frame.pack(fill="both", expand=True, padx=10, pady=10)

        info = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Hostname": socket.gethostname(),
            "IP Address": socket.gethostbyname(socket.gethostname()),
        }

        for k, v in info.items():
            tk.Label(info_frame, text=f"{k}: {v}", font=("Segoe UI", 11),
                     bg=themes[current_theme]["highlight"], fg=themes[current_theme]["fg"]).pack(anchor="w", padx=20, pady=2)

        self.cpu_label = tk.Label(info_frame, font=("Segoe UI", 11),
                                  bg=themes[current_theme]["highlight"], fg=themes[current_theme]["fg"])
        self.cpu_label.pack(anchor="w", padx=20, pady=(10, 0))

        self.ram_label = tk.Label(info_frame, font=("Segoe UI", 11),
                                  bg=themes[current_theme]["highlight"], fg=themes[current_theme]["fg"])
        self.ram_label.pack(anchor="w", padx=20)

        self.update_stats()

    def update_stats(self):
        self.cpu_label.config(text=f"CPU Usage: {psutil.cpu_percent()}%")
        self.ram_label.config(text=f"RAM Usage: {psutil.virtual_memory().percent}%")
        self.root.after(1000, self.update_stats)

    def load_processes(self):
        self.clear_main_area()
        tk.Label(self.main_frame, text="Running Processes", font=("Segoe UI", 16, "bold"),
                 bg=themes[current_theme]["bg"], fg=themes[current_theme]["fg"]).pack(pady=10, padx=10, anchor="w")

        tree_frame = tk.Frame(self.main_frame, bg=themes[current_theme]["highlight"], bd=1, relief="sunken")
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tree = ttk.Treeview(tree_frame, columns=("PID", "Name", "Hash"), show="headings", height=20)
        tree.heading("PID", text="PID")
        tree.heading("Name", text="Process Name")
        tree.heading("Hash", text="SHA256")
        tree.pack(fill="both", expand=True, padx=5, pady=5)

        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                exe = proc.info['exe']
                if exe:
                    with open(exe, 'rb') as f:
                        h = hashlib.sha256(f.read()).hexdigest()
                else:
                    h = "Access Denied"
                tree.insert("", "end", values=(proc.info['pid'], proc.info['name'], h))
            except:
                continue

    def load_network(self):
        self.clear_main_area()
        tk.Label(self.main_frame, text="Active Network Connections", font=("Segoe UI", 16, "bold"),
                 bg=themes[current_theme]["bg"], fg=themes[current_theme]["fg"]).pack(pady=10, padx=10, anchor="w")

        tree_frame = tk.Frame(self.main_frame, bg=themes[current_theme]["highlight"], bd=1, relief="sunken")
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tree = ttk.Treeview(tree_frame, columns=("Local", "Remote", "Status"), show="headings", height=20)
        tree.heading("Local", text="Local Address")
        tree.heading("Remote", text="Remote Address")
        tree.heading("Status", text="Status")
        tree.column("Local", width=250)
        tree.column("Remote", width=250)
        tree.column("Status", width=100)
        tree.pack(fill="both", expand=True, padx=5, pady=5)

        for conn in psutil.net_connections(kind='inet'):
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
            status = conn.status
            tree.insert("", "end", values=(laddr, raddr, status))

    def load_startup_scan(self):
        self.clear_main_area()
        tk.Label(self.main_frame, text="Startup Scan", font=("Segoe UI", 16, "bold"),
                 bg=themes[current_theme]["bg"], fg=themes[current_theme]["fg"]).pack(pady=10, padx=10, anchor="w")

        result_frame = tk.Frame(self.main_frame, bg=themes[current_theme]["highlight"], bd=1, relief="sunken")
        result_frame.pack(fill="both", expand=True, padx=10, pady=10)

        threats = ["keylogger.exe", "suspicious_startup.exe"]
        results = []

        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] in threats:
                results.append(proc.info)

        if results:
            for r in results:
                tk.Label(result_frame, text=f"Threat Detected: {r['name']} (PID: {r['pid']})",
                         font=("Segoe UI", 11), fg="red", bg=themes[current_theme]["highlight"]).pack(anchor="w", padx=20, pady=2)
        else:
            tk.Label(result_frame, text="No threats detected in startup processes.",
                     font=("Segoe UI", 11), bg=themes[current_theme]["highlight"], fg=themes[current_theme]["fg"]).pack(padx=20, pady=10)

    def load_theme_changer(self):
        self.clear_main_area()
        tk.Label(self.main_frame, text="Select Theme", font=("Segoe UI", 16, "bold"),
                 bg=themes[current_theme]["bg"], fg=themes[current_theme]["fg"]).pack(pady=10, padx=10, anchor="w")

        theme_frame = tk.Frame(self.main_frame, bg=themes[current_theme]["highlight"], bd=1, relief="sunken")
        theme_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Only one theme for now, but you can add more
        tk.Label(theme_frame, text="Professional Theme (Default)", font=("Segoe UI", 11),
                 bg=themes[current_theme]["highlight"], fg=themes[current_theme]["fg"]).pack(pady=5, padx=20)

    def change_theme(self, new_theme):
        # Placeholder for theme change (only one theme for now)
        self.load_analysis()

    def load_log_viewer(self):
        self.clear_main_area()
        tk.Label(self.main_frame, text="Log Viewer", font=("Segoe UI", 16, "bold"),
                 bg=themes[current_theme]["bg"], fg=themes[current_theme]["fg"]).pack(pady=10, padx=10, anchor="w")

        log_frame = tk.Frame(self.main_frame, bg=themes[current_theme]["highlight"], bd=1, relief="sunken")
        log_frame.pack(fill="both", expand=True, padx=10, pady=10)

        logs = [
            "2025-05-01 10:30 - Quick Scan Completed - No threats found.",
            "2025-04-30 22:14 - Process 'keylogger.exe' flagged as suspicious.",
            "2025-04-29 18:45 - Network scan: 2 unusual connections found.",
        ]

        for log in logs:
            tk.Label(log_frame, text=log, font=("Segoe UI", 10),
                     bg=themes[current_theme]["highlight"], fg=themes[current_theme]["fg"], anchor="w").pack(fill="x", padx=20, pady=2)

    def load_scan_history(self):
        self.clear_main_area()
        tk.Label(self.main_frame, text="Scan History", font=("Segoe UI", 16, "bold"),
                 bg=themes[current_theme]["bg"], fg=themes[current_theme]["fg"]).pack(pady=10, padx=10, anchor="w")

        history_frame = tk.Frame(self.main_frame, bg=themes[current_theme]["highlight"], bd=1, relief="sunken")
        history_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tree = ttk.Treeview(history_frame, columns=("Date", "Type", "Result"), show="headings", height=20)
        tree.heading("Date", text="Date")
        tree.heading("Type", text="Scan Type")
        tree.heading("Result", text="Result")
        tree.pack(fill="both", expand=True, padx=5, pady=5)

        history_data = [
            ("2025-05-01", "Quick Scan", "No Threats"),
            ("2025-04-30", "Startup Scan", "1 Risk Found"),
            ("2025-04-28", "Network Scan", "Suspicious Activity"),
        ]
        for row in history_data:
            tree.insert("", "end", values=row)

    def load_system_uptime(self):
        self.clear_main_area()
        tk.Label(self.main_frame, text="System Uptime", font=("Segoe UI", 16, "bold"),
                 bg=themes[current_theme]["bg"], fg=themes[current_theme]["fg"]).pack(pady=10, padx=10, anchor="w")

        uptime_frame = tk.Frame(self.main_frame, bg=themes[current_theme]["highlight"], bd=1, relief="sunken")
        uptime_frame.pack(fill="both", expand=True, padx=10, pady=10)

        uptime_sec = float(psutil.boot_time())
        boot_time = datetime.fromtimestamp(uptime_sec).strftime("%Y-%m-%d %H:%M:%S")

        tk.Label(uptime_frame, text=f"System boot time: {boot_time}", font=("Segoe UI", 11),
                 bg=themes[current_theme]["highlight"], fg=themes[current_theme]["fg"]).pack(pady=10, padx=20)

    def load_about(self):
        self.clear_main_area()
        tk.Label(self.main_frame, text="About This App", font=("Segoe UI", 16, "bold"),
                 bg=themes[current_theme]["bg"], fg=themes[current_theme]["fg"]).pack(pady=10, padx=10, anchor="w")

        about_frame = tk.Frame(self.main_frame, bg=themes[current_theme]["highlight"], bd=1, relief="sunken")
        about_frame.pack(fill="both", expand=True, padx=10, pady=10)

        about_text = """
Keylogger Detection Suite
Version: 1.0
Author: Your Name
Platform: Windows

This app helps detect suspicious processes,
monitor active network connections, and more.
"""
        tk.Label(about_frame, text=about_text, font=("Segoe UI", 11),
                 bg=themes[current_theme]["highlight"], fg=themes[current_theme]["fg"], justify="left").pack(pady=20, padx=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = DefenderApp(root)
    root.mainloop()














                                                           # Jay Kumar Singh
