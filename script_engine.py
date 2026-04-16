def generate_script(data):

    body = (
        "As a " + data.persona +
        ", let me explain " + data.topic +
        " in a " + data.tone.lower() +
        " way for " + data.platform + "."
    )

    cta = "Follow for more such content."

    return body, cta