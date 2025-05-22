import tkinter as tk
from tkinter import messagebox
import unittest

# --- Logic Function ---
def mark_attendance(employee_id):
    """
    Logic to mark attendance for given employee_id.
    Returns (success: bool, message: str)
    """
    if not employee_id:
        return False, "Employee ID cannot be empty"
    # Add DB or file saving logic here if needed
    return True, "Attendance marked successfully"

# --- UI Function ---
def open_attendance_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Attendance")
    win.geometry("400x250")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    title_label = tk.Label(frame, text="Attendance", font=("Helvetica", 16, "bold"), bg="#ffffff")
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    tk.Label(frame, text="Employee ID", bg="#ffffff", anchor="w").grid(row=1, column=0, sticky="w")
    emp_id_entry = tk.Entry(frame, width=30)
    emp_id_entry.grid(row=1, column=1, pady=5)

    def on_mark_present():
        emp_id = emp_id_entry.get().strip()
        success, message = mark_attendance(emp_id)
        if success:
            messagebox.showinfo("Success", message)
            emp_id_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", message)

    mark_btn = tk.Button(frame, text="Mark Present", bg="#4CAF50", fg="white", command=on_mark_present)
    mark_btn.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

    back_btn = tk.Button(frame, text="Back", bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()])
    back_btn.grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")

# --- Unit Test (Only One Function) ---
class TestAttendanceLogic(unittest.TestCase):
    def test_mark_attendance_success(self):
        success, msg = mark_attendance("123")
        self.assertTrue(success)
        self.assertEqual(msg, "Attendance marked successfully")

# Run tests or UI
if __name__ == "__main__":
    # To run UI, uncomment below lines and comment unittest.main()
    # root = tk.Tk()
    # root.withdraw()
    # open_attendance_ui(root, back_callback=lambda: print("Back pressed"))
    # root.mainloop()

    # To run unit test (only one function)
    unittest.main()
