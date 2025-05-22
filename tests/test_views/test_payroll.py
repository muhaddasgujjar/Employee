import tkinter as tk
from tkinter import messagebox
import unittest

# --- Logic function to validate payroll inputs ---
def validate_payroll_input(emp_id, salary):
    if not emp_id or not salary:
        return False, "Please enter both Employee ID and Salary."
    try:
        float_salary = float(salary)
        if float_salary < 0:
            return False, "Salary cannot be negative."
    except ValueError:
        return False, "Salary must be a number."
    return True, ""

# --- Logic function to generate payroll slip (placeholder) ---
def generate_payroll_slip(emp_id, salary):
    # This function could be extended to save to DB or generate a file
    # For now, just return a formatted string
    return f"Payroll Slip\nEmployee ID: {emp_id}\nSalary: ${salary}"

# --- UI function ---
def open_payroll_ui(main_root, back_callback):
    win = tk.Toplevel()
    win.title("Payroll Management")
    win.geometry("400x350")
    win.configure(bg="#f5f5f5")

    frame = tk.Frame(win, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Payroll Management", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)

    tk.Label(frame, text="Employee ID", bg="#ffffff").pack()
    emp_id_entry = tk.Entry(frame, width=30)
    emp_id_entry.pack(pady=5)

    tk.Label(frame, text="Salary", bg="#ffffff").pack()
    salary_entry = tk.Entry(frame, width=30)
    salary_entry.pack(pady=5)

    def on_generate():
        emp_id = emp_id_entry.get().strip()
        salary = salary_entry.get().strip()

        valid, msg = validate_payroll_input(emp_id, salary)
        if not valid:
            messagebox.showwarning("Input Error", msg)
            return

        slip = generate_payroll_slip(emp_id, salary)
        messagebox.showinfo("Payroll Slip", slip)
        emp_id_entry.delete(0, tk.END)
        salary_entry.delete(0, tk.END)

    tk.Button(frame, text="Generate Slip", bg="#4CAF50", fg="white", command=on_generate).pack(pady=10)
    tk.Button(frame, text="Back", bg="#f44336", fg="white", command=lambda: [win.destroy(), back_callback()]).pack()

# --- Unit tests for payroll logic ---
class TestPayrollLogic(unittest.TestCase):
    def test_validate_payroll_input_success(self):
        valid, msg = validate_payroll_input("123", "4500")
        self.assertTrue(valid)
        self.assertEqual(msg, "")

    def test_validate_payroll_input_empty_fields(self):
        valid, msg = validate_payroll_input("", "")
        self.assertFalse(valid)
        self.assertEqual(msg, "Please enter both Employee ID and Salary.")

    def test_validate_payroll_input_negative_salary(self):
        valid, msg = validate_payroll_input("123", "-1000")
        self.assertFalse(valid)
        self.assertEqual(msg, "Salary cannot be negative.")

    def test_validate_payroll_input_non_numeric_salary(self):
        valid, msg = validate_payroll_input("123", "abc")
        self.assertFalse(valid)
        self.assertEqual(msg, "Salary must be a number.")

if __name__ == "__main__":
    # To run UI, comment out unittest.main() and uncomment below:
    # root = tk.Tk()
    # root.withdraw()
    # open_payroll_ui(root, back_callback=lambda: print("Back pressed"))
    # root.mainloop()

    unittest.main()
