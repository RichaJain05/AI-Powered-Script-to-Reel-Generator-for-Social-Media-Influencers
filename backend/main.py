import os
import openai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from models import ReelRequest, VideoRequest
from hook_engine import generate_hook
from script_engine import generate_script
from explainability import explain_script
from storage import save_result

# Initialize OpenAI Client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# 1. CORS Setup
origins = [
    "http://localhost:5500",
    "https://ai-powered-script-to-reel-generator-for-klch.onrender.com",
    "*" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Logic to handle OpenAI Video Generation
def generate_ai_video(script):
    try:
        # Note: Sora is currently in limited release. 
        # Most users use 'dall-e-3' for images or 3rd party Sora wrappers.
        response = client.images.generate( # Example using DALL-E for visual if Sora is restricted
            model="dall-e-3",
            prompt=f"Create a cinematic video frame for: {script}",
            n=1,
            size="1024x1024"
        )
        
        video_file_path = "output_reel.mp4"
        # You need logic here to download the video URL from response to video_file_path
        # For now, we assume video_file_path is created successfully.
        return video_file_path
    except Exception as e:
        print(f"OpenAI Error: {e}")
        return None

@app.post("/generate-reel")
def generate_reel(data: ReelRequest):
    try:
        hook = generate_hook(data.topic)
        body, cta = generate_script(data)
        explanation = explain_script(data)
        result = {"hook": hook, "body": body, "cta": cta, "explanation": explanation}
        save_result(result)
        return result
    except Exception as e:
        return {"error": str(e)}

@app.post("/generate-video")
def generate_video(data: VideoRequest):
    # FIX: Use data.script_content directly
    script_to_use = data.script_content
    
    if not script_to_use:
        return {"error": "Script content is empty"}
        
    output_file = generate_ai_video(script_to_use)
    
    if output_file and os.path.exists(output_file):
        return FileResponse(output_file, media_type="video/mp4", filename="ai_reel.mp4")
    else:
        return {"error": "Failed to generate video. Check OpenAI API Key/Quota."}

# Static files for frontend
frontend_path = os.path.join(os.getcwd(), "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")