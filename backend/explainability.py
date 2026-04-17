def explain_script(data):
    """
    Explains the logic behind the generated script 
    to help the user understand the 'Why'.
    """
    explanation = {
        "topic_used": data.topic,
        "tone_used": data.tone,
        "platform_used": data.platform,
        "strategy": f"The script uses a {data.tone} tone to better suit {data.platform} users.",
        "hook_logic": "The first 3 seconds are designed as a 'Pattern Interrupt' to stop the scroll.",
        "message": "Script generated successfully based on your specific inputs."
    }

    return explanation