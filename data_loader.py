import pandas as pd

from models.student import Student
from models.course import Course
from models.slot import Slot

file_path = "ga_exam_timetable_dataset.xlsx"


def load_students():

    students = []
    data_file = pd.read_excel(file_path, sheet_name="Student_Courses")
    for _, row in data_file.iterrows():
        student_id = row["Student_ID"]
        courses = [course.strip() for course in row["Courses_Taken"].split(",")]

        student = Student(student_id, courses)
        students.append(student)

    return students


def load_courses():
    courses = []
    data_file = pd.read_excel(file_path, sheet_name="Course_Catalog")
    for _, row in data_file.iterrows():
        course_code = row["Course_Code"]
        credits = row["Credits"]
        enrollment = row["Enrollment"]
        course = Course(course_code, credits, enrollment)
        courses.append(course)
    return courses


def load_slots():
    slots = []
    data_file = pd.read_excel(file_path, sheet_name="Exam_Slots")
    for _, row in data_file.iterrows():
        slot_id = row["Slot_ID"]
        exam_day = row["Exam_Day"]
        slot_number = row["Slot_Number"]
        time = row["Time"]
        slot = Slot(slot_id, exam_day, slot_number, time)
        slots.append(slot)
    return slots
