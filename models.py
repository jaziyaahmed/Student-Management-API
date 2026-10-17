from pydantic import BaseModel
from datetime import date


class Student(BaseModel):
    id: str
    first_name: str
    last_name: str
    date_of_birth: date

class CreateStudentRequest(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
