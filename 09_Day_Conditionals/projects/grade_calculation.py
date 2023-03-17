"""
Project: Student Grade Calculator

The aim of this project is to build a program that calculates
the grades of students based on their exam scores and attendance.
The program should take as input the student's attendance percentage and
exam scores and output their final grade based on a predefined grading scale.
"""


def calculate_grade(attendance, exam_score):
    """
    This function calculates the student's final grade
    """
    if attendance >= 90:
        if exam_score >= 90:
            grade = "A+"
        elif exam_score >= 80:
            grade = "A"
        elif exam_score >= 70:
            grade = "B+"
        elif exam_score >= 60:
            grade = "B"
        elif exam_score >= 50:
            grade = "C+"
        else:
            grade = "C"
    elif attendance >= 80:
        if exam_score >= 90:
            grade = "A"
        elif exam_score >= 80:
            grade = "B+"
        elif exam_score >= 70:
            grade = "B"
        elif exam_score >= 60:
            grade = "C+"
        elif exam_score >= 50:
            grade = "C"
        else:
            grade = "D"
    else:
        grade = "F"
    return grade


# Main function
def main():
    attendance = int(input("Enter the attendance percentage: "))
    exam_score = int(input("Enter the exam score: "))
    grade = calculate_grade(attendance, exam_score)
    print(f"Final Grade: {grade}")


if __name__ == "__main__":
    main()
