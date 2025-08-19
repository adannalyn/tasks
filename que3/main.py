from fastapi import FastAPI, Query
from file_handler import load_application, save_application
from model import JobApplication

app = FastAPI()


@app.post("/applications")
def create_application(application: JobApplication):
    try:
        applications = load_application()
        applications.append(application.dict())
        save_application(applications)
        return {
            "message": "Application added successfully",
            "application": application
        }
    except Exception as e:
        return {
            "error": f"Could not save application: {str(e)}"
        }


@app.get("/applications")
def get_all_applications():
    try:
        applications = load_application()
        return applications
    except Exception as e:
        return {
            "error": f"Could not load application: {str(e)}"
        }


@app.get("/applications/search")
def search_applications(status: str = Query(...,
                                            description="Filter by status")):
    try:
        applications = load_application()
        matching = []
        for app in applications:
            if app.get("status", "").lower() == status.lower():
                matching.append(app)
        return matching
    except Exception as e:
        return {
            "error": f"Search failed: {str(e)}"
        }
