import tkinter as tk
from tkinter import messagebox
import unittest

# --- Logic Function ---
def add_department(department_name):
    """
    Logic to add a department.
    Returns (success: bool, message: str)
    """
    if not department_name:
        return False, "Department name cannot be empty"
    # Add DB or file saving logic here if needed
    return True, "Department added successfully"

# --- UI Function ---
def open_department_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Department Management")
    win.geometry("400x300")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Department Management", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)
    tk.Label(frame, text="Department Name", bg="#ffffff").pack()
    dept_name_entry = tk.Entry(frame, width=30)
    dept_name_entry.pack(pady=5)

    def on_add_department():
        dept_name = dept_name_entry.get().strip()
        success, message = add_department(dept_name)
        if success:
            messagebox.showinfo("Success", message)
            dept_name_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", message)

    tk.Button(frame, text="Add Department", bg="#4CAF50", fg="white", command=on_add_department).pack(pady=10)
    tk.Button(frame, text="Back", bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

# --- Unit Tests ---
class TestDepartmentLogic(unittest.TestCase):
    def test_add_department_success(self):
        success, msg = add_department("Finance")
        self.assertTrue(success)
        self.assertEqual(msg, "Department added successfully")

    def test_add_department_empty_name(self):
        success, msg = add_department("")
        self.assertFalse(success)
        self.assertEqual(msg, "Department name cannot be empty")

# Run tests only if this file is executed directly (not when imported)
if __name__ == "__main__":
    # To run UI, uncomment below lines and comment unittest.main()
    # root = tk.Tk()
    # root.withdraw()  # Hide root window if needed
    # open_department_ui(root, back_callback=lambda: print("Back pressed"))
    # root.mainloop()

    # To run unit tests, uncomment below:
    unittest.main()
