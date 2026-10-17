from uuid import uuid4
from models import CreateStudentRequest, Student
from student_repository import InMemoryStudentRepository


class StudentService:



    def __init__(self, repository:InMemoryStudentRepository):
        self.repository = repository

    def create_student(self,request: CreateStudentRequest):
        student= Student(
            id= str(uuid4()),
            first_name= request.first_name,
            last_name= request.last_name,
            date_of_birth= request.date_of_birth,

        )
        self.repository.save(student=student)
        return student

    def get_student(self,student_id):
        try:
            return self.repository.get_by_id(student_id)
        except Exception:
            return f"There is no student with this id: {student_id}"

    