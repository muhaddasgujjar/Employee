import tkinter as tk
from tkinter import messagebox
import unittest

# --- Logic: Validate performance inputs ---
def validate_performance_input(emp_name, notes):
    if not emp_name.strip() or not notes.strip():
        return False, "Please enter both Employee Name and Evaluation Notes."
    return True, ""

# --- Logic: Process performance submission (placeholder) ---
def process_performance_submission(emp_name, notes):
    # Extend this to save data to DB or file
    return f"Performance submitted for {emp_name} with notes:\n{notes}"

# --- UI function ---
def open_performance_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Performance Evaluation")
    win.geometry("400x350")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Performance Evaluation", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)

    tk.Label(frame, text="Employee Name", bg="#ffffff").pack()
    emp_name_entry = tk.Entry(frame, width=30)
    emp_name_entry.pack(pady=5)

    tk.Label(frame, text="Evaluation Notes", bg="#ffffff").pack()
    notes_entry = tk.Entry(frame, width=30)
    notes_entry.pack(pady=5)

    def on_submit():
        emp_name = emp_name_entry.get().strip()
        notes = notes_entry.get().strip()

        valid, msg = validate_performance_input(emp_name, notes)
        if not valid:
            messagebox.showwarning("Input Error", msg)
            return

        result = process_performance_submission(emp_name, notes)
        messagebox.showinfo("Success", result)
        emp_name_entry.delete(0, tk.END)
        notes_entry.delete(0, tk.END)

    tk.Button(frame, text="Submit", bg="#4CAF50", fg="white", command=on_submit).pack(pady=10)
    tk.Button(frame, text="Back", bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

# --- Unit tests ---
class TestPerformanceLogic(unittest.TestCase):
    def test_validate_success(self):
        valid, msg = validate_performance_input("Alice", "Great work!")
        self.assertTrue(valid)
        self.assertEqual(msg, "")

    def test_validate_empty_name(self):
        valid, msg = validate_performance_input("", "Good job")
        self.assertFalse(valid)
        self.assertEqual(msg, "Please enter both Employee Name and Evaluation Notes.")

    def test_validate_empty_notes(self):
        valid, msg = validate_performance_input("Alice", "")
        self.assertFalse(valid)
        self.assertEqual(msg, "Please enter both Employee Name and Evaluation Notes.")

if __name__ == "__main__":
    # To run UI, comment out unittest.main() and uncomment below:
    # root = tk.Tk()
    # root.withdraw()
    # open_performance_ui(root, back_callback=lambda: print("Back pressed"))
    # root.mainloop()

    unittest.main()
