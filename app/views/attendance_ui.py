import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

def save_attendance_to_db(employee_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Change if your MySQL has a password
            database="employee"  # Change DB name if different
        )
        cursor = conn.cursor()
        # Assume a table `attendance` with columns: id (auto), employee_id (varchar), date (datetime)
        query = "INSERT INTO attendance (employee_id, attendance_date) VALUES (%s, %s)"
        attendance_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(query, (employee_id, attendance_date))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return False

def open_attendance_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Attendance")
    win.geometry("400x300")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Attendance", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)

    tk.Label(frame, text="Employee ID", bg="#ffffff").pack()
    emp_id_entry = tk.Entry(frame, width=30)
    emp_id_entry.pack(pady=5)

    def on_mark_present():
        emp_id = emp_id_entry.get().strip()
        if not emp_id:
            messagebox.showwarning("Input Error", "Please enter Employee ID.")
            return
        if save_attendance_to_db(emp_id):
            messagebox.showinfo("Success", "✅ Attendance marked successfully.")
            emp_id_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Database Error", "❌ Could not save attendance. Check DB connection.")

    tk.Button(frame, text="Mark Present", bg="#4CAF50", fg="white", command=on_mark_present).pack(pady=10)
    tk.Button(frame, text="Back", bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("400x300")

    def show_main():
        root.deiconify()

    def open_attendance():
        root.withdraw()
        open_attendance_ui(root, show_main)

    tk.Button(root, text="Open Attendance", command=open_attendance).pack(pady=50)

    root.mainloop()
