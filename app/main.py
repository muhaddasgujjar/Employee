# main.py
import tkinter as tk
from tkinter import ttk
from app.views.login import open_login_ui
from app.views.employee_ui import open_employee_profile_ui
from app.views.leave_ui import open_leave_ui
from app.views.attendance_ui import open_attendance_ui
from app.views.payroll_ui import open_payroll_ui
from app.views.performance_ui import open_performance_ui
from app.views.department_ui import open_department_ui

# Global root to avoid multiple windows
root = tk.Tk()
root.title("HR Management System")
root.geometry("600x700")
root.configure(bg="#e6f2ff")

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def open_dashboard():
    clear_window()

    # Title Frame
    title_frame = tk.Frame(root, bg="#002b45", height=100)
    title_frame.pack(fill="x")

    title_label = tk.Label(title_frame, text="HR Management Dashboard",
                           font=("Helvetica", 20, "bold"), bg="#002b45", fg="white")
    title_label.pack(pady=30)

    # Main Buttons Frame
    button_frame = tk.Frame(root, bg="#ffffff", padx=40, pady=40, bd=3, relief=tk.RIDGE)
    button_frame.place(relx=0.5, rely=0.55, anchor="center")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Custom.TButton",
                    font=("Segoe UI", 12, "bold"),
                    padding=12,
                    width=35,
                    background="#ffffff",
                    foreground="#002b45",
                    borderwidth=1)
    style.map("Custom.TButton",
              background=[("active", "#005792")],
              foreground=[("active", "#ffffff")])

    ttk.Button(button_frame, text="1. Login / Role Access",
               style="Custom.TButton", command=lambda: open_login_ui(root, open_dashboard)).pack(pady=10)
    ttk.Button(button_frame, text="2. Add / Edit Employee Profile",
               style="Custom.TButton", command=lambda: open_employee_profile_ui(root, open_dashboard)).pack(pady=10)
    ttk.Button(button_frame, text="3. Leave Management",
               style="Custom.TButton", command=lambda: open_leave_ui(root, open_dashboard)).pack(pady=10)
    ttk.Button(button_frame, text="4. Attendance",
               style="Custom.TButton", command=lambda: open_attendance_ui(root, open_dashboard)).pack(pady=10)
    ttk.Button(button_frame, text="5. Payroll Management",
               style="Custom.TButton", command=lambda: open_payroll_ui(root, open_dashboard)).pack(pady=10)
    ttk.Button(button_frame, text="6. Performance Evaluation",
               style="Custom.TButton", command=lambda: open_performance_ui(root, open_dashboard)).pack(pady=10)
    ttk.Button(button_frame, text="7. Department Management",
               style="Custom.TButton", command=lambda: open_department_ui(root, open_dashboard)).pack(pady=10)

def show_login_screen():
    clear_window()

    def verify_credentials():
        username = username_entry.get()
        password = password_entry.get()

        if username == "muhaddas" and password == "admin123":
            open_dashboard()
        else:
            error_label.config(text="Access Denied! Invalid credentials.", fg="red")

    login_frame = tk.Frame(root, bg="#ffffff", padx=40, pady=40, bd=3, relief=tk.RIDGE)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(login_frame, text="Login", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#002b45").pack(pady=10)

    tk.Label(login_frame, text="Username:", bg="#ffffff", anchor="w").pack(fill="x")
    username_entry = tk.Entry(login_frame, font=("Segoe UI", 12))
    username_entry.pack(fill="x", pady=5)

    tk.Label(login_frame, text="Password:", bg="#ffffff", anchor="w").pack(fill="x")
    password_entry = tk.Entry(login_frame, show="*", font=("Segoe UI", 12))
    password_entry.pack(fill="x", pady=5)

    error_label = tk.Label(login_frame, text="", bg="#ffffff")
    error_label.pack()

    login_btn = tk.Button(login_frame, text="Login", bg="#005792", fg="white", font=("Segoe UI", 12, "bold"),
                          command=verify_credentials)
    login_btn.pack(pady=15)

# Start from login screen
show_login_screen()
root.mainloop()