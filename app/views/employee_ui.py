import tkinter as tk

def open_employee_profile_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Employee Profile")
    win.geometry("400x400")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Employee Profile", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)
    tk.Label(frame, text="Name", bg="#ffffff").pack()
    tk.Entry(frame, width=30).pack(pady=5)
    tk.Label(frame, text="Designation", bg="#ffffff").pack()
    tk.Entry(frame, width=30).pack(pady=5)
    tk.Button(frame, text="Save", bg="#4CAF50", fg="white").pack(pady=10)
    tk.Button(frame, text="Back", width=10, bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

