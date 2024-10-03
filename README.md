Overview and Documentation

The Student Grade Tracker is a simple GUI-based application built using Python's `tkinter` library. It allows users to input grades for eight subjects, calculates the overall grade, and converts that score into a corresponding letter grade and GPA (Grade Point Average) based on a predefined scale. The application also provides validation to ensure that grades are entered correctly (as numeric values between 0 and 100).

Features
- Input Validation: Ensures the grades are numeric values between 0 and 100. Displays an error message if input is invalid.
- Grade Calculation: Computes the overall grade from all subject scores entered by the user.
- Letter Grade & GPA Calculation: Converts the overall grade into both a letter grade and GPA using a predefined grading and GPA scale.
- User-friendly Interface: Built using `tkinter` for a simple and intuitive user experience.
  
Getting Started

Prerequisites:
- Python 3.x
- `tkinter` library (usually included with standard Python installations)

Running the Application:
1. Ensure you have Python installed.
2. Copy the provided Python script into a file named `grade_tracker.py`.
3. Run the script with the following command:
    "bash
   python grade_tracker.py
   "
   
5. The GUI window will open, displaying fields for eight subjects. Enter grades in the corresponding text fields and press the "Calculate Overall Grade" button to see the results.

### Usage

1. Input Grades: Enter a numeric grade (0-100) for each of the eight subjects in the input fields.
2. Calculate Grades: Click the "Calculate Overall Grade" button. The overall grade, letter grade, and GPA will be displayed below.
3. **Error Handling: If the user inputs a non-numeric value or a grade outside the 0-100 range, an error dialog will be shown, prompting the user to enter valid grades.

### Grading & GPA Scale

| Overall Grade | Letter Grade | GPA  |
| ------------- | ------------ | ---- |
| 100           | A+           | 10.0 |
| 90 - 99       | A            | 9.0  |
| 80 - 89       | B            | 8.0  |
| 70 - 79       | B+           | 7.0  |
| 60 - 69       | C            | 6.0  |
| 50 - 59       | C+           | 5.0  |
| 40 - 49       | D+           | 4.0  |
| 35 - 39       | D            | 3.0  |
| Below 35      | F            | 0.0  |

Future Improvements
- Add options to customize the number of subjects.
- Store and retrieve past grades for review.
- Introduce weighted grades for different subjects.
  
