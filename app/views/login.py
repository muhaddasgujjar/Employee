import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to insert login data into MySQL
def save_login_to_db(username, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="",            # Your MySQL username
            password="",        # Your MySQL password
            database="employee"  # Updated database name
        )
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"  # Updated table name
        cursor.execute(query, (username, password))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return False

# Login UI function
def open_login_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Login")
    win.geometry("400x300")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Login", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)

    tk.Label(frame, text="username", bg="#ffffff").pack()
    username_entry = tk.Entry(frame, width=30)
    username_entry.pack(pady=5)

    tk.Label(frame, text="password", bg="#ffffff").pack()
    password_entry = tk.Entry(frame, show="*", width=30)
    password_entry.pack(pady=5)

    def on_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password.")
            return

        if save_login_to_db(username, password):
            messagebox.showinfo("Success", "Your data has been saved to the database.")
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Database Error", "Could not save data. Check your database connection.")

    tk.Button(frame, text="Login", width=15, bg="#2196F3", fg="white", command=on_login).pack(pady=10)
    tk.Button(frame, text="Back", width=10, bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()
