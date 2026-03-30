from fastapi import FastAPI

from models import ReelRequest
from hook_engine import generate_hook
from script_engine import generate_script
from explainability import explain_script
from storage import save_result

app = FastAPI()


# Home route
@app.get("/")
def home():
    return {"message": "AI Reel Script Generator Backend Running"}


# Main API
@app.post("/generate-reel")
def generate_reel(data: ReelRequest):

    # Generate hook
    hook = generate_hook(data.topic)

    # Generate script and CTA
    body, cta = generate_script(data)

    # Generate explanation
    explanation = explain_script(data)

    # Final result
    result = {
        "hook": hook,
        "body": body,
        "cta": cta,
        "explanation": explanation
    }

    # Save result
    save_result(result)

    return result
