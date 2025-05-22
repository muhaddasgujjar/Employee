import tkinter as tk
from tkinter import messagebox
import mysql.connector

def save_performance_to_db(employee_name, evaluation_notes):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Update if your MySQL has a password
            database="employee"  # Your database name
        )
        cursor = conn.cursor()
        # Assuming a table `performance` with columns employee_name and evaluation_notes
        query = "INSERT INTO performance (employee_name, evaluation_notes) VALUES (%s, %s)"
        cursor.execute(query, (employee_name, evaluation_notes))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return False

def open_performance_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Performance Evaluation")
    win.geometry("400x350")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Performance Evaluation", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)

    tk.Label(frame, text="Employee Name", bg="#ffffff").pack()
    employee_name_entry = tk.Entry(frame, width=30)
    employee_name_entry.pack(pady=5)

    tk.Label(frame, text="Evaluation Notes", bg="#ffffff").pack()
    evaluation_notes_entry = tk.Entry(frame, width=30)
    evaluation_notes_entry.pack(pady=5)

    def on_submit():
        employee_name = employee_name_entry.get().strip()
        evaluation_notes = evaluation_notes_entry.get().strip()

        if not employee_name or not evaluation_notes:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        if save_performance_to_db(employee_name, evaluation_notes):
            messagebox.showinfo("Success", "✅ Performance data saved successfully.")
            employee_name_entry.delete(0, tk.END)
            evaluation_notes_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Database Error", "❌ Could not save data. Check DB connection.")

    tk.Button(frame, text="Submit", bg="#4CAF50", fg="white", command=on_submit).pack(pady=10)
    tk.Button(frame, text="Back", bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("400x300")

    def show_main():
        root.deiconify()

    def open_performance():
        root.withdraw()
        open_performance_ui(root, show_main)

    tk.Button(root, text="Open Performance Evaluation", command=open_performance).pack(pady=50)

    root.mainloop()
