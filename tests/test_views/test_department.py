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
    win.geometry("400x250")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    title_label = tk.Label(frame, text="Department Management", font=("Helvetica", 16, "bold"), bg="#ffffff")
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    tk.Label(frame, text="Department Name", bg="#ffffff", anchor="w").grid(row=1, column=0, sticky="w")
    dept_name_entry = tk.Entry(frame, width=30)
    dept_name_entry.grid(row=1, column=1, pady=5)

    def on_add_department():
        dept_name = dept_name_entry.get().strip()
        success, message = add_department(dept_name)
        if success:
            messagebox.showinfo("Success", message)
            dept_name_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", message)

    add_btn = tk.Button(frame, text="Add Department", bg="#4CAF50", fg="white", command=on_add_department)
    add_btn.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

    back_btn = tk.Button(frame, text="Back", bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()])
    back_btn.grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")

# --- Unit Test (Only One Function) ---
class TestDepartmentLogic(unittest.TestCase):
    def test_add_department_success(self):
        success, msg = add_department("Finance")
        self.assertTrue(success)
        self.assertEqual(msg, "Department added successfully")

# Run tests or UI
if __name__ == "__main__":
    # To run UI, uncomment below lines and comment unittest.main()
    # root = tk.Tk()
    # root.withdraw()  # Hide root window
    # open_department_ui(root, back_callback=lambda: print("Back pressed"))
    # root.mainloop()

    # To run unit test (only one function)
    unittest.main()
