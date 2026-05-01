from pydantic import BaseModel

class ReelRequest(BaseModel):
    topic: str
    persona: str
    tone: str
    platform: str 



class VideoRequest(BaseModel):
    script_content: str
