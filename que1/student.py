from fastapi import APIRouter, HTTPException, status
from typing import List
from model import Student
import json
import os


student_router = APIRouter()
FILE_PATH = "students.json"

def load_students() -> List[dict]:
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_students(students: List[dict]):
    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)

student_list = load_students()

@student_router.post("/students")
async def add_student(student_person: Student) -> dict:
    try:
        student_person.calculate_average_and_grade()
        student_list.append(student_person.dict())
        save_students(student_list)
        return {
            "message": "Student added successfully",
            "student": student_person.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@student_router.get("/students/{name}")
async def view_single_student(name: str) -> dict:
    try:
        for person in student_list:
            if person["name"] == name:
                return person
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No student with that name"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@student_router.get("/students")
async def view_student() -> dict:
    try:
        return {
            "students": student_list
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


