# This module contains functions to process student data.

def format_student_data(student):
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"

def display_students(students):
    for student in students:
        print(format_student_data(student))
