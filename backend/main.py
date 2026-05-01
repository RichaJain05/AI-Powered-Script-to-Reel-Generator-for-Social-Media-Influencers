from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import ReelRequest, VideoRequest
from hook_engine import generate_hook
from script_engine import generate_script
from explainability import explain_script
from storage import save_result
from video_engine import generate_ai_video
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from frontend
app.mount("/", StaticFiles(directory="static", html=True), name="frontend")

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

    print(result)
    save_result(result)

    return result

@app.post("/generate-video")
def generate_video(data: VideoRequest):
    output_file = generate_ai_video(data.script_text)
    
    if output_file and os.path.exists(output_file):
        return FileResponse(output_file, media_type="video/mp4", filename="ai_reel.mp4")
    else:
        return {"error": "Failed to generate video"}

# Mount the frontend directory to serve static HTML, CSS, and JS files.
# This must be at the bottom so it doesn't override the API routes above.
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")