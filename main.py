from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from pydantic import BaseModel
import json
from datetime import datetime

app = FastAPI()

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