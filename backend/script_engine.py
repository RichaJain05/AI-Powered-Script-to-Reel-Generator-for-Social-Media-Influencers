from llm_service import call_llm


def generate_script(data):

    prompt = f"""
    You are a student content creator.

    Create an Instagram reel script.

    Topic: {data.topic}
    Persona: {data.persona}
    Tone: {data.tone}
    Platform: {data.platform}

    Keep it:
    - Short
    - Easy to understand
    - conversational (Hinglish allowed)

    Format:
    Body:
    CTA:
    """

    result = call_llm(prompt)

   
    parts = result.split("CTA:")

    body = parts[0].replace("Body:", "").strip()

    if len(parts) > 1:
        cta = parts[1].strip()
    else:
        cta = "Follow for more such content."

    return body, cta
