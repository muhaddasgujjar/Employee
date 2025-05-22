import tkinter as tk
from tkinter import messagebox
import mysql.connector

def save_leave_to_db(emp_name, leave_dates):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Change to your MySQL password if set
            database="employee"  # Assuming the same DB; change if needed
        )
        cursor = conn.cursor()
        query = "INSERT INTO leave_requests (employee_name, leave_dates) VALUES (%s, %s)"
        cursor.execute(query, (emp_name, leave_dates))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return False

def open_leave_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Leave Management")
    win.geometry("400x350")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Leave Management", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)

    tk.Label(frame, text="Employee Name", bg="#ffffff").pack()
    emp_name_entry = tk.Entry(frame, width=30)
    emp_name_entry.pack(pady=5)

    tk.Label(frame, text="Leave Dates", bg="#ffffff").pack()
    leave_dates_entry = tk.Entry(frame, width=30)
    leave_dates_entry.pack(pady=5)

    def on_submit():
        emp_name = emp_name_entry.get().strip()
        leave_dates = leave_dates_entry.get().strip()

        if not emp_name or not leave_dates:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        if save_leave_to_db(emp_name, leave_dates):
            messagebox.showinfo("Success", "✅ Leave request saved successfully.")
            # Clear fields after successful save
            emp_name_entry.delete(0, tk.END)
            leave_dates_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Database Error", "❌ Could not save data. Check DB connection.")

    tk.Button(frame, text="Submit", bg="#4CAF50", fg="white", command=on_submit).pack(pady=10)
    tk.Button(frame, text="Back", bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

# Example usage (you can integrate this function into your main UI as needed)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("400x300")

    def show_main():
        root.deiconify()

    def open_leave():
        root.withdraw()
        open_leave_ui(root, show_main)

    tk.Button(root, text="Open Leave Management", command=open_leave).pack(pady=50)

    root.mainloop()
