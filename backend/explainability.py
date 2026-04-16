def explain_script(data):

    explanation = {
        "topic_used": data.topic,
        "tone_used": data.tone,
        "platform_used": data.platform,
        "message": "Hook grabs attention and script is generated based on user input."
    }

    return explanation