from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from datetime import datetime
import os

app = FastAPI(title="AI Script to Reel Generator")

# ENABLE CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Redirect root to docs
@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")


# Request Model
class ReelRequest(BaseModel):
    topic: str
    platform: str
    tone: str
    duration: int
    persona: str


# Generate Script
@app.post("/generate-reel")
def generate_reel(data: ReelRequest):

    # Hook
    hook = f"What if I told you {data.topic} could change everything?"

    # Body
    body = (
        f"As a {data.persona}, I will explain {data.topic} "
        f"in a {data.tone.lower()} way for {data.platform}. "
        f"This reel will be around {data.duration} seconds."
    )

    # Call to action
    cta = "Follow for more AI-powered content ideas!"

    explanation = {
        "message": "Script generated based on user input"
    }

    result = {
        "hook": hook,
        "body": body,
        "cta": cta,
        "explanation": explanation
    }

    # Save history
    history_entry = {
        "time": str(datetime.now()),
        "input": data.dict(),
        "output": result
    }

    try:
        if not os.path.exists("history.json"):
            with open("history.json", "w") as file:
                json.dump([], file)

        with open("history.json", "r+") as file:
            history = json.load(file)
            history.append(history_entry)
            file.seek(0)
            json.dump(history, file, indent=4)

    except Exception as e:
        print("Error saving history:", e)

    return result