import tkinter as tk
from tkinter import messagebox
import mysql.connector
import unittest

# --- Logic function to save login data ---
def save_login_to_db(username, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="",            # Your MySQL username
            password="",        # Your MySQL password
            database="employee"  # Your database name
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

# --- Logic function to validate inputs ---
def validate_login_input(username, password):
    if not username or not password:
        return False, "Please enter both username and password."
    return True, ""

# --- UI function ---
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

        valid, msg = validate_login_input(username, password)
        if not valid:
            messagebox.showwarning("Input Error", msg)
            return

        if save_login_to_db(username, password):
            messagebox.showinfo("Success", "Your data has been saved to the database.")
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Database Error", "Could not save data. Check your database connection.")

    tk.Button(frame, text="Login", width=15, bg="#2196F3", fg="white", command=on_login).pack(pady=10)
    tk.Button(frame, text="Back", width=10, bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

# --- Unit tests for logic ---
class TestLoginLogic(unittest.TestCase):
    def test_validate_login_input_success(self):
        valid, msg = validate_login_input("user1", "pass1")
        self.assertTrue(valid)
        self.assertEqual(msg, "")

    def test_validate_login_input_empty_username(self):
        valid, msg = validate_login_input("", "pass1")
        self.assertFalse(valid)
        self.assertEqual(msg, "Please enter both username and password.")

    def test_validate_login_input_empty_password(self):
        valid, msg = validate_login_input("user1", "")
        self.assertFalse(valid)
        self.assertEqual(msg, "Please enter both username and password.")

if __name__ == "__main__":
    # To run UI, comment out unittest.main() and uncomment below:
    # root = tk.Tk()
    # root.withdraw()
    # open_login_ui(root, back_callback=lambda: print("Back pressed"))
    # root.mainloop()

    unittest.main()
