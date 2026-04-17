import os
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt):
    try:
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024,
            stream=False,
        )
        
        return completion.choices[0].message.content

    except Exception as e:
        # srate limits (Groq uses 429 as well)
        if "429" in str(e):
            print("Groq Quota hit! Waiting 10 seconds...")
            time.sleep(10)
        
        print(f"Groq LLM Error: {e}")
        return "Error generating content."
    