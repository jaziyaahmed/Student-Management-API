from fastapi import FastAPI

from models import CreateStudentRequest
from student_repository import InMemoryStudentRepository
from student_service import StudentService

app = FastAPI()
students_service= StudentService(repository=InMemoryStudentRepository())

@app.get("/health")
def health():
    return "Yeah this is working"

@app.get("/students/{student_id}")
def get_student(student_id:str):
    return students_service.get_student(student_id)

@app.post("/students")
def create_student(student:CreateStudentRequest):
    return students_service.create_student(student)