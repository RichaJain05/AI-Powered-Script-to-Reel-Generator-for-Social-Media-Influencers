from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
from datetime import datetime

app = FastAPI()

# ENABLE CORS (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all frontend origins
    allow_credentials=True,
    allow_methods=["*"],   # allow GET, POST, OPTIONS
    allow_headers=["*"],
)

@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")


# take input from user
class ReelRequest(BaseModel):
    topic: str
    platform: str
    tone: str
    duration: int
    persona: str


@app.post("/generate-reel")
def generate_reel(data: ReelRequest):

    hook = "What if I told you " + data.topic + " could change everything?"

    body = (
        "As a " + data.persona +
        ", I will explain " + data.topic +
        " in a " + data.tone.lower() +
        " way for " + data.platform + "."
    )

    cta = "Follow for more such content"

    explanation = {
        "message": "Script generated based on user input details"
    }

    result = {
        "hook": hook,
        "body": body,
        "cta": cta,
        "explanation": explanation
    }

    # save history
    with open("history.json", "a") as file:
        json.dump(
            {
                "time": str(datetime.now()),
                "result": result
            },
            file
        )
        file.write("\n")

    return result