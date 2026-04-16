from fastapi import FastAPI

from models import ReelRequest
from hook_engine import generate_hook
from script_engine import generate_script
from explainability import explain_script
from storage import save_result

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Backend is running successfully"}


@app.post("/generate-reel")
def generate_reel(data: ReelRequest):

    hook = generate_hook(data.topic)

    body, cta = generate_script(data)

    explanation = explain_script(data)

    result = {
        "hook": hook,
        "body": body,
        "cta": cta,
        "explanation": explanation
    }

    save_result(result)

    return result