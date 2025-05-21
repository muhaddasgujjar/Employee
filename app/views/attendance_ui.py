import tkinter as tk

def open_attendance_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Attendance")
    win.geometry("400x300")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Attendance", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)
    tk.Label(frame, text="Employee ID", bg="#ffffff").pack()
    tk.Entry(frame, width=30).pack(pady=5)
    tk.Button(frame, text="Mark Present", bg="#4CAF50", fg="white").pack(pady=10)
    tk.Button(frame, text="Back", bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

