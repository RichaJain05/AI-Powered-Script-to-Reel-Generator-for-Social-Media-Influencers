from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # ✅ ADD THIS

from models import ReelRequest
from hook_engine import generate_hook
from script_engine import generate_script
from explainability import explain_script
from storage import save_result

app = FastAPI()

# ✅ ENABLE CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],   # allow POST, GET, OPTIONS
    allow_headers=["*"],
)

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