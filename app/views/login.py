import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to insert login data into MySQL
def save_login_to_db(username, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",           # Use your actual password if needed
            database="employee"
        )
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
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
    win.geometry("400x350")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    success_label = tk.Label(frame, text="", fg="green", bg="#ffffff", font=("Arial", 10, "bold"))
    success_label.pack(pady=(0, 5))

    tk.Label(frame, text="Login", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)

    tk.Label(frame, text="Username", bg="#ffffff").pack()
    username_entry = tk.Entry(frame, width=30)
    username_entry.pack(pady=5)

    tk.Label(frame, text="Password", bg="#ffffff").pack()
    password_entry = tk.Entry(frame, show="*", width=30)
    password_entry.pack(pady=5)

    def on_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password.")
            return

        if save_login_to_db(username, password):
            success_label.config(text="✅ Data stored successfully!")
            # Hide form fields
            username_entry.config(state='disabled')
            password_entry.config(state='disabled')
            login_btn.config(state='disabled')
        else:
            messagebox.showerror("Database Error", "❌ Could not save data. Check DB connection.")

    login_btn = tk.Button(frame, text="Login", width=15, bg="#2196F3", fg="white", command=on_login)
    login_btn.pack(pady=10)

    back_btn = tk.Button(frame, text="Back to Main", width=15, bg="#4CAF50", fg="white", command=lambda: [win.destroy(), back_callback()])
    back_btn.pack(pady=5)

# Main window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("400x300")

    def show_main():
        root.deiconify()  # Show the main window again

    def open_login():
        root.withdraw()  # Hide main window
        open_login_ui(root, show_main)

    # Add button to open login window
    btn = tk.Button(root, text="Open Login Window", command=open_login)
    btn.pack(pady=50)

    root.mainloop()
