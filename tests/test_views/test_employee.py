import tkinter as tk
from tkinter import messagebox
import unittest

# --- Logic Function ---
def save_employee_profile(name, designation):
    """
    Logic to save employee profile.
    Returns (success: bool, message: str)
    """
    if not name.strip():
        return False, "Name cannot be empty"
    if not designation.strip():
        return False, "Designation cannot be empty"
    # Add DB or file saving logic here if needed
    return True, "Employee profile saved successfully"

# --- UI Function ---
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

    def on_save():
        name = name_entry.get().strip()
        designation = designation_entry.get().strip()
        success, message = save_employee_profile(name, designation)
        if success:
            messagebox.showinfo("Success", message)
            name_entry.delete(0, tk.END)
            designation_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", message)

    tk.Button(frame, text="Save", bg="#4CAF50", fg="white", command=on_save).pack(pady=10)
    tk.Button(frame, text="Back", width=10, bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

# --- Unit Tests ---
class TestEmployeeProfileLogic(unittest.TestCase):
    def test_save_profile_success(self):
        success, msg = save_employee_profile("Alice", "Manager")
        self.assertTrue(success)
        self.assertEqual(msg, "Employee profile saved successfully")

    def test_save_profile_empty_name(self):
        success, msg = save_employee_profile("", "Manager")
        self.assertFalse(success)
        self.assertEqual(msg, "Name cannot be empty")

    def test_save_profile_empty_designation(self):
        success, msg = save_employee_profile("Alice", "")
        self.assertFalse(success)
        self.assertEqual(msg, "Designation cannot be empty")

if __name__ == "__main__":
    # To run UI, uncomment below and comment unittest.main()
    # root = tk.Tk()
    # root.withdraw()
    # open_employee_profile_ui(root, back_callback=lambda: print("Back pressed"))
    # root.mainloop()

    unittest.main()
