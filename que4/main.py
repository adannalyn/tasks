from fastapi import FastAPI, HTTPException
import os


NOTES_DIR = "notes_storage"
os.makedirs(NOTES_DIR, exist_ok=True)

app = FastAPI()


@app.post("/notes")
def create_note(title: str, content: str):
    try:
        filename = os.path.join(NOTES_DIR, f"{title}.txt")
        if os.path.exists(filename):
            raise HTTPException(status_code=400, detail="Note already exists")
        with open(filename, "w") as file:
            file.write(content)
        return {"message": f"Note '{title}' created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/notes/{title}")
def read_note(title: str):
    try:
        filename = os.path.join(NOTES_DIR, f"{title}.txt")
        if not os.path.exists(filename):
            raise HTTPException(status_code=404, detail="Note not found")
        with open(filename, "r") as file:
            content = file.read()
        return {"title": title, "content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/notes/{title}")
def update_note(title: str, new_content: str):
    try:
        filename = os.path.join(NOTES_DIR, f"{title}.txt")
        if not os.path.exists(filename):
            raise HTTPException(status_code=404, detail="Note not found")
        with open(filename, "w") as file:
            file.write(new_content)
        return {"message": f"Note '{title}' updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/notes/{title}")
def delete_note(title: str):
    try:
        filename = os.path.join(NOTES_DIR, f"{title}.txt")
        if not os.path.exists(filename):
            raise HTTPException(status_code=404, detail="Note not found")
        os.remove(filename)
        return {"message": f"Note '{title}' deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
