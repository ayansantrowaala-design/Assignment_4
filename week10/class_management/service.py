from dataclasses import asdict

from class_management.models import Course, Enrollment, Student
from class_management.storage import load_data, save_data


class ClassManager:
    def __init__(self) -> None:
        self.data = load_data()

    def _save(self) -> None:
        save_data(self.data)

    def add_student(self, student_id: str, name: str, age: int, email: str) -> bool:
        if any(student["student_id"] == student_id for student in self.data["students"]):
            return False

        student = Student(student_id=student_id, name=name, age=age, email=email)
        self.data["students"].append(asdict(student))
        self._save()
        return True

    def add_course(self, course_id: str, title: str, teacher: str) -> bool:
        if any(course["course_id"] == course_id for course in self.data["courses"]):
            return False

        course = Course(course_id=course_id, title=title, teacher=teacher)
        self.data["courses"].append(asdict(course))
        self._save()
        return True

    def enroll_student(self, student_id: str, course_id: str) -> bool:
        student_exists = any(student["student_id"] == student_id for student in self.data["students"])
        course_exists = any(course["course_id"] == course_id for course in self.data["courses"])
        already_enrolled = any(
            enrollment["student_id"] == student_id and enrollment["course_id"] == course_id
            for enrollment in self.data["enrollments"]
        )

        if not student_exists or not course_exists or already_enrolled:
            return False

        enrollment = Enrollment(student_id=student_id, course_id=course_id)
        self.data["enrollments"].append(asdict(enrollment))
        self._save()
        return True

    def mark_attendance(self, student_id: str, course_id: str, date: str) -> bool:
        for enrollment in self.data["enrollments"]:
            if enrollment["student_id"] == student_id and enrollment["course_id"] == course_id:
                if date not in enrollment["attendance"]:
                    enrollment["attendance"].append(date)
                    self._save()
                return True
        return False

    def add_grade(self, student_id: str, course_id: str, grade: float) -> bool:
        for enrollment in self.data["enrollments"]:
            if enrollment["student_id"] == student_id and enrollment["course_id"] == course_id:
                enrollment["grades"].append(grade)
                self._save()
                return True
        return False

    def get_students(self) -> list[dict]:
        return self.data["students"]

    def get_courses(self) -> list[dict]:
        return self.data["courses"]

    def get_enrollments(self) -> list[dict]:
        return self.data["enrollments"]
