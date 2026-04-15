from pydantic import BaseModel

class ReelRequest(BaseModel):
    topic: str
    platform: str
    tone: str
    duration: int = 30
    persona: str