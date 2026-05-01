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

# 1. UPDATED ORIGINS
# Added a wildcard for testing and ensured your specific frontend URL is correct
origins = [
    "http://localhost:5500",
    "https://ai-powered-script-to-reel-generator-for-klch.onrender.com",
    "*" # This helps bypass CORS issues during the demo
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-reel")
def generate_reel(data: ReelRequest):
    try:
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
    except Exception as e:
        return {"error": str(e)}

@app.post("/generate-video")
def generate_video(data: VideoRequest):
    # 2. MATCHING THE FRONTEND FIELD
    # Your frontend sends 'script_content', but your model might expect 'script_text'
    # Ensure your VideoRequest model or this line uses the correct attribute
    script_to_use = getattr(data, 'script_content', getattr(data, 'script_text', ""))
    
    output_file = generate_ai_video(script_to_use)
    
    if output_file and os.path.exists(output_file):
        return FileResponse(output_file, media_type="video/mp4", filename="ai_reel.mp4")
    else:
        return {"error": "Failed to generate video"}

# 3. FIXING THE STATIC MOUNT
# If you are deploying Frontend and Backend SEPARATELY on Render, 
# you don't actually need app.mount. 
# But if you are deploying them together, ensure the path is correct:
frontend_path = os.path.join(os.getcwd(), "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")