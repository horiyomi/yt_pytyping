from typing import Any, Callable, Optional, TypeVar, Iterable
from dataclasses import dataclass

# courses: list = ["Python Course", "Java Course", "Javscript Course"]

# student: dict[str, Any]

# student = courses

# print(student)


@dataclass
class Course:
    name: str
    code: str


def register_course(student_name: str, course: Course, callback: Callable[[str], bool]) -> bool:
    send_mail = callback("email@me.com")
    if send_mail:
        print("Sending email.....")
    return True


# course = Course("Python", "PY")
# register_course()

# Optional type
def pay_tax(tax_code: str, age: Optional[int]) -> str:
    if age:
        print("Logic....")

    return "Paid"


# Generics

T = TypeVar("T")


def send_mail(recipients: list[T]) -> None:
    for item in recipients:
        print(item)


# send_mail(["mailer@me.com", "mailsomebody@someone.com"])

# send_mail([1,2,3,4,4])


def student_register(students: Iterable[str]) -> str:

    for student in students:
        print(student)


student_register(("Dami", "Dan", "Ricky", "Jones"))