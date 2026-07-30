from dataclasses import dataclass, field


@dataclass
class Student:
    student_id: str
    name: str
    age: int
    email: str


@dataclass
class Course:
    course_id: str
    title: str
    teacher: str


@dataclass
class Enrollment:
    student_id: str
    course_id: str
    attendance: list[str] = field(default_factory=list)
    grades: list[float] = field(default_factory=list)
