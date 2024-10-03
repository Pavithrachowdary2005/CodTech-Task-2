from tkinter import messagebox
import tkinter as tk

class GradeTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Grade Tracker")
        self.grades = {}

        # Define subjects
        self.subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4","Subject 5", "Subject 6", "Subject 7", "Subject 8"]
        self.entries = {}

        # Create labels and entry fields for each subject
        for i, subject in enumerate(self.subjects):
            tk.Label(self.root, text=subject).grid(row=i, column=0)
            entry = tk.Entry(self.root, width=10)
            entry.grid(row=i, column=1)
            self.entries[subject] = entry

        # Create button to calculate overall grade
        calculate_button = tk.Button(self.root, text="Calculate Overall Grade", command=self.calculate_overall_grade)
        calculate_button.grid(row=len(self.subjects), column=0, columnspan=2)

        # Create label to display the overall grade result
        self.overall_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.overall_label.grid(row=len(self.subjects)+1, column=0, columnspan=2)

    def calculate_overall_grade(self):
        self.grades = {}

        # Collect grades and validate
        for subject, entry in self.entries.items():
            try:
                grade = float(entry.get())
                if not 0 <= grade <= 100:
                    messagebox.showerror("Invalid Grade", "Grade must be between 0 and 100")
                    return
                self.grades[subject] = grade
            except ValueError:
                messagebox.showerror("Invalid Grade", "Grade must be a number")
                return

        # Calculate and display overall grade, letter grade, and GPA
        overall_grade = sum(self.grades.values()) / len(self.grades)
        letter_grade = self.get_letter_grade(overall_grade)
        gpa = self.get_gpa(overall_grade)

        self.overall_label.config(text=f"Overall Grade: {overall_grade:.2f} ({letter_grade}, GPA: {gpa:.1f})")

    def get_letter_grade(self, grade):
        if grade == 100:
            return "A+"
        elif grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "B+"
        elif grade >= 60:
            return "C"
        elif grade >= 50:
            return "C+"
        elif grade >= 40:
            return "D+"
        elif grade >= 35:
            return "D"
        else:
            return "F"

    def get_gpa(self, grade):
        if grade == 100:
            return 10.0
        elif grade >= 90:
            return 9.0
        elif grade >= 80:
            return 8.0
        elif grade >= 70:
            return 7.0
        elif grade >= 60:
            return 6.0
        elif grade >= 50:
            return 5.0
        elif grade >= 40:
            return 4.0
        elif grade >= 30:
            return 3.0
        else:
            return 0.0

    def run(self):
        self.root.mainloop()

# Create and run the grade tracker application
tracker = GradeTracker()
tracker.run()
