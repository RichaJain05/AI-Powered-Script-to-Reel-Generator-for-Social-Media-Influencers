import random
from llm_service import call_llm

def generate_hook(topic):

    basic_hooks = [
        f"Stop scrolling! Here's something about {topic}.",
        f"Did you know this about {topic}?",
        f"Most people ignore this about {topic}.",
        f"Let me explain {topic} quickly.",
        f"This can change your thinking about {topic}."
    ]

    # 50% chance basic, 50% LLM
    if random.random() < 0.5:
        return random.choice(basic_hooks)

    # LLM hook
    prompt = f"""
    Generate 1 catchy Instagram reel hook on: {topic}

    Keep it:
    - Short
    - Attention grabbing
    - Student friendly
    """

    return call_llm(prompt)

