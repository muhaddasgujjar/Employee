import tkinter as tk
from tkinter import messagebox
import mysql.connector

def save_department_to_db(department_name):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Change if your MySQL has a password
            database="employee"  # Change to your DB name if different
        )
        cursor = conn.cursor()
        # Assuming table: departments with column: name (VARCHAR)
        query = "INSERT INTO departments (name) VALUES (%s)"
        cursor.execute(query, (department_name,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return False

def open_department_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Department Management")
    win.geometry("400x300")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Department Management", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)

    tk.Label(frame, text="Department Name", bg="#ffffff").pack()
    dept_entry = tk.Entry(frame, width=30)
    dept_entry.pack(pady=5)

    def on_add_department():
        dept_name = dept_entry.get().strip()
        if not dept_name:
            messagebox.showwarning("Input Error", "Please enter department name.")
            return
        if save_department_to_db(dept_name):
            messagebox.showinfo("Success", "✅ Department added successfully.")
            dept_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Database Error", "❌ Could not add department. Check DB connection.")

    tk.Button(frame, text="Add Department", bg="#4CAF50", fg="white", command=on_add_department).pack(pady=10)
    tk.Button(frame, text="Back", bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("400x300")

    def show_main():
        root.deiconify()

    def open_dept():
        root.withdraw()
        open_department_ui(root, show_main)

    tk.Button(root, text="Open Department Management", command=open_dept).pack(pady=50)

    root.mainloop()
