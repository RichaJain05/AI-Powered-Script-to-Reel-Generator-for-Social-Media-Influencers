import random

def generate_hook(topic):

    hooks = [
        f"Stop scrolling! Here's something interesting about {topic}.",
        f"Did you know this about {topic}?",
        f"Most people don't know this about {topic}.",
        f"Let me quickly explain {topic}.",
        f"This might change how you think about {topic}."
    ]

    hook = random.choice(hooks)

    return hook