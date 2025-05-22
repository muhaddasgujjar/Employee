import tkinter as tk
from tkinter import messagebox
import mysql.connector

def save_payroll_to_db(employee_id, salary):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Change if your MySQL has a password
            database="employee"  # Your database name
        )
        cursor = conn.cursor()
        # Assuming table payroll with columns: employee_id (VARCHAR), salary (FLOAT)
        query = "INSERT INTO payroll (employee_id, salary) VALUES (%s, %s)"
        cursor.execute(query, (employee_id, salary))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return False

def open_payroll_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Payroll Management")
    win.geometry("400x350")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Payroll Management", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)
    tk.Label(frame, text="Employee ID", bg="#ffffff").pack()
    emp_id_entry = tk.Entry(frame, width=30)
    emp_id_entry.pack(pady=5)

    tk.Label(frame, text="Salary", bg="#ffffff").pack()
    salary_entry = tk.Entry(frame, width=30)
    salary_entry.pack(pady=5)

    def on_generate_slip():
        employee_id = emp_id_entry.get().strip()
        salary_str = salary_entry.get().strip()

        if not employee_id or not salary_str:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        try:
            salary = float(salary_str)
        except ValueError:
            messagebox.showwarning("Input Error", "Salary must be a number.")
            return

        if save_payroll_to_db(employee_id, salary):
            messagebox.showinfo("Success", "✅ Payroll data saved successfully.")
            emp_id_entry.delete(0, tk.END)
            salary_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Database Error", "❌ Could not save data. Check DB connection.")

    tk.Button(frame, text="Generate Slip", bg="#4CAF50", fg="white", command=on_generate_slip).pack(pady=10)
    tk.Button(frame, text="Back", bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("400x300")

    def show_main():
        root.deiconify()

    def open_payroll():
        root.withdraw()
        open_payroll_ui(root, show_main)

    tk.Button(root, text="Open Payroll Management", command=open_payroll).pack(pady=50)

    root.mainloop()
