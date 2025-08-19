from fastapi import FastAPI
from student import student_router


app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "KodeCamp Class"
    }

app.include_router(student_router)
