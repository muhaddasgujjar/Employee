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
    win.geometry("400x300")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Attendance", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)
    tk.Label(frame, text="Employee ID", bg="#ffffff").pack()
    emp_id_entry = tk.Entry(frame, width=30)
    emp_id_entry.pack(pady=5)

    def on_mark_present():
        emp_id = emp_id_entry.get().strip()
        success, message = mark_attendance(emp_id)
        if success:
            messagebox.showinfo("Success", message)
            emp_id_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", message)

    tk.Button(frame, text="Mark Present", bg="#4CAF50", fg="white", command=on_mark_present).pack(pady=10)
    tk.Button(frame, text="Back", bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

# --- Unit Tests ---
class TestAttendanceLogic(unittest.TestCase):
    def test_mark_attendance_success(self):
        success, msg = mark_attendance("123")
        self.assertTrue(success)
        self.assertEqual(msg, "Attendance marked successfully")

    def test_mark_attendance_empty_id(self):
        success, msg = mark_attendance("")
        self.assertFalse(success)
        self.assertEqual(msg, "Employee ID cannot be empty")

# Run tests only if this file is executed directly (not when imported)
if __name__ == "__main__":
    # To run UI, uncomment below lines and comment unittest.main()
    # root = tk.Tk()
    # root.withdraw()  # Hide root window if needed
    # open_attendance_ui(root, back_callback=lambda: print("Back pressed"))
    # root.mainloop()

    # To run unit tests, uncomment below:
    unittest.main()
