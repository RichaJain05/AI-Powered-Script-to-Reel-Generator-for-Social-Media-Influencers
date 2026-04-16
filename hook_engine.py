import random

def generate_hook(topic):

    hooks = [
        f"Stop scrolling! Here's something about {topic}.",
        f"Did you know this about {topic}?",
        f"Most people ignore this about {topic}.",
        f"Let me explain {topic} quickly.",
        f"This can change your thinking about {topic}."
    ]

    return random.choice(hooks)