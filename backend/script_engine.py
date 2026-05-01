from llm_service import call_llm
import re


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

    Output in plain text, no markdown formatting.

    Format:
    Body:
    CTA:
    """

    result = call_llm(prompt)

    # Clean the result by removing markdown bold
    result = re.sub(r'\*\*', '', result)

    # Use regex to extract Body and CTA
    body_match = re.search(r'Body:\s*(.*?)\s*CTA:', result, re.DOTALL | re.IGNORECASE)
    cta_match = re.search(r'CTA:\s*(.*)', result, re.DOTALL | re.IGNORECASE)

    if body_match:
        body = body_match.group(1).strip()
    else:
        body = "Error: Could not parse body from response."

    if cta_match:
        cta = cta_match.group(1).strip()
    else:
        cta = "Follow for more such content."

    return body, cta

