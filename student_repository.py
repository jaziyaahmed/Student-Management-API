from models import Student


class InMemoryStudentRepository():

    def __init__(self):
        self._students = {}

    def save(self, student: Student ):
        self._students[student.id] = student
        return student

    def get_by_id(self,student_id:str):
        return self._students[student_id]