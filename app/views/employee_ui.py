import tkinter as tk
from tkinter import messagebox
import mysql.connector

def save_employee_to_db(name, designation):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Use your actual password if set
            database="employee"
        )
        cursor = conn.cursor()
        query = "INSERT INTO employee_profiles (name, designation) VALUES (%s, %s)"
        cursor.execute(query, (name, designation))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return False

def open_employee_profile_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Employee Profile")
    win.geometry("400x400")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Employee Profile", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)

    tk.Label(frame, text="Name", bg="#ffffff").pack()
    name_entry = tk.Entry(frame, width=30)
    name_entry.pack(pady=5)

    tk.Label(frame, text="Designation", bg="#ffffff").pack()
    designation_entry = tk.Entry(frame, width=30)
    designation_entry.pack(pady=5)

    success_label = tk.Label(frame, text="", bg="#ffffff", fg="green", font=("Helvetica", 10))
    success_label.pack(pady=5)

    # Hide initially, shown after successful save
    back_btn = tk.Button(frame, text="Go Back", bg="#f44336", fg="white", width=10,
                         command=lambda: [win.destroy(), back_callback()])
    back_btn.pack_forget()

    def on_save():
        name = name_entry.get().strip()
        designation = designation_entry.get().strip()

        if not name or not designation:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        # Try to save data
        if save_employee_to_db(name, designation):
            # Show success message
            success_label.config(text="✅ Data saved successfully!")
            # Show back button so user can go back
            back_btn.pack(pady=10)
            # Disable save button so user doesn't spam saves
            save_btn.config(state=tk.DISABLED)
            # Optional: Disable entries to prevent changes after save
            name_entry.config(state=tk.DISABLED)
            designation_entry.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Database Error", "❌ Could not save data. Check DB connection.")

    save_btn = tk.Button(frame, text="Save", bg="#4CAF50", fg="white", command=on_save)
    tk.Button(frame, text="Back", width=10, bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()
    save_btn.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("400x300")

    def show_main():
        root.deiconify()

    def open_profile():
        root.withdraw()
        open_employee_profile_ui(root, show_main)

    tk.Button(root, text="Open Employee Profile", command=open_profile).pack(pady=50)

    root.mainloop()
