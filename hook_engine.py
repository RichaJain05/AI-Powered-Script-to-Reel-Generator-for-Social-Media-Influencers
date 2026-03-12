import random

# different hook styles
hooks = [
    "What if I told you {topic} could change everything?",
    "Nobody talks about this but {topic} is a game changer.",
    "Stop scrolling! Here's something about {topic}.",
    "Most people ignore this about {topic}.",
    "This one trick about {topic} will surprise you."
]

def generate_hook(topic):
    return random.choice(hooks).format(topic=topic)