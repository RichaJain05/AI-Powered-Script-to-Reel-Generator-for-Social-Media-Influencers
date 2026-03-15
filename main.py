from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from datetime import datetime
import os

from hook_engine import generate_hook   # NEW IMPORT

app = FastAPI(title="AI Script to Reel Generator")

# enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# redirect root
@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")


# request model
class ReelRequest(BaseModel):
    topic: str
    platform: str
    tone: str
    duration: int
    persona: str


# generate reel
@app.post("/generate-reel")
def generate_reel(data: ReelRequest):

    # generate hook using hook engine
    hook = generate_hook(data.topic)

    body = (
        f"As a {data.persona}, I will explain {data.topic} "
        f"in a {data.tone.lower()} way for {data.platform}. "
        f"This reel will be around {data.duration} seconds."
    )

    cta = "Follow for more content ideas!"

    result = {
        "hook": hook,
        "body": body,
        "cta": cta,
        "platform": data.platform,
        "tone": data.tone,
        "duration": data.duration,
        "persona": data.persona
    }

    # save history
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